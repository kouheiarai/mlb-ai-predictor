"""Flatten gBizINFO update payloads into one row per (corporation, event).

A HojinInfoForChildV2 record carries the corporation's identity plus a list of
events for the requested kind.  The product sells the events, so we invert that
nesting and attach the corporation to each one.

Field names follow the OpenAPI schemas SubsidyInfoV2, ProcurementInfoV2,
CertificationInfoV2 and CommendationInfoV2.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any

from .client import EVENT_KINDS

# Every event schema shares these; the rest differ per kind.
_COMMON_FIELDS = ("title", "government_departments", "target", "category", "note")

_DIGITS = re.compile(r"[^0-9]")


def normalize_amount(value: Any) -> int | None:
    """Amounts arrive as int (procurement) or string (subsidy). Normalize to yen."""
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    digits = _DIGITS.sub("", str(value))
    if not digits:
        return None
    try:
        return int(digits)
    except ValueError:
        return None


def normalize_date(value: Any) -> str | None:
    """Return an ISO date string, accepting the yyyy-MM-dd and yyyyMMdd forms."""
    if not value:
        return None
    text = str(value).strip()
    if not text:
        return None
    digits = _DIGITS.sub("", text)
    if len(digits) >= 8:
        year, month, day = digits[0:4], digits[4:6], digits[6:8]
        if month == "00" or day == "00":
            return None
        return f"{year}-{month}-{day}"
    if len(digits) == 6:
        return f"{digits[0:4]}-{digits[4:6]}"
    return None


def event_id(row: dict[str, Any]) -> str:
    """Stable identity for an event, so re-fetching a period cannot duplicate it.

    gBizINFO has no per-event primary key, so identity comes from the fields that
    together pin down one award: who, what kind, which programme, when, how much.
    """
    parts = [
        row.get("event_type") or "",
        row.get("corporate_number") or "",
        row.get("title") or "",
        row.get("event_date") or "",
        str(row.get("amount") if row.get("amount") is not None else ""),
        row.get("government_departments") or "",
    ]
    digest = hashlib.sha256("".join(parts).encode("utf-8")).hexdigest()
    return digest[:32]


def content_hash(row: dict[str, Any]) -> str:
    """Hash of the payload fields, used to notice a revised event."""
    tracked = {k: row.get(k) for k in ("title", "amount", "event_date", "target", "category", "note")}
    blob = json.dumps(tracked, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def flatten_record(record: dict[str, Any], kind: str) -> list[dict[str, Any]]:
    """Turn one HojinInfoForChildV2 object into a list of flat event rows."""
    spec = EVENT_KINDS[kind]
    corporate_number = (record.get("corporate_number") or "").strip()
    name = (record.get("name") or "").strip()
    location = (record.get("location") or "").strip()

    rows: list[dict[str, Any]] = []
    for event in record.get(spec["list_key"]) or []:
        if not isinstance(event, dict):
            continue
        metadata = event.get("meta-data") or {}
        row: dict[str, Any] = {
            "event_type": kind,
            "corporate_number": corporate_number,
            "name": name,
            "location": location,
            "event_date": normalize_date(event.get(spec["date_field"])),
            "amount": normalize_amount(event.get("amount")),
        }
        for field in _COMMON_FIELDS:
            row[field] = (event.get(field) or "").strip() or None
        row["source"] = (metadata.get("source") or "").strip() or None
        row["import_frequency"] = (metadata.get("import_frequency") or "").strip() or None
        row["source_last_update_date"] = normalize_date(metadata.get("last_update_date"))
        row["event_id"] = event_id(row)
        row["content_hash"] = content_hash(row)
        rows.append(row)
    return rows


def flatten_records(records: list[dict[str, Any]], kind: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in records:
        rows.extend(flatten_record(record, kind))
    return rows
