# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-07T01:06:17.140389+00:00
- API requests remaining: 446
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 2.25
- AI probability: 53.2%
- EV: 19.7%
- 1/4 Kelly: 3.9%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.004
- Temperature: 24.5 C
- Rain probability: 0%
- Wind: 7.0 km/h (313 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.86 - San Diego Padres 2.55

### 2. Chicago White Sox
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

### 3. New York Yankees
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 1.65
- AI probability: 67.6%
- EV: 11.5%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.003
- Temperature: 20.8 C
- Rain probability: 3%
- Wind: 13.4 km/h (265 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.37 - New York Yankees 3.58

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.56
- Cover probability: 79.1%
- EV: 23.4%
- 1/4 Kelly: 10.5%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.00
- Weather run factor: 1.004
- Temperature: 24.5 C
- Rain probability: 0%
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

### 3. New York Yankees -1.5
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 2.44
- Cover probability: 44.4%
- EV: 8.4%
- 1/4 Kelly: 1.5%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 1.003
- Temperature: 20.8 C
- Rain probability: 3%
- Wind: 13.4 km/h (265 deg)
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