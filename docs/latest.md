# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-10T02:13:11.788547+00:00
- API requests remaining: 401
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Houston Astros
- Game: Houston Astros @ Philadelphia Phillies
- Odds: 2.54
- AI probability: 45.0%
- EV: 14.3%
- 1/4 Kelly: 2.3%
- Lineup: 未発表
- Lineup quality: +0.27
- Platoon proxy: -0.09
- Weather run factor: 1.026
- Temperature: 31.1 C
- Rain probability: 1%
- Wind: 15.2 km/h (263 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Houston Astros 3.81 - Philadelphia Phillies 4.06

## Run Line Buy Ranking

### 1. Houston Astros +1.5
- Game: Houston Astros @ Philadelphia Phillies
- Odds: 1.72
- Cover probability: 67.7%
- EV: 16.5%
- 1/4 Kelly: 5.7%
- Lineup: 未発表
- Lineup quality: +0.27
- Platoon proxy: -0.09
- Weather run factor: 1.026
- Temperature: 31.1 C
- Rain probability: 1%
- Wind: 15.2 km/h (263 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Houston Astros 3.81 - Philadelphia Phillies 4.06

### 2. Texas Rangers +1.5
- Game: Texas Rangers @ Seattle Mariners
- Odds: 1.51
- Cover probability: 70.6%
- EV: 6.6%
- 1/4 Kelly: 3.2%
- Lineup: 未発表
- Lineup quality: +0.17
- Platoon proxy: +0.00
- Weather run factor: 0.993
- Temperature: 17.4 C
- Rain probability: 0%
- Wind: 9.8 km/h (306 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Texas Rangers 3.01 - Seattle Mariners 3.22

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.