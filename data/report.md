# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-25T02:37:32.100972+00:00
- API requests remaining: 257
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Angels
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 2.18
- AI probability: 64.7%
- EV: 41.0%
- 1/4 Kelly: 8.7%
- Lineup: 未発表
- Lineup quality: -0.22
- Platoon proxy: -0.09
- Weather run factor: 0.991
- Temperature: 15.9 C
- Rain probability: 0%
- Wind: 10.8 km/h (356 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Los Angeles Angels 4.03 - Seattle Mariners 2.78

### 2. Tampa Bay Rays
- Game: Tampa Bay Rays @ Philadelphia Phillies
- Odds: 2.39
- AI probability: 46.7%
- EV: 11.6%
- 1/4 Kelly: 2.1%
- Lineup: 未発表
- Lineup quality: +0.40
- Platoon proxy: -0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Tampa Bay Rays 3.53 - Philadelphia Phillies 3.66

### 3. Texas Rangers
- Game: Texas Rangers @ Minnesota Twins
- Odds: 1.95
- AI probability: 56.1%
- EV: 9.3%
- 1/4 Kelly: 2.5%
- Lineup: 未発表
- Lineup quality: +0.12
- Platoon proxy: -0.01
- Weather run factor: 0.988
- Temperature: 16.7 C
- Rain probability: 0%
- Wind: 6.9 km/h (137 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Texas Rangers 4.23 - Minnesota Twins 3.71

### 4. Cleveland Guardians
- Game: Cleveland Guardians @ Kansas City Royals
- Odds: 1.75
- AI probability: 61.4%
- EV: 7.4%
- 1/4 Kelly: 2.5%
- Lineup: 未発表
- Lineup quality: -0.00
- Platoon proxy: +0.02
- Weather run factor: 1.017
- Temperature: 28.1 C
- Rain probability: 1%
- Wind: 12.5 km/h (136 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Cleveland Guardians 4.29 - Kansas City Royals 3.39

### 5. Pittsburgh Pirates
- Game: Pittsburgh Pirates @ Detroit Tigers
- Odds: 1.94
- AI probability: 54.9%
- EV: 6.4%
- 1/4 Kelly: 1.7%
- Lineup: 未発表
- Lineup quality: +0.36
- Platoon proxy: +0.07
- Weather run factor: 1.012
- Temperature: 24.2 C
- Rain probability: 0%
- Wind: 16.1 km/h (40 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Pittsburgh Pirates 3.43 - Detroit Tigers 3.04

## Run Line Buy Ranking

### 1. Los Angeles Angels +1.5
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 1.52
- Cover probability: 86.2%
- EV: 31.0%
- 1/4 Kelly: 14.9%
- Lineup: 未発表
- Lineup quality: -0.22
- Platoon proxy: -0.09
- Weather run factor: 0.991
- Temperature: 15.9 C
- Rain probability: 0%
- Wind: 10.8 km/h (356 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Los Angeles Angels 4.03 - Seattle Mariners 2.78

### 2. Tampa Bay Rays +1.5
- Game: Tampa Bay Rays @ Philadelphia Phillies
- Odds: 1.58
- Cover probability: 70.3%
- EV: 11.1%
- 1/4 Kelly: 4.8%
- Lineup: 未発表
- Lineup quality: +0.40
- Platoon proxy: -0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Tampa Bay Rays 3.53 - Philadelphia Phillies 3.66

### 3. Texas Rangers +1.5
- Game: Texas Rangers @ Minnesota Twins
- Odds: 1.44
- Cover probability: 76.9%
- EV: 10.8%
- 1/4 Kelly: 6.1%
- Lineup: 未発表
- Lineup quality: +0.12
- Platoon proxy: -0.01
- Weather run factor: 0.988
- Temperature: 16.7 C
- Rain probability: 0%
- Wind: 6.9 km/h (137 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Texas Rangers 4.23 - Minnesota Twins 3.71

### 4. Colorado Rockies +1.5
- Game: Colorado Rockies @ Chicago White Sox
- Odds: 1.88
- Cover probability: 56.3%
- EV: 5.8%
- 1/4 Kelly: 1.7%
- Lineup: 未発表
- Lineup quality: +0.52
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Colorado Rockies 2.71 - Chicago White Sox 3.85

### 5. Detroit Tigers +1.5
- Game: Pittsburgh Pirates @ Detroit Tigers
- Odds: 1.56
- Cover probability: 67.6%
- EV: 5.5%
- 1/4 Kelly: 2.4%
- Lineup: 未発表
- Lineup quality: +0.38
- Platoon proxy: -0.04
- Weather run factor: 1.012
- Temperature: 24.2 C
- Rain probability: 0%
- Wind: 16.1 km/h (40 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Pittsburgh Pirates 3.43 - Detroit Tigers 3.04

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.