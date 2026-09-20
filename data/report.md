# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-20T22:04:30.271293+00:00
- API requests remaining: 296
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

No EV 5%+ Moneyline bets.
## Run Line Buy Ranking

### 1. San Francisco Giants +1.5
- Game: Minnesota Twins @ San Francisco Giants
- Odds: 1.6
- Cover probability: 73.8%
- EV: 18.0%
- 1/4 Kelly: 7.5%
- Lineup: 未発表
- Lineup quality: -0.25
- Platoon proxy: +0.01
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Minnesota Twins 2.99 - San Francisco Giants 2.98

### 2. Baltimore Orioles +1.5
- Game: Milwaukee Brewers @ Baltimore Orioles
- Odds: 2.04
- Cover probability: 53.7%
- EV: 9.6%
- 1/4 Kelly: 2.3%
- Lineup: 発表済み
- Lineup quality: -0.24
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Milwaukee Brewers 3.60 - Baltimore Orioles 2.28

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.