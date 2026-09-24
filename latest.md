# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-24T22:51:56.667837+00:00
- API requests remaining: 260
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Angels
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 2.69
- AI probability: 65.6%
- EV: 76.6%
- 1/4 Kelly: 11.3%
- Lineup: 未発表
- Lineup quality: -0.22
- Platoon proxy: +0.14
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Los Angeles Angels 4.36 - Seattle Mariners 2.85

### 2. Athletics
- Game: Houston Astros @ Athletics
- Odds: 2.52
- AI probability: 50.1%
- EV: 26.3%
- 1/4 Kelly: 4.3%
- Lineup: 未発表
- Lineup quality: +0.18
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Houston Astros 3.24 - Athletics 3.37

### 3. New York Yankees
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 1.72
- AI probability: 69.0%
- EV: 18.6%
- 1/4 Kelly: 6.5%
- Lineup: 発表済み
- Lineup quality: +0.06
- Platoon proxy: +0.10
- Weather run factor: 0.994
- Temperature: 16.7 C
- Rain probability: 0%
- Wind: 12.1 km/h (17 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Tampa Bay Rays 2.47 - New York Yankees 3.86

### 4. Atlanta Braves
- Game: Cincinnati Reds @ Atlanta Braves
- Odds: 1.44
- AI probability: 76.0%
- EV: 9.4%
- 1/4 Kelly: 5.3%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.35 - Atlanta Braves 4.26

### 5. San Diego Padres
- Game: San Diego Padres @ Los Angeles Dodgers
- Odds: 2.51
- AI probability: 42.2%
- EV: 5.9%
- 1/4 Kelly: 1.0%
- Lineup: 発表済み
- Lineup quality: +0.21
- Platoon proxy: -0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 2.50 - Los Angeles Dodgers 2.91

## Run Line Buy Ranking

### 1. Los Angeles Angels +1.5
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 1.78
- Cover probability: 87.5%
- EV: 55.7%
- 1/4 Kelly: 17.9%
- Lineup: 未発表
- Lineup quality: -0.22
- Platoon proxy: +0.14
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Los Angeles Angels 4.36 - Seattle Mariners 2.85

### 2. Athletics +1.5
- Game: Houston Astros @ Athletics
- Odds: 1.96
- Cover probability: 74.4%
- EV: 45.8%
- 1/4 Kelly: 11.9%
- Lineup: 未発表
- Lineup quality: +0.18
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Houston Astros 3.24 - Athletics 3.37

### 3. New York Yankees -1.5
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 2.67
- Cover probability: 47.4%
- EV: 26.5%
- 1/4 Kelly: 4.0%
- Lineup: 発表済み
- Lineup quality: +0.06
- Platoon proxy: +0.10
- Weather run factor: 0.994
- Temperature: 16.7 C
- Rain probability: 0%
- Wind: 12.1 km/h (17 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Tampa Bay Rays 2.47 - New York Yankees 3.86

### 4. San Diego Padres +1.5
- Game: San Diego Padres @ Los Angeles Dodgers
- Odds: 1.69
- Cover probability: 69.3%
- EV: 17.1%
- 1/4 Kelly: 6.2%
- Lineup: 発表済み
- Lineup quality: +0.21
- Platoon proxy: -0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 2.50 - Los Angeles Dodgers 2.91

### 5. Atlanta Braves -1.5
- Game: Cincinnati Reds @ Atlanta Braves
- Odds: 1.95
- Cover probability: 55.5%
- EV: 8.3%
- 1/4 Kelly: 2.2%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.35 - Atlanta Braves 4.26

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.