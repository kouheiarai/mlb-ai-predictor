# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-28T20:39:51.158381+00:00
- API requests remaining: 281
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Milwaukee Brewers @ Tampa Bay Rays
- Odds: 1.72
- AI probability: 61.5%
- EV: 5.8%
- 1/4 Kelly: 2.0%
- Lineup: 発表済み
- Lineup quality: +0.09
- Platoon proxy: +0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 3.03 - Tampa Bay Rays 2.29

## Run Line Buy Ranking

### 1. Tampa Bay Rays +1.5
- Game: Milwaukee Brewers @ Tampa Bay Rays
- Odds: 1.69
- Cover probability: 63.9%
- EV: 8.0%
- 1/4 Kelly: 2.9%
- Lineup: 発表済み
- Lineup quality: +0.09
- Platoon proxy: +0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 3.03 - Tampa Bay Rays 2.29

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.