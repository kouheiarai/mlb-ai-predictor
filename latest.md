# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-08-03T08:53:38.504732+00:00
- API requests remaining: 332
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Pittsburgh Pirates @ Milwaukee Brewers
- Odds: 1.7
- AI probability: 62.1%
- EV: 5.5%
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

### 1. Arizona Diamondbacks +1.5
- Game: San Diego Padres @ Arizona Diamondbacks
- Odds: 1.55
- Cover probability: 73.6%
- EV: 14.1%
- 1/4 Kelly: 6.4%
- Lineup: 未発表
- Lineup quality: +0.13
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 2.92 - Arizona Diamondbacks 2.89

### 2. Colorado Rockies +1.5
- Game: Tampa Bay Rays @ Colorado Rockies
- Odds: 1.93
- Cover probability: 57.8%
- EV: 11.6%
- 1/4 Kelly: 3.1%
- Lineup: 未発表
- Lineup quality: +0.64
- Platoon proxy: +0.10
- Weather run factor: 1.030
- Temperature: 32.5 C
- Rain probability: 3%
- Wind: 16.6 km/h (48 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Tampa Bay Rays 3.97 - Colorado Rockies 2.95

### 3. Toronto Blue Jays +1.5
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