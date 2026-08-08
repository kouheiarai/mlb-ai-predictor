from __future__ import annotations

import csv
import json
from datetime import datetime, timedelta
from pathlib import Path

MODEL_VERSION = "26.0"
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


def check_no_in_play_games(rows: list[dict[str, str]], generated_at: str) -> None:
    """開始済みの試合が混ざっていないことを確かめる。

    ライブオッズはプレゲームのラインとは前提が違うため、9イニング分を
    シミュレートする本モデルの確率と比較すると期待値が数百パーセントに
    膨らむ。取得から書き出しまでのラグを見込んで 30 分の猶予を置く。
    """
    try:
        cutoff = datetime.fromisoformat(generated_at) - timedelta(minutes=30)
    except ValueError as exc:
        raise RuntimeError(f"generated_at_utc is unparsable: {generated_at}") from exc

    stale = []
    for row in rows:
        raw = row.get("commence_time_utc", "")
        try:
            commence = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            continue
        if commence < cutoff:
            stale.append(f"{row.get('away_team')} @ {row.get('home_team')} ({raw})")

    if stale:
        raise RuntimeError(
            "In-play games leaked into the predictions "
            f"({len(stale)}): {sorted(set(stale))[:5]}"
        )


def check_public_endpoints() -> None:
    """公開URLが想定どおりの中身かを検査する。

    過去にアップロード事故でルート直下の JSON/CSV/HTML に Python
    ソースが入り、ChatGPT や Claude から取得できなくなったことがある。
    同じ壊れ方を CI で止めるためのガード。
    """
    for name in ("index.html", "docs/index.html"):
        path = Path(name)
        require_file(path)
        head = path.read_text(encoding="utf-8", errors="replace").lstrip()[:200].lower()
        if not head.startswith("<!doctype html"):
            raise RuntimeError(f"{path} is not an HTML document")

    for name in (
        "prediction_latest.json",
        "docs/prediction_latest.json",
        "output_manifest.json",
        "data/output_manifest.json",
    ):
        path = Path(name)
        require_file(path)
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path} is not valid JSON: {exc}") from exc
        if payload.get("model_version") != MODEL_VERSION:
            raise RuntimeError(f"{path} is not Ver.{MODEL_VERSION}")

    for name in (
        "predictions.csv",
        "moneyline_predictions.csv",
        "runline_predictions.csv",
        "total_predictions.csv",
        "docs/predictions.csv",
    ):
        path = Path(name)
        require_file(path)
        header = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()[0]
        if "," not in header or "event_id" not in header:
            raise RuntimeError(f"{path} does not look like a predictions CSV")

    for name in ("llms.txt", "robots.txt", "latest.md", "docs/llms.txt"):
        require_file(Path(name))

    # 軽量な入口。取得サイズに制約のある環境向けなので上限も見る。
    for name in ("summary.txt", "summary.md", "docs/summary.txt"):
        path = Path(name)
        require_file(path)
        size = path.stat().st_size
        if size > 200_000:
            raise RuntimeError(f"{path} is too large to be a lightweight summary ({size} bytes)")

    for name in ("summary.json", "docs/summary.json"):
        path = Path(name)
        require_file(path)
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("model_version") != MODEL_VERSION:
            raise RuntimeError(f"{path} is not Ver.{MODEL_VERSION}")
        if "buy_rankings" not in payload:
            raise RuntimeError(f"{path} is missing buy_rankings")


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

    check_public_endpoints()

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
        raise RuntimeError("CSV model_version is not 26.0")

    markets = {row.get("market") for row in rows}
    if "moneyline" not in markets:
        raise RuntimeError("Moneyline rows are missing")
    # RL/totals may be absent only if Pinnacle did not return those markets.

    check_no_in_play_games(rows, rows[0].get("generated_at_utc", ""))

    latest = json.loads(Path("data/prediction_latest.json").read_text(encoding="utf-8"))
    if latest.get("model_version") != MODEL_VERSION:
        raise RuntimeError("prediction_latest.json is not Ver.26.0")
    if latest.get("game_count", 0) <= 0:
        raise RuntimeError("prediction_latest.json contains no games")

    manifest = json.loads(Path("data/output_manifest.json").read_text(encoding="utf-8"))
    if manifest.get("model_version") != MODEL_VERSION:
        raise RuntimeError("output_manifest.json is not Ver.26.0")
    if manifest.get("combined_rows") != len(rows):
        raise RuntimeError("Manifest/CSV row count mismatch")

    print(f"Validated Ver.{MODEL_VERSION}: {len(rows)} rows, markets={sorted(markets)}")


if __name__ == "__main__":
    main()
