# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-17T23:36:11.335799+00:00
- API requests remaining: 347
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 2.0
- AI probability: 57.5%
- EV: 15.0%
- 1/4 Kelly: 3.8%
- Lineup: 発表済み
- Lineup quality: +0.09
- Platoon proxy: +0.00
- Weather run factor: 0.993
- Temperature: 15.5 C
- Rain probability: 0%
- Wind: 13.6 km/h (201 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.03 - Cleveland Guardians 3.60

## Run Line Buy Ranking

### 1. Cleveland Guardians +1.5
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.54
- Cover probability: 79.8%
- EV: 22.9%
- 1/4 Kelly: 10.6%
- Lineup: 発表済み
- Lineup quality: +0.09
- Platoon proxy: +0.00
- Weather run factor: 0.993
- Temperature: 15.5 C
- Rain probability: 0%
- Wind: 13.6 km/h (201 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.03 - Cleveland Guardians 3.60

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.