# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-16T19:07:00.215306+00:00
- API requests remaining: 362
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.97
- AI probability: 54.7%
- EV: 7.7%
- 1/4 Kelly: 2.0%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 0.971
- Temperature: 8.4 C
- Rain probability: 0%
- Wind: 6.2 km/h (259 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.14 - Cleveland Guardians 3.49

## Run Line Buy Ranking

### 1. Cleveland Guardians +1.5
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.52
- Cover probability: 77.1%
- EV: 17.2%
- 1/4 Kelly: 8.3%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 0.971
- Temperature: 8.4 C
- Rain probability: 0%
- Wind: 6.2 km/h (259 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.14 - Cleveland Guardians 3.49

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.