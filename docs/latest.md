# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-08-03T17:19:51.821479+00:00
- API requests remaining: 313
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Philadelphia Phillies
- Odds: 2.43
- AI probability: 49.6%
- EV: 20.5%
- 1/4 Kelly: 3.6%
- Lineup: 未発表
- Lineup quality: +0.27
- Platoon proxy: +0.05
- Weather run factor: 1.019
- Temperature: 30.0 C
- Rain probability: 51%
- Wind: 10.6 km/h (198 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 3.22 - Philadelphia Phillies 3.13

### 2. Milwaukee Brewers
- Game: Pittsburgh Pirates @ Milwaukee Brewers
- Odds: 1.7
- AI probability: 62.1%
- EV: 5.6%
- 1/4 Kelly: 2.0%
- Lineup: 未発表
- Lineup quality: +0.46
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Pittsburgh Pirates 2.45 - Milwaukee Brewers 3.23

## Run Line Buy Ranking

### 1. Washington Nationals +1.5
- Game: Washington Nationals @ Philadelphia Phillies
- Odds: 1.69
- Cover probability: 74.3%
- EV: 25.6%
- 1/4 Kelly: 9.3%
- Lineup: 未発表
- Lineup quality: +0.27
- Platoon proxy: +0.05
- Weather run factor: 1.019
- Temperature: 30.0 C
- Rain probability: 51%
- Wind: 10.6 km/h (198 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 3.22 - Philadelphia Phillies 3.13

### 2. Chicago Cubs +1.5
- Game: Los Angeles Dodgers @ Chicago Cubs
- Odds: 1.65
- Cover probability: 71.4%
- EV: 17.8%
- 1/4 Kelly: 6.9%
- Lineup: 未発表
- Lineup quality: +0.30
- Platoon proxy: +0.00
- Weather run factor: 1.012
- Temperature: 27.1 C
- Rain probability: 30%
- Wind: 10.2 km/h (129 deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Los Angeles Dodgers 2.97 - Chicago Cubs 2.78

### 3. Colorado Rockies +1.5
- Game: Tampa Bay Rays @ Colorado Rockies
- Odds: 2.01
- Cover probability: 57.8%
- EV: 16.3%
- 1/4 Kelly: 4.0%
- Lineup: 未発表
- Lineup quality: +0.64
- Platoon proxy: +0.10
- Weather run factor: 1.023
- Temperature: 31.1 C
- Rain probability: 2%
- Wind: 13.0 km/h (51 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Tampa Bay Rays 3.94 - Colorado Rockies 2.93

### 4. San Diego Padres +1.5
- Game: San Diego Padres @ Arizona Diamondbacks
- Odds: 1.48
- Cover probability: 74.7%
- EV: 10.6%
- 1/4 Kelly: 5.5%
- Lineup: 未発表
- Lineup quality: -0.10
- Platoon proxy: +0.14
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: San Diego Padres 2.92 - Arizona Diamondbacks 2.89

### 5. Toronto Blue Jays +1.5
- Game: Toronto Blue Jays @ Houston Astros
- Odds: 1.57
- Cover probability: 67.4%
- EV: 5.8%
- 1/4 Kelly: 2.5%
- Lineup: 未発表
- Lineup quality: -0.08
- Platoon proxy: -0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Toronto Blue Jays 3.29 - Houston Astros 3.66

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.