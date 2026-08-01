from __future__ import annotations

from typing import Any

import requests

GAME_FEED_URL = "https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"


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
    return output
