from __future__ import annotations

from typing import Any
import requests

STATS_URL = "https://statsapi.mlb.com/api/v1/stats"


def _float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _fetch(group: str, season: int) -> list[dict[str, Any]]:
    response = requests.get(
        STATS_URL,
        params={
            "stats": "season",
            "group": group,
            "teamId": "",
            "season": season,
            "sportIds": 1,
            "hydrate": "team",
        },
        timeout=45,
    )
    response.raise_for_status()
    blocks = response.json().get("stats") or []
    return blocks[0].get("splits", []) if blocks else []


def fetch_team_metrics(season: int) -> dict[str, dict[str, Any]]:
    """Return team runs/game and team ERA. Falls back gracefully if unavailable."""
    metrics: dict[str, dict[str, Any]] = {}
    try:
        for split in _fetch("hitting", season):
            team = (split.get("team") or {}).get("name")
            stat = split.get("stat") or {}
            games = _float(stat.get("gamesPlayed")) or 0
            runs = _float(stat.get("runs"))
            if team:
                metrics.setdefault(team, {})["runs_per_game"] = (
                    runs / games if runs is not None and games > 0 else None
                )
        for split in _fetch("pitching", season):
            team = (split.get("team") or {}).get("name")
            stat = split.get("stat") or {}
            if team:
                metrics.setdefault(team, {})["team_pitching_era"] = _float(stat.get("era"))
    except requests.RequestException:
        return metrics
    return metrics
