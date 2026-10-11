# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-11T23:17:50.612714+00:00
- API requests remaining: 401
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Cleveland Guardians @ Tampa Bay Rays
- Odds: 2.45
- AI probability: 48.0%
- EV: 17.6%
- 1/4 Kelly: 3.0%
- Lineup: 未発表
- Lineup quality: -0.19
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 3.34 - Tampa Bay Rays 3.37

## Run Line Buy Ranking

### 1. Cleveland Guardians +1.5
- Game: Cleveland Guardians @ Tampa Bay Rays
- Odds: 1.63
- Cover probability: 72.4%
- EV: 18.0%
- 1/4 Kelly: 7.1%
- Lineup: 未発表
- Lineup quality: -0.19
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 3.34 - Tampa Bay Rays 3.37

### 2. Los Angeles Dodgers +1.5
- Game: Los Angeles Dodgers @ Milwaukee Brewers
- Odds: 1.4
- Cover probability: 75.6%
- EV: 5.8%
- 1/4 Kelly: 3.6%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Los Angeles Dodgers 2.29 - Milwaukee Brewers 2.38

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.