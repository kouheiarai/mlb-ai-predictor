# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-24T22:04:29.016756+00:00
- API requests remaining: 299
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Tampa Bay Rays @ Milwaukee Brewers
- Odds: 1.87
- AI probability: 63.8%
- EV: 19.4%
- 1/4 Kelly: 5.6%
- Lineup: 発表済み
- Lineup quality: +0.10
- Platoon proxy: +0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.27 - Milwaukee Brewers 3.23

## Run Line Buy Ranking

### 1. Milwaukee Brewers -1.5
- Game: Tampa Bay Rays @ Milwaukee Brewers
- Odds: 2.94
- Cover probability: 39.7%
- EV: 16.8%
- 1/4 Kelly: 2.2%
- Lineup: 発表済み
- Lineup quality: +0.10
- Platoon proxy: +0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.27 - Milwaukee Brewers 3.23

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.