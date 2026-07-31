from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

import requests


MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"


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

    response = requests.get(
        MLB_SCHEDULE_URL,
        params=params,
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()
    games: list[dict[str, Any]] = []

    for date_block in data.get("dates", []):
        for game in date_block.get("games", []):
            away = game.get("teams", {}).get("away", {})
            home = game.get("teams", {}).get("home", {})

            away_pitcher = away.get("probablePitcher", {})
            home_pitcher = home.get("probablePitcher", {})

            games.append(
                {
                    "game_pk": game.get("gamePk"),
                    "game_date_utc": game.get("gameDate"),
                    "status": game.get("status", {}).get("detailedState", ""),
                    "away_team": away.get("team", {}).get("name", ""),
                    "home_team": home.get("team", {}).get("name", ""),
                    "away_probable_pitcher": away_pitcher.get(
                        "fullName",
                        "未発表",
                    ),
                    "home_probable_pitcher": home_pitcher.get(
                        "fullName",
                        "未発表",
                    ),
                }
            )

    return games
