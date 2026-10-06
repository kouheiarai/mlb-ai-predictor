# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-06T03:55:21.655517+00:00
- API requests remaining: 452
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 1.87
- AI probability: 62.8%
- EV: 17.4%
- 1/4 Kelly: 5.0%
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
- Odds: 2.12
- AI probability: 53.7%
- EV: 13.8%
- 1/4 Kelly: 3.1%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.012
- Temperature: 27.8 C
- Rain probability: 0%
- Wind: 8.1 km/h (291 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.88 - San Diego Padres 2.57

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.5
- Cover probability: 79.1%
- EV: 18.7%
- 1/4 Kelly: 9.3%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.012
- Temperature: 27.8 C
- Rain probability: 0%
- Wind: 8.1 km/h (291 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.88 - San Diego Padres 2.57

### 2. Chicago White Sox -1.5
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 2.81
- Cover probability: 40.5%
- EV: 13.8%
- 1/4 Kelly: 1.9%
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
- Odds: 1.52
- Cover probability: 74.4%
- EV: 13.1%
- 1/4 Kelly: 6.3%
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