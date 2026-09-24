# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-24T02:21:08.413838+00:00
- API requests remaining: 266
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Miami Marlins
- Game: Miami Marlins @ Chicago Cubs
- Odds: 2.79
- AI probability: 49.3%
- EV: 37.5%
- 1/4 Kelly: 5.2%
- Lineup: 未発表
- Lineup quality: +0.11
- Platoon proxy: +0.06
- Weather run factor: 0.995
- Temperature: 17.9 C
- Rain probability: 0%
- Wind: 11.4 km/h (79 deg)
- Bullpen fatigue proxy: 0.30
- Expected score: Miami Marlins 3.45 - Chicago Cubs 3.33

### 2. Colorado Rockies
- Game: Arizona Diamondbacks @ Colorado Rockies
- Odds: 2.62
- AI probability: 52.4%
- EV: 37.4%
- 1/4 Kelly: 5.8%
- Lineup: 未発表
- Lineup quality: +0.48
- Platoon proxy: +0.07
- Weather run factor: 1.004
- Temperature: 22.1 C
- Rain probability: 5%
- Wind: 11.8 km/h (12 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Arizona Diamondbacks 3.83 - Colorado Rockies 4.16

### 3. New York Yankees
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 1.69
- AI probability: 69.3%
- EV: 17.1%
- 1/4 Kelly: 6.2%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: -0.01
- Weather run factor: 0.995
- Temperature: 17.1 C
- Rain probability: 0%
- Wind: 12.4 km/h (26 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Tampa Bay Rays 2.49 - New York Yankees 3.91

### 4. Atlanta Braves
- Game: Cincinnati Reds @ Atlanta Braves
- Odds: 1.48
- AI probability: 75.1%
- EV: 11.1%
- 1/4 Kelly: 5.8%
- Lineup: 未発表
- Lineup quality: +0.29
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.40 - Atlanta Braves 4.27

### 5. San Diego Padres
- Game: San Diego Padres @ Los Angeles Dodgers
- Odds: 2.52
- AI probability: 42.1%
- EV: 6.1%
- 1/4 Kelly: 1.0%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: San Diego Padres 2.41 - Los Angeles Dodgers 2.81

## Run Line Buy Ranking

### 1. Colorado Rockies +1.5
- Game: Arizona Diamondbacks @ Colorado Rockies
- Odds: 2.04
- Cover probability: 74.7%
- EV: 52.5%
- 1/4 Kelly: 12.6%
- Lineup: 未発表
- Lineup quality: +0.48
- Platoon proxy: +0.07
- Weather run factor: 1.004
- Temperature: 22.1 C
- Rain probability: 5%
- Wind: 11.8 km/h (12 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Arizona Diamondbacks 3.83 - Colorado Rockies 4.16

### 2. New York Yankees -1.5
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 2.57
- Cover probability: 47.8%
- EV: 22.9%
- 1/4 Kelly: 3.6%
- Lineup: 未発表
- Lineup quality: +0.24
- Platoon proxy: -0.01
- Weather run factor: 0.995
- Temperature: 17.1 C
- Rain probability: 0%
- Wind: 12.4 km/h (26 deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Tampa Bay Rays 2.49 - New York Yankees 3.91

### 3. San Diego Padres +1.5
- Game: San Diego Padres @ Los Angeles Dodgers
- Odds: 1.68
- Cover probability: 69.6%
- EV: 16.9%
- 1/4 Kelly: 6.2%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: San Diego Padres 2.41 - Los Angeles Dodgers 2.81

### 4. Atlanta Braves -1.5
- Game: Cincinnati Reds @ Atlanta Braves
- Odds: 2.08
- Cover probability: 55.0%
- EV: 14.4%
- 1/4 Kelly: 3.3%
- Lineup: 未発表
- Lineup quality: +0.29
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.40 - Atlanta Braves 4.27

### 5. St. Louis Cardinals +1.5
- Game: St. Louis Cardinals @ Pittsburgh Pirates
- Odds: 1.61
- Cover probability: 68.3%
- EV: 9.9%
- 1/4 Kelly: 4.1%
- Lineup: 未発表
- Lineup quality: +0.05
- Platoon proxy: +0.02
- Weather run factor: 0.995
- Temperature: 15.6 C
- Rain probability: 0%
- Wind: 15.3 km/h (66 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: St. Louis Cardinals 2.84 - Pittsburgh Pirates 3.24

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.