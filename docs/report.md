# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-06T21:50:17.111846+00:00
- API requests remaining: 434
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Los Angeles Dodgers
- Odds: 2.7
- AI probability: 60.1%
- EV: 62.2%
- 1/4 Kelly: 9.2%
- Lineup: 未発表
- Lineup quality: +0.47
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Washington Nationals 3.58 - Los Angeles Dodgers 2.65

### 2. Chicago White Sox
- Game: Minnesota Twins @ Chicago White Sox
- Odds: 1.71
- AI probability: 63.8%
- EV: 9.1%
- 1/4 Kelly: 3.2%
- Lineup: 発表済み
- Lineup quality: +0.29
- Platoon proxy: +0.16
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Minnesota Twins 2.46 - Chicago White Sox 3.38

## Run Line Buy Ranking

### 1. Washington Nationals +1.5
- Game: Washington Nationals @ Los Angeles Dodgers
- Odds: 1.79
- Cover probability: 84.4%
- EV: 51.0%
- 1/4 Kelly: 16.1%
- Lineup: 未発表
- Lineup quality: +0.47
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Washington Nationals 3.58 - Los Angeles Dodgers 2.65

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.