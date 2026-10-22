# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-22T02:31:48.293640+00:00
- API requests remaining: 320
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Tampa Bay Rays @ Milwaukee Brewers
- Odds: 1.63
- AI probability: 68.2%
- EV: 11.1%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.35 - Milwaukee Brewers 3.60

## Run Line Buy Ranking

### 1. Milwaukee Brewers -1.5
- Game: Tampa Bay Rays @ Milwaukee Brewers
- Odds: 2.51
- Cover probability: 45.2%
- EV: 13.5%
- 1/4 Kelly: 2.2%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Tampa Bay Rays 2.35 - Milwaukee Brewers 3.60

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.