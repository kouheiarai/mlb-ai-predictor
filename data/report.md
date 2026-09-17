# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-17T19:23:22.542826+00:00
- API requests remaining: 329
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Angels
- Game: Minnesota Twins @ Los Angeles Angels
- Odds: 1.95
- AI probability: 70.5%
- EV: 37.4%
- 1/4 Kelly: 9.8%
- Lineup: 未発表
- Lineup quality: -0.18
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Minnesota Twins 2.38 - Los Angeles Angels 4.01

### 2. Boston Red Sox
- Game: Boston Red Sox @ Texas Rangers
- Odds: 1.85
- AI probability: 65.6%
- EV: 21.4%
- 1/4 Kelly: 6.3%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.15
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Boston Red Sox 3.65 - Texas Rangers 2.48

### 3. New York Mets
- Game: Philadelphia Phillies @ New York Mets
- Odds: 1.81
- AI probability: 66.8%
- EV: 20.9%
- 1/4 Kelly: 6.5%
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

### 1. Los Angeles Angels +1.5
- Game: Minnesota Twins @ Los Angeles Angels
- Odds: 1.56
- Cover probability: 90.0%
- EV: 40.4%
- 1/4 Kelly: 18.1%
- Lineup: 未発表
- Lineup quality: -0.18
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Minnesota Twins 2.38 - Los Angeles Angels 4.01

### 2. New York Mets -1.5
- Game: Philadelphia Phillies @ New York Mets
- Odds: 2.64
- Cover probability: 45.2%
- EV: 19.4%
- 1/4 Kelly: 3.0%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Philadelphia Phillies 2.58 - New York Mets 3.83

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.