# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-03T02:58:19.649202+00:00
- API requests remaining: 476
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 2.14
- AI probability: 63.0%
- EV: 34.8%
- 1/4 Kelly: 7.6%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.28 - Tampa Bay Rays 2.28

### 2. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.32
- AI probability: 55.3%
- EV: 28.3%
- 1/4 Kelly: 5.4%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: 16.0 C
- Rain probability: 0%
- Wind: 19.7 km/h (329 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.26 - Cleveland Guardians 2.76

### 3. Atlanta Braves
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 2.91
- AI probability: 42.9%
- EV: 24.9%
- 1/4 Kelly: 3.3%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.44 - Los Angeles Dodgers 2.73

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 1.92
- Cover probability: 71.5%
- EV: 37.3%
- 1/4 Kelly: 10.1%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.44 - Los Angeles Dodgers 2.73

### 2. New York Yankees +1.5
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.51
- Cover probability: 86.6%
- EV: 30.7%
- 1/4 Kelly: 15.1%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.28 - Tampa Bay Rays 2.28

### 3. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.59
- Cover probability: 80.0%
- EV: 27.2%
- 1/4 Kelly: 11.5%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: 16.0 C
- Rain probability: 0%
- Wind: 19.7 km/h (329 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.26 - Cleveland Guardians 2.76

### 4. San Diego Padres +1.5
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 1.81
- Cover probability: 64.7%
- EV: 17.1%
- 1/4 Kelly: 5.3%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 2.98

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.