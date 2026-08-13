#!/usr/bin/env python3
"""Japan Money Weekly — 1 号ぶんのリサーチと執筆を行い、下書きを書き出す。

Claude に Web 検索させて素材を集めさせ、house_style.md の editorial ルールに従って
本文 HTML まで書かせる。生成物は state/issues/ に残り、config.yaml の publish.mode が
local 以外なら beehiiv にも送る。

使い方:
    python generate.py                    # config.yaml に従って自動判定
    python generate.py --type boj         # 号種を明示
    python generate.py --dry-run          # 生成するが保存も配信もしない
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

import yaml

# anthropic の import は call_claude() 内で行う。手動モード（--print-prompt / ingest.py）を
# SDK 未インストールでも動かせるようにするため。

BASE_DIR = Path(__file__).resolve().parent

# Claude API の料金（$/100万トークン）。実行ごとの概算コスト表示にのみ使う。
PRICE_INPUT_PER_MTOK = 5.00
PRICE_OUTPUT_PER_MTOK = 25.00
PRICE_PER_WEB_SEARCH = 0.01  # 1000 回で $10

# 本文が長い HTML になるため、JSON ではなくマーカー区切りで受け取る（エスケープ事故を避ける）
SECTION_MARKERS = (
    "TITLE", "SUBTITLE", "TOPICS", "SUBJECT_LINES", "SOURCES", "REVIEW_JA", "BODY_HTML",
)


# --------------------------------------------------------------------------- config


def load_config(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def resolve(cfg: dict[str, Any], dotted: str, default: Any = None) -> Any:
    node: Any = cfg
    for key in dotted.split("."):
        if not isinstance(node, dict) or key not in node:
            return default
        node = node[key]
    return node


# --------------------------------------------------------------------------- state


def load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        return {"issues": []}
    with state_path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    data.setdefault("issues", [])
    return data


def save_state(state_path: Path, state: dict[str, Any]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with state_path.open("w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def format_history(state: dict[str, Any], lookback: int) -> tuple[str, str]:
    """過去号のタイトル一覧と扱ったトピック一覧を、プロンプト差し込み用の文字列にする。"""
    issues = state["issues"][-lookback:]
    if not issues:
        return ("(none yet — this is the first issue)", "(none yet)")

    titles = "\n".join(
        f"- {item.get('date', '?')} [{item.get('type', '?')}] {item.get('title', '')}"
        for item in issues
    )

    seen: list[str] = []
    for item in issues:
        for topic in item.get("topics", []):
            if topic not in seen:
                seen.append(topic)
    topics = "\n".join(f"- {topic}" for topic in seen) if seen else "(none yet)"
    return titles, topics


# --------------------------------------------------------------------------- 号種の判定


def parse_md(value: str, year: int) -> dt.date:
    month, day = (int(part) for part in value.split("-"))
    return dt.date(year, month, day)


def decide_issue_type(cfg: dict[str, Any], today: dt.date) -> tuple[str, dict[str, Any]]:
    """日銀号 → 春闘号 → 通常号 の優先順で今日の号種を決める。"""
    types = cfg["issue_types"]

    # 1. 金融政策決定会合の直後なら日銀号。会合は年 8 回しかないので最優先。
    boj = types.get("boj", {})
    window = int(boj.get("trigger_window_days", 2))
    for raw in boj.get("meeting_dates") or []:
        meeting = dt.date.fromisoformat(str(raw))
        if 0 <= (today - meeting).days <= window:
            return "boj", {"BOJ_MEETING_DATE": meeting.isoformat()}

    # 2. 春闘シーズンなら every_nth 回に 1 回を春闘号にして、通常号と交互に出す。
    shunto = types.get("shunto", {})
    start_md, end_md = shunto.get("window_start"), shunto.get("window_end")
    if start_md and end_md:
        start, end = parse_md(start_md, today.year), parse_md(end_md, today.year)
        every = max(1, int(shunto.get("every_nth", 2)))
        if start <= today <= end and ((today - start).days // 7) % every == 0:
            return "shunto", {}

    return "weekly", {}


# --------------------------------------------------------------------------- プロンプト構築


def build_prompts(
    cfg: dict[str, Any], issue_type: str, today: dt.date, extra: dict[str, Any]
) -> tuple[str, str]:
    spec = cfg["issue_types"][issue_type]
    system = (BASE_DIR / "prompts" / "house_style.md").read_text(encoding="utf-8")
    user = (BASE_DIR / spec["prompt"]).read_text(encoding="utf-8")

    state = load_state(BASE_DIR / resolve(cfg, "dedup.state_file", "state/topics.json"))
    recent, covered = format_history(state, int(resolve(cfg, "dedup.lookback", 40)))

    values = {
        "NEWSLETTER_NAME": cfg["newsletter"]["name"],
        "TODAY": today.strftime("%A, %B %d, %Y"),
        "TARGET_WORDS": str(spec.get("target_words", 900)),
        "RECENT_ISSUES": recent,
        "COVERED_TOPICS": covered,
        **{key: str(val) for key, val in extra.items()},
    }
    for key, val in values.items():
        token = "{{" + key + "}}"
        system = system.replace(token, val)
        user = user.replace(token, val)
    return system, user


# --------------------------------------------------------------------------- Claude 呼び出し


def call_claude(cfg: dict[str, Any], system: str, user: str) -> tuple[str, dict[str, int]]:
    """Web 検索つきで 1 号ぶん書かせる。pause_turn とリフューザルを扱う。"""
    import anthropic

    client = anthropic.Anthropic()
    model_cfg = cfg["model"]

    tools = [
        {
            "type": "web_search_20260209",
            "name": "web_search",
            "max_uses": int(model_cfg.get("max_web_searches", 12)),
        }
    ]
    # house_style.md は毎号同一なのでキャッシュさせる（2 号目以降の入力コストが約 1/10 になる）
    system_blocks = [
        {"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}
    ]

    params: dict[str, Any] = {
        "model": model_cfg.get("id", "claude-opus-5"),
        "max_tokens": int(model_cfg.get("max_tokens", 32000)),
        "system": system_blocks,
        "tools": tools,
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": model_cfg.get("effort", "high")},
        # 安全性分類器が誤って拒否した場合に、Anthropic 推奨の代替モデルへ自動で回す。
        "betas": ["server-side-fallback-2026-07-01"],
        "fallbacks": "default",
    }

    messages: list[dict[str, Any]] = [{"role": "user", "content": user}]
    totals = {"input": 0, "output": 0, "searches": 0}
    max_resumes = int(model_cfg.get("max_resumes", 4))

    for attempt in range(max_resumes + 1):
        message = _stream_once(client, params, messages)

        usage = message.usage
        totals["input"] += (
            (usage.input_tokens or 0)
            + (getattr(usage, "cache_creation_input_tokens", 0) or 0)
            + (getattr(usage, "cache_read_input_tokens", 0) or 0)
        )
        totals["output"] += usage.output_tokens or 0
        server_use = getattr(usage, "server_tool_use", None)
        if server_use is not None:
            totals["searches"] += getattr(server_use, "web_search_requests", 0) or 0

        if message.stop_reason == "refusal":
            detail = getattr(message, "stop_details", None)
            category = getattr(detail, "category", None) if detail else None
            raise RuntimeError(
                f"Claude declined this request (category={category}). "
                "Rephrase the prompt or narrow the topic."
            )

        # 検索ツールがサーバ側の往復上限に達した。会話をそのまま差し戻せば続きから再開する。
        if message.stop_reason == "pause_turn":
            if attempt == max_resumes:
                raise RuntimeError(
                    f"Research did not finish within {max_resumes} resumes. "
                    "Lower model.max_web_searches or raise model.max_resumes."
                )
            messages = [
                {"role": "user", "content": user},
                {"role": "assistant", "content": message.content},
            ]
            print(f"  … research paused, resuming ({attempt + 1}/{max_resumes})")
            continue

        if message.stop_reason == "max_tokens":
            raise RuntimeError(
                "Output hit max_tokens and is truncated. Raise model.max_tokens in config.yaml."
            )

        text = "".join(block.text for block in message.content if block.type == "text")
        if not text.strip():
            raise RuntimeError("Claude returned no text content.")
        return text, totals

    raise RuntimeError("unreachable")


def _stream_once(client: Any, params: dict[str, Any], messages: list[Any]):
    """SDK が fallbacks に未対応な場合はそれを外して再試行する（CI で古い SDK を踏んでも止めない）。"""
    import anthropic

    try:
        with client.beta.messages.stream(**params, messages=messages) as stream:
            return stream.get_final_message()
    except TypeError as exc:
        if "fallbacks" not in str(exc):
            raise
    except anthropic.BadRequestError as exc:
        if "fallback" not in str(exc).lower():
            raise

    print("  … this SDK/account does not accept server-side fallbacks; continuing without them")
    reduced = {key: val for key, val in params.items() if key not in ("fallbacks", "betas")}
    with client.messages.stream(**reduced, messages=messages) as stream:
        return stream.get_final_message()


# --------------------------------------------------------------------------- 出力の解析


def parse_output(raw: str) -> dict[str, Any]:
    """===MARKER=== 区切りの応答を分解する。"""
    pattern = "|".join(SECTION_MARKERS)
    parts = re.split(rf"^===({pattern})===\s*$", raw.strip(), flags=re.MULTILINE)

    sections: dict[str, str] = {}
    for idx in range(1, len(parts) - 1, 2):
        sections[parts[idx]] = parts[idx + 1].strip()

    missing = [name for name in SECTION_MARKERS if not sections.get(name)]
    if missing:
        raise RuntimeError(
            f"Response was missing required sections: {', '.join(missing)}. "
            "Check prompts/house_style.md — the output contract may have drifted."
        )

    def bullets(text: str) -> list[str]:
        return [
            line.lstrip("-*").strip()
            for line in text.splitlines()
            if line.strip().startswith(("-", "*"))
        ]

    body = sections["BODY_HTML"]
    # モデルがコードフェンスで包んでしまった場合に備えて剥がす
    body = re.sub(r"^```(?:html)?\s*|\s*```$", "", body.strip())

    return {
        "title": sections["TITLE"].strip().strip("#").strip(),
        "subtitle": sections["SUBTITLE"].strip(),
        "topics": bullets(sections["TOPICS"]),
        "subject_lines": bullets(sections["SUBJECT_LINES"]),
        "sources": bullets(sections["SOURCES"]),
        "review_ja": sections["REVIEW_JA"].strip(),
        "body_html": body,
    }


def slugify(text: str, limit: int = 60) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
    return (slug[:limit].rstrip("-") or "issue")


def to_ascii_html(markup: str) -> str:
    """非 ASCII 文字を数値文字参照に変換する。

    ¥ や em dash（—）は UTF-8 では multi-byte になるため、Windows のメモ帳や Excel など
    CP932 を既定とするアプリで開くと「ﾂ･」「窶」のように化ける。数値文字参照にしておけば
    ファイルは純 ASCII になり、どのエンコーディングで開いても壊れず、ブラウザと beehiiv は
    元の文字として描画する。
    """
    return markup.encode("ascii", "xmlcharrefreplace").decode("ascii")


def write_issue(out_dir: Path, today: dt.date, issue_type: str, issue: dict[str, Any]) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{today.isoformat()}-{slugify(issue['title'])}"

    # 貼り付け用。純 ASCII なので文字化けしない。
    (out_dir / f"{stem}.html").write_text(
        to_ascii_html(issue["body_html"]) + "\n", encoding="utf-8"
    )

    # 日本語のレビュー用サマリーを先頭に置く。公開前に最初に読む場所であり、配信はされない。
    review = [
        f"# {issue['title']}",
        "",
        f"*{issue['subtitle']}*",
        "",
        f"- 配信日: {today.isoformat()}",
        f"- 号種: {issue_type}",
        "",
        "---",
        "",
        "## レビュー用サマリー（日本語・配信されません）",
        "",
        issue["review_ja"],
        "",
        "---",
        "",
        "## 件名の候補（beehiiv の Subject line に入れる）",
        "",
        "スマホの受信箱では先頭 40 文字ほどしか見えない。前半だけで意味が通るものを選ぶ。",
        "",
        *[f"{i}. {line}  （{len(line)} 文字）" for i, line in enumerate(issue["subject_lines"], 1)],
        "",
        "---",
        "",
        "## 出典",
        "",
        *[f"- {src}" for src in issue["sources"]],
        "",
        "## 扱ったトピック",
        "",
        *[f"- {topic}" for topic in issue["topics"]],
        "",
        "## 本文（この HTML を beehiiv に貼る）",
        "",
        "```html",
        to_ascii_html(issue["body_html"]),
        "```",
        "",
    ]
    review_path = out_dir / f"{stem}.md"
    # BOM 付きで書く。日本語のレビュー欄を含むので純 ASCII にはできないが、BOM があれば
    # Windows のメモ帳や Excel が UTF-8 と判定するため、CP932 として読まれて化けるのを防げる。
    review_path.write_text("\n".join(review), encoding="utf-8-sig")
    return review_path


# --------------------------------------------------------------------------- entrypoint


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate one issue of the newsletter.")
    parser.add_argument("--config", default=str(BASE_DIR / "config.yaml"))
    parser.add_argument("--type", choices=["weekly", "boj", "shunto"], help="号種を明示する")
    parser.add_argument("--date", help="実行日を YYYY-MM-DD で上書きする（テスト用）")
    parser.add_argument("--dry-run", action="store_true", help="生成するが保存も配信もしない")
    parser.add_argument(
        "--print-prompt",
        action="store_true",
        help="API を呼ばず、claude.ai に貼るためのプロンプトを出力する（無料の手動モード）",
    )
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()

    if args.type:
        issue_type, extra = args.type, {}
        if issue_type == "boj":
            extra = {"BOJ_MEETING_DATE": today.isoformat()}
    else:
        issue_type, extra = decide_issue_type(cfg, today)

    # --print-prompt では標準出力がそのまま貼り付け用の文章になるので、
    # 進捗ログは必ず標準エラーへ出す。
    log = sys.stderr if args.print_prompt else sys.stdout
    print(f"[{today}] edition: {issue_type}", file=log)

    system, user = build_prompts(cfg, issue_type, today, extra)

    if args.print_prompt:
        # 手動モード。この出力をまるごと claude.ai に貼り、リサーチ（Web 検索）を有効にして送る。
        # 返ってきた応答を丸ごと保存し、`python ingest.py <file>` に渡せば API 版と同じ成果物になる。
        print("=" * 78, file=sys.stderr)
        print(
            f"以下を claude.ai に貼り付けてください（{issue_type} 号 / {today}）。\n"
            "リサーチ機能（Web 検索）を必ず有効にすること。\n"
            "返ってきた応答を丸ごとファイルに保存し、次を実行します:\n"
            f"    python ingest.py response.txt --type {issue_type} --date {today}",
            file=sys.stderr,
        )
        print("=" * 78, file=sys.stderr)
        # プロンプト本体だけを標準出力に出すので、そのままファイルへリダイレクトできる
        print(system)
        print()
        print("-" * 78)
        print()
        print(user)
        return 0

    print("  researching and writing (this usually takes several minutes) …")
    raw, totals = call_claude(cfg, system, user)
    issue = parse_output(raw)

    cost = (
        totals["input"] / 1_000_000 * PRICE_INPUT_PER_MTOK
        + totals["output"] / 1_000_000 * PRICE_OUTPUT_PER_MTOK
        + totals["searches"] * PRICE_PER_WEB_SEARCH
    )
    print(f"  title: {issue['title']}")
    print(
        f"  usage: {totals['input']:,} in / {totals['output']:,} out / "
        f"{totals['searches']} searches  ≈ ${cost:.2f}"
    )

    if args.dry_run:
        print("\n--- dry run, nothing written ---\n")
        print(issue["body_html"][:2000])
        return 0

    out_dir = BASE_DIR / resolve(cfg, "output.dir", "state/issues")
    review_path = write_issue(out_dir, today, issue_type, issue)
    print(f"  wrote: {review_path.relative_to(BASE_DIR)}")

    state_path = BASE_DIR / resolve(cfg, "dedup.state_file", "state/topics.json")
    state = load_state(state_path)
    state["issues"].append(
        {
            "date": today.isoformat(),
            "type": issue_type,
            "title": issue["title"],
            "subtitle": issue["subtitle"],
            "topics": issue["topics"],
            "sources": issue["sources"],
            "estimated_cost_usd": round(cost, 4),
        }
    )
    save_state(state_path, state)

    mode = resolve(cfg, "publish.mode", "local")
    if mode == "local":
        print("  publish.mode=local — beehiiv untouched. Paste the HTML above by hand.")
        return 0

    from beehiiv import publish  # 遅延 import：local 運用では requests すら不要にする

    post_url = publish(cfg, issue, status=mode)
    print(f"  beehiiv: created as '{mode}' — {post_url}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
