from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule"


def fetch_bullpen_fatigue_proxy(lookback_days: int = 4) -> dict[str, dict[str, Any]]:
    today = datetime.now(timezone.utc).date()
    start_date = today - timedelta(days=lookback_days)

    response = requests.get(
        MLB_SCHEDULE_URL,
        params={
            "sportId": 1,
            "startDate": start_date.isoformat(),
            "endDate": today.isoformat(),
            "gameType": "R",
            "hydrate": "linescore",
        },
        timeout=45,
    )
    response.raise_for_status()

    team_games: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)

    for date_block in response.json().get("dates", []):
        game_date = date_block.get("date", "")

        for game in date_block.get("games", []):
            if game.get("status", {}).get("abstractGameState") != "Final":
                continue

            innings = (
                game.get("linescore", {}).get("currentInning")
                or len(game.get("linescore", {}).get("innings", []))
                or 9
            )
            entry = {
                "date": game_date,
                "innings": int(innings),
                "double_header": game.get("doubleHeader") not in ("N", None),
            }

            for side in ("away", "home"):
                team_name = (
                    game.get("teams", {})
                    .get(side, {})
                    .get("team", {})
                    .get("name", "")
                )
                if team_name:
                    team_games[team_name].append(entry)

    fatigue: dict[str, dict[str, Any]] = {}

    for team, games in team_games.items():
        games.sort(key=lambda item: item["date"])
        games_played = len(games)
        unique_dates = len({game["date"] for game in games})
        extra_inning_games = sum(
            1 for game in games if game.get("innings", 9) > 9
        )
        doubleheaders = sum(
            1 for game in games if game.get("double_header")
        )

        score = 0.0
        score += min(0.45, games_played * 0.10)
        if unique_dates >= 3:
            score += 0.15
        score += min(0.20, extra_inning_games * 0.10)
        score += min(0.20, doubleheaders * 0.10)

        fatigue[team] = {
            "fatigue_score": round(min(1.0, score), 4),
            "games_played_lookback": games_played,
            "unique_game_dates": unique_dates,
            "extra_inning_games": extra_inning_games,
            "doubleheader_games": doubleheaders,
        }

    return fatigue
