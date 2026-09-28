# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-28T21:27:28.885231+00:00
- API requests remaining: 227
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Houston Astros
- Odds: 2.1
- AI probability: 57.9%
- EV: 21.7%
- 1/4 Kelly: 4.9%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago White Sox 3.53 - Houston Astros 2.87

### 2. San Diego Padres
- Game: Chicago Cubs @ San Diego Padres
- Odds: 1.83
- AI probability: 63.2%
- EV: 15.6%
- 1/4 Kelly: 4.7%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 0.999
- Temperature: 22.5 C
- Rain probability: 0%
- Wind: 6.0 km/h (253 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago Cubs 2.91 - San Diego Padres 3.90

### 3. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.55
- AI probability: 70.4%
- EV: 9.2%
- 1/4 Kelly: 4.2%
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

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Houston Astros
- Odds: 1.54
- Cover probability: 81.4%
- EV: 25.3%
- 1/4 Kelly: 11.7%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago White Sox 3.53 - Houston Astros 2.87

### 2. San Diego Padres -1.5
- Game: Chicago Cubs @ San Diego Padres
- Odds: 2.74
- Cover probability: 41.5%
- EV: 13.6%
- 1/4 Kelly: 2.0%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 0.999
- Temperature: 22.5 C
- Rain probability: 0%
- Wind: 6.0 km/h (253 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago Cubs 2.91 - San Diego Padres 3.90

### 3. Boston Red Sox +1.5
- Game: Boston Red Sox @ New York Yankees
- Odds: 1.52
- Cover probability: 73.3%
- EV: 11.5%
- 1/4 Kelly: 5.5%
- Lineup: 未発表
- Lineup quality: -0.02
- Platoon proxy: +0.13
- Weather run factor: 1.001
- Temperature: 21.6 C
- Rain probability: 0%
- Wind: 10.2 km/h (188 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Boston Red Sox 2.46 - New York Yankees 2.64

### 4. Atlanta Braves -1.5
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 2.23
- Cover probability: 48.2%
- EV: 7.6%
- 1/4 Kelly: 1.5%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Philadelphia Phillies 2.46 - Atlanta Braves 3.90

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.