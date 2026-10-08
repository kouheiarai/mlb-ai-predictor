# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-08T01:25:40.045624+00:00
- API requests remaining: 437
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 2.01
- AI probability: 58.3%
- EV: 17.2%
- 1/4 Kelly: 4.3%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.65 - Chicago White Sox 3.26

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Cleveland Guardians @ Chicago White Sox
- Odds: 1.56
- Cover probability: 81.6%
- EV: 27.3%
- 1/4 Kelly: 12.2%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Cleveland Guardians 2.65 - Chicago White Sox 3.26

### 2. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.45
- Cover probability: 78.6%
- EV: 14.0%
- 1/4 Kelly: 7.8%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.76 - San Diego Padres 2.53

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.