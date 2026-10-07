# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-07T03:23:10.253724+00:00
- API requests remaining: 443
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 1.9
- AI probability: 62.7%
- EV: 19.1%
- 1/4 Kelly: 5.3%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.64 - Chicago White Sox 3.58

### 2. New York Yankees
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 1.63
- AI probability: 67.6%
- EV: 10.1%
- 1/4 Kelly: 4.0%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 0.999
- Temperature: 19.5 C
- Rain probability: 0%
- Wind: 12.2 km/h (270 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.37 - New York Yankees 3.57

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Los Angeles Dodgers @ Atlanta Braves
- Odds: 1.7
- Cover probability: 73.2%
- EV: 24.5%
- 1/4 Kelly: 8.7%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Los Angeles Dodgers 2.54 - Atlanta Braves 2.33

### 2. Chicago White Sox -1.5
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 2.91
- Cover probability: 40.5%
- EV: 17.8%
- 1/4 Kelly: 2.3%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.64 - Chicago White Sox 3.58

### 3. New York Yankees -1.5
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 2.42
- Cover probability: 44.1%
- EV: 6.8%
- 1/4 Kelly: 1.2%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 0.999
- Temperature: 19.5 C
- Rain probability: 0%
- Wind: 12.2 km/h (270 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.37 - New York Yankees 3.57

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.