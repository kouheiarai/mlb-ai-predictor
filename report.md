# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-15T22:45:24.847153+00:00
- API requests remaining: 368
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Milwaukee Brewers @ Los Angeles Dodgers
- Odds: 2.33
- AI probability: 47.2%
- EV: 9.9%
- 1/4 Kelly: 1.9%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.52 - Los Angeles Dodgers 2.63

### 2. Cleveland Guardians
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.96
- AI probability: 54.7%
- EV: 7.2%
- 1/4 Kelly: 1.9%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 0.973
- Temperature: 8.9 C
- Rain probability: 0%
- Wind: 7.0 km/h (258 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.15 - Cleveland Guardians 3.50

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ Los Angeles Dodgers
- Odds: 1.63
- Cover probability: 74.4%
- EV: 21.3%
- 1/4 Kelly: 8.5%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.52 - Los Angeles Dodgers 2.63

### 2. Cleveland Guardians +1.5
- Game: Tampa Bay Rays @ Cleveland Guardians
- Odds: 1.51
- Cover probability: 77.1%
- EV: 16.4%
- 1/4 Kelly: 8.1%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 0.973
- Temperature: 8.9 C
- Rain probability: 0%
- Wind: 7.0 km/h (258 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 3.15 - Cleveland Guardians 3.50

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.