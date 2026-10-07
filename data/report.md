# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-07T20:53:08.354809+00:00
- API requests remaining: 440
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. New York Yankees
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 1.62
- AI probability: 67.7%
- EV: 9.6%
- 1/4 Kelly: 3.9%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 0.988
- Temperature: 16.5 C
- Rain probability: 0%
- Wind: 7.3 km/h (318 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.34 - New York Yankees 3.53

### 2. Milwaukee Brewers
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.97
- AI probability: 55.3%
- EV: 9.0%
- 1/4 Kelly: 2.3%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.06
- Weather run factor: 1.006
- Temperature: 25.5 C
- Rain probability: 0%
- Wind: 7.3 km/h (328 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.96 - San Diego Padres 2.56

## Run Line Buy Ranking

### 1. Atlanta Braves +1.5
- Game: Los Angeles Dodgers @ Atlanta Braves
- Odds: 1.74
- Cover probability: 72.3%
- EV: 25.7%
- 1/4 Kelly: 8.7%
- Lineup: 発表済み
- Lineup quality: +0.20
- Platoon proxy: +0.08
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Los Angeles Dodgers 2.59 - Atlanta Braves 2.32

### 2. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ San Diego Padres
- Odds: 1.45
- Cover probability: 80.2%
- EV: 16.3%
- 1/4 Kelly: 9.0%
- Lineup: 未発表
- Lineup quality: +0.39
- Platoon proxy: +0.06
- Weather run factor: 1.006
- Temperature: 25.5 C
- Rain probability: 0%
- Wind: 7.3 km/h (328 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.96 - San Diego Padres 2.56

### 3. New York Yankees -1.5
- Game: Tampa Bay Rays @ New York Yankees
- Odds: 2.42
- Cover probability: 44.0%
- EV: 6.6%
- 1/4 Kelly: 1.2%
- Lineup: 未発表
- Lineup quality: +0.22
- Platoon proxy: +0.00
- Weather run factor: 0.988
- Temperature: 16.5 C
- Rain probability: 0%
- Wind: 7.3 km/h (318 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.34 - New York Yankees 3.53

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.