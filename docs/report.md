# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-08T20:54:28.701968+00:00
- API requests remaining: 431
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 2.05
- AI probability: 61.8%
- EV: 26.8%
- 1/4 Kelly: 6.4%
- Lineup: 発表済み
- Lineup quality: +0.20
- Platoon proxy: +0.12
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.38 - Chicago White Sox 3.24

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 1.58
- Cover probability: 85.1%
- EV: 34.4%
- 1/4 Kelly: 14.8%
- Lineup: 発表済み
- Lineup quality: +0.20
- Platoon proxy: +0.12
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.38 - Chicago White Sox 3.24

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.