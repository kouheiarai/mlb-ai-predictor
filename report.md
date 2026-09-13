# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-13T21:56:54.312008+00:00
- API requests remaining: 365
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

No EV 5%+ Moneyline bets.
## Run Line Buy Ranking

### 1. San Francisco Giants +1.5
- Game: San Diego Padres @ San Francisco Giants
- Odds: 1.68
- Cover probability: 65.2%
- EV: 9.5%
- 1/4 Kelly: 3.5%
- Lineup: 発表済み
- Lineup quality: -0.39
- Platoon proxy: +0.02
- Weather run factor: 1.016
- Temperature: 21.1 C
- Rain probability: 0%
- Wind: 26.2 km/h (297 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 3.12 - San Francisco Giants 2.50

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.