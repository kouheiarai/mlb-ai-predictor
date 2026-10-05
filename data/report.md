# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-05T22:14:38.284425+00:00
- API requests remaining: 455
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. New York Yankees
- Game: New York Yankees @ Tampa Bay Rays
- Odds: 1.85
- AI probability: 64.8%
- EV: 19.8%
- 1/4 Kelly: 5.8%
- Lineup: 発表済み
- Lineup quality: +0.19
- Platoon proxy: +0.20
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: New York Yankees 3.34 - Tampa Bay Rays 2.28

### 2. Milwaukee Brewers
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 2.18
- AI probability: 53.5%
- EV: 16.6%
- 1/4 Kelly: 3.5%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.010
- Temperature: 26.6 C
- Rain probability: 0%
- Wind: 8.3 km/h (288 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.88 - San Diego Padres 2.57

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.52
- Cover probability: 79.2%
- EV: 20.4%
- 1/4 Kelly: 9.8%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.010
- Temperature: 26.6 C
- Rain probability: 0%
- Wind: 8.3 km/h (288 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.88 - San Diego Padres 2.57

### 2. Atlanta Braves +1.5
- Game: Los Angeles Dodgers @ Atlanta Braves
- Odds: 1.5
- Cover probability: 74.4%
- EV: 11.6%
- 1/4 Kelly: 5.8%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Los Angeles Dodgers 2.60 - Atlanta Braves 2.52

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.