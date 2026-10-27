# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-27T20:17:56.885632+00:00
- API requests remaining: 284
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Milwaukee Brewers @ Tampa Bay Rays
- Odds: 1.86
- AI probability: 63.7%
- EV: 18.4%
- 1/4 Kelly: 5.4%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 3.39 - Tampa Bay Rays 2.41

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