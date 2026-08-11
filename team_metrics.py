from __future__ import annotations

from typing import Any
import requests

# Team-level season totals. The generic /v1/stats endpoint returns *player*
# splits even when a team hydrate is requested, which silently turned this
# module into "one arbitrary player per team" — see MLB_TEAMS and the sanity
# check below, both of which exist to keep that from recurring unnoticed.
TEAM_STATS_URL = "https://statsapi.mlb.com/api/v1/teams/stats"

MLB_TEAMS = 30

# A league that scores outside this band is not MLB; it is a broken feed.
# Historical team scoring has stayed between roughly 3.4 and 5.5 runs a game.
PLAUSIBLE_LEAGUE_RUNS_PER_GAME = (3.0, 6.5)
PLAUSIBLE_LEAGUE_ERA = (2.5, 6.0)


class TeamMetricsError(RuntimeError):
    """Raised when the feed is reachable but the numbers cannot be MLB."""


def _float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _fetch(group: str, season: int) -> list[dict[str, Any]]:
    response = requests.get(
        TEAM_STATS_URL,
        params={
            "stats": "season",
            "group": group,
            "season": season,
            "sportIds": 1,
        },
        timeout=45,
    )
    response.raise_for_status()
    blocks = response.json().get("stats") or []
    return blocks[0].get("splits", []) if blocks else []


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def validate_metrics(metrics: dict[str, dict[str, Any]]) -> None:
    """Reject a feed whose league averages are not physically plausible.

    Scoring is the single input the run model is most sensitive to, so a wrong
    scale here quietly biases every total and run line in the slate. Failing
    loudly is better than publishing a slate of impossible Unders.
    """
    runs = [
        value["runs_per_game"]
        for value in metrics.values()
        if isinstance(value.get("runs_per_game"), (int, float))
    ]
    eras = [
        value["team_pitching_era"]
        for value in metrics.values()
        if isinstance(value.get("team_pitching_era"), (int, float))
    ]

    if len(runs) < MLB_TEAMS:
        raise TeamMetricsError(
            f"expected runs/game for {MLB_TEAMS} teams, got {len(runs)}. "
            "The stats feed is probably returning player splits again."
        )

    league_runs = _mean(runs)
    low, high = PLAUSIBLE_LEAGUE_RUNS_PER_GAME
    if league_runs is None or not low <= league_runs <= high:
        raise TeamMetricsError(
            f"league runs/game is {league_runs}, outside the plausible "
            f"range {low}-{high}. Refusing to publish a broken run model."
        )

    if eras:
        league_era = _mean(eras)
        low, high = PLAUSIBLE_LEAGUE_ERA
        if league_era is None or not low <= league_era <= high:
            raise TeamMetricsError(
                f"league ERA is {league_era}, outside the plausible range {low}-{high}."
            )


def fetch_team_metrics(season: int) -> dict[str, dict[str, Any]]:
    """Return per-team runs/game and team ERA from season team totals."""
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

    validate_metrics(metrics)
    return metrics
