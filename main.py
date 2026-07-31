from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

API_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/"
OUTPUT_DIR = Path("data")


def require_api_key() -> str:
    key = os.getenv("THE_ODDS_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "THE_ODDS_API_KEY is missing. Add it under "
            "Settings > Secrets and variables > Actions."
        )
    return key


def fetch_odds(api_key: str) -> tuple[list[dict[str, Any]], dict[str, str]]:
    params = {
        "apiKey": api_key,
        "bookmakers": "pinnacle",
        "markets": "h2h,spreads",
        "oddsFormat": "decimal",
        "dateFormat": "iso",
    }
    response = requests.get(API_URL, params=params, timeout=30)
    if response.status_code != 200:
        raise RuntimeError(
            f"The Odds API returned HTTP {response.status_code}: "
            f"{response.text[:1000]}"
        )
    headers = {
        "requests_remaining": response.headers.get("x-requests-remaining", ""),
        "requests_used": response.headers.get("x-requests-used", ""),
        "requests_last": response.headers.get("x-requests-last", ""),
    }
    return response.json(), headers


def american_odds(decimal_price: float | None) -> str:
    if decimal_price is None or decimal_price <= 1:
        return ""
    if decimal_price >= 2:
        return f"+{round((decimal_price - 1) * 100)}"
    return str(round(-100 / (decimal_price - 1)))


def implied_probability(decimal_price: float | None) -> float | None:
    if decimal_price is None or decimal_price <= 1:
        return None
    return 1 / decimal_price


def flatten(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for event in events:
        pinnacle = next(
            (
                book
                for book in (event.get("bookmakers") or [])
                if book.get("key") == "pinnacle"
            ),
            None,
        )
        if not pinnacle:
            continue

        common = {
            "event_id": event.get("id", ""),
            "commence_time_utc": event.get("commence_time", ""),
            "away_team": event.get("away_team", ""),
            "home_team": event.get("home_team", ""),
            "bookmaker": "pinnacle",
            "bookmaker_last_update": pinnacle.get("last_update", ""),
        }

        for market in pinnacle.get("markets") or []:
            for outcome in market.get("outcomes") or []:
                price = outcome.get("price")
                implied = implied_probability(price)
                rows.append(
                    {
                        **common,
                        "market": market.get("key", ""),
                        "selection": outcome.get("name", ""),
                        "point": outcome.get("point", ""),
                        "decimal_odds": price,
                        "american_odds": american_odds(price),
                        "implied_probability": round(implied, 6) if implied else "",
                    }
                )

    rows.sort(
        key=lambda row: (
            row["commence_time_utc"],
            row["away_team"],
            row["market"],
            row["selection"],
        )
    )
    return rows


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    fields = [
        "event_id",
        "commence_time_utc",
        "away_team",
        "home_team",
        "bookmaker",
        "bookmaker_last_update",
        "market",
        "selection",
        "point",
        "decimal_odds",
        "american_odds",
        "implied_probability",
    ]
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, Any]], fetched_at: str, quota: dict[str, str], path: Path) -> None:
    games: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for row in rows:
        key = (row["commence_time_utc"], row["away_team"], row["home_team"])
        games.setdefault(key, []).append(row)

    lines = [
        "# MLB Pinnacle Odds",
        "",
        f"- Updated: {fetched_at}",
        f"- API requests remaining: {quota.get('requests_remaining') or 'unknown'}",
        f"- Games: {len(games)}",
        "",
    ]

    if not games:
        lines.append("No Pinnacle MLB odds were returned.")
    else:
        for (start, away, home), game_rows in games.items():
            lines.extend([f"## {away} @ {home}", f"- Start (UTC): {start}"])
            for row in game_rows:
                point = row["point"]
                point_text = f" {point:+g}" if isinstance(point, (int, float)) else ""
                lines.append(
                    f"- {row['market']}: {row['selection']}{point_text} "
                    f"@ {row['decimal_odds']} ({row['american_odds']})"
                )
            lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        events, quota = fetch_odds(require_api_key())
        rows = flatten(events)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fetched_at = datetime.now(timezone.utc).isoformat()

        payload = {"fetched_at_utc": fetched_at, "quota": quota, "events": events}
        (OUTPUT_DIR / "latest_odds.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        write_csv(rows, OUTPUT_DIR / "latest_odds.csv")
        write_report(rows, fetched_at, quota, OUTPUT_DIR / "report.md")

        print(f"Fetched {len(events)} events and wrote {len(rows)} odds rows.")
        print(f"Requests remaining: {quota.get('requests_remaining') or 'unknown'}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
