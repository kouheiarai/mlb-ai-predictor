# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-17T02:11:43.259630+00:00
- API requests remaining: 356
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 2.03
- AI probability: 54.6%
- EV: 10.9%
- 1/4 Kelly: 2.6%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 0.993
- Temperature: 15.2 C
- Rain probability: 0%
- Wind: 14.7 km/h (201 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.21 - Cleveland Guardians 3.57

## Run Line Buy Ranking

### 1. Cleveland Guardians +1.5
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.55
- Cover probability: 77.0%
- EV: 19.4%
- 1/4 Kelly: 8.8%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 0.993
- Temperature: 15.2 C
- Rain probability: 0%
- Wind: 14.7 km/h (201 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.21 - Cleveland Guardians 3.57

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.