# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-22T19:36:13.704308+00:00
- API requests remaining: 317
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Tampa Bay Rays @ Milwaukee Brewers
- Odds: 1.64
- AI probability: 68.1%
- EV: 11.7%
- 1/4 Kelly: 4.6%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.35 - Milwaukee Brewers 3.60

## Run Line Buy Ranking

### 1. Milwaukee Brewers -1.5
- Game: Tampa Bay Rays @ Milwaukee Brewers
- Odds: 2.52
- Cover probability: 45.2%
- EV: 14.0%
- 1/4 Kelly: 2.3%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.35 - Milwaukee Brewers 3.60

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.