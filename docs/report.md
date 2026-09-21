# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-21T02:28:44.135331+00:00
- API requests remaining: 293
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Detroit Tigers
- Odds: 2.33
- AI probability: 71.5%
- EV: 66.6%
- 1/4 Kelly: 12.5%
- Lineup: 未発表
- Lineup quality: +0.08
- Platoon proxy: -0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 4.72 - Detroit Tigers 2.71

### 2. Baltimore Orioles
- Game: Toronto Blue Jays @ Baltimore Orioles
- Odds: 1.94
- AI probability: 63.9%
- EV: 23.9%
- 1/4 Kelly: 6.4%
- Lineup: 未発表
- Lineup quality: -0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.15 - Baltimore Orioles 4.28

## Run Line Buy Ranking

### 1. Washington Nationals +1.5
- Game: Washington Nationals @ Detroit Tigers
- Odds: 1.62
- Cover probability: 90.8%
- EV: 47.0%
- 1/4 Kelly: 19.0%
- Lineup: 未発表
- Lineup quality: +0.08
- Platoon proxy: -0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 4.72 - Detroit Tigers 2.71

### 2. Baltimore Orioles +1.5
- Game: Toronto Blue Jays @ Baltimore Orioles
- Odds: 1.55
- Cover probability: 83.8%
- EV: 30.0%
- 1/4 Kelly: 13.6%
- Lineup: 未発表
- Lineup quality: -0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.15 - Baltimore Orioles 4.28

### 3. San Francisco Giants +1.5
- Game: Minnesota Twins @ San Francisco Giants
- Odds: 1.6
- Cover probability: 68.1%
- EV: 9.0%
- 1/4 Kelly: 3.7%
- Lineup: 未発表
- Lineup quality: -0.13
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Minnesota Twins 3.30 - San Francisco Giants 2.93

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.