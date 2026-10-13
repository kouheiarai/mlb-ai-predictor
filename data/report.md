# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-13T20:52:53.801114+00:00
- API requests remaining: 389
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Cleveland Guardians
- Game: Cleveland Guardians @ Tampa Bay Rays
- Odds: 2.18
- AI probability: 54.6%
- EV: 19.0%
- 1/4 Kelly: 4.0%
- Lineup: 発表済み
- Lineup quality: -0.00
- Platoon proxy: +0.17
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 3.46 - Tampa Bay Rays 3.04

### 2. Milwaukee Brewers
- Game: Milwaukee Brewers @ Los Angeles Dodgers
- Odds: 2.52
- AI probability: 46.5%
- EV: 17.3%
- 1/4 Kelly: 2.8%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.53 - Los Angeles Dodgers 2.63

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ Los Angeles Dodgers
- Odds: 1.68
- Cover probability: 74.4%
- EV: 24.9%
- 1/4 Kelly: 9.2%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.53 - Los Angeles Dodgers 2.63

### 2. Cleveland Guardians +1.5
- Game: Cleveland Guardians @ Tampa Bay Rays
- Odds: 1.56
- Cover probability: 78.3%
- EV: 22.2%
- 1/4 Kelly: 9.9%
- Lineup: 発表済み
- Lineup quality: -0.00
- Platoon proxy: +0.17
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 3.46 - Tampa Bay Rays 3.04

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.