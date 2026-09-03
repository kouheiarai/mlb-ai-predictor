# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-03T23:50:18.880842+00:00
- API requests remaining: 467
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Athletics
- Game: Athletics @ Seattle Mariners
- Odds: 2.88
- AI probability: 46.1%
- EV: 32.7%
- 1/4 Kelly: 4.3%
- Lineup: 未発表
- Lineup quality: -0.04
- Platoon proxy: -0.02
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Athletics 3.15 - Seattle Mariners 3.24

### 2. Texas Rangers
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

## Run Line Buy Ranking

### 1. Athletics +1.5
- Game: Athletics @ Seattle Mariners
- Odds: 1.83
- Cover probability: 72.0%
- EV: 31.8%
- 1/4 Kelly: 9.6%
- Lineup: 未発表
- Lineup quality: -0.04
- Platoon proxy: -0.02
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Athletics 3.15 - Seattle Mariners 3.24

### 2. Texas Rangers +1.5
- Game: Tampa Bay Rays @ Texas Rangers
- Odds: 1.65
- Cover probability: 74.7%
- EV: 23.2%
- 1/4 Kelly: 8.9%
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
- Odds: 2.13
- Cover probability: 56.1%
- EV: 19.4%
- 1/4 Kelly: 4.3%
- Lineup: 発表済み
- Lineup quality: -0.01
- Platoon proxy: +0.22
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 2.28 - Los Angeles Dodgers 3.47

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.