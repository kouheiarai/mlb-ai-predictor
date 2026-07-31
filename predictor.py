from __future__ import annotations

import hashlib
import math
import re
from collections import defaultdict, deque
from datetime import date
from typing import Any

import numpy as np
import requests


MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"
DEFAULT_ELO = 1500.0
K_FACTOR = 20.0
HOME_FIELD_ELO = 35.0
LEAGUE_RUNS_PER_TEAM = 4.40
SIMULATIONS = 100_000

TEAM_ALIASES = {
    "athletics": "oakland athletics",
    "los angeles angels": "los angeles angels",
    "la angels": "los angeles angels",
    "arizona diamondbacks": "arizona diamondbacks",
    "d backs": "arizona diamondbacks",
}

PARK_FACTORS = {
    "colorado rockies": 1.12,
    "boston red sox": 1.05,
    "cincinnati reds": 1.04,
    "philadelphia phillies": 1.03,
    "new york yankees": 1.03,
    "los angeles dodgers": 1.01,
    "seattle mariners": 0.96,
    "san francisco giants": 0.96,
    "san diego padres": 0.97,
    "tampa bay rays": 0.98,
}


def normalize_team(name: str) -> str:
    value = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
    return TEAM_ALIASES.get(value, value)


def fetch_completed_games(season: int | None = None) -> list[dict[str, Any]]:
    season = season or date.today().year
    response = requests.get(
        MLB_SCHEDULE_URL,
        params={
            "sportId": 1,
            "season": season,
            "gameType": "R",
            "hydrate": "team",
        },
        timeout=60,
    )
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
        multiplier = math.log(max(margin, 1) + 1) * (
            2.2 / ((abs(home_elo - away_elo) * 0.001) + 2.2)
        )
        change = K_FACTOR * multiplier * (actual_home - expected_home)

        ratings[home_team] += change
        ratings[away_team] -= change

    return dict(ratings)


def build_recent_form(
    completed_games: list[dict[str, Any]],
    window: int = 10,
) -> dict[str, float]:
    results: defaultdict[str, deque[int]] = defaultdict(
        lambda: deque(maxlen=window)
    )

    for game in completed_games:
        away = normalize_team(game["away_team"])
        home = normalize_team(game["home_team"])
        home_win = game["home_score"] > game["away_score"]
        results[home].append(1 if home_win else 0)
        results[away].append(0 if home_win else 1)

    return {
        team: sum(values) / len(values)
        for team, values in results.items()
        if values
    }


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

    return max(-1.0, min(1.0, sum(parts) / len(parts))) if parts else 0.0


def _lookup_metrics(
    team_name: str,
    team_metrics: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    wanted = normalize_team(team_name)
    for name, values in team_metrics.items():
        if normalize_team(name) == wanted:
            return values
    return {}


def schedule_index(
    schedule: list[dict[str, Any]],
) -> dict[tuple[str, str], dict[str, Any]]:
    return {
        (
            normalize_team(game.get("away_team", "")),
            normalize_team(game.get("home_team", "")),
        ): game
        for game in schedule
    }


def expected_runs(
    offense_metrics: dict[str, Any],
    opponent_pitching_metrics: dict[str, Any],
    opponent_starter_quality: float,
    recent_form: float,
    park_factor: float,
    home: bool,
) -> float:
    offense_rpg = offense_metrics.get("runs_per_game")
    if not isinstance(offense_rpg, (int, float)):
        offense_rpg = LEAGUE_RUNS_PER_TEAM

    opponent_era = opponent_pitching_metrics.get("team_pitching_era")
    if not isinstance(opponent_era, (int, float)):
        opponent_era = 4.20

    offense_factor = max(0.70, min(1.30, offense_rpg / LEAGUE_RUNS_PER_TEAM))
    pitching_factor = max(0.75, min(1.30, opponent_era / 4.20))
    starter_factor = max(0.80, min(1.20, 1.0 - opponent_starter_quality * 0.12))
    form_factor = max(0.90, min(1.10, 1.0 + (recent_form - 0.5) * 0.20))
    home_factor = 1.025 if home else 0.985

    lam = (
        LEAGUE_RUNS_PER_TEAM
        * offense_factor
        * pitching_factor
        * starter_factor
        * form_factor
        * park_factor
        * home_factor
    )
    return max(2.2, min(7.5, lam))


def deterministic_seed(event_id: str) -> int:
    digest = hashlib.sha256(event_id.encode("utf-8")).hexdigest()
    return int(digest[:16], 16) % (2**32)


def simulate_game(
    event_id: str,
    away_lambda: float,
    home_lambda: float,
) -> dict[str, float]:
    rng = np.random.default_rng(deterministic_seed(event_id))
    away_runs = rng.poisson(away_lambda, SIMULATIONS)
    home_runs = rng.poisson(home_lambda, SIMULATIONS)

    ties = away_runs == home_runs
    while np.any(ties):
        tie_count = int(np.sum(ties))
        home_extra = rng.binomial(1, 0.52, tie_count)
        away_extra = 1 - home_extra
        away_runs[ties] += away_extra
        home_runs[ties] += home_extra
        ties = away_runs == home_runs

    home_ml = float(np.mean(home_runs > away_runs))
    away_ml = 1.0 - home_ml

    return {
        "away_ml": away_ml,
        "home_ml": home_ml,
        "away_minus_1_5": float(np.mean((away_runs - home_runs) >= 2)),
        "away_plus_1_5": float(np.mean((away_runs - home_runs) >= -1)),
        "home_minus_1_5": float(np.mean((home_runs - away_runs) >= 2)),
        "home_plus_1_5": float(np.mean((home_runs - away_runs) >= -1)),
        "away_expected_runs": float(np.mean(away_runs)),
        "home_expected_runs": float(np.mean(home_runs)),
    }


def make_predictions(
    odds_rows: list[dict[str, Any]],
    elo_ratings: dict[str, float],
    completed_games: list[dict[str, Any]],
    schedule: list[dict[str, Any]],
    team_metrics: dict[str, dict[str, Any]],
    market_weight: float = 0.15,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    by_event: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in odds_rows:
        by_event[str(row.get("event_id", ""))].append(row)

    recent_form = build_recent_form(completed_games)
    schedule_by_matchup = schedule_index(schedule)
    ml_predictions: list[dict[str, Any]] = []
    rl_predictions: list[dict[str, Any]] = []

    for event_id, rows in by_event.items():
        if not rows:
            continue

        first = rows[0]
        away_team = first["away_team"]
        home_team = first["home_team"]
        away_key = normalize_team(away_team)
        home_key = normalize_team(home_team)

        game = schedule_by_matchup.get((away_key, home_key), {})
        away_starter = starter_quality(game.get("away_starter_stats"))
        home_starter = starter_quality(game.get("home_starter_stats"))

        away_metrics = _lookup_metrics(away_team, team_metrics)
        home_metrics = _lookup_metrics(home_team, team_metrics)
        away_form = recent_form.get(away_key, 0.5)
        home_form = recent_form.get(home_key, 0.5)
        park = PARK_FACTORS.get(home_key, 1.0)

        away_lambda = expected_runs(
            away_metrics,
            home_metrics,
            home_starter,
            away_form,
            park,
            home=False,
        )
        home_lambda = expected_runs(
            home_metrics,
            away_metrics,
            away_starter,
            home_form,
            park,
            home=True,
        )

        sim = simulate_game(event_id, away_lambda, home_lambda)

        h2h_rows = [row for row in rows if row.get("market") == "h2h"]
        if len(h2h_rows) == 2:
            by_selection = {row["selection"]: row for row in h2h_rows}
            away_row = by_selection.get(away_team)
            home_row = by_selection.get(home_team)

            if away_row and home_row:
                away_price = float(away_row["decimal_odds"])
                home_price = float(home_row["decimal_odds"])
                market_away, market_home = remove_vig_two_way(
                    away_price,
                    home_price,
                )

                model_away = (
                    (1.0 - market_weight) * sim["away_ml"]
                    + market_weight * market_away
                )
                model_home = 1.0 - model_away

                for team, price, probability, market_probability in [
                    (away_team, away_price, model_away, market_away),
                    (home_team, home_price, model_home, market_home),
                ]:
                    ev = expected_value(probability, price)
                    ml_predictions.append(
                        {
                            "market": "moneyline",
                            "event_id": event_id,
                            "commence_time_utc": first["commence_time_utc"],
                            "away_team": away_team,
                            "home_team": home_team,
                            "selection": team,
                            "point": "",
                            "decimal_odds": round(price, 3),
                            "market_no_vig_probability": round(market_probability, 6),
                            "model_probability": round(probability, 6),
                            "ev": round(ev, 6),
                            "quarter_kelly": round(
                                quarter_kelly(probability, price),
                                6,
                            ),
                            "away_expected_runs": round(
                                sim["away_expected_runs"],
                                3,
                            ),
                            "home_expected_runs": round(
                                sim["home_expected_runs"],
                                3,
                            ),
                            "simulations": SIMULATIONS,
                            "recommendation": (
                                "BUY"
                                if ev >= 0.05
                                else ("LEAN" if ev > 0 else "PASS")
                            ),
                        }
                    )

        spread_rows = [row for row in rows if row.get("market") == "spreads"]
        for row in spread_rows:
            team = row["selection"]
            point = float(row["point"])
            price = float(row["decimal_odds"])

            if team == away_team:
                probability = (
                    sim["away_minus_1_5"]
                    if point <= -1.5
                    else sim["away_plus_1_5"]
                )
            elif team == home_team:
                probability = (
                    sim["home_minus_1_5"]
                    if point <= -1.5
                    else sim["home_plus_1_5"]
                )
            else:
                continue

            ev = expected_value(probability, price)
            rl_predictions.append(
                {
                    "market": "runline",
                    "event_id": event_id,
                    "commence_time_utc": first["commence_time_utc"],
                    "away_team": away_team,
                    "home_team": home_team,
                    "selection": team,
                    "point": point,
                    "decimal_odds": round(price, 3),
                    "model_probability": round(probability, 6),
                    "ev": round(ev, 6),
                    "quarter_kelly": round(
                        quarter_kelly(probability, price),
                        6,
                    ),
                    "away_expected_runs": round(
                        sim["away_expected_runs"],
                        3,
                    ),
                    "home_expected_runs": round(
                        sim["home_expected_runs"],
                        3,
                    ),
                    "simulations": SIMULATIONS,
                    "recommendation": (
                        "BUY"
                        if ev >= 0.05
                        else ("LEAN" if ev > 0 else "PASS")
                    ),
                }
            )

    ml_predictions.sort(key=lambda row: row["ev"], reverse=True)
    rl_predictions.sort(key=lambda row: row["ev"], reverse=True)
    return ml_predictions, rl_predictions
