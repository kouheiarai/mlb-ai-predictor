# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-14T00:43:26.640199+00:00
- API requests remaining: 386
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Milwaukee Brewers
- Game: Milwaukee Brewers @ Los Angeles Dodgers
- Odds: 2.54
- AI probability: 46.5%
- EV: 18.1%
- 1/4 Kelly: 2.9%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.53 - Los Angeles Dodgers 2.63

## Run Line Buy Ranking

### 1. Milwaukee Brewers +1.5
- Game: Milwaukee Brewers @ Los Angeles Dodgers
- Odds: 1.69
- Cover probability: 74.4%
- EV: 25.7%
- 1/4 Kelly: 9.3%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.00
- Expected score: Milwaukee Brewers 2.53 - Los Angeles Dodgers 2.63

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.