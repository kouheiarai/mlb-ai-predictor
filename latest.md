# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-06T20:38:37.328507+00:00
- API requests remaining: 449
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 1.88
- AI probability: 62.7%
- EV: 18.0%
- 1/4 Kelly: 5.1%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.64 - Chicago White Sox 3.58

### 2. Milwaukee Brewers
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 2.17
- AI probability: 53.4%
- EV: 16.0%
- 1/4 Kelly: 3.4%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.004
- Temperature: 24.5 C
- Rain probability: 1%
- Wind: 7.0 km/h (313 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.86 - San Diego Padres 2.55

### 3. New York Yankees
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 1.65
- AI probability: 67.5%
- EV: 11.3%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.001
- Temperature: 21.2 C
- Rain probability: 0%
- Wind: 10.3 km/h (324 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.37 - New York Yankees 3.58

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.53
- Cover probability: 79.1%
- EV: 21.1%
- 1/4 Kelly: 9.9%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.004
- Temperature: 24.5 C
- Rain probability: 1%
- Wind: 7.0 km/h (313 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.86 - San Diego Padres 2.55

### 2. Chicago White Sox -1.5
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 2.84
- Cover probability: 40.5%
- EV: 15.0%
- 1/4 Kelly: 2.0%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.64 - Chicago White Sox 3.58

### 3. Atlanta Braves +1.5
- Game: Los Angeles Dodgers @ Atlanta Braves
- Odds: 1.51
- Cover probability: 72.9%
- EV: 10.0%
- 1/4 Kelly: 4.9%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Los Angeles Dodgers 2.55 - Atlanta Braves 2.34

### 4. New York Yankees -1.5
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 2.44
- Cover probability: 44.3%
- EV: 8.0%
- 1/4 Kelly: 1.4%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.001
- Temperature: 21.2 C
- Rain probability: 0%
- Wind: 10.3 km/h (324 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.37 - New York Yankees 3.58

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.