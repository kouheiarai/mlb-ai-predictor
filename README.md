# MLB AI Predictor Ver.26.0 Clean Build

GitHub ActionsでPinnacle系オッズ、MLB公式日程・予告先発、ラインアップ、ブルペン代理指標、天候、チーム指標を取得し、ML・ランライン・合計得点の予測ファイルを生成します。

## 必須設定

GitHubリポジトリの **Settings → Secrets and variables → Actions** に次を登録してください。

- `THE_ODDS_API_KEY`

## 実行

**Actions → MLB AI Predictor Ver.26.0 Auto Update → Run workflow**

## 主な公開ファイル

- `data/predictions.csv`
- `data/prediction_latest.json`
- `data/output_manifest.json`
- `prediction_latest.json`
- `docs/prediction_latest.json`

## 注意

このビルドはクリーン構成です。古いPythonファイルや重複ワークフローを混在させないでください。現行モデルの一部指標は公開データから作る代理指標であり、すべてがStatcast由来の厳密なWAR/FIP分解ではありません。
