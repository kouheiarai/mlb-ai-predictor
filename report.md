# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-10T22:05:41.858868+00:00
- API requests remaining: 395
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Pittsburgh Pirates @ Chicago White Sox
- Odds: 1.92
- AI probability: 55.3%
- EV: 6.1%
- 1/4 Kelly: 1.7%
- Lineup: 発表済み
- Lineup quality: +0.26
- Platoon proxy: +0.12
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Pittsburgh Pirates 2.71 - Chicago White Sox 3.07

## Run Line Buy Ranking

No EV 5%+ Run Line bets.
## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.