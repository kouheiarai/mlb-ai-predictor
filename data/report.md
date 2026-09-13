# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-13T18:25:05.433276+00:00
- API requests remaining: 368
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Boston Red Sox
- Game: Kansas City Royals @ Boston Red Sox
- Odds: 1.52
- AI probability: 76.1%
- EV: 15.7%
- 1/4 Kelly: 7.5%
- Lineup: 発表済み
- Lineup quality: +0.19
- Platoon proxy: +0.16
- Weather run factor: 0.999
- Temperature: 19.2 C
- Rain probability: 90%
- Wind: 12.6 km/h (88 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Kansas City Royals 2.33 - Boston Red Sox 4.32

### 2. Athletics
- Game: Seattle Mariners @ Athletics
- Odds: 2.18
- AI probability: 49.8%
- EV: 8.6%
- 1/4 Kelly: 1.8%
- Lineup: 発表済み
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Seattle Mariners 3.55 - Athletics 3.58

### 3. Texas Rangers
- Game: Texas Rangers @ Arizona Diamondbacks
- Odds: 2.16
- AI probability: 49.2%
- EV: 6.2%
- 1/4 Kelly: 1.3%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: +0.14
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Texas Rangers 3.72 - Arizona Diamondbacks 3.70

### 4. San Diego Padres
- Game: San Diego Padres @ San Francisco Giants
- Odds: 1.82
- AI probability: 57.7%
- EV: 5.1%
- 1/4 Kelly: 1.5%
- Lineup: 未発表
- Lineup quality: -0.06
- Platoon proxy: -0.05
- Weather run factor: 1.018
- Temperature: 21.2 C
- Rain probability: 0%
- Wind: 27.2 km/h (298 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 3.14 - San Francisco Giants 2.61

## Run Line Buy Ranking

### 1. Athletics +1.5
- Game: Seattle Mariners @ Athletics
- Odds: 1.74
- Cover probability: 72.2%
- EV: 25.7%
- 1/4 Kelly: 8.7%
- Lineup: 発表済み
- Lineup quality: +0.07
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Seattle Mariners 3.55 - Athletics 3.58

### 2. Boston Red Sox -1.5
- Game: Kansas City Royals @ Boston Red Sox
- Odds: 2.18
- Cover probability: 57.1%
- EV: 24.5%
- 1/4 Kelly: 5.2%
- Lineup: 発表済み
- Lineup quality: +0.19
- Platoon proxy: +0.16
- Weather run factor: 0.999
- Temperature: 19.2 C
- Rain probability: 90%
- Wind: 12.6 km/h (88 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Kansas City Royals 2.33 - Boston Red Sox 4.32

### 3. Texas Rangers +1.5
- Game: Texas Rangers @ Arizona Diamondbacks
- Odds: 1.56
- Cover probability: 71.9%
- EV: 12.2%
- 1/4 Kelly: 5.4%
- Lineup: 発表済み
- Lineup quality: +0.25
- Platoon proxy: +0.14
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Texas Rangers 3.72 - Arizona Diamondbacks 3.70

### 4. San Francisco Giants +1.5
- Game: San Diego Padres @ San Francisco Giants
- Odds: 1.63
- Cover probability: 66.7%
- EV: 8.8%
- 1/4 Kelly: 3.5%
- Lineup: 未発表
- Lineup quality: +0.01
- Platoon proxy: +0.09
- Weather run factor: 1.018
- Temperature: 21.2 C
- Rain probability: 0%
- Wind: 27.2 km/h (298 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: San Diego Padres 3.14 - San Francisco Giants 2.61

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.