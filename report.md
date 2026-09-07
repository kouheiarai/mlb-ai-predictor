# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-07T19:29:05.225087+00:00
- API requests remaining: 425
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ San Diego Padres
- Odds: 2.75
- AI probability: 47.2%
- EV: 29.8%
- 1/4 Kelly: 4.3%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.05
- Weather run factor: 1.020
- Temperature: 28.7 C
- Rain probability: 15%
- Wind: 14.5 km/h (256 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Washington Nationals 2.80 - San Diego Padres 2.83

### 2. Los Angeles Dodgers
- Game: Cincinnati Reds @ Los Angeles Dodgers
- Odds: 1.58
- AI probability: 77.6%
- EV: 22.7%
- 1/4 Kelly: 9.8%
- Lineup: 未発表
- Lineup quality: +0.13
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.32 - Los Angeles Dodgers 4.53

### 3. St. Louis Cardinals
- Game: St. Louis Cardinals @ San Francisco Giants
- Odds: 2.16
- AI probability: 52.2%
- EV: 12.7%
- 1/4 Kelly: 2.7%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.014
- Temperature: 29.6 C
- Rain probability: 0%
- Wind: 7.4 km/h (346 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 3.40 - San Francisco Giants 3.17

### 4. Athletics
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.79
- AI probability: 40.0%
- EV: 11.7%
- 1/4 Kelly: 1.6%
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
- Odds: 2.27
- Cover probability: 60.0%
- EV: 36.3%
- 1/4 Kelly: 7.1%
- Lineup: 未発表
- Lineup quality: +0.13
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cincinnati Reds 2.32 - Los Angeles Dodgers 4.53

### 2. Washington Nationals +1.5
- Game: Washington Nationals @ San Diego Padres
- Odds: 1.82
- Cover probability: 74.3%
- EV: 35.3%
- 1/4 Kelly: 10.8%
- Lineup: 未発表
- Lineup quality: +0.28
- Platoon proxy: +0.05
- Weather run factor: 1.020
- Temperature: 28.7 C
- Rain probability: 15%
- Wind: 14.5 km/h (256 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Washington Nationals 2.80 - San Diego Padres 2.83

### 3. Athletics +1.5
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.06
- Cover probability: 64.7%
- EV: 33.2%
- 1/4 Kelly: 7.8%
- Lineup: 未発表
- Lineup quality: -0.03
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.43 - Athletics 2.84

### 4. St. Louis Cardinals +1.5
- Game: St. Louis Cardinals @ San Francisco Giants
- Odds: 1.53
- Cover probability: 75.7%
- EV: 15.9%
- 1/4 Kelly: 7.5%
- Lineup: 未発表
- Lineup quality: +0.10
- Platoon proxy: +0.05
- Weather run factor: 1.014
- Temperature: 29.6 C
- Rain probability: 0%
- Wind: 7.4 km/h (346 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 3.40 - San Francisco Giants 3.17

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.