# MLB AI Predictor

The Odds APIからPinnacleのMLBオッズを取得し、GitHub Actionsで毎日自動更新する土台です。

## 現時点で自動化されるもの

- Pinnacle Moneyline（`h2h`）
- Pinnacle Run Line（`spreads`）
- 小数オッズ・アメリカンオッズ
- 市場の暗黙勝率
- CSV / JSON / Markdownの自動生成
- 毎日07:10（日本時間）の自動実行
- GitHubリポジトリへの結果保存

## 出力

- `data/latest_odds.csv`
- `data/latest_odds.json`
- `data/report.md`

## 必要なSecret

`Settings > Secrets and variables > Actions > New repository secret`

- Name: `THE_ODDS_API_KEY`
- Secret: The Odds APIのAPIキー

## 初回テスト

1. `Actions` を開く
2. `MLB Odds Auto Update` を選択
3. `Run workflow` を押す
4. 緑のチェックになったら成功
5. `data/report.md` を開いて結果を確認

## 大事な点

この段階の `implied_probability` はPinnacleオッズから計算した市場確率です。
独自のAI勝率、EV、Kelly、先発・打線・ブルペン評価は次の段階で追加します。
