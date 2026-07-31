from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import requests


OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# Approximate MLB home-stadium coordinates.
STADIUMS: dict[str, dict[str, Any]] = {
    "Arizona Diamondbacks": {"lat": 33.4453, "lon": -112.0667, "roof": True},
    "Athletics": {"lat": 38.0529, "lon": -122.2834, "roof": False},
    "Atlanta Braves": {"lat": 33.8907, "lon": -84.4677, "roof": False},
    "Baltimore Orioles": {"lat": 39.2839, "lon": -76.6217, "roof": False},
    "Boston Red Sox": {"lat": 42.3467, "lon": -71.0972, "roof": False},
    "Chicago Cubs": {"lat": 41.9484, "lon": -87.6553, "roof": False},
    "Chicago White Sox": {"lat": 41.8299, "lon": -87.6338, "roof": False},
    "Cincinnati Reds": {"lat": 39.0979, "lon": -84.5082, "roof": False},
    "Cleveland Guardians": {"lat": 41.4962, "lon": -81.6852, "roof": False},
    "Colorado Rockies": {"lat": 39.7559, "lon": -104.9942, "roof": False},
    "Detroit Tigers": {"lat": 42.3390, "lon": -83.0485, "roof": False},
    "Houston Astros": {"lat": 29.7573, "lon": -95.3555, "roof": True},
    "Kansas City Royals": {"lat": 39.0517, "lon": -94.4803, "roof": False},
    "Los Angeles Angels": {"lat": 33.8003, "lon": -117.8827, "roof": False},
    "Los Angeles Dodgers": {"lat": 34.0739, "lon": -118.2400, "roof": False},
    "Miami Marlins": {"lat": 25.7781, "lon": -80.2197, "roof": True},
    "Milwaukee Brewers": {"lat": 43.0280, "lon": -87.9712, "roof": True},
    "Minnesota Twins": {"lat": 44.9817, "lon": -93.2776, "roof": False},
    "New York Mets": {"lat": 40.7571, "lon": -73.8458, "roof": False},
    "New York Yankees": {"lat": 40.8296, "lon": -73.9262, "roof": False},
    "Oakland Athletics": {"lat": 38.0529, "lon": -122.2834, "roof": False},
    "Philadelphia Phillies": {"lat": 39.9061, "lon": -75.1665, "roof": False},
    "Pittsburgh Pirates": {"lat": 40.4469, "lon": -80.0057, "roof": False},
    "San Diego Padres": {"lat": 32.7076, "lon": -117.1570, "roof": False},
    "San Francisco Giants": {"lat": 37.7786, "lon": -122.3893, "roof": False},
    "Seattle Mariners": {"lat": 47.5914, "lon": -122.3325, "roof": True},
    "St. Louis Cardinals": {"lat": 38.6226, "lon": -90.1928, "roof": False},
    "Tampa Bay Rays": {"lat": 27.7683, "lon": -82.6534, "roof": True},
    "Texas Rangers": {"lat": 32.7473, "lon": -97.0847, "roof": True},
    "Toronto Blue Jays": {"lat": 43.6414, "lon": -79.3894, "roof": True},
    "Washington Nationals": {"lat": 38.8730, "lon": -77.0074, "roof": False},
}


def _parse_utc(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(
            timezone.utc
        )
    except ValueError:
        return None


def fetch_game_weather(
    home_team: str,
    game_date_utc: str | None,
) -> dict[str, Any]:
    stadium = STADIUMS.get(home_team)
    game_time = _parse_utc(game_date_utc)

    empty = {
        "available": False,
        "indoor_or_retractable": bool(stadium and stadium.get("roof")),
        "temperature_c": None,
        "precipitation_probability": None,
        "wind_speed_kmh": None,
        "wind_direction_deg": None,
        "weather_run_factor": 1.0,
    }

    if not stadium or not game_time:
        return empty

    if stadium.get("roof"):
        return {**empty, "available": True}

    response = requests.get(
        OPEN_METEO_URL,
        params={
            "latitude": stadium["lat"],
            "longitude": stadium["lon"],
            "hourly": (
                "temperature_2m,precipitation_probability,"
                "wind_speed_10m,wind_direction_10m"
            ),
            "timezone": "UTC",
            "forecast_days": 7,
        },
        timeout=30,
    )
    response.raise_for_status()
    hourly = response.json().get("hourly") or {}
    times = hourly.get("time") or []

    if not times:
        return empty

    target = game_time.replace(minute=0, second=0, microsecond=0)
    parsed = [
        datetime.fromisoformat(item).replace(tzinfo=timezone.utc)
        for item in times
    ]
    index = min(
        range(len(parsed)),
        key=lambda i: abs((parsed[i] - target).total_seconds()),
    )

    def at(key: str) -> Any:
        values = hourly.get(key) or []
        return values[index] if index < len(values) else None

    temperature = at("temperature_2m")
    precipitation = at("precipitation_probability")
    wind_speed = at("wind_speed_10m")
    wind_direction = at("wind_direction_10m")

    factor = 1.0
    if isinstance(temperature, (int, float)):
        factor *= max(0.96, min(1.05, 1.0 + (temperature - 20.0) * 0.002))
    if isinstance(wind_speed, (int, float)):
        # Direction is retained in the report, but without a park-axis model
        # only a small generic wind-speed effect is applied.
        factor *= max(1.0, min(1.035, 1.0 + max(0.0, wind_speed - 10.0) * 0.0015))
    if isinstance(precipitation, (int, float)) and precipitation >= 50:
        factor *= 0.985

    return {
        "available": True,
        "indoor_or_retractable": False,
        "temperature_c": temperature,
        "precipitation_probability": precipitation,
        "wind_speed_kmh": wind_speed,
        "wind_direction_deg": wind_direction,
        "weather_run_factor": round(max(0.94, min(1.08, factor)), 4),
    }


def attach_weather(schedule: list[dict[str, Any]]) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []

    for game in schedule:
        row = dict(game)
        try:
            row["weather"] = fetch_game_weather(
                row.get("home_team", ""),
                row.get("game_date_utc"),
            )
        except requests.RequestException:
            row["weather"] = {
                "available": False,
                "indoor_or_retractable": False,
                "temperature_c": None,
                "precipitation_probability": None,
                "wind_speed_kmh": None,
                "wind_direction_deg": None,
                "weather_run_factor": 1.0,
            }
        enriched.append(row)

    return enriched
