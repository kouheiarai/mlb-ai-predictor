# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-01T20:38:33.941604+00:00
- API requests remaining: 491
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.95
- AI probability: 69.7%
- EV: 35.8%
- 1/4 Kelly: 9.4%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: +0.11
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Philadelphia Phillies 2.27 - Atlanta Braves 3.78

### 2. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.36
- AI probability: 53.7%
- EV: 26.8%
- 1/4 Kelly: 4.9%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 0.994
- Temperature: 17.1 C
- Rain probability: 0%
- Wind: 12.0 km/h (36 deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Chicago White Sox 3.16 - Cleveland Guardians 2.78

### 3. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 2.18
- AI probability: 54.9%
- EV: 19.7%
- 1/4 Kelly: 4.2%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: New York Yankees 2.94 - Tampa Bay Rays 2.53

### 4. San Diego Padres
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 2.96
- AI probability: 35.6%
- EV: 5.5%
- 1/4 Kelly: 0.7%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 3.09

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.55
- Cover probability: 89.8%
- EV: 39.2%
- 1/4 Kelly: 17.8%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: +0.11
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Philadelphia Phillies 2.27 - Atlanta Braves 3.78

### 2. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.59
- Cover probability: 78.9%
- EV: 25.5%
- 1/4 Kelly: 10.8%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 0.994
- Temperature: 17.1 C
- Rain probability: 0%
- Wind: 12.0 km/h (36 deg)
- Bullpen fatigue proxy: 0.10
- Expected score: Chicago White Sox 3.16 - Cleveland Guardians 2.78

### 3. New York Yankees +1.5
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.51
- Cover probability: 80.3%
- EV: 21.3%
- 1/4 Kelly: 10.4%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: New York Yankees 2.94 - Tampa Bay Rays 2.53

### 4. San Diego Padres +1.5
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 1.83
- Cover probability: 62.6%
- EV: 14.6%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.10
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 3.09

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.