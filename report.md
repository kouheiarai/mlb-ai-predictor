# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-30T20:23:16.033322+00:00
- API requests remaining: 209
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Houston Astros
- Odds: 2.34
- AI probability: 57.2%
- EV: 33.9%
- 1/4 Kelly: 6.3%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Chicago White Sox 3.39 - Houston Astros 2.75

### 2. San Diego Padres
- Game: Chicago Cubs @ San Diego Padres
- Odds: 1.71
- AI probability: 62.1%
- EV: 6.3%
- 1/4 Kelly: 2.2%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.002
- Temperature: 21.6 C
- Rain probability: 0%
- Wind: 10.9 km/h (333 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Chicago Cubs 2.80 - San Diego Padres 3.64

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Houston Astros
- Odds: 1.6
- Cover probability: 81.5%
- EV: 30.4%
- 1/4 Kelly: 12.7%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Chicago White Sox 3.39 - Houston Astros 2.75

### 2. Boston Red Sox +1.5
- Game: Boston Red Sox @ New York Yankees
- Odds: 1.53
- Cover probability: 73.4%
- EV: 12.3%
- 1/4 Kelly: 5.8%
- Lineup: 未発表
- Lineup quality: -0.02
- Platoon proxy: +0.12
- Weather run factor: 0.993
- Temperature: 19.3 C
- Rain probability: 4%
- Wind: 6.1 km/h (152 deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Boston Red Sox 2.29 - New York Yankees 2.51

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.