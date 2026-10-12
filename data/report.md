# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-12T22:38:51.353274+00:00
- API requests remaining: 395
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Cleveland Guardians @ Tampa Bay Rays
- Odds: 2.45
- AI probability: 54.3%
- EV: 33.0%
- 1/4 Kelly: 5.7%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 3.45 - Tampa Bay Rays 2.99

## Run Line Buy Ranking

### 1. Cleveland Guardians +1.5
- Game: Cleveland Guardians @ Tampa Bay Rays
- Odds: 1.67
- Cover probability: 78.8%
- EV: 31.6%
- 1/4 Kelly: 11.8%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 3.45 - Tampa Bay Rays 2.99

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.