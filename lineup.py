from __future__ import annotations

from typing import Any

import requests


LIVE_FEED_URL = "https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
PEOPLE_STATS_URL = "https://statsapi.mlb.com/api/v1/people/{person_id}/stats"


def _to_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_game_lineups(game_pk: int | None) -> dict[str, Any]:
    """
    MLB live feedから発表済み打順を取得する。
    未発表の場合は announced=False と空の打順を返す。
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
        LIVE_FEED_URL.format(game_pk=game_pk),
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()

    boxscore = data.get("liveData", {}).get("boxscore", {})
    teams = boxscore.get("teams", {})

    result: dict[str, Any] = {}

    for side in ("away", "home"):
        team_box = teams.get(side, {})
        batting_order = team_box.get("battingOrder") or []
        players = team_box.get("players") or {}

        hitters: list[dict[str, Any]] = []
        for person_id in batting_order[:9]:
            player = players.get(f"ID{person_id}", {})
            person = player.get("person", {})
            position = player.get("position", {})

            hitters.append(
                {
                    "person_id": person.get("id") or person_id,
                    "name": person.get("fullName", ""),
                    "position": position.get("abbreviation", ""),
                    "batting_order": player.get("battingOrder", ""),
                }
            )

        result[f"{side}_announced"] = len(hitters) >= 8
        result[f"{side}_batting_order"] = hitters

    return {**empty, **result}


def fetch_hitter_season_stats(
    person_id: int | None,
    season: int,
) -> dict[str, Any]:
    empty = {
        "person_id": person_id,
        "ops": None,
        "avg": None,
        "obp": None,
        "slg": None,
        "plate_appearances": None,
    }

    if not person_id:
        return empty

    response = requests.get(
        PEOPLE_STATS_URL.format(person_id=person_id),
        params={
            "stats": "season",
            "group": "hitting",
            "season": season,
        },
        timeout=30,
    )
    response.raise_for_status()

    blocks = response.json().get("stats") or []
    if not blocks:
        return empty

    splits = blocks[0].get("splits") or []
    if not splits:
        return empty

    stat = splits[0].get("stat") or {}

    return {
        "person_id": person_id,
        "ops": _to_float(stat.get("ops")),
        "avg": _to_float(stat.get("avg")),
        "obp": _to_float(stat.get("obp")),
        "slg": _to_float(stat.get("slg")),
        "plate_appearances": _to_float(stat.get("plateAppearances")),
    }


def enrich_lineups_with_stats(
    lineups: dict[str, Any],
    season: int,
) -> dict[str, Any]:
    cache: dict[int, dict[str, Any]] = {}
    enriched = dict(lineups)

    for side in ("away", "home"):
        hitters = []

        for hitter in lineups.get(f"{side}_batting_order", []):
            person_id = hitter.get("person_id")

            if person_id not in cache:
                try:
                    cache[person_id] = fetch_hitter_season_stats(
                        person_id,
                        season,
                    )
                except requests.RequestException:
                    cache[person_id] = {
                        "person_id": person_id,
                        "ops": None,
                        "avg": None,
                        "obp": None,
                        "slg": None,
                        "plate_appearances": None,
                    }

            hitters.append({**hitter, "season_stats": cache[person_id]})

        enriched[f"{side}_batting_order"] = hitters

    return enriched


def attach_lineups(
    schedule: list[dict[str, Any]],
    season: int,
) -> list[dict[str, Any]]:
    enriched_schedule: list[dict[str, Any]] = []

    for game in schedule:
        row = dict(game)

        try:
            lineups = fetch_game_lineups(game.get("game_pk"))
            lineups = enrich_lineups_with_stats(lineups, season)
        except requests.RequestException:
            lineups = {
                "away_announced": False,
                "home_announced": False,
                "away_batting_order": [],
                "home_batting_order": [],
            }

        row["lineups"] = lineups
        enriched_schedule.append(row)

    return enriched_schedule
