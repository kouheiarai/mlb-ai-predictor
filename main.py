from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from mlb_api import attach_probable_pitcher_stats, fetch_mlb_schedule
from predictor import (
    build_elo_ratings,
    fetch_completed_games,
    make_predictions,
)
from team_metrics import fetch_team_metrics

API_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/"
OUTPUT_DIR = Path("data")


def require_api_key() -> str:
    key = os.getenv("THE_ODDS_API_KEY", "").strip()
    if not key:
        raise RuntimeError("THE_ODDS_API_KEY is missing.")
    return key


def fetch_odds(api_key: str) -> tuple[list[dict[str, Any]], dict[str, str]]:
    response = requests.get(
        API_URL,
        params={
            "apiKey": api_key,
            "bookmakers": "pinnacle",
            "markets": "h2h,spreads",
            "oddsFormat": "decimal",
            "dateFormat": "iso",
        },
        timeout=30,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"The Odds API returned HTTP {response.status_code}: "
            f"{response.text[:1000]}"
        )
    return response.json(), {
        "requests_remaining": response.headers.get("x-requests-remaining", ""),
        "requests_used": response.headers.get("x-requests-used", ""),
        "requests_last": response.headers.get("x-requests-last", ""),
    }


def american_odds(decimal_price: float | None) -> str:
    if decimal_price is None or decimal_price <= 1:
        return ""
    if decimal_price >= 2:
        return f"+{round((decimal_price - 1) * 100)}"
    return str(round(-100 / (decimal_price - 1)))


def flatten_odds(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for event in events:
        pinnacle = next(
            (
                book
                for book in event.get("bookmakers", [])
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

        for market in pinnacle.get("markets", []):
            for outcome in market.get("outcomes", []):
                price = outcome.get("price")
                rows.append(
                    {
                        **common,
                        "market": market.get("key", ""),
                        "selection": outcome.get("name", ""),
                        "point": outcome.get("point", ""),
                        "decimal_odds": price,
                        "american_odds": american_odds(price),
                        "implied_probability": (
                            round(1 / price, 6)
                            if isinstance(price, (int, float)) and price > 1
                            else ""
                        ),
                    }
                )
    return rows


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    fields = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        if not fields:
            file.write("")
            return
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def pct(value: Any) -> str:
    try:
        return f"{float(value) * 100:.1f}%"
    except (TypeError, ValueError):
        return ""


def write_report(
    ml_predictions: list[dict[str, Any]],
    rl_predictions: list[dict[str, Any]],
    schedule: list[dict[str, Any]],
    fetched_at: str,
    quota: dict[str, str],
    path: Path,
) -> None:
    lines = [
        "# MLB Ver.18 Prediction Report",
        "",
        f"- Updated: {fetched_at}",
        f"- API requests remaining: {quota.get('requests_remaining') or 'unknown'}",
        "- Simulation: 100,000 Poisson score simulations per game",
        "",
        "## Moneyline Buy Ranking",
        "",
    ]

    ml_buys = [row for row in ml_predictions if row["recommendation"] == "BUY"]
    if not ml_buys:
        lines.append("No EV 5%+ Moneyline bets.")
    else:
        for index, row in enumerate(ml_buys, 1):
            lines.extend(
                [
                    f"### {index}. {row['selection']}",
                    f"- Game: {row['away_team']} @ {row['home_team']}",
                    f"- Odds: {row['decimal_odds']}",
                    f"- AI probability: {pct(row['model_probability'])}",
                    f"- EV: {pct(row['ev'])}",
                    f"- 1/4 Kelly: {pct(row['quarter_kelly'])}",
                    f"- Expected score: "
                    f"{row['away_team']} {row['away_expected_runs']:.2f} - "
                    f"{row['home_team']} {row['home_expected_runs']:.2f}",
                    "",
                ]
            )

    lines.extend(["## Run Line Buy Ranking", ""])
    rl_buys = [row for row in rl_predictions if row["recommendation"] == "BUY"]
    if not rl_buys:
        lines.append("No EV 5%+ Run Line bets.")
    else:
        for index, row in enumerate(rl_buys, 1):
            lines.extend(
                [
                    f"### {index}. {row['selection']} {row['point']:+g}",
                    f"- Game: {row['away_team']} @ {row['home_team']}",
                    f"- Odds: {row['decimal_odds']}",
                    f"- Cover probability: {pct(row['model_probability'])}",
                    f"- EV: {pct(row['ev'])}",
                    f"- 1/4 Kelly: {pct(row['quarter_kelly'])}",
                    f"- Expected score: "
                    f"{row['away_team']} {row['away_expected_runs']:.2f} - "
                    f"{row['home_team']} {row['home_expected_runs']:.2f}",
                    "",
                ]
            )

    lines.extend(["## Probable Pitchers", ""])
    for game in schedule:
        away_stats = game.get("away_starter_stats", {})
        home_stats = game.get("home_starter_stats", {})
        lines.extend(
            [
                f"### {game['away_team']} @ {game['home_team']}",
                f"- Away: {game['away_probable_pitcher']} "
                f"(ERA {away_stats.get('era')}, WHIP {away_stats.get('whip')})",
                f"- Home: {game['home_probable_pitcher']} "
                f"(ERA {home_stats.get('era')}, WHIP {home_stats.get('whip')})",
                "",
            ]
        )

    lines.extend(
        [
            "## Model Notes",
            "",
            "- Expected runs use offense, opponent team pitching, probable starter, recent form, park factor and home edge.",
            "- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.",
            "- Moneyline is blended 85% model / 15% Pinnacle no-vig market.",
            "- BUY threshold is EV 5% or higher.",
            "- Confirmed lineup, true bullpen fatigue, weather and handedness splits are not included yet.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        season = datetime.now(timezone.utc).year
        api_key = require_api_key()

        odds_events, quota = fetch_odds(api_key)
        odds_rows = flatten_odds(odds_events)

        schedule = attach_probable_pitcher_stats(
            fetch_mlb_schedule(days=3),
            season,
        )

        completed_games = fetch_completed_games(season)
        elo_ratings = build_elo_ratings(completed_games)
        team_metrics = fetch_team_metrics(season)

        ml_predictions, rl_predictions = make_predictions(
            odds_rows,
            elo_ratings,
            completed_games,
            schedule,
            team_metrics,
        )

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        fetched_at = datetime.now(timezone.utc).isoformat()

        payloads = {
            "latest_odds.json": {"fetched_at_utc": fetched_at, "events": odds_events},
            "mlb_schedule.json": {"fetched_at_utc": fetched_at, "games": schedule},
            "elo_ratings.json": {"fetched_at_utc": fetched_at, "ratings": elo_ratings},
            "team_metrics.json": {
                "fetched_at_utc": fetched_at,
                "metrics": team_metrics,
            },
            "predictions.json": {
                "fetched_at_utc": fetched_at,
                "moneyline": ml_predictions,
                "runline": rl_predictions,
            },
        }

        for filename, payload in payloads.items():
            (OUTPUT_DIR / filename).write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

        write_csv(odds_rows, OUTPUT_DIR / "latest_odds.csv")
        write_csv(ml_predictions, OUTPUT_DIR / "moneyline_predictions.csv")
        write_csv(rl_predictions, OUTPUT_DIR / "runline_predictions.csv")
        write_report(
            ml_predictions,
            rl_predictions,
            schedule,
            fetched_at,
            quota,
            OUTPUT_DIR / "report.md",
        )

        print(
            f"Generated {len(ml_predictions)} ML predictions and "
            f"{len(rl_predictions)} RL predictions."
        )
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
