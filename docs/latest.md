# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-27T19:24:24.518302+00:00
- API requests remaining: 236
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. New York Yankees
- Game: Baltimore Orioles @ New York Yankees
- Odds: 1.88
- AI probability: 59.5%
- EV: 11.8%
- 1/4 Kelly: 3.3%
- Lineup: 未発表
- Lineup quality: +0.14
- Platoon proxy: -0.04
- Weather run factor: 1.007
- Temperature: 17.2 C
- Rain probability: 43%
- Wind: 24.7 km/h (48 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Baltimore Orioles 2.91 - New York Yankees 3.59

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