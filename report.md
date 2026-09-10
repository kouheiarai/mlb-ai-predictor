# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-10T18:50:01.301794+00:00
- API requests remaining: 398
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Pittsburgh Pirates @ Chicago White Sox
- Odds: 1.96
- AI probability: 55.6%
- EV: 9.1%
- 1/4 Kelly: 2.4%
- Lineup: 未発表
- Lineup quality: +0.41
- Platoon proxy: +0.10
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Pittsburgh Pirates 2.72 - Chicago White Sox 3.11

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