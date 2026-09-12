# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-12T21:50:10.853878+00:00
- API requests remaining: 377
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Houston Astros
- Game: Houston Astros @ Tampa Bay Rays
- Odds: 2.27
- AI probability: 55.4%
- EV: 25.7%
- 1/4 Kelly: 5.1%
- Lineup: 未発表
- Lineup quality: +0.29
- Platoon proxy: -0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Houston Astros 3.92 - Tampa Bay Rays 3.39

### 2. Athletics
- Game: Seattle Mariners @ Athletics
- Odds: 2.48
- AI probability: 49.8%
- EV: 23.5%
- 1/4 Kelly: 4.0%
- Lineup: 未発表
- Lineup quality: +0.03
- Platoon proxy: +0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Seattle Mariners 3.47 - Athletics 3.56

### 3. Texas Rangers
- Game: Texas Rangers @ Arizona Diamondbacks
- Odds: 2.2
- AI probability: 48.3%
- EV: 6.3%
- 1/4 Kelly: 1.3%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Texas Rangers 3.75 - Arizona Diamondbacks 3.80

### 4. Atlanta Braves
- Game: Philadelphia Phillies @ Atlanta Braves
- Odds: 1.73
- AI probability: 61.2%
- EV: 5.9%
- 1/4 Kelly: 2.0%
- Lineup: 未発表
- Lineup quality: +0.05
- Platoon proxy: +0.03
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Philadelphia Phillies 3.29 - Atlanta Braves 4.12

### 5. Milwaukee Brewers
- Game: Cincinnati Reds @ Milwaukee Brewers
- Odds: 1.49
- AI probability: 70.9%
- EV: 5.6%
- 1/4 Kelly: 2.9%
- Lineup: 未発表
- Lineup quality: +0.40
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.45 - Milwaukee Brewers 3.89

## Run Line Buy Ranking

### 1. Athletics +1.5
- Game: Seattle Mariners @ Athletics
- Odds: 1.93
- Cover probability: 73.2%
- EV: 41.3%
- 1/4 Kelly: 11.1%
- Lineup: 未発表
- Lineup quality: +0.03
- Platoon proxy: +0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Seattle Mariners 3.47 - Athletics 3.56

### 2. Houston Astros +1.5
- Game: Houston Astros @ Tampa Bay Rays
- Odds: 1.6
- Cover probability: 78.1%
- EV: 24.9%
- 1/4 Kelly: 10.4%
- Lineup: 未発表
- Lineup quality: +0.29
- Platoon proxy: -0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Houston Astros 3.92 - Tampa Bay Rays 3.39

### 3. Texas Rangers +1.5
- Game: Texas Rangers @ Arizona Diamondbacks
- Odds: 1.57
- Cover probability: 70.6%
- EV: 10.9%
- 1/4 Kelly: 4.8%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Texas Rangers 3.75 - Arizona Diamondbacks 3.80

### 4. Chicago White Sox +1.5
- Game: Chicago White Sox @ St. Louis Cardinals
- Odds: 1.45
- Cover probability: 74.4%
- EV: 7.9%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: +0.23
- Platoon proxy: +0.10
- Weather run factor: 1.018
- Temperature: 29.8 C
- Rain probability: 11%
- Wind: 10.2 km/h (337 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Chicago White Sox 3.06 - St. Louis Cardinals 3.01

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.