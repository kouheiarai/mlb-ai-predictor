from __future__ import annotations

from typing import Any

import requests

MLB_TEAMS_URL = "https://statsapi.mlb.com/api/v1/teams"
MLB_STATS_URL = "https://statsapi.mlb.com/api/v1/stats"


def _to_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_team_ids() -> dict[str, int]:
    response = requests.get(
        MLB_TEAMS_URL,
        params={"sportId": 1, "activeStatus": "Y"},
        timeout=30,
    )
    response.raise_for_status()

    return {
        team.get("name", ""): int(team["id"])
        for team in response.json().get("teams", [])
        if team.get("id") is not None and team.get("name")
    }


def fetch_team_group_stats(team_id: int, season: int, group: str) -> dict[str, Any]:
    response = requests.get(
        MLB_STATS_URL,
        params={
            "stats": "season",
            "group": group,
            "teamId": team_id,
            "season": season,
            "gameType": "R",
        },
        timeout=30,
    )
    response.raise_for_status()

    blocks = response.json().get("stats") or []
    if not blocks:
        return {}

    splits = blocks[0].get("splits") or []
    if not splits:
        return {}

    return splits[0].get("stat") or {}


def fetch_team_metrics(season: int) -> dict[str, dict[str, Any]]:
    metrics: dict[str, dict[str, Any]] = {}

    for team_name, team_id in fetch_team_ids().items():
        try:
            hitting = fetch_team_group_stats(team_id, season, "hitting")
            pitching = fetch_team_group_stats(team_id, season, "pitching")
        except requests.RequestException:
            metrics[team_name] = {
                "team_id": team_id,
                "ops": None,
                "runs_per_game": None,
                "team_pitching_era": None,
                "team_pitching_whip": None,
            }
            continue

        games_played = _to_float(hitting.get("gamesPlayed"))
        runs = _to_float(hitting.get("runs"))
        runs_per_game = (
            runs / games_played
            if runs is not None and games_played and games_played > 0
            else None
        )

        metrics[team_name] = {
            "team_id": team_id,
            "ops": _to_float(hitting.get("ops")),
            "runs_per_game": runs_per_game,
            "team_pitching_era": _to_float(pitching.get("era")),
            "team_pitching_whip": _to_float(pitching.get("whip")),
        }

    return metrics
