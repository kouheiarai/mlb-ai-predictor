# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-04T03:27:46.442575+00:00
- API requests remaining: 467
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.36
- AI probability: 55.4%
- EV: 30.7%
- 1/4 Kelly: 5.6%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 0.998
- Temperature: 14.9 C
- Rain probability: 0%
- Wind: 20.1 km/h (327 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.75

### 2. New York Yankees
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

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.58
- Cover probability: 80.2%
- EV: 26.7%
- 1/4 Kelly: 11.5%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.04
- Weather run factor: 0.998
- Temperature: 14.9 C
- Rain probability: 0%
- Wind: 20.1 km/h (327 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.75

### 2. Atlanta Braves +1.5
- Game: Atlanta Braves @ Los Angeles Dodgers
- Odds: 1.59
- Cover probability: 69.7%
- EV: 10.8%
- 1/4 Kelly: 4.6%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Atlanta Braves 2.29 - Los Angeles Dodgers 2.72

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.