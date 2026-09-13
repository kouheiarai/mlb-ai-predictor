# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-13T23:46:42.004278+00:00
- API requests remaining: 362
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Atlanta Braves
- Game: Atlanta Braves @ Chicago Cubs
- Odds: 2.19
- AI probability: 62.3%
- EV: 36.5%
- 1/4 Kelly: 7.7%
- Lineup: 未発表
- Lineup quality: +0.32
- Platoon proxy: +0.07
- Weather run factor: 1.011
- Temperature: 26.3 C
- Rain probability: 32%
- Wind: 10.7 km/h (340 deg)
- Bullpen fatigue proxy: 0.70
- Expected score: Atlanta Braves 3.75 - Chicago Cubs 2.71

### 2. Los Angeles Dodgers
- Game: Los Angeles Dodgers @ Cincinnati Reds
- Odds: 1.5
- AI probability: 81.8%
- EV: 22.7%
- 1/4 Kelly: 11.3%
- Lineup: 未発表
- Lineup quality: +0.05
- Platoon proxy: +0.01
- Weather run factor: 1.022
- Temperature: 33.0 C
- Rain probability: 0%
- Wind: 7.6 km/h (199 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Los Angeles Dodgers 5.14 - Cincinnati Reds 2.35

## Run Line Buy Ranking

### 1. Los Angeles Dodgers -1.5
- Game: Los Angeles Dodgers @ Cincinnati Reds
- Odds: 1.85
- Cover probability: 68.0%
- EV: 25.7%
- 1/4 Kelly: 7.6%
- Lineup: 未発表
- Lineup quality: +0.05
- Platoon proxy: +0.01
- Weather run factor: 1.022
- Temperature: 33.0 C
- Rain probability: 0%
- Wind: 7.6 km/h (199 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Los Angeles Dodgers 5.14 - Cincinnati Reds 2.35

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.