# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-30T03:03:54.162470+00:00
- API requests remaining: 212
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.98
- AI probability: 67.9%
- EV: 34.5%
- 1/4 Kelly: 8.8%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Philadelphia Phillies 2.38 - Atlanta Braves 3.75

### 2. Chicago White Sox
- Game: Chicago White Sox @ Houston Astros
- Odds: 2.3
- AI probability: 57.3%
- EV: 31.8%
- 1/4 Kelly: 6.1%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Chicago White Sox 3.39 - Houston Astros 2.75

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
- Bullpen fatigue proxy: 0.20
- Expected score: Philadelphia Phillies 2.38 - Atlanta Braves 3.75

### 2. Chicago White Sox +1.5
- Game: Chicago White Sox @ Houston Astros
- Odds: 1.58
- Cover probability: 81.5%
- EV: 28.8%
- 1/4 Kelly: 12.4%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Chicago White Sox 3.39 - Houston Astros 2.75

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.