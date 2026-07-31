name: MLB Predictor Auto Update

on:
  workflow_dispatch:
  schedule:
    - cron: "10 * * * *"

permissions:
  contents: write

concurrency:
  group: mlb-predictor-update
  cancel-in-progress: false

jobs:
  update-predictions:
    runs-on: ubuntu-latest
    timeout-minutes: 20

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Generate MLB predictions
        env:
          THE_ODDS_API_KEY: ${{ secrets.THE_ODDS_API_KEY }}
        run: python main.py

      - name: Commit updated predictions
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add data/ docs/
          if git diff --cached --quiet; then
            echo "No changes to commit."
          else
            git commit -m "Update MLB predictions"
            git push
          fi
