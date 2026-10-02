# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-02T01:11:08.076174+00:00
- API requests remaining: 488
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.36
- AI probability: 53.7%
- EV: 26.7%
- 1/4 Kelly: 4.9%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 0.996
- Temperature: 17.1 C
- Rain probability: 0%
- Wind: 13.5 km/h (31 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.13 - Cleveland Guardians 2.75

### 2. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 2.17
- AI probability: 54.9%
- EV: 19.1%
- 1/4 Kelly: 4.1%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 2.90 - Tampa Bay Rays 2.50

### 3. San Diego Padres
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 2.95
- AI probability: 36.2%
- EV: 6.7%
- 1/4 Kelly: 0.9%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 3.06

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.59
- Cover probability: 79.0%
- EV: 25.5%
- 1/4 Kelly: 10.8%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 0.996
- Temperature: 17.1 C
- Rain probability: 0%
- Wind: 13.5 km/h (31 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.13 - Cleveland Guardians 2.75

### 2. New York Yankees +1.5
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.51
- Cover probability: 80.5%
- EV: 21.5%
- 1/4 Kelly: 10.5%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 2.90 - Tampa Bay Rays 2.50

### 3. San Diego Padres +1.5
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