# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-28T02:39:16.851014+00:00
- API requests remaining: 230
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. San Diego Padres
- Game: Chicago Cubs @ San Diego Padres
- Odds: 1.83
- AI probability: 63.0%
- EV: 15.2%
- 1/4 Kelly: 4.6%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.003
- Temperature: 22.8 C
- Rain probability: 0%
- Wind: 9.1 km/h (279 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago Cubs 2.92 - San Diego Padres 3.91

### 2. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.53
- AI probability: 70.5%
- EV: 7.9%
- 1/4 Kelly: 3.7%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Philadelphia Phillies 2.46 - Atlanta Braves 3.90

## Run Line Buy Ranking

### 1. San Diego Padres -1.5
- Game: Chicago Cubs @ San Diego Padres
- Odds: 2.77
- Cover probability: 41.7%
- EV: 15.5%
- 1/4 Kelly: 2.2%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.003
- Temperature: 22.8 C
- Rain probability: 0%
- Wind: 9.1 km/h (279 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago Cubs 2.92 - San Diego Padres 3.91

### 2. Atlanta Braves -1.5
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 2.25
- Cover probability: 48.2%
- EV: 8.6%
- 1/4 Kelly: 1.7%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Philadelphia Phillies 2.46 - Atlanta Braves 3.90

### 3. Boston Red Sox +1.5
- Game: Boston Red Sox @ New York Yankees
- Odds: 1.54
- Cover probability: 70.2%
- EV: 8.1%
- 1/4 Kelly: 3.8%
- Lineup: 未発表
- Lineup quality: -0.02
- Platoon proxy: +0.13
- Weather run factor: 1.002
- Temperature: 21.5 C
- Rain probability: 0%
- Wind: 10.5 km/h (186 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Boston Red Sox 2.46 - New York Yankees 2.82

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.