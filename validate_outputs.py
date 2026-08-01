from __future__ import annotations

import csv
import json
from pathlib import Path

MODEL_VERSION = "25.3"
REQUIRED_CSV_COLUMNS = {
    "model_version",
    "generated_at_utc",
    "target_date_utc",
    "market",
    "event_id",
    "commence_time_utc",
    "away_team",
    "home_team",
    "away_probable_pitcher",
    "home_probable_pitcher",
    "selection",
    "decimal_odds",
    "model_probability",
    "ev",
    "quarter_kelly",
    "recommendation",
}


def require_file(path: Path) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        raise RuntimeError(f"Missing or empty output: {path}")


def main() -> None:
    paths = [
        Path("data/predictions.csv"),
        Path("predictions.csv"),
        Path("data/prediction_latest.json"),
        Path("prediction_latest.json"),
        Path("docs/prediction_latest.json"),
        Path("data/output_manifest.json"),
    ]
    for path in paths:
        require_file(path)

    with Path("data/predictions.csv").open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_CSV_COLUMNS - columns
        if missing:
            raise RuntimeError(f"CSV is old/incomplete; missing columns: {sorted(missing)}")
        rows = list(reader)

    if not rows:
        raise RuntimeError("CSV contains no predictions")
    if any(row.get("model_version") != MODEL_VERSION for row in rows):
        raise RuntimeError("CSV model_version is not 25.3")

    markets = {row.get("market") for row in rows}
    if "moneyline" not in markets:
        raise RuntimeError("Moneyline rows are missing")
    # RL/totals may be absent only if Pinnacle did not return those markets.

    latest = json.loads(Path("data/prediction_latest.json").read_text(encoding="utf-8"))
    if latest.get("model_version") != MODEL_VERSION:
        raise RuntimeError("prediction_latest.json is not Ver.25.3")
    if latest.get("game_count", 0) <= 0:
        raise RuntimeError("prediction_latest.json contains no games")

    manifest = json.loads(Path("data/output_manifest.json").read_text(encoding="utf-8"))
    if manifest.get("model_version") != MODEL_VERSION:
        raise RuntimeError("output_manifest.json is not Ver.25.3")
    if manifest.get("combined_rows") != len(rows):
        raise RuntimeError("Manifest/CSV row count mismatch")

    print(f"Validated Ver.{MODEL_VERSION}: {len(rows)} rows, markets={sorted(markets)}")


if __name__ == "__main__":
    main()
