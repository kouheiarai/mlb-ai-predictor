"""公開エンドポイントを生成する。

`data/` に置かれた生成物を正本として、GitHub Pages のルートと `docs/` に
同じ内容を配布し、ChatGPT / Claude などが取得しやすい形の
`index.html` / `llms.txt` / `latest.md` / `robots.txt` を書き出す。

`python publish.py` 単体でも実行できる（main.py の実行後に呼ぶ想定）。
"""

from __future__ import annotations

import html
import json
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

DATA_DIR = Path("data")
DOCS_DIR = Path("docs")
ROOT_DIR = Path(".")
SITE_URL = "https://kouheiarai.github.io/mlb-ai-predictor"
JST = timezone(timedelta(hours=9))

# data/ 配下からルートと docs/ へ配布するファイル。
MIRRORED_SUFFIXES = (".json", ".csv", ".md")

AI_USER_AGENTS = (
    "GPTBot",
    "ChatGPT-User",
    "OAI-SearchBot",
    "ClaudeBot",
    "Claude-User",
    "Claude-SearchBot",
    "anthropic-ai",
    "PerplexityBot",
    "Perplexity-User",
    "Google-Extended",
    "Applebot-Extended",
    "CCBot",
    "Bingbot",
)

MARKET_LABELS = {
    "moneyline": "マネーライン",
    "runline": "ランライン",
    "total": "合計得点",
}


def _to_jst(iso_utc: str) -> str:
    try:
        return (
            datetime.fromisoformat(iso_utc.replace("Z", "+00:00"))
            .astimezone(JST)
            .strftime("%Y-%m-%d %H:%M JST")
        )
    except (TypeError, ValueError):
        return iso_utc or "-"


def _pct(value: Any) -> str:
    try:
        return f"{float(value) * 100:.1f}%"
    except (TypeError, ValueError):
        return "-"


def _num(value: Any, digits: int = 2) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return "-"


def _selection_label(row: dict[str, Any]) -> str:
    selection = str(row.get("selection", "") or "")
    point = row.get("point", "")
    if point in (None, "", "-"):
        return selection
    try:
        point_value = float(point)
    except (TypeError, ValueError):
        return f"{selection} {point}"
    return f"{selection} {point_value:+g}"


def mirror_data_outputs() -> list[str]:
    """data/ の生成物をルートと docs/ にコピーする。"""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for source in sorted(DATA_DIR.iterdir()):
        if not source.is_file() or source.suffix not in MIRRORED_SUFFIXES:
            continue
        for target_dir in (ROOT_DIR, DOCS_DIR):
            shutil.copyfile(source, target_dir / source.name)
        copied.append(source.name)
    # 全文レポートは latest.md という判別しやすい名前でも公開する。
    report = DATA_DIR / "report.md"
    if report.is_file():
        for target_dir in (ROOT_DIR, DOCS_DIR):
            shutil.copyfile(report, target_dir / "latest.md")
        copied.append("latest.md")
    return copied


STALE_AFTER_HOURS = 12


def data_age_hours(latest: dict[str, Any]) -> float | None:
    """データが生成されてから何時間経ったか。"""
    try:
        updated = datetime.fromisoformat(str(latest.get("updated_at_utc", "")))
    except ValueError:
        return None
    return (datetime.now(timezone.utc) - updated).total_seconds() / 3600


def staleness_notice(latest: dict[str, Any]) -> list[str]:
    """古いデータであることを読み手に必ず伝えるための文言。

    The Odds API のクレジットが尽きると更新が止まり、公開ファイルは最後に
    成功した内容のまま残る。何も書かないと、読んだ AI が終わった試合を
    今日の予想として提示してしまうため、先頭で明示する。
    """
    hours = data_age_hours(latest)
    if hours is None or hours < STALE_AFTER_HOURS:
        return []
    days, rest = divmod(int(hours), 24)
    elapsed = f"{days}日{rest}時間前" if days else f"{rest}時間前"
    return [
        "【重要・古いデータです】",
        f"このデータは {_to_jst(str(latest.get('updated_at_utc', '')))} 時点のもので、"
        f"{elapsed}に生成されました。",
        "The Odds API の月間クレジットを使い切ったため自動更新が止まっています。",
        "以下に並ぶ試合はすでに終了している可能性が高く、本日の予想ではありません。",
        "クレジットは翌月にリセットされ、その時点で自動的に更新が再開します。",
        "",
    ]


def build_summary_text(latest: dict[str, Any]) -> str:
    """1リクエストで読み切れる軽量なテキスト版の推奨一覧を作る。

    prediction_latest.json は全試合の全指標を含むため 180KB 前後になり、
    ChatGPT の取得ツールでは読み込めないことがある。BUY だけを 1行に
    まとめた数 KB の入口を別に用意する。
    """
    summary = latest.get("summary", {}) or {}
    rankings = latest.get("buy_rankings", {}) or {}
    updated = str(latest.get("updated_at_utc", ""))

    lines = [
        f"MLB AI Predictor Ver.{latest.get('model_version', '-')} 推奨一覧",
        "",
        *staleness_notice(latest),
        f"更新: {_to_jst(updated)}（UTC {updated}）",
        f"対象日 (UTC): {', '.join(latest.get('target_dates_utc', []) or []) or '-'}",
        f"対象試合数: {latest.get('game_count', '-')}",
        f"BUY 件数: マネーライン {summary.get('moneyline_buy_count', 0)} / "
        f"ランライン {summary.get('runline_buy_count', 0)} / "
        f"合計得点 {summary.get('total_buy_count', 0)}",
        f"オッズ: {(latest.get('source') or {}).get('odds', '-')}",
        "",
    ]

    for market, label in MARKET_LABELS.items():
        rows = rankings.get(market) or []
        lines.append(f"## {label}（EV 降順・{len(rows)} 件）")
        if not rows:
            lines.extend(["BUY 判定なし。", ""])
            continue
        for index, row in enumerate(rows, start=1):
            lines.append(
                f"{index}. {_selection_label(row)} | "
                f"{row.get('away_team', '')} @ {row.get('home_team', '')} | "
                f"{_to_jst(str(row.get('commence_time_utc', '')))} | "
                f"オッズ {_num(row.get('decimal_odds'))} | "
                f"AI勝率 {_pct(row.get('model_probability'))} | "
                f"EV {_pct(row.get('ev'))} | "
                f"1/4ケリー {_pct(row.get('quarter_kelly'))} | "
                f"信頼度 {row.get('confidence', '-') or '-'}"
            )
        lines.append("")

    lines.extend(
        [
            "## 注意",
            "",
            "- 予測であり的中を保証しない。",
            "- 掲載しているのは開始前の試合のみ。試合中のライブオッズは"
            "前提が異なるため除外している。",
            f"- 全試合の全指標は {SITE_URL}/prediction_latest.json"
            f"（約 180KB）または {SITE_URL}/predictions.csv にある。",
            "",
        ]
    )
    return "\n".join(lines)


def build_summary_json(latest: dict[str, Any]) -> str:
    """BUY のみ・項目を絞った軽量 JSON。"""
    keep = (
        "market",
        "away_team",
        "home_team",
        "commence_time_utc",
        "selection",
        "point",
        "decimal_odds",
        "model_probability",
        "ev",
        "quarter_kelly",
        "confidence",
    )
    rankings = latest.get("buy_rankings", {}) or {}
    hours = data_age_hours(latest)
    payload = {
        "model_version": latest.get("model_version"),
        "updated_at_utc": latest.get("updated_at_utc"),
        "data_age_hours": round(hours, 1) if hours is not None else None,
        "is_stale": bool(hours is not None and hours >= STALE_AFTER_HOURS),
        "stale_warning": (
            "The Odds API の月間クレジットを使い切ったため自動更新が止まっている。"
            "掲載の試合はすでに終了している可能性が高く、本日の予想ではない。"
            if hours is not None and hours >= STALE_AFTER_HOURS
            else None
        ),
        "target_dates_utc": latest.get("target_dates_utc"),
        "game_count": latest.get("game_count"),
        "summary": latest.get("summary", {}),
        "note": (
            "BUY 判定のみを抜粋した軽量版。全試合の全指標は "
            f"{SITE_URL}/prediction_latest.json を参照。"
        ),
        "buy_rankings": {
            market: [{k: row.get(k) for k in keep} for row in (rankings.get(market) or [])]
            for market in MARKET_LABELS
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _rows_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return '<p class="empty">この市場に BUY 判定はありません。</p>'
    cells = []
    for index, row in enumerate(rows, start=1):
        cells.append(
            "<tr>"
            f"<td>{index}</td>"
            f"<td class=\"pick\">{html.escape(_selection_label(row))}</td>"
            f"<td>{html.escape(str(row.get('away_team', '')))} @ "
            f"{html.escape(str(row.get('home_team', '')))}</td>"
            f"<td>{html.escape(_to_jst(str(row.get('commence_time_utc', ''))))}</td>"
            f"<td>{_num(row.get('decimal_odds'))}</td>"
            f"<td>{_pct(row.get('model_probability'))}</td>"
            f"<td class=\"ev\">{_pct(row.get('ev'))}</td>"
            f"<td>{_pct(row.get('quarter_kelly'))}</td>"
            f"<td>{html.escape(str(row.get('confidence', '-') or '-'))}</td>"
            "</tr>"
        )
    return (
        '<div class="table-wrap"><table>'
        "<thead><tr><th>#</th><th>ピック</th><th>試合</th><th>開始</th>"
        "<th>オッズ</th><th>AI勝率</th><th>EV</th><th>1/4ケリー</th><th>信頼度</th>"
        "</tr></thead><tbody>" + "".join(cells) + "</tbody></table></div>"
    )


def build_index_html(latest: dict[str, Any]) -> str:
    updated_utc = str(latest.get("updated_at_utc", ""))
    summary = latest.get("summary", {}) or {}
    rankings = latest.get("buy_rankings", {}) or {}

    sections = []
    for market, label in MARKET_LABELS.items():
        rows = rankings.get(market) or []
        sections.append(
            f'<section id="{market}"><h2>{label} BUY ランキング '
            f'<span class="count">{len(rows)} 件</span></h2>{_rows_table(rows)}</section>'
        )

    quota = latest.get("api_quota", {}) or {}
    source = latest.get("source", {}) or {}
    target_dates = ", ".join(latest.get("target_dates_utc", []) or []) or "-"

    notice = staleness_notice(latest)
    banner = (
        '<div class="stale"><strong>'
        + html.escape(notice[0])
        + "</strong><br>"
        + "<br>".join(html.escape(line) for line in notice[1:] if line)
        + "</div>"
        if notice
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MLB AI Predictor Ver.{html.escape(str(latest.get('model_version', '')))} - 最新予測</title>
<meta name="description" content="MLB の勝敗・ランライン・合計得点をモンテカルロ法で予測した最新結果。更新: {html.escape(updated_utc)} (UTC)。JSON / CSV エンドポイント公開中。">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/">
<style>
  :root {{ color-scheme: light dark; --bg:#ffffff; --fg:#16181d; --muted:#5b6472;
           --line:#e2e6ec; --card:#f6f8fa; --accent:#0b7d3e; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg:#0f1216; --fg:#e8ecf1; --muted:#98a2b3; --line:#252b33;
             --card:#161b22; --accent:#3fb96f; }}
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; padding:1.5rem 1rem 4rem; background:var(--bg); color:var(--fg);
         font:15px/1.6 system-ui,-apple-system,"Hiragino Sans","Noto Sans JP",sans-serif; }}
  main {{ max-width: 1080px; margin: 0 auto; }}
  h1 {{ font-size:1.5rem; margin:0 0 .25rem; }}
  h2 {{ font-size:1.1rem; margin:2rem 0 .6rem; border-bottom:1px solid var(--line);
        padding-bottom:.4rem; }}
  .count {{ font-size:.8rem; color:var(--muted); font-weight:400; }}
  .meta {{ color:var(--muted); font-size:.85rem; margin:0 0 1.25rem; }}
  .cards {{ display:grid; gap:.75rem; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); }}
  .card {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:.75rem .9rem; }}
  .card b {{ display:block; font-size:1.35rem; }}
  .card span {{ color:var(--muted); font-size:.8rem; }}
  .table-wrap {{ overflow-x:auto; }}
  table {{ border-collapse:collapse; width:100%; font-size:.86rem; min-width:760px; }}
  th, td {{ text-align:left; padding:.45rem .55rem; border-bottom:1px solid var(--line); white-space:nowrap; }}
  th {{ color:var(--muted); font-weight:600; }}
  td.pick {{ font-weight:600; }}
  td.ev {{ color:var(--accent); font-weight:600; }}
  .empty {{ color:var(--muted); }}
  .stale {{ background:#fdf2d5; color:#5c4409; border:1px solid #e6c65c;
            border-radius:10px; padding:.8rem 1rem; margin:0 0 1.25rem; font-size:.9rem; }}
  @media (prefers-color-scheme: dark) {{
    .stale {{ background:#332a10; color:#f2dfa4; border-color:#6b551d; }}
  }}
  ul.endpoints {{ padding-left:1.1rem; }}
  ul.endpoints code {{ font-size:.85rem; }}
  footer {{ margin-top:2.5rem; color:var(--muted); font-size:.8rem;
            border-top:1px solid var(--line); padding-top:1rem; }}
</style>
</head>
<body>
<main>
  <h1>MLB AI Predictor Ver.{html.escape(str(latest.get('model_version', '')))}</h1>
  {banner}
  <p class="meta">
    最終更新: <strong>{html.escape(_to_jst(updated_utc))}</strong>
    （UTC: {html.escape(updated_utc)}）<br>
    対象日 (UTC): {html.escape(target_dates)} ／ 対象試合数: {html.escape(str(latest.get('game_count', '-')))}
    ／ 1試合あたり {int(latest.get('simulation_count_per_game') or 0):,} 回シミュレーション<br>
    オッズ: {html.escape(str(source.get('odds', '-')))} ／ データ: {html.escape(str(source.get('baseball_data', '-')))}
  </p>

  <div class="cards">
    <div class="card"><b>{summary.get('moneyline_buy_count', 0)}</b><span>マネーライン BUY</span></div>
    <div class="card"><b>{summary.get('runline_buy_count', 0)}</b><span>ランライン BUY</span></div>
    <div class="card"><b>{summary.get('total_buy_count', 0)}</b><span>合計得点 BUY</span></div>
    <div class="card"><b>{_pct(latest.get('buy_threshold_ev'))}</b><span>BUY 判定の EV 閾値</span></div>
  </div>

  {''.join(sections)}

  <section id="endpoints">
    <h2>機械可読エンドポイント</h2>
    <p>ChatGPT・Claude などから読み込む場合は下記 URL を直接指定してください。自動更新されます。
    取得サイズに制約がある環境では、まず軽量な <code>summary.txt</code> を使ってください。</p>
    <ul class="endpoints">
      <li><code><a href="{SITE_URL}/summary.txt">{SITE_URL}/summary.txt</a></code> — <strong>推奨ピックのみ（数 KB・軽量）</strong></li>
      <li><code><a href="{SITE_URL}/summary.json">{SITE_URL}/summary.json</a></code> — 同上の JSON 版</li>
      <li><code><a href="{SITE_URL}/prediction_latest.json">{SITE_URL}/prediction_latest.json</a></code> — 全予測（正本 JSON・約 180KB）</li>
      <li><code><a href="{SITE_URL}/predictions.csv">{SITE_URL}/predictions.csv</a></code> — 全市場まとめ CSV</li>
      <li><code><a href="{SITE_URL}/moneyline_predictions.csv">{SITE_URL}/moneyline_predictions.csv</a></code> — マネーライン CSV</li>
      <li><code><a href="{SITE_URL}/runline_predictions.csv">{SITE_URL}/runline_predictions.csv</a></code> — ランライン CSV</li>
      <li><code><a href="{SITE_URL}/total_predictions.csv">{SITE_URL}/total_predictions.csv</a></code> — 合計得点 CSV</li>
      <li><code><a href="{SITE_URL}/latest.md">{SITE_URL}/latest.md</a></code> — テキスト版レポート</li>
      <li><code><a href="{SITE_URL}/output_manifest.json">{SITE_URL}/output_manifest.json</a></code> — 生成メタ情報</li>
      <li><code><a href="{SITE_URL}/llms.txt">{SITE_URL}/llms.txt</a></code> — AI 向けエンドポイント一覧</li>
    </ul>
  </section>

  <footer>
    The Odds API 残リクエスト: {html.escape(str(quota.get('requests_remaining', '-')))}
    ／ schema_version {html.escape(str(latest.get('schema_version', '-')))}<br>
    予測値であり的中を保証するものではありません。賭博に関する法令は各自の居住地のものに従ってください。
  </footer>
</main>
</body>
</html>
"""


def build_llms_txt(latest: dict[str, Any]) -> str:
    summary = latest.get("summary", {}) or {}
    notice = staleness_notice(latest)
    warning = ("\n".join(f"> **{line}**" if i == 0 else f"> {line}"
                         for i, line in enumerate(notice) if line) + "\n") if notice else ""
    return f"""# MLB AI Predictor

{warning}

> MLB の各試合について、マネーライン・ランライン・合計得点を
> モンテカルロ法（1試合 {int(latest.get('simulation_count_per_game') or 0):,} 回）で予測し、
> Pinnacle のオッズと比較して期待値 (EV) とケリー基準の推奨賭け率を算出する公開データセット。
> GitHub Actions により毎時更新される。

- モデルバージョン: {latest.get('model_version', '-')}
- 最終更新 (UTC): {latest.get('updated_at_utc', '-')}
- 対象日 (UTC): {', '.join(latest.get('target_dates_utc', []) or []) or '-'}
- 対象試合数: {latest.get('game_count', '-')}
- BUY 件数: マネーライン {summary.get('moneyline_buy_count', 0)} / ランライン {summary.get('runline_buy_count', 0)} / 合計得点 {summary.get('total_buy_count', 0)}

## まずこれを読む（軽量・数 KB）

- [summary.txt]({SITE_URL}/summary.txt): BUY 判定の全ピックを 1行 1件のプレーンテキストにしたもの。取得サイズに制約がある環境はこれを使う。
- [summary.json]({SITE_URL}/summary.json): 同じ内容の JSON。項目を 11 個に絞ってある。
- [summary.md]({SITE_URL}/summary.md): summary.txt と同一内容（拡張子違い）。

## 全量エンドポイント

- [prediction_latest.json]({SITE_URL}/prediction_latest.json): 全予測を含む JSON。`summary`（各市場の推奨1件）、`buy_rankings`（EV 降順の BUY 一覧）、`all_predictions`（全試合）を持つ。約 180KB あるので取得制限に注意。
- [predictions.csv]({SITE_URL}/predictions.csv): 3市場をまとめた CSV。1行 = 1ピック。表計算・集計向け。
- [latest.md]({SITE_URL}/latest.md): 全試合の詳細を含む人間可読レポート（Markdown）。

## 市場別 CSV

- [moneyline_predictions.csv]({SITE_URL}/moneyline_predictions.csv): 勝敗（マネーライン）。
- [runline_predictions.csv]({SITE_URL}/runline_predictions.csv): ランライン（±1.5 点ハンデ）。
- [total_predictions.csv]({SITE_URL}/total_predictions.csv): 合計得点のオーバー／アンダー。

## 補助データ

- [output_manifest.json]({SITE_URL}/output_manifest.json): 生成時刻と行数のメタ情報。取得データの鮮度確認に使う。
- [mlb_schedule.json]({SITE_URL}/mlb_schedule.json): 日程と予告先発。
- [elo_ratings.json]({SITE_URL}/elo_ratings.json): チーム別 Elo レーティング。
- [team_metrics.json]({SITE_URL}/team_metrics.json): チーム打撃・投球指標。
- [bullpen_fatigue.json]({SITE_URL}/bullpen_fatigue.json): ブルペン疲労の代理指標。
- [weather.json]({SITE_URL}/weather.json): 球場の気象データと得点補正係数。
- [lineups_latest.json]({SITE_URL}/lineups_latest.json): 発表済みまたは推定のスターティングラインアップ。
- [latest_odds.json]({SITE_URL}/latest_odds.json): 取得した生オッズ。

## 主要フィールドの意味

- `decimal_odds`: ブックメーカーのデシマルオッズ。
- `market_no_vig_probability`: 控除率を除いた市場の含意確率。
- `model_probability`: 本モデルが推定した的中確率。
- `ev`: 期待値。`model_probability * decimal_odds - 1`。
- `quarter_kelly`: ケリー基準の 1/4 を推奨賭け率としたもの。
- `recommendation`: `BUY`（EV が閾値 {latest.get('buy_threshold_ev', 0.05)} 超）または `PASS`。
- `confidence`: A/B/C/S などの信頼度ランク。ラインアップ発表状況やデータ被覆率を反映。

## 注意

- 予測であり結果を保証しない。過去成績の検証データは含まれない。
- 一部指標は公開データから構成した代理指標であり、Statcast 由来の厳密な分解ではない。
- 同じ内容は `{SITE_URL}/docs/` 配下および GitHub リポジトリの `data/` 配下にも配置されている。
"""


def build_robots_txt() -> str:
    lines = [
        "# MLB AI Predictor - AI クローラーおよび検索エンジンの取得を許可する。",
        "User-agent: *",
        "Allow: /",
        "",
    ]
    for agent in AI_USER_AGENTS:
        lines.extend([f"User-agent: {agent}", "Allow: /", ""])
    lines.append(f"Sitemap: {SITE_URL}/sitemap.xml")
    lines.append("")
    return "\n".join(lines)


def build_sitemap_xml(latest: dict[str, Any]) -> str:
    updated = str(latest.get("updated_at_utc", ""))[:10] or datetime.now(
        timezone.utc
    ).strftime("%Y-%m-%d")
    paths = ("/", "/prediction_latest.json", "/predictions.csv", "/latest.md", "/llms.txt")
    entries = "".join(
        f"<url><loc>{SITE_URL}{path}</loc><lastmod>{updated}</lastmod>"
        "<changefreq>hourly</changefreq></url>"
        for path in paths
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}</urlset>\n"
    )


def _write_both(name: str, content: str) -> None:
    for target_dir in (ROOT_DIR, DOCS_DIR):
        (target_dir / name).write_text(content, encoding="utf-8")


def publish() -> None:
    latest_path = DATA_DIR / "prediction_latest.json"
    if not latest_path.is_file():
        raise RuntimeError(f"{latest_path} が見つかりません。先に main.py を実行してください。")
    latest = json.loads(latest_path.read_text(encoding="utf-8"))

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    copied = mirror_data_outputs()

    # 軽量な入口。ChatGPT のように取得サイズに制約がある環境向け。
    summary_text = build_summary_text(latest)
    _write_both("summary.txt", summary_text)
    _write_both("summary.md", summary_text)
    _write_both("summary.json", build_summary_json(latest))

    _write_both("index.html", build_index_html(latest))
    _write_both("llms.txt", build_llms_txt(latest))
    _write_both("robots.txt", build_robots_txt())
    _write_both("sitemap.xml", build_sitemap_xml(latest))
    # Jekyll による加工を無効化し、data/ や _ 始まりのファイルもそのまま配信する。
    for target_dir in (ROOT_DIR, DOCS_DIR):
        (target_dir / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Published {len(copied)} data files + index.html/llms.txt/robots.txt/sitemap.xml")


if __name__ == "__main__":
    publish()
