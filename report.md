# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-05T03:06:11.487201+00:00
- API requests remaining: 458
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.36
- AI probability: 54.3%
- EV: 28.1%
- 1/4 Kelly: 5.2%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 0.997
- Temperature: 14.9 C
- Rain probability: 0%
- Wind: 19.3 km/h (337 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.82

### 2. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.82
- AI probability: 64.7%
- EV: 17.7%
- 1/4 Kelly: 5.4%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.33 - Tampa Bay Rays 2.28

### 3. Milwaukee Brewers
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 2.18
- AI probability: 53.5%
- EV: 16.7%
- 1/4 Kelly: 3.5%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.011
- Temperature: 26.7 C
- Rain probability: 0%
- Wind: 9.8 km/h (294 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.88 - San Diego Padres 2.57

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.58
- Cover probability: 79.1%
- EV: 25.0%
- 1/4 Kelly: 10.8%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 0.997
- Temperature: 14.9 C
- Rain probability: 0%
- Wind: 19.3 km/h (337 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.82

### 2. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.53
- Cover probability: 79.1%
- EV: 21.0%
- 1/4 Kelly: 9.9%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.011
- Temperature: 26.7 C
- Rain probability: 0%
- Wind: 9.8 km/h (294 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.88 - San Diego Padres 2.57

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.