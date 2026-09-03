# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-03T22:01:52.347097+00:00
- API requests remaining: 470
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Athletics
- Game: Athletics @ Seattle Mariners
- Odds: 2.88
- AI probability: 46.2%
- EV: 33.0%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: -0.04
- Platoon proxy: -0.02
- Weather run factor: 0.996
- Temperature: 16.6 C
- Rain probability: 10%
- Wind: 14.8 km/h (357 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Athletics 3.14 - Seattle Mariners 3.22

### 2. Miami Marlins
- Game: Miami Marlins @ Kansas City Royals
- Odds: 2.04
- AI probability: 61.8%
- EV: 26.0%
- 1/4 Kelly: 6.2%
- Lineup: 発表済み
- Lineup quality: +0.21
- Platoon proxy: +0.04
- Weather run factor: 1.036
- Temperature: 36.7 C
- Rain probability: 0%
- Wind: 14.1 km/h (176 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Miami Marlins 3.91 - Kansas City Royals 2.94

### 3. Milwaukee Brewers
- Game: Milwaukee Brewers @ Chicago Cubs
- Odds: 1.83
- AI probability: 68.1%
- EV: 24.6%
- 1/4 Kelly: 7.4%
- Lineup: 発表済み
- Lineup quality: +0.46
- Platoon proxy: +0.04
- Weather run factor: 1.010
- Temperature: 25.9 C
- Rain probability: 4%
- Wind: 10.4 km/h (136 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Milwaukee Brewers 3.80 - Chicago Cubs 2.41

### 4. Boston Red Sox
- Game: Boston Red Sox @ Baltimore Orioles
- Odds: 1.84
- AI probability: 64.9%
- EV: 19.3%
- 1/4 Kelly: 5.8%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Boston Red Sox 3.63 - Baltimore Orioles 2.53

### 5. Texas Rangers
- Game: Tampa Bay Rays @ Texas Rangers
- Odds: 2.11
- AI probability: 52.5%
- EV: 10.8%
- 1/4 Kelly: 2.4%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Tampa Bay Rays 3.43 - Texas Rangers 3.65

### 6. St. Louis Cardinals
- Game: St. Louis Cardinals @ Los Angeles Dodgers
- Odds: 3.64
- AI probability: 29.0%
- EV: 5.5%
- 1/4 Kelly: 0.5%
- Lineup: 未発表
- Lineup quality: -0.06
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 2.27 - Los Angeles Dodgers 3.57

## Run Line Buy Ranking

### 1. Athletics +1.5
- Game: Athletics @ Seattle Mariners
- Odds: 1.83
- Cover probability: 72.2%
- EV: 32.1%
- 1/4 Kelly: 9.7%
- Lineup: 未発表
- Lineup quality: -0.04
- Platoon proxy: -0.02
- Weather run factor: 0.996
- Temperature: 16.6 C
- Rain probability: 10%
- Wind: 14.8 km/h (357 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Athletics 3.14 - Seattle Mariners 3.22

### 2. Miami Marlins +1.5
- Game: Miami Marlins @ Kansas City Royals
- Odds: 1.48
- Cover probability: 83.7%
- EV: 23.8%
- 1/4 Kelly: 12.4%
- Lineup: 発表済み
- Lineup quality: +0.21
- Platoon proxy: +0.04
- Weather run factor: 1.036
- Temperature: 36.7 C
- Rain probability: 0%
- Wind: 14.1 km/h (176 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Miami Marlins 3.91 - Kansas City Royals 2.94

### 3. Texas Rangers +1.5
- Game: Tampa Bay Rays @ Texas Rangers
- Odds: 1.64
- Cover probability: 74.7%
- EV: 22.5%
- 1/4 Kelly: 8.8%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Tampa Bay Rays 3.43 - Texas Rangers 3.65

### 4. St. Louis Cardinals +1.5
- Game: St. Louis Cardinals @ Los Angeles Dodgers
- Odds: 2.22
- Cover probability: 54.2%
- EV: 20.4%
- 1/4 Kelly: 4.2%
- Lineup: 未発表
- Lineup quality: -0.06
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 2.27 - Los Angeles Dodgers 3.57

### 5. Milwaukee Brewers -1.5
- Game: Milwaukee Brewers @ Chicago Cubs
- Odds: 2.39
- Cover probability: 47.5%
- EV: 13.5%
- 1/4 Kelly: 2.4%
- Lineup: 発表済み
- Lineup quality: +0.46
- Platoon proxy: +0.04
- Weather run factor: 1.010
- Temperature: 25.9 C
- Rain probability: 4%
- Wind: 10.4 km/h (136 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Milwaukee Brewers 3.80 - Chicago Cubs 2.41

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.