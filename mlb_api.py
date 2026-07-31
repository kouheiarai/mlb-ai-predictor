from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

import requests


MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"
MLB_PEOPLE_URL = "https://statsapi.mlb.com/api/v1/people"


def fetch_mlb_schedule(days: int = 3) -> list[dict[str, Any]]:
    """MLB公式データから試合日程と予告先発を取得する。"""
    today_utc = datetime.now(timezone.utc).date()
    end_date = today_utc + timedelta(days=days)

    params = {
        "sportId": 1,
        "startDate": today_utc.isoformat(),
        "endDate": end_date.isoformat(),
        "hydrate": "probablePitcher",
    }

    response = requests.get(MLB_SCHEDULE_URL, params=params, timeout=30)
    response.raise_for_status()

    games: list[dict[str, Any]] = []

    for date_block in response.json().get("dates", []):
        for game in date_block.get("games", []):
            away = game.get("teams", {}).get("away", {})
            home = game.get("teams", {}).get("home", {})

            away_pitcher = away.get("probablePitcher") or {}
            home_pitcher = home.get("probablePitcher") or {}

            games.append(
                {
                    "game_pk": game.get("gamePk"),
                    "game_date_utc": game.get("gameDate"),
                    "status": game.get("status", {}).get("detailedState", ""),
                    "away_team": away.get("team", {}).get("name", ""),
                    "home_team": home.get("team", {}).get("name", ""),
                    "away_probable_pitcher_id": away_pitcher.get("id"),
                    "home_probable_pitcher_id": home_pitcher.get("id"),
                    "away_probable_pitcher": away_pitcher.get("fullName", "未発表"),
                    "home_probable_pitcher": home_pitcher.get("fullName", "未発表"),
                }
            )

    return games


def fetch_pitcher_season_stats(
    pitcher_id: int | None,
    season: int,
) -> dict[str, Any]:
    """予告先発のシーズン成績を取得する。データなしでも安全に空値を返す。"""
    empty = {
        "pitcher_id": pitcher_id,
        "era": None,
        "whip": None,
        "strikeout_walk_ratio": None,
        "innings_pitched": None,
        "games_started": None,
    }

    if not pitcher_id:
        return empty

    url = f"{MLB_PEOPLE_URL}/{pitcher_id}/stats"
    params = {
        "stats": "season",
        "group": "pitching",
        "season": season,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    payload = response.json()

    stats_blocks = payload.get("stats") or []
    if not stats_blocks:
        return empty

    splits = stats_blocks[0].get("splits") or []
    if not splits:
        return empty

    stat = splits[0].get("stat") or {}

    def as_float(value: Any) -> float | None:
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    return {
        "pitcher_id": pitcher_id,
        "era": as_float(stat.get("era")),
        "whip": as_float(stat.get("whip")),
        "strikeout_walk_ratio": as_float(stat.get("strikeoutWalkRatio")),
        "innings_pitched": as_float(stat.get("inningsPitched")),
        "games_started": stat.get("gamesStarted"),
    }


def attach_probable_pitcher_stats(
    schedule: list[dict[str, Any]],
    season: int,
) -> list[dict[str, Any]]:
    """日程データへ両先発のシーズン成績を追加する。"""
    cache: dict[int, dict[str, Any]] = {}

    def get_stats(pitcher_id: int | None) -> dict[str, Any]:
        if not pitcher_id:
            return fetch_pitcher_season_stats(None, season)

        if pitcher_id not in cache:
            try:
                cache[pitcher_id] = fetch_pitcher_season_stats(
                    pitcher_id,
                    season,
                )
            except requests.RequestException:
                cache[pitcher_id] = {
                    "pitcher_id": pitcher_id,
                    "era": None,
                    "whip": None,
                    "strikeout_walk_ratio": None,
                    "innings_pitched": None,
                    "games_started": None,
                }

        return cache[pitcher_id]

    enriched: list[dict[str, Any]] = []

    for game in schedule:
        row = dict(game)
        row["away_starter_stats"] = get_stats(
            game.get("away_probable_pitcher_id")
        )
        row["home_starter_stats"] = get_stats(
            game.get("home_probable_pitcher_id")
        )
        enriched.append(row)

    return enriched
