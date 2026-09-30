# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-30T00:51:13.798246+00:00
- API requests remaining: 215
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 2.01
- AI probability: 67.8%
- EV: 36.3%
- 1/4 Kelly: 9.0%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Philadelphia Phillies 2.38 - Atlanta Braves 3.75

### 2. San Diego Padres
- Game: Chicago Cubs @ San Diego Padres
- Odds: 1.76
- AI probability: 61.9%
- EV: 9.0%
- 1/4 Kelly: 3.0%
- Lineup: 未発表
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.008
- Temperature: 24.9 C
- Rain probability: 0%
- Wind: 9.7 km/h (297 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Chicago Cubs 2.82 - San Diego Padres 3.66

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.56
- Cover probability: 88.5%
- EV: 38.0%
- 1/4 Kelly: 17.0%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Philadelphia Phillies 2.38 - Atlanta Braves 3.75

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.