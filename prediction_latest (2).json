from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
import requests

VENUE_COORDS = {
    "Yankee Stadium": (40.8296, -73.9262), "Fenway Park": (42.3467, -71.0972),
    "Wrigley Field": (41.9484, -87.6553), "Coors Field": (39.7559, -104.9942),
    "Dodger Stadium": (34.0739, -118.2400), "Oracle Park": (37.7786, -122.3893),
    "Petco Park": (32.7076, -117.1570), "T-Mobile Park": (47.5914, -122.3325),
    "Citizens Bank Park": (39.9061, -75.1665), "Great American Ball Park": (39.0979, -84.5082),
    "Busch Stadium": (38.6226, -90.1928), "Target Field": (44.9817, -93.2776),
    "Comerica Park": (42.3390, -83.0485), "Progressive Field": (41.4962, -81.6852),
    "Kauffman Stadium": (39.0517, -94.4803), "PNC Park": (40.4469, -80.0057),
}


def _neutral() -> dict[str, Any]:
    return {"weather_run_factor": 1.0, "temperature_c": None,
            "precipitation_probability": None, "wind_speed_kmh": None,
            "wind_direction_deg": None}


def attach_weather(schedule: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output = []
    for game in schedule:
        row = dict(game)
        weather = _neutral()
        coords = VENUE_COORDS.get(str(row.get("venue_name", "")))
        game_date = row.get("game_date_utc")
        if coords and game_date:
            try:
                dt = datetime.fromisoformat(str(game_date).replace("Z", "+00:00")).astimezone(timezone.utc)
                response = requests.get(
                    "https://api.open-meteo.com/v1/forecast",
                    params={"latitude": coords[0], "longitude": coords[1],
                            "hourly": "temperature_2m,precipitation_probability,wind_speed_10m,wind_direction_10m",
                            "timezone": "UTC", "forecast_days": 4}, timeout=20)
                response.raise_for_status()
                hourly = response.json().get("hourly") or {}
                times = hourly.get("time") or []
                target = dt.strftime("%Y-%m-%dT%H:00")
                if target in times:
                    i = times.index(target)
                    temp = hourly.get("temperature_2m", [None] * len(times))[i]
                    rain = hourly.get("precipitation_probability", [None] * len(times))[i]
                    wind = hourly.get("wind_speed_10m", [None] * len(times))[i]
                    direction = hourly.get("wind_direction_10m", [None] * len(times))[i]
                    factor = 1.0
                    if isinstance(temp, (int, float)): factor *= max(0.97, min(1.04, 1 + (temp - 20) * 0.002))
                    if isinstance(wind, (int, float)): factor *= max(0.98, min(1.02, 1 + (wind - 12) * 0.001))
                    weather = {"weather_run_factor": round(factor, 4), "temperature_c": temp,
                               "precipitation_probability": rain, "wind_speed_kmh": wind,
                               "wind_direction_deg": direction}
            except (requests.RequestException, ValueError, IndexError):
                pass
        row["weather"] = weather
        output.append(row)
    return output
