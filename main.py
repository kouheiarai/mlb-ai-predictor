from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from mlb_api import fetch_mlb_schedule

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


def flatten_odds(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for event in events:
        bookmakers = event.get("bookmakers") or []
        pinnacle = next(
            (book for book in bookmakers if book.get("key") == "pinnacle"),
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
            market_key = market.get("key", "")

            for outcome in market.get("outcomes") or []:
                decimal_price = outcome.get("price")
                implied = implied_probability(decimal_price)

                rows.append(
                    {
                        **common,
                        "market": market_key,
                        "selection": outcome.get("name", ""),
                        "point": outcome.get("point", ""),
                        "decimal_odds": decimal_price,
                        "american_odds": american_odds(decimal_price),
                        "implied_probability": (
                            round(implied, 6) if implied is not None else ""
                        ),
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


def write_report(
    odds_rows: list[dict[str, Any]],
    schedule: list[dict[str, Any]],
    fetched_at: str,
    quota: dict[str, str],
    path: Path,
) -> None:
    lines = [
        "# MLB Daily Data",
        "",
        f"- Updated: {fetched_at}",
        f"- API requests remaining: "
        f"{quota.get('requests_remaining') or 'unknown'}",
        f"- Odds rows: {len(odds_rows)}",
        f"- MLB schedule games: {len(schedule)}",
        "",
        "## Probable Pitchers",
        "",
    ]

    if not schedule:
        lines.append("No MLB schedule data was returned.")
    else:
        for game in schedule:
            lines.extend(
                [
                    f"### {game['away_team']} @ {game['home_team']}",
                    f"- Start (UTC): {game['game_date_utc']}",
                    f"- Status: {game['status']}",
                    f"- Away starter: {game['away_probable_pitcher']}",
                    f"- Home starter: {game['home_probable_pitcher']}",
                    "",
                ]
            )

    lines.extend(["## Pinnacle Odds", ""])

    if not odds_rows:
        lines.append("No Pinnacle MLB odds were returned.")
    else:
        current_game: tuple[str, str, str] | None = None

        for row in odds_rows:
            game_key = (
                row["commence_time_utc"],
                row["away_team"],
                row["home_team"],
            )

            if game_key != current_game:
                current_game = game_key
                lines.extend(
                    [
                        f"### {row['away_team']} @ {row['home_team']}",
                        f"- Start (UTC): {row['commence_time_utc']}",
                    ]
                )

            point = ""
            if isinstance(row["point"], (int, float)):
                point = f" {row['point']:+g}"

            lines.append(
                f"- {row['market']}: {row['selection']}{point} "
                f"@ {row['decimal_odds']} ({row['american_odds']})"
            )

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        api_key = require_api_key()

        odds_events, quota = fetch_odds(api_key)
        odds_rows = flatten_odds(odds_events)
        schedule = fetch_mlb_schedule(days=3)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fetched_at = datetime.now(timezone.utc).isoformat()

        odds_payload = {
            "fetched_at_utc": fetched_at,
            "quota": quota,
            "events": odds_events,
        }

        (OUTPUT_DIR / "latest_odds.json").write_text(
            json.dumps(odds_payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        (OUTPUT_DIR / "mlb_schedule.json").write_text(
            json.dumps(
                {
                    "fetched_at_utc": fetched_at,
                    "games": schedule,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        write_csv(odds_rows, OUTPUT_DIR / "latest_odds.csv")
        write_report(
            odds_rows,
            schedule,
            fetched_at,
            quota,
            OUTPUT_DIR / "report.md",
        )

        print(
            f"Fetched {len(odds_events)} odds events, "
            f"{len(odds_rows)} odds rows, "
            f"and {len(schedule)} MLB games."
        )
        print(
            f"Requests remaining: "
            f"{quota.get('requests_remaining') or 'unknown'}"
        )
        return 0

    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
