# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-07T22:25:29.534475+00:00
- API requests remaining: 422
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Dodgers
- Game: Cincinnati Reds @ Los Angeles Dodgers
- Odds: 1.59
- AI probability: 77.6%
- EV: 23.4%
- 1/4 Kelly: 9.9%
- Lineup: 未発表
- Lineup quality: +0.13
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.32 - Los Angeles Dodgers 4.53

### 2. St. Louis Cardinals
- Game: St. Louis Cardinals @ San Francisco Giants
- Odds: 2.19
- AI probability: 51.9%
- EV: 13.7%
- 1/4 Kelly: 2.9%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 3.35 - San Francisco Giants 3.13

### 3. Athletics
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.82
- AI probability: 40.0%
- EV: 12.8%
- 1/4 Kelly: 1.8%
- Lineup: 未発表
- Lineup quality: -0.03
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.43 - Athletics 2.84

## Run Line Buy Ranking

### 1. Los Angeles Dodgers -1.5
- Game: Cincinnati Reds @ Los Angeles Dodgers
- Odds: 2.28
- Cover probability: 60.0%
- EV: 36.9%
- 1/4 Kelly: 7.2%
- Lineup: 未発表
- Lineup quality: +0.13
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.32 - Los Angeles Dodgers 4.53

### 2. Athletics +1.5
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.07
- Cover probability: 64.7%
- EV: 33.9%
- 1/4 Kelly: 7.9%
- Lineup: 未発表
- Lineup quality: -0.03
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.43 - Athletics 2.84

### 3. St. Louis Cardinals +1.5
- Game: St. Louis Cardinals @ San Francisco Giants
- Odds: 1.55
- Cover probability: 75.9%
- EV: 17.7%
- 1/4 Kelly: 8.0%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 3.35 - San Francisco Giants 3.13

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.