from __future__ import annotations

from typing import Any

import requests


PEOPLE_URL = "https://statsapi.mlb.com/api/v1/people/{person_id}"


def fetch_player_bio(person_id: int | None) -> dict[str, Any]:
    """MLB公式の選手プロフィールから打席・投球側を取得する。"""
    if not person_id:
        return {
            "person_id": person_id,
            "bat_side": None,
            "pitch_hand": None,
        }

    response = requests.get(
        PEOPLE_URL.format(person_id=person_id),
        timeout=30,
    )
    response.raise_for_status()

    people = response.json().get("people") or []
    if not people:
        return {
            "person_id": person_id,
            "bat_side": None,
            "pitch_hand": None,
        }

    person = people[0]
    return {
        "person_id": person_id,
        "bat_side": (person.get("batSide") or {}).get("code"),
        "pitch_hand": (person.get("pitchHand") or {}).get("code"),
    }


def attach_handedness(schedule: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    発表済み打順と予告先発へ左右情報を追加する。

    注意:
    この版は左右別の実績成績そのものではなく、
    選手プロフィールの打席・投球側を使う「プラトーン代理補正」。
    """
    cache: dict[int, dict[str, Any]] = {}
    enriched_schedule: list[dict[str, Any]] = []

    def get_bio(person_id: int | None) -> dict[str, Any]:
        if not person_id:
            return {
                "person_id": person_id,
                "bat_side": None,
                "pitch_hand": None,
            }

        if person_id not in cache:
            try:
                cache[person_id] = fetch_player_bio(person_id)
            except requests.RequestException:
                cache[person_id] = {
                    "person_id": person_id,
                    "bat_side": None,
                    "pitch_hand": None,
                }

        return cache[person_id]

    for game in schedule:
        row = dict(game)
        lineups = dict(row.get("lineups") or {})

        away_pitcher_bio = get_bio(
            row.get("away_probable_pitcher_id")
        )
        home_pitcher_bio = get_bio(
            row.get("home_probable_pitcher_id")
        )

        row["away_probable_pitcher_hand"] = (
            away_pitcher_bio.get("pitch_hand")
        )
        row["home_probable_pitcher_hand"] = (
            home_pitcher_bio.get("pitch_hand")
        )

        for side in ("away", "home"):
            hitters = []

            for hitter in lineups.get(f"{side}_batting_order", []):
                bio = get_bio(hitter.get("person_id"))
                hitters.append(
                    {
                        **hitter,
                        "bat_side": bio.get("bat_side"),
                    }
                )

            lineups[f"{side}_batting_order"] = hitters

        row["lineups"] = lineups
        enriched_schedule.append(row)

    return enriched_schedule
