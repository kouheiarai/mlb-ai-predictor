# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-02T20:14:04.502370+00:00
- API requests remaining: 482
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.31
- AI probability: 57.9%
- EV: 33.8%
- 1/4 Kelly: 6.4%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 0.996
- Temperature: 18.0 C
- Rain probability: 0%
- Wind: 11.8 km/h (67 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.13 - Cleveland Guardians 2.46

### 2. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 2.13
- AI probability: 57.9%
- EV: 23.4%
- 1/4 Kelly: 5.2%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 2.90 - Tampa Bay Rays 2.30

### 3. Atlanta Braves
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 2.87
- AI probability: 43.0%
- EV: 23.4%
- 1/4 Kelly: 3.1%
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
- Odds: 1.88
- Cover probability: 71.5%
- EV: 34.4%
- 1/4 Kelly: 9.8%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.44 - Los Angeles Dodgers 2.73

### 2. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.59
- Cover probability: 82.9%
- EV: 31.8%
- 1/4 Kelly: 13.5%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 0.996
- Temperature: 18.0 C
- Rain probability: 0%
- Wind: 11.8 km/h (67 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.13 - Cleveland Guardians 2.46

### 3. New York Yankees +1.5
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.51
- Cover probability: 83.4%
- EV: 25.9%
- 1/4 Kelly: 12.7%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 2.90 - Tampa Bay Rays 2.30

### 4. San Diego Padres +1.5
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 1.83
- Cover probability: 63.4%
- EV: 16.0%
- 1/4 Kelly: 4.8%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 3.06

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.