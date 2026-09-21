# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-21T20:13:35.881925+00:00
- API requests remaining: 290
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Detroit Tigers
- Odds: 2.17
- AI probability: 72.0%
- EV: 56.2%
- 1/4 Kelly: 12.0%
- Lineup: 未発表
- Lineup quality: +0.08
- Platoon proxy: -0.05
- Weather run factor: 1.008
- Temperature: 17.8 C
- Rain probability: 31%
- Wind: 24.0 km/h (85 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 4.75 - Detroit Tigers 2.73

### 2. Baltimore Orioles
- Game: Toronto Blue Jays @ Baltimore Orioles
- Odds: 1.97
- AI probability: 63.8%
- EV: 25.7%
- 1/4 Kelly: 6.6%
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
- Odds: 1.56
- Cover probability: 90.7%
- EV: 41.5%
- 1/4 Kelly: 18.5%
- Lineup: 未発表
- Lineup quality: +0.08
- Platoon proxy: -0.05
- Weather run factor: 1.008
- Temperature: 17.8 C
- Rain probability: 31%
- Wind: 24.0 km/h (85 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 4.75 - Detroit Tigers 2.73

### 2. Baltimore Orioles -1.5
- Game: Toronto Blue Jays @ Baltimore Orioles
- Odds: 3.04
- Cover probability: 44.0%
- EV: 33.7%
- 1/4 Kelly: 4.1%
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
- Odds: 1.64
- Cover probability: 68.2%
- EV: 11.9%
- 1/4 Kelly: 4.6%
- Lineup: 未発表
- Lineup quality: -0.13
- Platoon proxy: +0.00
- Weather run factor: 1.001
- Temperature: 22.5 C
- Rain probability: 0%
- Wind: 8.1 km/h (328 deg)
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