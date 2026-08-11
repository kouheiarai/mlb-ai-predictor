"""Append-only event store with first-seen tracking.

The product is not the event list — gBizINFO already serves that — but the
answer to "what is new since yesterday". That requires remembering what we had
already seen, which is what this module owns.

Layout under the data root:

    events/YYYY-MM.jsonl   every event we have ever observed, one JSON per line
    state/seen.json        event_id -> {first_seen, last_seen, content_hash}
    daily/YYYY-MM-DD.json  the signal for one run: newly appeared + revised events
"""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable


class EventStore:
    def __init__(self, root: Path | str) -> None:
        self.root = Path(root)
        self.events_dir = self.root / "events"
        self.state_dir = self.root / "state"
        self.daily_dir = self.root / "daily"
        for directory in (self.events_dir, self.state_dir, self.daily_dir):
            directory.mkdir(parents=True, exist_ok=True)
        self.seen_path = self.state_dir / "seen.json"

    # ---------- seen index ----------

    def load_seen(self) -> dict[str, dict[str, Any]]:
        if not self.seen_path.exists():
            return {}
        try:
            with self.seen_path.open(encoding="utf-8") as handle:
                data = json.load(handle)
        except (json.JSONDecodeError, OSError):
            return {}
        return data if isinstance(data, dict) else {}

    def save_seen(self, seen: dict[str, dict[str, Any]]) -> None:
        tmp = self.seen_path.with_suffix(".json.tmp")
        with tmp.open("w", encoding="utf-8") as handle:
            json.dump(seen, handle, ensure_ascii=False, sort_keys=True)
        tmp.replace(self.seen_path)

    # ---------- ingest ----------

    def ingest(
        self, rows: Iterable[dict[str, Any]], observed_at: datetime | None = None
    ) -> dict[str, list[dict[str, Any]]]:
        """Classify rows against what we have seen and persist the new ones.

        Returns the run's signal: rows never seen before, and rows whose payload
        changed since we last saw them.
        """
        observed = (observed_at or datetime.now(timezone.utc)).isoformat()
        seen = self.load_seen()

        new_rows: list[dict[str, Any]] = []
        revised_rows: list[dict[str, Any]] = []
        batch: dict[str, list[dict[str, Any]]] = {}

        for row in rows:
            key = row.get("event_id")
            if not key:
                continue
            record = seen.get(key)
            if record is None:
                enriched = dict(row, first_seen_utc=observed)
                new_rows.append(enriched)
                seen[key] = {
                    "first_seen": observed,
                    "last_seen": observed,
                    "content_hash": row.get("content_hash"),
                }
                batch.setdefault(_partition(row), []).append(enriched)
            else:
                record["last_seen"] = observed
                if record.get("content_hash") != row.get("content_hash"):
                    enriched = dict(
                        row,
                        first_seen_utc=record.get("first_seen"),
                        revised_at_utc=observed,
                        previous_content_hash=record.get("content_hash"),
                    )
                    revised_rows.append(enriched)
                    record["content_hash"] = row.get("content_hash")
                    batch.setdefault(_partition(row), []).append(enriched)

        for partition, partition_rows in batch.items():
            self._append(partition, partition_rows)
        self.save_seen(seen)

        return {"new": new_rows, "revised": revised_rows}

    def _append(self, partition: str, rows: list[dict[str, Any]]) -> None:
        path = self.events_dir / f"{partition}.jsonl"
        with path.open("a", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    # ---------- daily signal ----------

    def write_daily(self, run_date: date, signal: dict[str, Any]) -> Path:
        path = self.daily_dir / f"{run_date.isoformat()}.json"
        with path.open("w", encoding="utf-8") as handle:
            json.dump(signal, handle, ensure_ascii=False, indent=2)
        return path

    def iter_events(self) -> Iterable[dict[str, Any]]:
        for path in sorted(self.events_dir.glob("*.jsonl")):
            with path.open(encoding="utf-8") as handle:
                for line in handle:
                    line = line.strip()
                    if line:
                        yield json.loads(line)

    def stats(self) -> dict[str, Any]:
        seen = self.load_seen()
        by_type: dict[str, int] = {}
        for row in self.iter_events():
            key = row.get("event_type") or "unknown"
            by_type[key] = by_type.get(key, 0) + 1
        first_seen_dates = sorted(
            record["first_seen"][:10] for record in seen.values() if record.get("first_seen")
        )
        return {
            "unique_events": len(seen),
            "rows_by_type": by_type,
            "accumulating_since": first_seen_dates[0] if first_seen_dates else None,
        }


def _partition(row: dict[str, Any]) -> str:
    """Partition by the event's own month, falling back to the observation month."""
    event_date = row.get("event_date") or ""
    if len(event_date) >= 7 and event_date[4] == "-":
        return event_date[:7]
    return datetime.now(timezone.utc).strftime("%Y-%m")
