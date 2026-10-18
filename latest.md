# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-18T18:21:00.728684+00:00
- API requests remaining: 344
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 2.13
- AI probability: 52.7%
- EV: 12.2%
- 1/4 Kelly: 2.7%
- Lineup: 発表済み
- Lineup quality: -0.03
- Platoon proxy: +0.22
- Weather run factor: 0.994
- Temperature: 15.8 C
- Rain probability: 0%
- Wind: 14.0 km/h (191 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.96 - Cleveland Guardians 3.18

## Run Line Buy Ranking

### 1. Cleveland Guardians +1.5
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.65
- Cover probability: 76.3%
- EV: 26.0%
- 1/4 Kelly: 10.0%
- Lineup: 発表済み
- Lineup quality: -0.03
- Platoon proxy: +0.22
- Weather run factor: 0.994
- Temperature: 15.8 C
- Rain probability: 0%
- Wind: 14.0 km/h (191 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.96 - Cleveland Guardians 3.18

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.