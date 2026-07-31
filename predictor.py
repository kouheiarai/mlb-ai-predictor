from __future__ import annotations

import math
import re
from collections import defaultdict, deque
from datetime import date
from typing import Any

import requests

MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"
DEFAULT_ELO = 1500.0
K_FACTOR = 20.0
HOME_FIELD_ELO = 35.0

TEAM_ALIASES = {
    "athletics": "oakland athletics",
    "la angels": "los angeles angels",
    "d backs": "arizona diamondbacks",
}


def normalize_team(name: str) -> str:
    value = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
    return TEAM_ALIASES.get(value, value)


def fetch_completed_games(season: int | None = None) -> list[dict[str, Any]]:
    season = season or date.today().year
    params = {"sportId": 1, "season": season, "gameType": "R", "hydrate": "team"}
    response = requests.get(MLB_SCHEDULE_URL, params=params, timeout=60)
    response.raise_for_status()
    games: list[dict[str, Any]] = []
    for date_block in response.json().get("dates", []):
        for game in date_block.get("games", []):
            if game.get("status", {}).get("abstractGameState") != "Final":
                continue
            away = game.get("teams", {}).get("away", {})
            home = game.get("teams", {}).get("home", {})
            away_score = away.get("score")
            home_score = home.get("score")
            if away_score is None or home_score is None:
                continue
            games.append({
                "game_date": game.get("gameDate", ""),
                "away_team": away.get("team", {}).get("name", ""),
                "home_team": home.get("team", {}).get("name", ""),
                "away_score": int(away_score),
                "home_score": int(home_score),
            })
    games.sort(key=lambda game: game["game_date"])
    return games


def expected_home_win_probability(home_elo: float, away_elo: float) -> float:
    adjusted_home_elo = home_elo + HOME_FIELD_ELO
    return 1.0 / (1.0 + 10 ** ((away_elo - adjusted_home_elo) / 400.0))


def build_elo_ratings(completed_games: list[dict[str, Any]]) -> dict[str, float]:
    ratings: defaultdict[str, float] = defaultdict(lambda: DEFAULT_ELO)
    for game in completed_games:
        away_team = normalize_team(game["away_team"])
        home_team = normalize_team(game["home_team"])
        away_score = game["away_score"]
        home_score = game["home_score"]
        away_elo = ratings[away_team]
        home_elo = ratings[home_team]
        expected_home = expected_home_win_probability(home_elo, away_elo)
        actual_home = 1.0 if home_score > away_score else 0.0
        margin = abs(home_score - away_score)
        multiplier = math.log(max(margin, 1) + 1) * (2.2 / ((abs(home_elo - away_elo) * 0.001) + 2.2))
        change = K_FACTOR * multiplier * (actual_home - expected_home)
        ratings[home_team] += change
        ratings[away_team] -= change
    return dict(ratings)


def build_recent_form(completed_games: list[dict[str, Any]], window: int = 10) -> dict[str, float]:
    results: defaultdict[str, deque[int]] = defaultdict(lambda: deque(maxlen=window))
    for game in completed_games:
        away = normalize_team(game["away_team"])
        home = normalize_team(game["home_team"])
        home_win = game["home_score"] > game["away_score"]
        results[home].append(1 if home_win else 0)
        results[away].append(0 if home_win else 1)
    return {team: sum(values) / len(values) for team, values in results.items() if values}


def remove_vig_two_way(price_a: float, price_b: float) -> tuple[float, float]:
    implied_a = 1.0 / price_a
    implied_b = 1.0 / price_b
    total = implied_a + implied_b
    return (implied_a / total, implied_b / total) if total > 0 else (0.5, 0.5)


def quarter_kelly(probability: float, decimal_odds: float) -> float:
    if decimal_odds <= 1.0:
        return 0.0
    b = decimal_odds - 1.0
    full_kelly = ((b * probability) - (1.0 - probability)) / b
    return max(0.0, full_kelly / 4.0)


def expected_value(probability: float, decimal_odds: float) -> float:
    return (probability * decimal_odds) - 1.0


def starter_quality(stats: dict[str, Any] | None) -> float:
    if not stats:
        return 0.0
    era = stats.get("era")
    whip = stats.get("whip")
    kbb = stats.get("strikeout_walk_ratio")
    ip = stats.get("innings_pitched")
    if not isinstance(ip, (int, float)) or ip < 10:
        return 0.0
    parts: list[float] = []
    if isinstance(era, (int, float)):
        parts.append((4.20 - era) / 1.50)
    if isinstance(whip, (int, float)):
        parts.append((1.30 - whip) / 0.35)
    if isinstance(kbb, (int, float)):
        parts.append((kbb - 2.80) / 2.00)
    if not parts:
        return 0.0
    return max(-1.0, min(1.0, sum(parts) / len(parts)))


def make_moneyline_predictions(odds_rows: list[dict[str, Any]], elo_ratings: dict[str, float], completed_games: list[dict[str, Any]], schedule: list[dict[str, Any]], market_weight: float = 0.25) -> list[dict[str, Any]]:
    games: dict[str, list[dict[str, Any]]] = {}
    for row in odds_rows:
        if row.get("market") == "h2h":
            games.setdefault(str(row.get("event_id", "")), []).append(row)
    recent_form = build_recent_form(completed_games)
    schedule_by_matchup = {(normalize_team(g.get("away_team", "")), normalize_team(g.get("home_team", ""))): g for g in schedule}
    predictions: list[dict[str, Any]] = []
    for event_id, rows in games.items():
        if len(rows) != 2:
            continue
        first = rows[0]
        away_team = first["away_team"]
        home_team = first["home_team"]
        away_key = normalize_team(away_team)
        home_key = normalize_team(home_team)
        by_selection = {row["selection"]: row for row in rows}
        away_row = by_selection.get(away_team)
        home_row = by_selection.get(home_team)
        if not away_row or not home_row:
            continue
        away_price = float(away_row["decimal_odds"])
        home_price = float(home_row["decimal_odds"])
        market_away, market_home = remove_vig_two_way(away_price, home_price)
        away_elo = elo_ratings.get(away_key, DEFAULT_ELO)
        home_elo = elo_ratings.get(home_key, DEFAULT_ELO)
        elo_home = expected_home_win_probability(home_elo, away_elo)
        game = schedule_by_matchup.get((away_key, home_key), {})
        away_starter = starter_quality(game.get("away_starter_stats"))
        home_starter = starter_quality(game.get("home_starter_stats"))
        starter_adjustment = (home_starter - away_starter) * 0.045
        away_form = recent_form.get(away_key, 0.5)
        home_form = recent_form.get(home_key, 0.5)
        form_adjustment = (home_form - away_form) * 0.06
        baseball_home = max(0.20, min(0.80, elo_home + starter_adjustment + form_adjustment))
        model_home = (1.0 - market_weight) * baseball_home + market_weight * market_home
        model_home = max(0.05, min(0.95, model_home))
        model_away = 1.0 - model_home
        for team, price, probability, market_probability, rating, starter, form in [
            (away_team, away_price, model_away, market_away, away_elo, away_starter, away_form),
            (home_team, home_price, model_home, market_home, home_elo, home_starter, home_form),
        ]:
            ev = expected_value(probability, price)
            kelly = quarter_kelly(probability, price)
            recommendation = "BUY" if ev >= 0.05 else ("LEAN" if ev > 0 else "PASS")
            predictions.append({
                "event_id": event_id,
                "commence_time_utc": first["commence_time_utc"],
                "away_team": away_team,
                "home_team": home_team,
                "selection": team,
                "decimal_odds": round(price, 3),
                "market_no_vig_probability": round(market_probability, 6),
                "elo_rating": round(rating, 1),
                "recent_10_win_pct": round(form, 4),
                "starter_quality": round(starter, 4),
                "model_probability": round(probability, 6),
                "ev": round(ev, 6),
                "quarter_kelly": round(kelly, 6),
                "recommendation": recommendation,
            })
    predictions.sort(key=lambda row: (row["ev"], row["model_probability"]), reverse=True)
    return predictions
