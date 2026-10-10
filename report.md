# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-10T23:03:41.588045+00:00
- API requests remaining: 410
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Chicago White Sox
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 2.26
- AI probability: 57.0%
- EV: 28.9%
- 1/4 Kelly: 5.7%
- Lineup: 発表済み
- Lineup quality: +0.27
- Platoon proxy: +0.11
- Weather run factor: 0.998
- Temperature: 18.6 C
- Rain probability: 4%
- Wind: 13.1 km/h (137 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.65

## Run Line Buy Ranking

### 1. Chicago White Sox +1.5
- Game: Chicago White Sox @ Cleveland Guardians
- Odds: 1.56
- Cover probability: 81.6%
- EV: 27.3%
- 1/4 Kelly: 12.2%
- Lineup: 発表済み
- Lineup quality: +0.27
- Platoon proxy: +0.11
- Weather run factor: 0.998
- Temperature: 18.6 C
- Rain probability: 4%
- Wind: 13.1 km/h (137 deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Chicago White Sox 3.25 - Cleveland Guardians 2.65

### 2. Los Angeles Dodgers +1.5
- Game: Los Angeles Dodgers @ Milwaukee Brewers
- Odds: 1.4
- Cover probability: 78.7%
- EV: 10.2%
- 1/4 Kelly: 6.4%
- Lineup: 未発表
- Lineup quality: +0.29
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Los Angeles Dodgers 2.57 - Milwaukee Brewers 2.40

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.