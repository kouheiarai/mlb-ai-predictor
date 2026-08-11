"""Daily run: pull the window of updated events, store them, emit the signal.

Mirrors the shape of the MLB pipeline in this repository — a scheduled fetch
that writes deterministic files and never publishes a partial result.

    GBIZINFO_API_TOKEN=... python -m gbiz.main --lookback-days 7
"""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .client import EVENT_KINDS, GBizClient, GBizError
from .normalize import flatten_records
from .store import EventStore

# gBizINFO backfills: an award approved last week can appear in the API days
# later. A window wider than one day costs nothing (the store deduplicates) and
# stops those late arrivals from being missed forever.
DEFAULT_LOOKBACK_DAYS = 7


def collect(
    client: GBizClient, start: date, end: date, kinds: list[str]
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    rows: list[dict[str, Any]] = []
    fetched: dict[str, int] = {}
    for kind in kinds:
        records = list(client.iter_update_info(kind, start, end))
        kind_rows = flatten_records(records, kind)
        fetched[kind] = len(kind_rows)
        rows.extend(kind_rows)
    return rows, fetched


def build_signal(
    run_date: date,
    start: date,
    end: date,
    fetched: dict[str, int],
    result: dict[str, list[dict[str, Any]]],
    store_stats: dict[str, Any],
) -> dict[str, Any]:
    new_rows = result["new"]
    by_type: dict[str, int] = {}
    for row in new_rows:
        key = row.get("event_type") or "unknown"
        by_type[key] = by_type.get(key, 0) + 1

    top = sorted(
        (row for row in new_rows if row.get("amount")),
        key=lambda row: row["amount"],
        reverse=True,
    )[:50]

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "run_date": run_date.isoformat(),
        "window": {"from": start.isoformat(), "to": end.isoformat()},
        "source": "gBizINFO (経済産業省) — 政府標準利用規約2.0",
        "attribution": "出典: gBizINFO（経済産業省） https://info.gbiz.go.jp/",
        "fetched_rows_by_type": fetched,
        "new_event_count": len(new_rows),
        "revised_event_count": len(result["revised"]),
        "new_events_by_type": by_type,
        "store": store_stats,
        "top_new_events_by_amount": top,
        "new_events": new_rows,
        "revised_events": result["revised"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lookback-days", type=int, default=DEFAULT_LOOKBACK_DAYS)
    parser.add_argument("--kinds", nargs="*", default=list(EVENT_KINDS), choices=list(EVENT_KINDS))
    parser.add_argument("--data-root", type=Path, default=Path("gbiz_data"))
    parser.add_argument(
        "--dry-run", action="store_true", help="fetch and report without writing to the store"
    )
    args = parser.parse_args()

    try:
        client = GBizClient()
    except GBizError as exc:
        print(f"[gbiz] {exc}")
        return 1

    run_date = datetime.now(timezone.utc).date()
    start = run_date - timedelta(days=max(0, args.lookback_days - 1))

    try:
        rows, fetched = collect(client, start, run_date, args.kinds)
    except GBizError as exc:
        print(f"[gbiz] collection failed: {exc}")
        return 1

    print(f"[gbiz] window {start} .. {run_date}")
    for kind, count in fetched.items():
        print(f"[gbiz]   {kind:<14} {count} rows")

    if args.dry_run:
        print(f"[gbiz] dry run — {len(rows)} rows fetched, nothing written")
        return 0

    store = EventStore(args.data_root)
    result = store.ingest(rows)
    signal = build_signal(run_date, start, run_date, fetched, result, store.stats())
    path = store.write_daily(run_date, signal)

    latest = Path(args.data_root) / "latest.json"
    with latest.open("w", encoding="utf-8") as handle:
        json.dump(signal, handle, ensure_ascii=False, indent=2)

    print(
        f"[gbiz] new={signal['new_event_count']} "
        f"revised={signal['revised_event_count']} "
        f"total_unique={signal['store']['unique_events']}"
    )
    print(f"[gbiz] wrote {path} and {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
