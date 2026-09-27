# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-27T22:40:29.255394+00:00
- API requests remaining: 233
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. San Diego Padres
- Game: Chicago Cubs @ San Diego Padres
- Odds: 1.8
- AI probability: 64.7%
- EV: 16.4%
- 1/4 Kelly: 5.1%
- Lineup: 未発表
- Lineup quality: +0.02
- Platoon proxy: +0.00
- Weather run factor: 1.003
- Temperature: 23.8 C
- Rain probability: 0%
- Wind: 7.1 km/h (246 deg)
- Bullpen fatigue proxy: 0.60
- Expected score: Chicago Cubs 2.81 - San Diego Padres 3.91

## Run Line Buy Ranking

### 1. San Diego Padres -1.5
- Game: Chicago Cubs @ San Diego Padres
- Odds: 2.73
- Cover probability: 43.2%
- EV: 18.0%
- 1/4 Kelly: 2.6%
- Lineup: 未発表
- Lineup quality: +0.02
- Platoon proxy: +0.00
- Weather run factor: 1.003
- Temperature: 23.8 C
- Rain probability: 0%
- Wind: 7.1 km/h (246 deg)
- Bullpen fatigue proxy: 0.60
- Expected score: Chicago Cubs 2.81 - San Diego Padres 3.91

### 2. Boston Red Sox +1.5
- Game: Boston Red Sox @ New York Yankees
- Odds: 1.54
- Cover probability: 69.3%
- EV: 6.7%
- 1/4 Kelly: 3.1%
- Lineup: 未発表
- Lineup quality: +0.02
- Platoon proxy: +0.14
- Weather run factor: 0.996
- Temperature: 19.7 C
- Rain probability: 0%
- Wind: 8.1 km/h (32 deg)
- Bullpen fatigue proxy: 0.80
- Expected score: Boston Red Sox 2.36 - New York Yankees 2.80

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.