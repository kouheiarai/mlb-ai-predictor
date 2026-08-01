from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from bullpen import fetch_bullpen_fatigue_proxy
from lineup import attach_lineups
from mlb_api import attach_probable_pitcher_stats, fetch_mlb_schedule
from platoon import attach_handedness
from predictor import build_elo_ratings, fetch_completed_games, make_predictions
from weather_data import attach_weather
from team_metrics import fetch_team_metrics

API_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/"
OUTPUT_DIR = Path("data")
DOCS_DIR = Path("docs")
MODEL_VERSION = "26.0"


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
            "markets": "h2h,spreads,totals",
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
    fields = list(dict.fromkeys(key for row in rows for key in row.keys())) if rows else []
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


def lineup_label(value: Any) -> str:
    return "発表済み" if value else "未発表"


def write_report(
    ml_predictions: list[dict[str, Any]],
    rl_predictions: list[dict[str, Any]],
    schedule: list[dict[str, Any]],
    fetched_at: str,
    quota: dict[str, str],
    path: Path,
) -> None:
    lines = [
        "# MLB AI Predictor Ver.26.0 Prediction Report",
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
                    f"- Lineup: {lineup_label(row['lineup_announced'])}",
                    f"- Lineup quality: {row['lineup_quality']:+.2f}",
                    f"- Platoon proxy: {row['platoon_proxy']:+.2f}",
                    f"- Weather run factor: {row['weather_run_factor']:.3f}",
                    f"- Temperature: {row.get('temperature_c')} C",
                    f"- Rain probability: {row.get('precipitation_probability')}%",
                    f"- Wind: {row.get('wind_speed_kmh')} km/h "
                    f"({row.get('wind_direction_deg')} deg)",
                    f"- Bullpen fatigue proxy: {row['bullpen_fatigue']:.2f}",
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
                    f"- Lineup: {lineup_label(row['lineup_announced'])}",
                    f"- Lineup quality: {row['lineup_quality']:+.2f}",
                    f"- Platoon proxy: {row['platoon_proxy']:+.2f}",
                    f"- Weather run factor: {row['weather_run_factor']:.3f}",
                    f"- Temperature: {row.get('temperature_c')} C",
                    f"- Rain probability: {row.get('precipitation_probability')}%",
                    f"- Wind: {row.get('wind_speed_kmh')} km/h "
                    f"({row.get('wind_direction_deg')} deg)",
                    f"- Bullpen fatigue proxy: {row['bullpen_fatigue']:.2f}",
                    f"- Expected score: "
                    f"{row['away_team']} {row['away_expected_runs']:.2f} - "
                    f"{row['home_team']} {row['home_expected_runs']:.2f}",
                    "",
                ]
            )

    lines.extend(
        [
            "## Model Notes",
            "",
            "- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.",
            "- It is a conservative proxy, not a true split-stat model.",
            "- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.",
            "- BUY threshold is EV 5% or higher.",
            "- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.",
            "- Temperature, rain probability and wind speed affect expected runs conservatively.",
            "- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.",
            "- BUY threshold is EV 5% or higher.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")



def confidence_label(row: dict[str, Any]) -> str:
    """Return a conservative confidence grade for display/API consumers."""
    ev = float(row.get("ev") or 0.0)
    probability = float(row.get("model_probability") or 0.0)
    lineup_announced = bool(row.get("lineup_announced"))

    score = 0
    if ev >= 0.15:
        score += 2
    elif ev >= 0.08:
        score += 1
    if probability >= 0.62:
        score += 2
    elif probability >= 0.56:
        score += 1
    if lineup_announced:
        score += 1

    return "S" if score >= 5 else "A" if score >= 3 else "B" if score >= 1 else "C"


def compact_pick(row: dict[str, Any]) -> dict[str, Any]:
    """Stable, compact representation used by ChatGPT and other clients."""
    result = {
        "market": row.get("market"),
        "event_id": row.get("event_id"),
        "commence_time_utc": row.get("commence_time_utc"),
        "away_team": row.get("away_team"),
        "home_team": row.get("home_team"),
        "away_probable_pitcher": row.get("away_probable_pitcher"),
        "home_probable_pitcher": row.get("home_probable_pitcher"),
        "away_elo": row.get("away_elo"),
        "home_elo": row.get("home_elo"),
        "away_recent_form": row.get("away_recent_form"),
        "home_recent_form": row.get("home_recent_form"),
        "park_factor": row.get("park_factor"),
        "weather_run_factor": row.get("weather_run_factor"),
        "selection": row.get("selection"),
        "point": row.get("point"),
        "decimal_odds": row.get("decimal_odds"),
        "market_no_vig_probability": row.get("market_no_vig_probability"),
        "model_probability": row.get("model_probability"),
        "ev": row.get("ev"),
        "quarter_kelly": row.get("quarter_kelly"),
        "recommendation": row.get("recommendation"),
        "confidence": confidence_label(row),
        "lineup_announced": row.get("lineup_announced"),
        "away_expected_runs": row.get("away_expected_runs"),
        "home_expected_runs": row.get("home_expected_runs"),
        "simulations": row.get("simulations"),
    }
    return result


def build_latest_payload(
    ml_predictions: list[dict[str, Any]],
    rl_predictions: list[dict[str, Any]],
    total_predictions: list[dict[str, Any]],
    fetched_at: str,
    quota: dict[str, str],
) -> dict[str, Any]:
    ml_buys = [compact_pick(row) for row in ml_predictions if row.get("recommendation") == "BUY"]
    rl_buys = [compact_pick(row) for row in rl_predictions if row.get("recommendation") == "BUY"]
    total_buys = [compact_pick(row) for row in total_predictions if row.get("recommendation") == "BUY"]
    ml_buys.sort(key=lambda row: float(row.get("ev") or 0.0), reverse=True)
    rl_buys.sort(key=lambda row: float(row.get("ev") or 0.0), reverse=True)
    total_buys.sort(key=lambda row: float(row.get("ev") or 0.0), reverse=True)

    target_dates = sorted({str(row.get("commence_time_utc", ""))[:10] for row in ml_predictions if row.get("commence_time_utc")})
    game_count = len({row.get("event_id") for row in ml_predictions if row.get("event_id")})

    return {
        "schema_version": "1.0",
        "model_version": MODEL_VERSION,
        "updated_at_utc": fetched_at,
        "target_dates_utc": target_dates,
        "game_count": game_count,
        "simulation_count_per_game": 100000,
        "buy_threshold_ev": 0.05,
        "kelly_fraction": 0.25,
        "source": {
            "odds": "Pinnacle via The Odds API",
            "baseball_data": "MLB Stats API",
        },
        "api_quota": {
            "requests_remaining": quota.get("requests_remaining", ""),
            "requests_used": quota.get("requests_used", ""),
            "requests_last": quota.get("requests_last", ""),
        },
        "summary": {
            "moneyline_buy_count": len(ml_buys),
            "runline_buy_count": len(rl_buys),
            "total_buy_count": len(total_buys),
            "best_moneyline": ml_buys[0] if ml_buys else None,
            "best_runline": rl_buys[0] if rl_buys else None,
            "best_total": total_buys[0] if total_buys else None,
        },
        "buy_rankings": {
            "moneyline": ml_buys,
            "runline": rl_buys,
            "total": total_buys,
        },
        "all_predictions": {
            "moneyline": [compact_pick(row) for row in ml_predictions],
            "runline": [compact_pick(row) for row in rl_predictions],
            "total": [compact_pick(row) for row in total_predictions],
        },
    }

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
        schedule = attach_lineups(schedule, season)
        schedule = attach_handedness(schedule)
        schedule = attach_weather(schedule)

        completed_games = fetch_completed_games(season)
        elo_ratings = build_elo_ratings(completed_games)
        team_metrics = fetch_team_metrics(season)
        bullpen_fatigue = fetch_bullpen_fatigue_proxy()

        ml_predictions, rl_predictions, total_predictions = make_predictions(
            odds_rows,
            elo_ratings,
            completed_games,
            schedule,
            team_metrics,
            bullpen_fatigue,
        )

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        fetched_at = datetime.now(timezone.utc).isoformat()

        payloads = {
            "latest_odds.json": {"fetched_at_utc": fetched_at, "events": odds_events},
            "mlb_schedule.json": {"fetched_at_utc": fetched_at, "games": schedule},
            "elo_ratings.json": {"fetched_at_utc": fetched_at, "ratings": elo_ratings},
            "team_metrics.json": {
                "fetched_at_utc": fetched_at,
                "metrics": team_metrics,
            },
            "bullpen_fatigue.json": {
                "fetched_at_utc": fetched_at,
                "fatigue": bullpen_fatigue,
            },
            "lineups_latest.json": {
                "fetched_at_utc": fetched_at,
                "games": [
                    {
                        "game_pk": game.get("game_pk"),
                        "game_date_utc": game.get("game_date_utc"),
                        "away_team": game.get("away_team"),
                        "home_team": game.get("home_team"),
                        "lineups": game.get("lineups"),
                    }
                    for game in schedule
                ],
            },
            "weather.json": {
                "fetched_at_utc": fetched_at,
                "games": [
                    {
                        "game_pk": game.get("game_pk"),
                        "away_team": game.get("away_team"),
                        "home_team": game.get("home_team"),
                        "game_date_utc": game.get("game_date_utc"),
                        "weather": game.get("weather"),
                    }
                    for game in schedule
                ],
            },
            "predictions.json": {
                "fetched_at_utc": fetched_at,
                "moneyline": ml_predictions,
                "runline": rl_predictions,
                "total": total_predictions,
            },
        }

        for filename, payload in payloads.items():
            (OUTPUT_DIR / filename).write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

        # Ver.25: publish one stable endpoint in all useful locations.
        latest_payload = build_latest_payload(
            ml_predictions, rl_predictions, total_predictions, fetched_at, quota
        )
        latest_json = json.dumps(latest_payload, ensure_ascii=False, indent=2)
        for latest_path in (
            OUTPUT_DIR / "prediction_latest.json",
            DOCS_DIR / "prediction_latest.json",
            Path("prediction_latest.json"),
        ):
            latest_path.write_text(latest_json, encoding="utf-8")

        write_csv(odds_rows, OUTPUT_DIR / "latest_odds.csv")
        write_csv(ml_predictions, OUTPUT_DIR / "moneyline_predictions.csv")
        write_csv(rl_predictions, OUTPUT_DIR / "runline_predictions.csv")
        write_csv(total_predictions, OUTPUT_DIR / "total_predictions.csv")
        # Backward-compatible endpoint used by ChatGPT: all markets in one CSV.
        combined_predictions = []
        for row in [*ml_predictions, *rl_predictions, *total_predictions]:
            combined_predictions.append({
                "model_version": MODEL_VERSION,
                "generated_at_utc": fetched_at,
                "target_date_utc": str(row.get("commence_time_utc", ""))[:10],
                **row,
            })
        # Publish the combined CSV both under data/ and at repository root.
        # The data/ path is the canonical ChatGPT endpoint; the root copy is a fallback.
        write_csv(combined_predictions, OUTPUT_DIR / "predictions.csv")
        write_csv(combined_predictions, Path("predictions.csv"))
        write_csv(ml_predictions, Path("moneyline_predictions.csv"))
        write_csv(rl_predictions, Path("runline_predictions.csv"))
        write_csv(total_predictions, Path("total_predictions.csv"))

        manifest = {
            "model_version": MODEL_VERSION,
            "generated_at_utc": fetched_at,
            "moneyline_rows": len(ml_predictions),
            "runline_rows": len(rl_predictions),
            "total_rows": len(total_predictions),
            "combined_rows": len(combined_predictions),
            "canonical_csv": "data/predictions.csv",
            "canonical_json": "data/prediction_latest.json",
        }
        manifest_json = json.dumps(manifest, ensure_ascii=False, indent=2)
        (OUTPUT_DIR / "output_manifest.json").write_text(manifest_json, encoding="utf-8")
        Path("output_manifest.json").write_text(manifest_json, encoding="utf-8")

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
            f"{len(rl_predictions)} RL predictions and "
            f"{len(total_predictions)} total predictions."
        )
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
