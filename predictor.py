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
    "la angels": "los angeles angels",
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
        params={"sportId": 1, "season": season, "gameType": "R", "hydrate": "team"},
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
    return 1.0 / (
        1.0 + 10 ** ((away_elo - (home_elo + HOME_FIELD_ELO)) / 400.0)
    )


def build_elo_ratings(completed_games: list[dict[str, Any]]) -> dict[str, float]:
    ratings: defaultdict[str, float] = defaultdict(lambda: DEFAULT_ELO)

    for game in completed_games:
        away = normalize_team(game["away_team"])
        home = normalize_team(game["home_team"])
        away_elo = ratings[away]
        home_elo = ratings[home]
        expected_home = expected_home_win_probability(home_elo, away_elo)
        actual_home = 1.0 if game["home_score"] > game["away_score"] else 0.0
        margin = abs(game["home_score"] - game["away_score"])
        multiplier = math.log(max(margin, 1) + 1) * (
            2.2 / ((abs(home_elo - away_elo) * 0.001) + 2.2)
        )
        change = K_FACTOR * multiplier * (actual_home - expected_home)
        ratings[home] += change
        ratings[away] -= change

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


def lineup_quality(
    lineup: list[dict[str, Any]],
    announced: bool,
) -> float:
    if not announced or len(lineup) < 8:
        return 0.0

    weights = [1.10, 1.08, 1.15, 1.18, 1.05, 0.95, 0.90, 0.85, 0.80]
    weighted_scores = []
    used_weights = []

    for index, hitter in enumerate(lineup[:9]):
        stats = hitter.get("season_stats", {})
        ops = stats.get("ops")
        pa = stats.get("plate_appearances")

        if not isinstance(ops, (int, float)):
            continue

        reliability = 1.0
        if isinstance(pa, (int, float)):
            reliability = max(0.35, min(1.0, pa / 250.0))

        score = ((ops - 0.720) / 0.120) * reliability
        weight = weights[index]
        weighted_scores.append(score * weight)
        used_weights.append(weight)

    if not weighted_scores:
        return 0.0

    return max(
        -1.0,
        min(1.0, sum(weighted_scores) / sum(used_weights)),
    )


def platoon_proxy(
    lineup: list[dict[str, Any]],
    pitcher_hand: str | None,
    announced: bool,
) -> float:
    """
    打者の打席側と先発の投球側から-1〜+1の代理補正を作る。

    S打者は小幅プラス、逆側打者はプラス、同側打者はマイナス。
    左右別実績そのものではないため、補正幅は小さく制限する。
    """
    if not announced or not pitcher_hand or len(lineup) < 8:
        return 0.0

    weights = [1.10, 1.08, 1.15, 1.18, 1.05, 0.95, 0.90, 0.85, 0.80]
    values = []

    for index, hitter in enumerate(lineup[:9]):
        bat_side = hitter.get("bat_side")

        if bat_side == "S":
            value = 0.35
        elif bat_side and bat_side != pitcher_hand:
            value = 0.25
        elif bat_side and bat_side == pitcher_hand:
            value = -0.20
        else:
            value = 0.0

        values.append(value * weights[index])

    score = sum(values) / sum(weights[: len(values)])
    return max(-1.0, min(1.0, score))


def _lookup(team_name: str, source: dict[str, dict[str, Any]]) -> dict[str, Any]:
    wanted = normalize_team(team_name)
    for name, values in source.items():
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
    opponent_bullpen_fatigue: float,
    recent_form: float,
    lineup_adjustment: float,
    platoon_adjustment: float,
    park_factor: float,
    weather_run_factor: float,
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
    bullpen_factor = max(1.0, min(1.18, 1.0 + opponent_bullpen_fatigue * 0.12))
    form_factor = max(0.90, min(1.10, 1.0 + (recent_form - 0.5) * 0.20))
    lineup_factor = max(0.88, min(1.12, 1.0 + lineup_adjustment * 0.10))
    platoon_factor = max(0.96, min(1.04, 1.0 + platoon_adjustment * 0.04))
    home_factor = 1.025 if home else 0.985

    lam = (
        LEAGUE_RUNS_PER_TEAM
        * offense_factor
        * pitching_factor
        * starter_factor
        * bullpen_factor
        * form_factor
        * lineup_factor
        * platoon_factor
        * park_factor
        * weather_run_factor
        * home_factor
    )
    return max(2.2, min(8.0, lam))


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
    return {
        "away_ml": 1.0 - home_ml,
        "home_ml": home_ml,
        "away_minus_1_5": float(np.mean((away_runs - home_runs) >= 2)),
        "away_plus_1_5": float(np.mean((away_runs - home_runs) >= -1)),
        "home_minus_1_5": float(np.mean((home_runs - away_runs) >= 2)),
        "home_plus_1_5": float(np.mean((home_runs - away_runs) >= -1)),
        "away_expected_runs": float(np.mean(away_runs)),
        "home_expected_runs": float(np.mean(home_runs)),
    }


def simulate_total_probability(
    event_id: str,
    away_lambda: float,
    home_lambda: float,
    total_line: float,
) -> tuple[float, float, float]:
    """Return over, under, and push probabilities using a separate deterministic draw."""
    rng = np.random.default_rng(deterministic_seed(f"{event_id}:total:{total_line}"))
    totals = rng.poisson(away_lambda, SIMULATIONS) + rng.poisson(home_lambda, SIMULATIONS)
    over = float(np.mean(totals > total_line))
    under = float(np.mean(totals < total_line))
    push = max(0.0, 1.0 - over - under)
    return over, under, push


def make_predictions(
    odds_rows: list[dict[str, Any]],
    elo_ratings: dict[str, float],
    completed_games: list[dict[str, Any]],
    schedule: list[dict[str, Any]],
    team_metrics: dict[str, dict[str, Any]],
    bullpen_fatigue: dict[str, dict[str, Any]],
    market_weight: float = 0.15,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    by_event: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in odds_rows:
        by_event[str(row.get("event_id", ""))].append(row)

    recent_form = build_recent_form(completed_games)
    schedule_by_matchup = schedule_index(schedule)
    ml_predictions: list[dict[str, Any]] = []
    rl_predictions: list[dict[str, Any]] = []
    total_predictions: list[dict[str, Any]] = []

    for event_id, rows in by_event.items():
        first = rows[0]
        away_team = first["away_team"]
        home_team = first["home_team"]
        away_key = normalize_team(away_team)
        home_key = normalize_team(home_team)

        game = schedule_by_matchup.get((away_key, home_key), {})
        away_starter = starter_quality(game.get("away_starter_stats"))
        home_starter = starter_quality(game.get("home_starter_stats"))

        lineups = game.get("lineups", {})
        away_announced = bool(lineups.get("away_announced"))
        home_announced = bool(lineups.get("home_announced"))
        away_status = str(lineups.get("away_lineup_status") or ("official" if away_announced else "unavailable"))
        home_status = str(lineups.get("home_lineup_status") or ("official" if home_announced else "unavailable"))
        away_reliability = float(lineups.get("away_lineup_reliability") or (1.0 if away_announced else 0.0))
        home_reliability = float(lineups.get("home_lineup_reliability") or (1.0 if home_announced else 0.0))
        away_reliability = max(0.0, min(1.0, away_reliability))
        home_reliability = max(0.0, min(1.0, home_reliability))
        away_lineup = lineups.get("away_batting_order", [])
        home_lineup = lineups.get("home_batting_order", [])
        away_usable = away_status in {"official", "predicted"} and len(away_lineup) >= 8
        home_usable = home_status in {"official", "predicted"} and len(home_lineup) >= 8

        away_lineup_quality_raw = lineup_quality(away_lineup, away_usable)
        home_lineup_quality_raw = lineup_quality(home_lineup, home_usable)
        away_lineup_quality = away_lineup_quality_raw * away_reliability
        home_lineup_quality = home_lineup_quality_raw * home_reliability

        away_platoon_raw = platoon_proxy(
            away_lineup,
            game.get("home_probable_pitcher_hand"),
            away_usable,
        )
        home_platoon_raw = platoon_proxy(
            home_lineup,
            game.get("away_probable_pitcher_hand"),
            home_usable,
        )
        away_platoon = away_platoon_raw * away_reliability
        home_platoon = home_platoon_raw * home_reliability

        away_metrics = _lookup(away_team, team_metrics)
        home_metrics = _lookup(home_team, team_metrics)
        away_bullpen = _lookup(away_team, bullpen_fatigue)
        home_bullpen = _lookup(home_team, bullpen_fatigue)

        away_fatigue = float(away_bullpen.get("fatigue_score") or 0.0)
        home_fatigue = float(home_bullpen.get("fatigue_score") or 0.0)
        away_form = recent_form.get(away_key, 0.5)
        home_form = recent_form.get(home_key, 0.5)
        park = PARK_FACTORS.get(home_key, 1.0)
        weather = game.get("weather") or {}
        weather_run_factor = float(weather.get("weather_run_factor") or 1.0)

        away_lambda = expected_runs(
            away_metrics,
            home_metrics,
            home_starter,
            home_fatigue,
            away_form,
            away_lineup_quality,
            away_platoon,
            park,
            weather_run_factor,
            home=False,
        )
        home_lambda = expected_runs(
            home_metrics,
            away_metrics,
            away_starter,
            away_fatigue,
            home_form,
            home_lineup_quality,
            home_platoon,
            park,
            weather_run_factor,
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

                selections = [
                    (
                        away_team,
                        away_price,
                        model_away,
                        market_away,
                        away_fatigue,
                        away_announced,
                        away_lineup_quality,
                        away_platoon,
                    ),
                    (
                        home_team,
                        home_price,
                        model_home,
                        market_home,
                        home_fatigue,
                        home_announced,
                        home_lineup_quality,
                        home_platoon,
                    ),
                ]

                for (
                    team,
                    price,
                    probability,
                    market_probability,
                    fatigue,
                    lineup_announced,
                    lineup_score,
                    platoon_score,
                ) in selections:
                    ev = expected_value(probability, price)
                    ml_predictions.append(
                        {
                            "market": "moneyline",
                            "event_id": event_id,
                            "commence_time_utc": first["commence_time_utc"],
                            "away_team": away_team,
                            "home_team": home_team,
                            "away_probable_pitcher": game.get("away_probable_pitcher"),
                            "home_probable_pitcher": game.get("home_probable_pitcher"),
                            "away_starter_quality": round(away_starter, 4),
                            "home_starter_quality": round(home_starter, 4),
                            "away_elo": round(float(elo_ratings.get(away_key, DEFAULT_ELO)), 2),
                            "home_elo": round(float(elo_ratings.get(home_key, DEFAULT_ELO)), 2),
                            "away_recent_form": round(away_form, 4),
                            "home_recent_form": round(home_form, 4),
                            "park_factor": round(park, 4),
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
                            "bullpen_fatigue": round(fatigue, 4),
                            "lineup_announced": lineup_announced,
                            "lineup_status": away_status if team == away_team else home_status,
                            "lineup_reliability": round(away_reliability if team == away_team else home_reliability, 4),
                            "lineup_confidence": lineups.get("away_lineup_confidence") if team == away_team else lineups.get("home_lineup_confidence"),
                            "lineup_quality": round(lineup_score, 4),
                            "platoon_proxy": round(platoon_score, 4),
                            "weather_run_factor": round(weather_run_factor, 4),
                            "temperature_c": weather.get("temperature_c"),
                            "precipitation_probability": weather.get(
                                "precipitation_probability"
                            ),
                            "wind_speed_kmh": weather.get("wind_speed_kmh"),
                            "wind_direction_deg": weather.get("wind_direction_deg"),
                            "away_expected_runs": round(sim["away_expected_runs"], 3),
                            "home_expected_runs": round(sim["home_expected_runs"], 3),
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
                fatigue = away_fatigue
                announced = away_announced
                lineup_score = away_lineup_quality
                platoon_score = away_platoon
            elif team == home_team:
                probability = (
                    sim["home_minus_1_5"]
                    if point <= -1.5
                    else sim["home_plus_1_5"]
                )
                fatigue = home_fatigue
                announced = home_announced
                lineup_score = home_lineup_quality
                platoon_score = home_platoon
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
                    "away_probable_pitcher": game.get("away_probable_pitcher"),
                    "home_probable_pitcher": game.get("home_probable_pitcher"),
                    "away_starter_quality": round(away_starter, 4),
                    "home_starter_quality": round(home_starter, 4),
                    "away_elo": round(float(elo_ratings.get(away_key, DEFAULT_ELO)), 2),
                    "home_elo": round(float(elo_ratings.get(home_key, DEFAULT_ELO)), 2),
                    "away_recent_form": round(away_form, 4),
                    "home_recent_form": round(home_form, 4),
                    "park_factor": round(park, 4),
                    "selection": team,
                    "point": point,
                    "decimal_odds": round(price, 3),
                    "model_probability": round(probability, 6),
                    "ev": round(ev, 6),
                    "quarter_kelly": round(
                        quarter_kelly(probability, price),
                        6,
                    ),
                    "bullpen_fatigue": round(fatigue, 4),
                    "lineup_announced": announced,
                    "lineup_status": away_status if team == away_team else home_status,
                    "lineup_reliability": round(away_reliability if team == away_team else home_reliability, 4),
                    "lineup_confidence": lineups.get("away_lineup_confidence") if team == away_team else lineups.get("home_lineup_confidence"),
                    "lineup_quality": round(lineup_score, 4),
                    "platoon_proxy": round(platoon_score, 4),
                    "weather_run_factor": round(weather_run_factor, 4),
                    "temperature_c": weather.get("temperature_c"),
                    "precipitation_probability": weather.get(
                        "precipitation_probability"
                    ),
                    "wind_speed_kmh": weather.get("wind_speed_kmh"),
                    "wind_direction_deg": weather.get("wind_direction_deg"),
                    "away_expected_runs": round(sim["away_expected_runs"], 3),
                    "home_expected_runs": round(sim["home_expected_runs"], 3),
                    "simulations": SIMULATIONS,
                    "recommendation": (
                        "BUY"
                        if ev >= 0.05
                        else ("LEAN" if ev > 0 else "PASS")
                    ),
                }
            )

        total_rows = [row for row in rows if row.get("market") == "totals"]
        by_line: dict[float, list[dict[str, Any]]] = defaultdict(list)
        for row in total_rows:
            try:
                by_line[float(row["point"])].append(row)
            except (TypeError, ValueError, KeyError):
                continue

        for total_line, line_rows in by_line.items():
            over_p, under_p, push_p = simulate_total_probability(
                event_id, away_lambda, home_lambda, total_line
            )
            for row in line_rows:
                selection = str(row.get("selection", ""))
                probability = over_p if selection.lower() == "over" else under_p
                price = float(row["decimal_odds"])
                ev = expected_value(probability, price)
                total_predictions.append({
                    "market": "total",
                    "event_id": event_id,
                    "commence_time_utc": first["commence_time_utc"],
                    "away_team": away_team,
                    "home_team": home_team,
                    "away_probable_pitcher": game.get("away_probable_pitcher"),
                    "home_probable_pitcher": game.get("home_probable_pitcher"),
                    "selection": selection,
                    "point": total_line,
                    "decimal_odds": round(price, 3),
                    "model_probability": round(probability, 6),
                    "push_probability": round(push_p, 6),
                    "ev": round(ev, 6),
                    "quarter_kelly": round(quarter_kelly(probability, price), 6),
                    "weather_run_factor": round(weather_run_factor, 4),
                    "park_factor": round(park, 4),
                    "away_expected_runs": round(sim["away_expected_runs"], 3),
                    "home_expected_runs": round(sim["home_expected_runs"], 3),
                    "simulations": SIMULATIONS,
                    "recommendation": "BUY" if ev >= 0.05 else ("LEAN" if ev > 0 else "PASS"),
                })

    ml_predictions.sort(key=lambda row: row["ev"], reverse=True)
    rl_predictions.sort(key=lambda row: row["ev"], reverse=True)
    total_predictions.sort(key=lambda row: row["ev"], reverse=True)
    return ml_predictions, rl_predictions, total_predictions
