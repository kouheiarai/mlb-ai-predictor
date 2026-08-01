from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import os
from statistics import median
from typing import Any

import requests

GAME_FEED_URL = "https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"


def _to_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _player_id_from_key(key: str, player: dict[str, Any]) -> int | None:
    person_id = (player.get("person") or {}).get("id")
    if isinstance(person_id, int):
        return person_id
    if key.startswith("ID"):
        try:
            return int(key[2:])
        except ValueError:
            return None
    return None


def _season_batting_stats(player: dict[str, Any]) -> dict[str, Any]:
    batting = ((player.get("seasonStats") or {}).get("batting") or {})
    return {
        "ops": _to_float(batting.get("ops")),
        "plate_appearances": _to_float(batting.get("plateAppearances")),
        "avg": _to_float(batting.get("avg")),
        "obp": _to_float(batting.get("obp")),
        "slg": _to_float(batting.get("slg")),
    }


def _extract_team_lineup(team_box: dict[str, Any]) -> tuple[list[dict[str, Any]], bool]:
    players = team_box.get("players") or {}
    order: list[tuple[int, dict[str, Any]]] = []

    for key, player in players.items():
        batting_order = player.get("battingOrder")
        try:
            order_value = int(batting_order)
        except (TypeError, ValueError):
            continue

        person = player.get("person") or {}
        person_id = _player_id_from_key(str(key), player)
        order.append(
            (
                order_value,
                {
                    "person_id": person_id,
                    "full_name": person.get("fullName") or person.get("name") or "",
                    "batting_order": order_value // 100,
                    "position": ((player.get("position") or {}).get("abbreviation")),
                    "season_stats": _season_batting_stats(player),
                },
            )
        )

    order.sort(key=lambda item: item[0])
    hitters = [item[1] for item in order[:9]]
    return hitters, len(hitters) >= 8


def fetch_game_lineups(game_pk: int | None) -> dict[str, Any]:
    """Return announced batting orders from MLB's live game feed.

    Before lineups are posted, the function returns empty orders with announced=False.
    """
    empty = {
        "away_announced": False,
        "home_announced": False,
        "away_batting_order": [],
        "home_batting_order": [],
    }
    if not game_pk:
        return empty

    response = requests.get(
        GAME_FEED_URL.format(game_pk=game_pk),
        timeout=30,
    )
    response.raise_for_status()
    teams = (((response.json().get("liveData") or {}).get("boxscore") or {}).get("teams") or {})

    away_order, away_announced = _extract_team_lineup(teams.get("away") or {})
    home_order, home_announced = _extract_team_lineup(teams.get("home") or {})
    return {
        "away_announced": away_announced,
        "home_announced": home_announced,
        "away_batting_order": away_order,
        "home_batting_order": home_order,
    }



def _recent_completed_games(
    team_names: set[str],
    lookback_days: int = 14,
    games_per_team: int = 3,
) -> dict[str, list[tuple[int, str]]]:
    """Return recent completed game ids and team side for requested teams."""
    today = datetime.now(timezone.utc).date()
    response = requests.get(
        SCHEDULE_URL,
        params={
            "sportId": 1,
            "startDate": (today - timedelta(days=lookback_days)).isoformat(),
            "endDate": (today - timedelta(days=1)).isoformat(),
            "gameType": "R",
        },
        timeout=30,
    )
    response.raise_for_status()

    found: dict[str, list[tuple[int, str]]] = defaultdict(list)
    games: list[dict[str, Any]] = []
    for block in response.json().get("dates", []):
        games.extend(block.get("games", []))

    for game in reversed(games):
        if (game.get("status") or {}).get("abstractGameState") != "Final":
            continue
        game_pk = game.get("gamePk")
        if not isinstance(game_pk, int):
            continue
        for side in ("away", "home"):
            name = ((((game.get("teams") or {}).get(side) or {}).get("team") or {}).get("name"))
            if name in team_names and len(found[name]) < games_per_team:
                found[name].append((game_pk, side))
        if all(len(found[name]) >= games_per_team for name in team_names):
            break
    return found


def _predict_lineup_from_history(
    history: list[tuple[int, str]],
    feed_cache: dict[int, dict[str, Any]],
) -> tuple[list[dict[str, Any]], int]:
    """Build a conservative predicted batting order from recent official lineups."""
    appearances: Counter[int] = Counter()
    orders: dict[int, list[int]] = defaultdict(list)
    names: dict[int, str] = {}
    positions: dict[int, str | None] = {}
    latest_stats: dict[int, dict[str, Any]] = {}
    used_games = 0

    for game_pk, side in history:
        if game_pk not in feed_cache:
            response = requests.get(GAME_FEED_URL.format(game_pk=game_pk), timeout=30)
            response.raise_for_status()
            feed_cache[game_pk] = response.json()
        teams = (((feed_cache[game_pk].get("liveData") or {}).get("boxscore") or {}).get("teams") or {})
        hitters, announced = _extract_team_lineup(teams.get(side) or {})
        if not announced:
            continue
        used_games += 1
        for hitter in hitters:
            person_id = hitter.get("person_id")
            order = hitter.get("batting_order")
            if not isinstance(person_id, int) or not isinstance(order, int):
                continue
            appearances[person_id] += 1
            orders[person_id].append(order)
            names[person_id] = hitter.get("full_name") or names.get(person_id, "")
            positions[person_id] = hitter.get("position")
            latest_stats[person_id] = hitter.get("season_stats") or {}

    ranked = sorted(
        appearances,
        key=lambda pid: (-appearances[pid], median(orders[pid]), names.get(pid, "")),
    )[:9]
    ranked.sort(key=lambda pid: (median(orders[pid]), -appearances[pid]))

    predicted: list[dict[str, Any]] = []
    for slot, person_id in enumerate(ranked, start=1):
        predicted.append({
            "person_id": person_id,
            "full_name": names.get(person_id, ""),
            "batting_order": slot,
            "position": positions.get(person_id),
            "season_stats": latest_stats.get(person_id, {}),
            "prediction_start_count": appearances[person_id],
            "prediction_median_order": float(median(orders[person_id])),
        })
    return predicted, used_games


def attach_predicted_lineups(
    schedule: list[dict[str, Any]],
    games_per_team: int = 3,
) -> list[dict[str, Any]]:
    """Fill only unannounced lineups with recent-lineup predictions.

    Safety rule: official lineups are never overwritten. Failure returns the input
    schedule unchanged except for status metadata. Predicted lineups are marked
    announced=False, so the existing prediction model does not use them yet.
    """
    output = [dict(game) for game in schedule]
    team_names = {
        str(game.get(key))
        for game in output
        for key in ("away_team", "home_team")
        if game.get(key)
    }
    try:
        history = _recent_completed_games(team_names, games_per_team=games_per_team)
        feed_cache: dict[int, dict[str, Any]] = {}
        predicted_cache: dict[str, tuple[list[dict[str, Any]], int]] = {}
        for team in team_names:
            predicted_cache[team] = _predict_lineup_from_history(history.get(team, []), feed_cache)
    except (requests.RequestException, ValueError, TypeError):
        predicted_cache = {}

    for row in output:
        lineups = dict(row.get("lineups") or {})
        for side in ("away", "home"):
            announced = bool(lineups.get(f"{side}_announced"))
            team = str(row.get(f"{side}_team") or "")
            if announced:
                lineups[f"{side}_lineup_status"] = "official"
                lineups[f"{side}_prediction_source_games"] = 0
                continue
            predicted, used_games = predicted_cache.get(team, ([], 0))
            if predicted:
                lineups[f"{side}_batting_order"] = predicted
                lineups[f"{side}_lineup_status"] = "predicted"
                lineups[f"{side}_prediction_source_games"] = used_games
            else:
                lineups.setdefault(f"{side}_batting_order", [])
                lineups[f"{side}_lineup_status"] = "unavailable"
                lineups[f"{side}_prediction_source_games"] = 0
        row["lineups"] = lineups
    return output

def attach_lineups(
    schedule: list[dict[str, Any]],
    season: int | None = None,
) -> list[dict[str, Any]]:
    """Attach MLB official announced lineups to every schedule row.

    ``season`` is accepted for backward compatibility with main.py. The MLB feed
    already supplies season batting stats for announced hitters, so no separate
    per-player API calls are necessary.
    """
    del season
    output: list[dict[str, Any]] = []
    for game in schedule:
        row = dict(game)
        try:
            row["lineups"] = fetch_game_lineups(row.get("game_pk"))
        except (requests.RequestException, ValueError, TypeError):
            row["lineups"] = {
                "away_announced": False,
                "home_announced": False,
                "away_batting_order": [],
                "home_batting_order": [],
            }
        output.append(row)

    enabled = os.getenv("ENABLE_PREDICTED_LINEUPS", "1").strip().lower() not in {"0", "false", "no"}
    if not enabled:
        for row in output:
            lineups = dict(row.get("lineups") or {})
            for side in ("away", "home"):
                lineups[f"{side}_lineup_status"] = (
                    "official" if lineups.get(f"{side}_announced") else "unavailable"
                )
                lineups[f"{side}_prediction_source_games"] = 0
            row["lineups"] = lineups
        return output

    try:
        games_per_team = max(1, min(5, int(os.getenv("PREDICTED_LINEUP_GAMES", "3"))))
    except ValueError:
        games_per_team = 3
    return attach_predicted_lineups(output, games_per_team=games_per_team)
