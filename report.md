# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-03T19:01:00.784182+00:00
- API requests remaining: 473
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Athletics
- Game: Athletics @ Seattle Mariners
- Odds: 2.87
- AI probability: 46.2%
- EV: 32.7%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: -0.04
- Platoon proxy: -0.02
- Weather run factor: 0.996
- Temperature: 16.6 C
- Rain probability: 6%
- Wind: 14.8 km/h (357 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Athletics 3.14 - Seattle Mariners 3.22

### 2. Milwaukee Brewers
- Game: Milwaukee Brewers @ Chicago Cubs
- Odds: 1.9
- AI probability: 67.6%
- EV: 28.5%
- 1/4 Kelly: 7.9%
- Lineup: 未発表
- Lineup quality: +0.42
- Platoon proxy: +0.00
- Weather run factor: 1.006
- Temperature: 24.9 C
- Rain probability: 5%
- Wind: 8.4 km/h (110 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Milwaukee Brewers 3.77 - Chicago Cubs 2.40

### 3. Miami Marlins
- Game: Miami Marlins @ Kansas City Royals
- Odds: 2.03
- AI probability: 61.2%
- EV: 24.2%
- 1/4 Kelly: 5.9%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: -0.04
- Weather run factor: 1.037
- Temperature: 37.1 C
- Rain probability: 0%
- Wind: 14.6 km/h (171 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Miami Marlins 3.86 - Kansas City Royals 2.93

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
- Odds: 2.14
- AI probability: 52.4%
- EV: 12.2%
- 1/4 Kelly: 2.7%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Tampa Bay Rays 3.43 - Texas Rangers 3.65

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
- Rain probability: 6%
- Wind: 14.8 km/h (357 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Athletics 3.14 - Seattle Mariners 3.22

### 2. Texas Rangers +1.5
- Game: Tampa Bay Rays @ Texas Rangers
- Odds: 1.66
- Cover probability: 74.7%
- EV: 24.0%
- 1/4 Kelly: 9.1%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Tampa Bay Rays 3.43 - Texas Rangers 3.65

### 3. St. Louis Cardinals +1.5
- Game: St. Louis Cardinals @ Los Angeles Dodgers
- Odds: 2.19
- Cover probability: 54.2%
- EV: 18.8%
- 1/4 Kelly: 3.9%
- Lineup: 未発表
- Lineup quality: -0.06
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 2.27 - Los Angeles Dodgers 3.57

### 4. Milwaukee Brewers -1.5
- Game: Milwaukee Brewers @ Chicago Cubs
- Odds: 2.47
- Cover probability: 47.2%
- EV: 16.6%
- 1/4 Kelly: 2.8%
- Lineup: 未発表
- Lineup quality: +0.42
- Platoon proxy: +0.00
- Weather run factor: 1.006
- Temperature: 24.9 C
- Rain probability: 5%
- Wind: 8.4 km/h (110 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Milwaukee Brewers 3.77 - Chicago Cubs 2.40

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.