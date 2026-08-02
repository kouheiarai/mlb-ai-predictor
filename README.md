# MLB AI Predictor

GitHub ActionsでPinnacle系オッズ、MLB公式日程・予告先発、ラインアップ、ブルペン代理指標、天候、チーム指標を取得し、ML・ランライン・合計得点の予測ファイルを毎時生成・公開します。

## ChatGPT / Claude から読む

以下の URL をそのまま渡してください（GitHub Pages で公開、毎時更新）。

| 用途 | URL | サイズ目安 |
| --- | --- | --- |
| **まずこれ**（推奨ピックのみ・軽量） | https://kouheiarai.github.io/mlb-ai-predictor/summary.txt | 約 10KB |
| 同じ内容の JSON | https://kouheiarai.github.io/mlb-ai-predictor/summary.json | 約 25KB |
| 全予測 JSON（正本） | https://kouheiarai.github.io/mlb-ai-predictor/prediction_latest.json | 約 180KB |
| 表形式で集計したいとき | https://kouheiarai.github.io/mlb-ai-predictor/predictions.csv | 約 45KB |
| 全試合の詳細レポート | https://kouheiarai.github.io/mlb-ai-predictor/latest.md | 約 15KB |
| 人が見るダッシュボード | https://kouheiarai.github.io/mlb-ai-predictor/ | 約 18KB |
| AI 向けの案内 | https://kouheiarai.github.io/mlb-ai-predictor/llms.txt | 約 4KB |
| 更新時刻・件数の確認 | https://kouheiarai.github.io/mlb-ai-predictor/output_manifest.json | 約 0.3KB |

市場別 CSV は `moneyline_predictions.csv` / `runline_predictions.csv` / `total_predictions.csv`、
補助データは `mlb_schedule.json` / `elo_ratings.json` / `team_metrics.json` /
`bullpen_fatigue.json` / `weather.json` / `lineups_latest.json` / `latest_odds.json` を
同じ階層に置いています。全ファイルは `docs/` 配下と GitHub の `data/` 配下にも同内容で存在します。

`robots.txt` で GPTBot・ChatGPT-User・OAI-SearchBot・ClaudeBot・Claude-User などの取得を明示的に許可しています。

### AI が「取得できない」と言うとき

サーバ側は全 URL が 200 を返し、上記のクローラーもブロックしていません。
取得できない場合は AI 側の事情なので、次の順に試してください。

1. **`summary.txt` を渡す。** `prediction_latest.json` は約 180KB あり、取得ツールが
   読み込めないことがあります。`summary.txt` は約 10KB で BUY 判定を全部含みます。
2. **GitHub コネクタではなく Web 閲覧で読ませる。** コネクタはリポジトリ内のファイルしか
   読めず、`github.io` の URL は取得対象外です。コネクタを使う場合は URL ではなく
   リポジトリ内のパス（例: `kouheiarai/mlb-ai-predictor` の `summary.txt`）を指定してください。
3. **新しい会話で試す。** 以前に壊れたファイルを読んだ会話を続けると、その内容が
   文脈に残って誤った回答が続きます。

## 必須設定

GitHubリポジトリの **Settings → Secrets and variables → Actions** に次を登録してください。

- `THE_ODDS_API_KEY`

GitHub Pages は **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`** で有効化します。

## 実行

**Actions → MLB AI Predictor Auto Update → Run workflow**

処理の流れは次のとおりです。

1. `python main.py` — オッズと各種データを取得し、`data/` に予測ファイル一式を生成する。
2. `python publish.py` — `data/` を正本として、リポジトリ直下と `docs/` に公開用ファイル
   （`index.html` / `llms.txt` / `robots.txt` / `sitemap.xml` / `latest.md` と各 JSON・CSV）を配布する。
3. `python validate_outputs.py` — 公開 URL が想定どおりの中身か検査する。

## 主な CSV / JSON の項目

- `decimal_odds` — ブックメーカーのデシマルオッズ
- `market_no_vig_probability` — 控除率を除いた市場の含意確率
- `model_probability` — 本モデルの推定的中確率
- `ev` — 期待値（`model_probability * decimal_odds - 1`）
- `quarter_kelly` — ケリー基準の 1/4 を推奨賭け率としたもの
- `recommendation` — `BUY` または `PASS`
- `confidence` — 信頼度ランク（ラインアップ発表状況やデータ被覆率を反映）

## 注意

- ファイルを GitHub の「Add files via upload」でまとめて差し替えると、名前と中身が入れ違いになる事故が起きています。
  公開ファイルは手で置き換えず、`python main.py && python publish.py` で生成してください。
  `validate_outputs.py` が同種の破損を CI で検知します。
- 現行モデルの一部指標は公開データから作る代理指標であり、すべてがStatcast由来の厳密なWAR/FIP分解ではありません。
- 予測であり結果を保証するものではありません。
