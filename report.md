# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-17T02:30:27.781885+00:00
- API requests remaining: 332
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Athletics
- Game: Athletics @ Tampa Bay Rays
- Odds: 3.35
- AI probability: 36.5%
- EV: 22.2%
- 1/4 Kelly: 2.4%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Athletics 3.16 - Tampa Bay Rays 3.98

### 2. New York Mets
- Game: Philadelphia Phillies @ New York Mets
- Odds: 1.76
- AI probability: 67.0%
- EV: 17.9%
- 1/4 Kelly: 5.9%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Philadelphia Phillies 2.58 - New York Mets 3.83

## Run Line Buy Ranking

### 1. Athletics +1.5
- Game: Athletics @ Tampa Bay Rays
- Odds: 2.03
- Cover probability: 60.9%
- EV: 23.6%
- 1/4 Kelly: 5.7%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Athletics 3.16 - Tampa Bay Rays 3.98

### 2. New York Mets -1.5
- Game: Philadelphia Phillies @ New York Mets
- Odds: 2.57
- Cover probability: 45.2%
- EV: 16.3%
- 1/4 Kelly: 2.6%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Philadelphia Phillies 2.58 - New York Mets 3.83

### 3. Colorado Rockies +1.5
- Game: San Diego Padres @ Colorado Rockies
- Odds: 1.94
- Cover probability: 58.3%
- EV: 13.1%
- 1/4 Kelly: 3.5%
- Lineup: 未発表
- Lineup quality: +0.35
- Platoon proxy: +0.16
- Weather run factor: 1.006
- Temperature: 27.7 C
- Rain probability: 10%
- Wind: 2.5 km/h (188 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 4.00 - Colorado Rockies 3.02

### 4. Detroit Tigers +1.5
- Game: Detroit Tigers @ Chicago White Sox
- Odds: 1.54
- Cover probability: 69.7%
- EV: 7.3%
- 1/4 Kelly: 3.4%
- Lineup: 未発表
- Lineup quality: +0.04
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Detroit Tigers 2.87 - Chicago White Sox 3.17

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.