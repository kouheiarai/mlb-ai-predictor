from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

import requests

SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"
PEOPLE_STATS_URL = "https://statsapi.mlb.com/api/v1/people/{person_id}/stats"


def _to_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_mlb_schedule(days: int = 3) -> list[dict[str, Any]]:
    """Fetch upcoming MLB games and probable pitchers from MLB Stats API."""
    today = datetime.now(timezone.utc).date()
    response = requests.get(
        SCHEDULE_URL,
        params={
            "sportId": 1,
            "startDate": today.isoformat(),
            "endDate": (today + timedelta(days=max(0, days - 1))).isoformat(),
            "hydrate": "probablePitcher,venue",
        },
        timeout=45,
    )
    response.raise_for_status()

    games: list[dict[str, Any]] = []
    for block in response.json().get("dates", []):
        for game in block.get("games", []):
            teams = game.get("teams", {})
            away = teams.get("away", {})
            home = teams.get("home", {})
            away_pitcher = away.get("probablePitcher") or {}
            home_pitcher = home.get("probablePitcher") or {}
            venue = game.get("venue") or {}
            games.append(
                {
                    "game_pk": game.get("gamePk"),
                    "game_date_utc": game.get("gameDate", ""),
                    "status": (game.get("status") or {}).get("detailedState", ""),
                    "away_team": (away.get("team") or {}).get("name", ""),
                    "home_team": (home.get("team") or {}).get("name", ""),
                    "away_probable_pitcher_id": away_pitcher.get("id"),
                    "away_probable_pitcher": away_pitcher.get("fullName", "TBD"),
                    "home_probable_pitcher_id": home_pitcher.get("id"),
                    "home_probable_pitcher": home_pitcher.get("fullName", "TBD"),
                    "venue_id": venue.get("id"),
                    "venue_name": venue.get("name", ""),
                }
            )
    return games


def fetch_pitcher_season_stats(person_id: int | None, season: int) -> dict[str, Any]:
    empty = {
        "person_id": person_id,
        "era": None,
        "whip": None,
        "strikeout_walk_ratio": None,
        "innings_pitched": None,
    }
    if not person_id:
        return empty

    response = requests.get(
        PEOPLE_STATS_URL.format(person_id=person_id),
        params={"stats": "season", "group": "pitching", "season": season},
        timeout=30,
    )
    response.raise_for_status()
    blocks = response.json().get("stats") or []
    splits = blocks[0].get("splits") if blocks else []
    stat = (splits[0].get("stat") if splits else {}) or {}
    strikeouts = _to_float(stat.get("strikeOuts"))
    walks = _to_float(stat.get("baseOnBalls"))
    ratio = None
    if strikeouts is not None and walks is not None:
        ratio = strikeouts / max(walks, 1.0)

    return {
        "person_id": person_id,
        "era": _to_float(stat.get("era")),
        "whip": _to_float(stat.get("whip")),
        "strikeout_walk_ratio": ratio,
        "innings_pitched": _to_float(stat.get("inningsPitched")),
    }


def attach_probable_pitcher_stats(
    schedule: list[dict[str, Any]], season: int
) -> list[dict[str, Any]]:
    cache: dict[int, dict[str, Any]] = {}
    output: list[dict[str, Any]] = []
    for game in schedule:
        row = dict(game)
        for side in ("away", "home"):
            person_id = row.get(f"{side}_probable_pitcher_id")
            if person_id and person_id not in cache:
                try:
                    cache[person_id] = fetch_pitcher_season_stats(person_id, season)
                except requests.RequestException:
                    cache[person_id] = fetch_pitcher_season_stats(None, season)
                    cache[person_id]["person_id"] = person_id
            row[f"{side}_starter_stats"] = cache.get(
                person_id, fetch_pitcher_season_stats(None, season)
            )
        output.append(row)
    return output
