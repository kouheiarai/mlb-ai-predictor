# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-01T03:10:50.830214+00:00
- API requests remaining: 494
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.98
- AI probability: 67.5%
- EV: 33.7%
- 1/4 Kelly: 8.6%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Philadelphia Phillies 2.36 - Atlanta Braves 3.71

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.55
- Cover probability: 88.5%
- EV: 37.2%
- 1/4 Kelly: 16.9%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Philadelphia Phillies 2.36 - Atlanta Braves 3.71

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.