# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-08-03T21:55:25.854937+00:00
- API requests remaining: 300
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Philadelphia Phillies
- Odds: 2.35
- AI probability: 49.7%
- EV: 16.9%
- 1/4 Kelly: 3.1%
- Lineup: 未発表
- Lineup quality: +0.27
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 3.16 - Philadelphia Phillies 3.08

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
- Odds: 1.66
- Cover probability: 74.8%
- EV: 24.1%
- 1/4 Kelly: 9.1%
- Lineup: 未発表
- Lineup quality: +0.27
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 3.16 - Philadelphia Phillies 3.08

### 2. Colorado Rockies +1.5
- Game: Tampa Bay Rays @ Colorado Rockies
- Odds: 2.06
- Cover probability: 57.8%
- EV: 19.1%
- 1/4 Kelly: 4.5%
- Lineup: 未発表
- Lineup quality: +0.64
- Platoon proxy: +0.10
- Weather run factor: 1.026
- Temperature: 31.1 C
- Rain probability: 1%
- Wind: 15.3 km/h (51 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Tampa Bay Rays 3.95 - Colorado Rockies 2.94

### 3. Chicago Cubs +1.5
- Game: Los Angeles Dodgers @ Chicago Cubs
- Odds: 1.65
- Cover probability: 71.5%
- EV: 18.0%
- 1/4 Kelly: 6.9%
- Lineup: 未発表
- Lineup quality: +0.30
- Platoon proxy: +0.00
- Weather run factor: 1.010
- Temperature: 26.3 C
- Rain probability: 28%
- Wind: 9.7 km/h (169 deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Los Angeles Dodgers 2.97 - Chicago Cubs 2.78

### 4. San Diego Padres +1.5
- Game: San Diego Padres @ Arizona Diamondbacks
- Odds: 1.47
- Cover probability: 74.7%
- EV: 9.8%
- 1/4 Kelly: 5.2%
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
- Odds: 1.58
- Cover probability: 67.4%
- EV: 6.5%
- 1/4 Kelly: 2.8%
- Lineup: 未発表
- Lineup quality: -0.08
- Platoon proxy: -0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Toronto Blue Jays 3.29 - Houston Astros 3.66

### 6. San Francisco Giants +1.5
- Game: San Francisco Giants @ Texas Rangers
- Odds: 1.51
- Cover probability: 69.7%
- EV: 5.2%
- 1/4 Kelly: 2.5%
- Lineup: 未発表
- Lineup quality: -0.07
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: San Francisco Giants 3.37 - Texas Rangers 3.57

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.