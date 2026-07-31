# MLB AI Predictor Ver.23.1

Pinnacleオッズ、MLB公式データ、予告先発、打線、ELO、ブルペン疲労、天候、左右情報を統合し、各試合10万回のスコアシミュレーションでMoneyline／Run Lineを評価します。

## 出力

- `data/predictions.json`：全予測
- `data/moneyline_predictions.csv`
- `data/runline_predictions.csv`
- `data/report.md`
- `docs/prediction_latest.json`：外部参照用の最新JSON
- `docs/index.html`：GitHub Pages用ダッシュボード

## 初期設定

1. GitHubの `Settings > Secrets and variables > Actions` を開く
2. `THE_ODDS_API_KEY` を登録する
3. `Actions > MLB Predictor Auto Update > Run workflow` を実行する
4. `Settings > Pages` で `Deploy from a branch` を選ぶ
5. Branchを `main`、Folderを `/docs` に設定して保存する

公開URL例：

- `https://kouheiarai.github.io/mlb-ai-predictor/`
- `https://kouheiarai.github.io/mlb-ai-predictor/prediction_latest.json`
