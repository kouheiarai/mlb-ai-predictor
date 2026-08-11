"""Answer the go/no-go question before building anything on top of this data.

The business case assumes gBizINFO publishes enough dated events, often enough,
to be worth a daily notification. That assumption is untested. This script tests
it directly: it walks backwards month by month, asks the API how many events
each month produced, and reads the import_frequency metadata the API attaches to
the records themselves.

Run it as soon as a token arrives:

    GBIZINFO_API_TOKEN=... python -m gbiz.probe --months 12

A month showing thousands of events means a daily product has something to say.
A month showing a handful means the signal is too thin and the plan needs to
change before any code is written on top of it.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from .client import EVENT_KINDS, GBizClient, GBizError


def month_bounds(year: int, month: int) -> tuple[date, date]:
    start = date(year, month, 1)
    if month == 12:
        end = date(year, 12, 31)
    else:
        end = date(year, month + 1, 1).toordinal() - 1
        end = date.fromordinal(end)
    return start, end


def recent_months(count: int, today: date | None = None) -> list[tuple[int, int]]:
    cursor = today or datetime.now(timezone.utc).date()
    months: list[tuple[int, int]] = []
    year, month = cursor.year, cursor.month
    for _ in range(count):
        months.append((year, month))
        month -= 1
        if month == 0:
            year, month = year - 1, 12
    return list(reversed(months))


def probe(client: GBizClient, months: int, kinds: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "probed_at_utc": datetime.now(timezone.utc).isoformat(),
        "months_requested": months,
        "kinds": {},
    }

    for kind in kinds:
        monthly: list[dict[str, Any]] = []
        frequencies: Counter[str] = Counter()
        sources: Counter[str] = Counter()

        for year, month in recent_months(months):
            start, end = month_bounds(year, month)
            try:
                count = client.count_update_info(kind, start, end)
            except GBizError as exc:
                monthly.append({"month": f"{year}-{month:02d}", "error": str(exc)})
                continue
            monthly.append({"month": f"{year}-{month:02d}", "total_count": count})

        # Sample one page of the most recent non-empty month to read metadata.
        for entry in reversed(monthly):
            if entry.get("total_count"):
                year, month = (int(part) for part in entry["month"].split("-"))
                start, end = month_bounds(year, month)
                try:
                    for record in client.iter_update_info(kind, start, end, max_pages=1):
                        for event in record.get(EVENT_KINDS[kind]["list_key"]) or []:
                            metadata = (event or {}).get("meta-data") or {}
                            if metadata.get("import_frequency"):
                                frequencies[str(metadata["import_frequency"])] += 1
                            if metadata.get("source"):
                                sources[str(metadata["source"])] += 1
                except GBizError:
                    pass
                break

        counts = [e["total_count"] for e in monthly if isinstance(e.get("total_count"), int)]
        result["kinds"][kind] = {
            "monthly": monthly,
            "months_with_data": sum(1 for c in counts if c > 0),
            "median_per_month": _median(counts),
            "max_per_month": max(counts) if counts else 0,
            "import_frequency_seen": dict(frequencies),
            "sources_seen": dict(sources.most_common(10)),
        }

    result["verdict"] = _verdict(result["kinds"])
    return result


def _median(values: list[int]) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2


def _verdict(kinds: dict[str, Any]) -> dict[str, Any]:
    """Translate the raw counts into the decision the probe exists to inform."""
    viable: list[str] = []
    thin: list[str] = []
    for kind, summary in kinds.items():
        median = summary.get("median_per_month") or 0
        # ~30 events a month is roughly one a day: below that a daily product
        # has nothing to send on most days.
        if median >= 30 and summary.get("months_with_data", 0) >= 2:
            viable.append(kind)
        else:
            thin.append(kind)
    return {
        "viable_for_daily_signal": viable,
        "too_thin": thin,
        "note": (
            "A kind counts as viable at roughly one event per day or more. "
            "Check import_frequency_seen as well: if the upstream import is "
            "monthly, a daily poll adds latency but not freshness."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--months", type=int, default=12, help="how many months back to probe")
    parser.add_argument(
        "--kinds",
        nargs="*",
        default=list(EVENT_KINDS),
        choices=list(EVENT_KINDS),
        help="event kinds to probe",
    )
    parser.add_argument(
        "--out", type=Path, default=Path("gbiz_data/probe_result.json"), help="where to write the report"
    )
    args = parser.parse_args()

    try:
        client = GBizClient()
    except GBizError as exc:
        print(f"[probe] {exc}")
        return 1

    report = probe(client, args.months, args.kinds)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)

    print(f"\ngBizINFO probe — {args.months} months\n")
    for kind, summary in report["kinds"].items():
        median = summary["median_per_month"]
        print(f"  {kind:<14} median/month={median!s:<9} max={summary['max_per_month']:<8} "
              f"months_with_data={summary['months_with_data']}")
        if summary["import_frequency_seen"]:
            print(f"  {'':<14} import_frequency={summary['import_frequency_seen']}")
    verdict = report["verdict"]
    print(f"\n  viable for a daily signal : {verdict['viable_for_daily_signal'] or 'none'}")
    print(f"  too thin                  : {verdict['too_thin'] or 'none'}")
    print(f"\n  written to {args.out}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
