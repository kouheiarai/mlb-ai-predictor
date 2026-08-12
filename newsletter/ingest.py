#!/usr/bin/env python3
"""手動モード用。claude.ai から返ってきた応答を取り込んで、API 版と同じ成果物にする。

Anthropic の API は従量課金なので、無料で回したいときはブラウザの Claude を使う。

    python generate.py --print-prompt > prompt.txt   # 貼り付ける文面を作る
    （claude.ai に貼って、リサーチを有効にして送る。応答を response.txt に保存する）
    python ingest.py response.txt                    # 取り込む

保存先も重複防止の履歴も beehiiv への配信も、API 版とまったく同じ経路を通る。
あとから API 版に切り替えても、それまでの履歴はそのまま引き継がれる。
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from generate import (
    BASE_DIR,
    load_config,
    load_state,
    parse_output,
    resolve,
    save_state,
    write_issue,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="claude.ai の応答を取り込んで 1 号として保存する。"
    )
    parser.add_argument(
        "response",
        nargs="?",
        help="claude.ai の応答を保存したファイル。省略すると標準入力から読む。",
    )
    parser.add_argument("--config", default=str(BASE_DIR / "config.yaml"))
    parser.add_argument(
        "--type",
        choices=["weekly", "boj", "shunto"],
        default="weekly",
        help="号種。--print-prompt が表示したものを指定する。",
    )
    parser.add_argument("--date", help="配信日を YYYY-MM-DD で指定する（既定は今日）")
    args = parser.parse_args()

    raw = Path(args.response).read_text(encoding="utf-8") if args.response else sys.stdin.read()
    if not raw.strip():
        raise RuntimeError("入力が空です。claude.ai の応答をそのまま渡してください。")

    cfg = load_config(Path(args.config))
    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()

    issue = parse_output(raw)

    out_dir = BASE_DIR / resolve(cfg, "output.dir", "state/issues")
    review_path = write_issue(out_dir, today, args.type, issue)

    state_path = BASE_DIR / resolve(cfg, "dedup.state_file", "state/topics.json")
    state = load_state(state_path)

    # 同じ号を二度取り込んでしまっても履歴が汚れないようにする
    already = [
        item
        for item in state["issues"]
        if item.get("date") == today.isoformat() and item.get("title") == issue["title"]
    ]
    if already:
        print("  note: この日付・タイトルの号はすでに履歴にあります。追記をスキップしました。")
    else:
        state["issues"].append(
            {
                "date": today.isoformat(),
                "type": args.type,
                "title": issue["title"],
                "subtitle": issue["subtitle"],
                "topics": issue["topics"],
                "sources": issue["sources"],
                "source": "manual",
            }
        )
        save_state(state_path, state)

    print(f"[{today}] {args.type}: {issue['title']}")
    print(f"  wrote: {review_path.relative_to(BASE_DIR)}")

    mode = resolve(cfg, "publish.mode", "local")
    if mode == "local":
        print("  publish.mode=local — beehiiv untouched. Paste the HTML by hand.")
        return 0

    from beehiiv import publish

    print(f"  beehiiv: created as '{mode}' — {publish(cfg, issue, status=mode)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
