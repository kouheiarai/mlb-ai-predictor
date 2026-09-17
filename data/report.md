# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-17T22:33:15.182000+00:00
- API requests remaining: 326
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Angels
- Game: Minnesota Twins @ Los Angeles Angels
- Odds: 1.91
- AI probability: 70.6%
- EV: 34.9%
- 1/4 Kelly: 9.6%
- Lineup: 未発表
- Lineup quality: -0.18
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Minnesota Twins 2.38 - Los Angeles Angels 4.01

### 2. New York Mets
- Game: Philadelphia Phillies @ New York Mets
- Odds: 1.83
- AI probability: 66.7%
- EV: 22.1%
- 1/4 Kelly: 6.7%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Philadelphia Phillies 2.58 - New York Mets 3.83

### 3. Boston Red Sox
- Game: Boston Red Sox @ Texas Rangers
- Odds: 1.86
- AI probability: 64.8%
- EV: 20.5%
- 1/4 Kelly: 6.0%
- Lineup: 発表済み
- Lineup quality: +0.11
- Platoon proxy: +0.11
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Boston Red Sox 3.58 - Texas Rangers 2.47

### 4. Chicago White Sox
- Game: Detroit Tigers @ Chicago White Sox
- Odds: 1.91
- AI probability: 55.9%
- EV: 6.8%
- 1/4 Kelly: 1.9%
- Lineup: 未発表
- Lineup quality: +0.08
- Platoon proxy: -0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Detroit Tigers 2.77 - Chicago White Sox 3.17

### 5. Houston Astros
- Game: Kansas City Royals @ Houston Astros
- Odds: 1.7
- AI probability: 62.1%
- EV: 5.6%
- 1/4 Kelly: 2.0%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: -0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Kansas City Royals 3.23 - Houston Astros 4.13

## Run Line Buy Ranking

### 1. Los Angeles Angels +1.5
- Game: Minnesota Twins @ Los Angeles Angels
- Odds: 1.54
- Cover probability: 90.0%
- EV: 38.6%
- 1/4 Kelly: 17.9%
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
- Odds: 2.66
- Cover probability: 45.2%
- EV: 20.3%
- 1/4 Kelly: 3.1%
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