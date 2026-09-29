# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-29T03:21:16.172301+00:00
- API requests remaining: 221
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Houston Astros
- Odds: 2.1
- AI probability: 58.0%
- EV: 21.8%
- 1/4 Kelly: 4.9%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Chicago White Sox 3.49 - Houston Astros 2.83

### 2. San Diego Padres
- Game: Chicago Cubs @ San Diego Padres
- Odds: 1.82
- AI probability: 62.5%
- EV: 13.7%
- 1/4 Kelly: 4.2%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.011
- Temperature: 25.4 C
- Rain probability: 0%
- Wind: 12.0 km/h (316 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Chicago Cubs 2.91 - San Diego Padres 3.83

### 3. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.54
- AI probability: 70.3%
- EV: 8.3%
- 1/4 Kelly: 3.9%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Philadelphia Phillies 2.44 - Atlanta Braves 3.86

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Houston Astros
- Odds: 1.54
- Cover probability: 81.3%
- EV: 25.3%
- 1/4 Kelly: 11.7%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Chicago White Sox 3.49 - Houston Astros 2.83

### 2. San Diego Padres -1.5
- Game: Chicago Cubs @ San Diego Padres
- Odds: 2.74
- Cover probability: 40.4%
- EV: 10.8%
- 1/4 Kelly: 1.5%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.011
- Temperature: 25.4 C
- Rain probability: 0%
- Wind: 12.0 km/h (316 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Chicago Cubs 2.91 - San Diego Padres 3.83

### 3. Boston Red Sox +1.5
- Game: Boston Red Sox @ New York Yankees
- Odds: 1.52
- Cover probability: 72.1%
- EV: 9.7%
- 1/4 Kelly: 4.6%
- Lineup: 未発表
- Lineup quality: -0.02
- Platoon proxy: +0.12
- Weather run factor: 1.003
- Temperature: 23.2 C
- Rain probability: 1%
- Wind: 8.7 km/h (197 deg)
- Bullpen fatigue proxy: 0.50
- Expected score: Boston Red Sox 2.38 - New York Yankees 2.64

### 4. Atlanta Braves -1.5
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 2.22
- Cover probability: 47.8%
- EV: 6.1%
- 1/4 Kelly: 1.3%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Philadelphia Phillies 2.44 - Atlanta Braves 3.86

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.