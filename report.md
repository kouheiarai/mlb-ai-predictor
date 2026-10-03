# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-03T18:52:47.931956+00:00
- API requests remaining: 473
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 2.19
- AI probability: 62.9%
- EV: 37.8%
- 1/4 Kelly: 7.9%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.28 - Tampa Bay Rays 2.28

### 2. Atlanta Braves
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 3.0
- AI probability: 40.4%
- EV: 21.2%
- 1/4 Kelly: 2.7%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.29 - Los Angeles Dodgers 2.74

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 1.93
- Cover probability: 69.3%
- EV: 33.7%
- 1/4 Kelly: 9.1%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.29 - Los Angeles Dodgers 2.74

### 2. New York Yankees +1.5
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.52
- Cover probability: 86.6%
- EV: 31.6%
- 1/4 Kelly: 15.2%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.28 - Tampa Bay Rays 2.28

### 3. San Diego Padres +1.5
- Game: San Diego Padres @ Milwaukee Brewers
- Odds: 1.83
- Cover probability: 64.7%
- EV: 18.4%
- 1/4 Kelly: 5.6%
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