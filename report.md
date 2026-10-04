# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-04T18:52:50.974908+00:00
- API requests remaining: 464
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Atlanta Braves
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 3.03
- AI probability: 45.3%
- EV: 37.4%
- 1/4 Kelly: 4.6%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.29 - Los Angeles Dodgers 2.41

### 2. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.36
- AI probability: 54.3%
- EV: 28.2%
- 1/4 Kelly: 5.2%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 0.998
- Temperature: 14.7 C
- Rain probability: 0%
- Wind: 20.6 km/h (314 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.83

### 3. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.83
- AI probability: 64.7%
- EV: 18.3%
- 1/4 Kelly: 5.5%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.33 - Tampa Bay Rays 2.28

### 4. Milwaukee Brewers
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 1.78
- AI probability: 60.8%
- EV: 8.3%
- 1/4 Kelly: 2.6%
- Lineup: 発表済み
- Lineup quality: +0.30
- Platoon proxy: +0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: San Diego Padres 2.28 - Milwaukee Brewers 2.96

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 1.88
- Cover probability: 75.2%
- EV: 41.4%
- 1/4 Kelly: 11.8%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.29 - Los Angeles Dodgers 2.41

### 2. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.58
- Cover probability: 79.2%
- EV: 25.1%
- 1/4 Kelly: 10.8%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 0.998
- Temperature: 14.7 C
- Rain probability: 0%
- Wind: 20.6 km/h (314 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.83

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.