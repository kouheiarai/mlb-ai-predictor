# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-08-04T07:51:26.037246+00:00
- API requests remaining: 277
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Philadelphia Phillies
- Odds: 3.18
- AI probability: 42.1%
- EV: 34.0%
- 1/4 Kelly: 3.9%
- Lineup: 未発表
- Lineup quality: +0.58
- Platoon proxy: +0.02
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 2.67 - Philadelphia Phillies 3.00

### 2. Chicago Cubs
- Game: Los Angeles Dodgers @ Chicago Cubs
- Odds: 2.7
- AI probability: 49.6%
- EV: 34.0%
- 1/4 Kelly: 5.0%
- Lineup: 未発表
- Lineup quality: +0.31
- Platoon proxy: +0.15
- Weather run factor: 1.003
- Temperature: 23.4 C
- Rain probability: 5%
- Wind: 7.9 km/h (267 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Los Angeles Dodgers 2.83 - Chicago Cubs 2.94

### 3. Athletics
- Game: Athletics @ Cincinnati Reds
- Odds: 2.17
- AI probability: 58.9%
- EV: 27.8%
- 1/4 Kelly: 5.9%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.01
- Weather run factor: 1.020
- Temperature: 30.7 C
- Rain probability: 7%
- Wind: 11.0 km/h (251 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Athletics 4.57 - Cincinnati Reds 3.72

### 4. Minnesota Twins
- Game: Minnesota Twins @ Kansas City Royals
- Odds: 1.71
- AI probability: 73.1%
- EV: 25.1%
- 1/4 Kelly: 8.8%
- Lineup: 未発表
- Lineup quality: +0.18
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Minnesota Twins 4.86 - Kansas City Royals 2.88

### 5. New York Mets
- Game: New York Mets @ Cleveland Guardians
- Odds: 2.33
- AI probability: 52.5%
- EV: 22.4%
- 1/4 Kelly: 4.2%
- Lineup: 未発表
- Lineup quality: -0.31
- Platoon proxy: +0.11
- Weather run factor: 1.010
- Temperature: 25.4 C
- Rain probability: 8%
- Wind: 11.5 km/h (311 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.87 - Cleveland Guardians 2.59

### 6. Tampa Bay Rays
- Game: Tampa Bay Rays @ Colorado Rockies
- Odds: 1.7
- AI probability: 65.5%
- EV: 11.4%
- 1/4 Kelly: 4.1%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.05
- Weather run factor: 1.014
- Temperature: 26.7 C
- Rain probability: 1%
- Wind: 13.0 km/h (34 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Tampa Bay Rays 4.05 - Colorado Rockies 2.86

## Run Line Buy Ranking

### 1. Washington Nationals +1.5
- Game: Washington Nationals @ Philadelphia Phillies
- Odds: 2.04
- Cover probability: 69.9%
- EV: 42.6%
- 1/4 Kelly: 10.2%
- Lineup: 未発表
- Lineup quality: +0.58
- Platoon proxy: +0.02
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Washington Nationals 2.67 - Philadelphia Phillies 3.00

### 2. New York Mets +1.5
- Game: New York Mets @ Cleveland Guardians
- Odds: 1.59
- Cover probability: 78.9%
- EV: 25.5%
- 1/4 Kelly: 10.8%
- Lineup: 未発表
- Lineup quality: -0.31
- Platoon proxy: +0.11
- Weather run factor: 1.010
- Temperature: 25.4 C
- Rain probability: 8%
- Wind: 11.5 km/h (311 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.87 - Cleveland Guardians 2.59

### 3. Athletics +1.5
- Game: Athletics @ Cincinnati Reds
- Odds: 1.57
- Cover probability: 79.8%
- EV: 25.3%
- 1/4 Kelly: 11.1%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.01
- Weather run factor: 1.020
- Temperature: 30.7 C
- Rain probability: 7%
- Wind: 11.0 km/h (251 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Athletics 4.57 - Cincinnati Reds 3.72

### 4. Minnesota Twins -1.5
- Game: Minnesota Twins @ Kansas City Royals
- Odds: 2.13
- Cover probability: 56.4%
- EV: 20.1%
- 1/4 Kelly: 4.4%
- Lineup: 未発表
- Lineup quality: +0.18
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Minnesota Twins 4.86 - Kansas City Royals 2.88

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.