from __future__ import annotations

import math
from collections import defaultdict
from datetime import date
from typing import Any

import requests


MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"
DEFAULT_ELO = 1500.0
K_FACTOR = 20.0
HOME_FIELD_ELO = 35.0


def fetch_completed_games(season: int | None = None) -> list[dict[str, Any]]:
    """Fetch completed MLB regular-season games for Elo calculation."""
    season = season or date.today().year

    params = {
        "sportId": 1,
        "season": season,
        "gameType": "R",
        "hydrate": "team",
    }

    response = requests.get(MLB_SCHEDULE_URL, params=params, timeout=60)
    response.raise_for_status()

    games: list[dict[str, Any]] = []

    for date_block in response.json().get("dates", []):
        for game in date_block.get("games", []):
            status = game.get("status", {}).get("abstractGameState", "")
            if status != "Final":
                continue

            away = game.get("teams", {}).get("away", {})
            home = game.get("teams", {}).get("home", {})

            away_score = away.get("score")
            home_score = home.get("score")

            if away_score is None or home_score is None:
                continue

            games.append(
                {
                    "game_date": game.get("gameDate", ""),
                    "away_team": away.get("team", {}).get("name", ""),
                    "home_team": home.get("team", {}).get("name", ""),
                    "away_score": int(away_score),
                    "home_score": int(home_score),
                }
            )

    games.sort(key=lambda game: game["game_date"])
    return games


def expected_home_win_probability(
    home_elo: float,
    away_elo: float,
) -> float:
    adjusted_home_elo = home_elo + HOME_FIELD_ELO
    return 1.0 / (1.0 + 10 ** ((away_elo - adjusted_home_elo) / 400.0))


def build_elo_ratings(
    completed_games: list[dict[str, Any]],
) -> dict[str, float]:
    ratings: defaultdict[str, float] = defaultdict(lambda: DEFAULT_ELO)

    for game in completed_games:
        away_team = game["away_team"]
        home_team = game["home_team"]
        away_score = game["away_score"]
        home_score = game["home_score"]

        away_elo = ratings[away_team]
        home_elo = ratings[home_team]
        expected_home = expected_home_win_probability(home_elo, away_elo)

        if home_score > away_score:
            actual_home = 1.0
        else:
            actual_home = 0.0

        margin = abs(home_score - away_score)
        margin_multiplier = math.log(max(margin, 1) + 1) * (
            2.2 / ((abs(home_elo - away_elo) * 0.001) + 2.2)
        )

        change = K_FACTOR * margin_multiplier * (actual_home - expected_home)

        ratings[home_team] += change
        ratings[away_team] -= change

    return dict(ratings)


def remove_vig_two_way(
    price_a: float,
    price_b: float,
) -> tuple[float, float]:
    implied_a = 1.0 / price_a
    implied_b = 1.0 / price_b
    total = implied_a + implied_b

    if total <= 0:
        return 0.5, 0.5

    return implied_a / total, implied_b / total


def quarter_kelly(
    probability: float,
    decimal_odds: float,
) -> float:
    if decimal_odds <= 1.0:
        return 0.0

    b = decimal_odds - 1.0
    q = 1.0 - probability
    full_kelly = ((b * probability) - q) / b
    return max(0.0, full_kelly / 4.0)


def expected_value(
    probability: float,
    decimal_odds: float,
) -> float:
    return (probability * decimal_odds) - 1.0


def make_moneyline_predictions(
    odds_rows: list[dict[str, Any]],
    elo_ratings: dict[str, float],
    market_weight: float = 0.35,
) -> list[dict[str, Any]]:
    """Create transparent Elo + market blended ML predictions."""
    games: dict[str, list[dict[str, Any]]] = {}

    for row in odds_rows:
        if row.get("market") != "h2h":
            continue
        games.setdefault(str(row.get("event_id", "")), []).append(row)

    predictions: list[dict[str, Any]] = []

    for event_id, rows in games.items():
        if len(rows) != 2:
            continue

        first = rows[0]
        away_team = first["away_team"]
        home_team = first["home_team"]

        by_selection = {row["selection"]: row for row in rows}
        away_row = by_selection.get(away_team)
        home_row = by_selection.get(home_team)

        if not away_row or not home_row:
            continue

        away_price = float(away_row["decimal_odds"])
        home_price = float(home_row["decimal_odds"])

        market_away, market_home = remove_vig_two_way(
            away_price,
            home_price,
        )

        away_elo = elo_ratings.get(away_team, DEFAULT_ELO)
        home_elo = elo_ratings.get(home_team, DEFAULT_ELO)
        elo_home = expected_home_win_probability(home_elo, away_elo)
        elo_away = 1.0 - elo_home

        model_home = (
            (1.0 - market_weight) * elo_home
            + market_weight * market_home
        )
        model_away = 1.0 - model_home

        for team, price, probability, market_probability, rating in [
            (away_team, away_price, model_away, market_away, away_elo),
            (home_team, home_price, model_home, market_home, home_elo),
        ]:
            ev = expected_value(probability, price)
            kelly = quarter_kelly(probability, price)

            if ev >= 0.05:
                recommendation = "BUY"
            elif ev > 0:
                recommendation = "LEAN"
            else:
                recommendation = "PASS"

            predictions.append(
                {
                    "event_id": event_id,
                    "commence_time_utc": first["commence_time_utc"],
                    "away_team": away_team,
                    "home_team": home_team,
                    "selection": team,
                    "decimal_odds": round(price, 3),
                    "market_no_vig_probability": round(
                        market_probability,
                        6,
                    ),
                    "elo_rating": round(rating, 1),
                    "model_probability": round(probability, 6),
                    "ev": round(ev, 6),
                    "quarter_kelly": round(kelly, 6),
                    "recommendation": recommendation,
                }
            )

    predictions.sort(
        key=lambda row: (row["ev"], row["model_probability"]),
        reverse=True,
    )
    return predictions
