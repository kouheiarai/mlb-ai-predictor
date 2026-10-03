# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-03T22:31:08.591521+00:00
- API requests remaining: 470
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 2.23
- AI probability: 62.8%
- EV: 40.0%
- 1/4 Kelly: 8.1%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.28 - Tampa Bay Rays 2.28

## Run Line Buy Ranking

### 1. New York Yankees +1.5
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.53
- Cover probability: 86.6%
- EV: 32.5%
- 1/4 Kelly: 15.3%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.28 - Tampa Bay Rays 2.28

### 2. San Diego Padres +1.5
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 1.83
- Cover probability: 64.7%
- EV: 18.4%
- 1/4 Kelly: 5.6%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 2.98

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.