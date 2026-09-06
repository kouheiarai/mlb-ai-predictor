# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-06T23:22:41.220877+00:00
- API requests remaining: 431
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Los Angeles Dodgers
- Odds: 2.71
- AI probability: 60.1%
- EV: 62.9%
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

### 2. Atlanta Braves
- Game: Atlanta Braves @ Philadelphia Phillies
- Odds: 2.45
- AI probability: 49.2%
- EV: 20.4%
- 1/4 Kelly: 3.5%
- Lineup: 未発表
- Lineup quality: +0.25
- Platoon proxy: +0.05
- Weather run factor: 1.004
- Temperature: 24.6 C
- Rain probability: 0%
- Wind: 6.6 km/h (331 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Atlanta Braves 3.80 - Philadelphia Phillies 3.73

## Run Line Buy Ranking

### 1. Washington Nationals +1.5
- Game: Washington Nationals @ Los Angeles Dodgers
- Odds: 1.79
- Cover probability: 84.5%
- EV: 51.3%
- 1/4 Kelly: 16.2%
- Lineup: 未発表
- Lineup quality: +0.47
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Washington Nationals 3.58 - Los Angeles Dodgers 2.65

### 2. Atlanta Braves +1.5
- Game: Atlanta Braves @ Philadelphia Phillies
- Odds: 1.67
- Cover probability: 72.2%
- EV: 20.5%
- 1/4 Kelly: 7.7%
- Lineup: 未発表
- Lineup quality: +0.25
- Platoon proxy: +0.05
- Weather run factor: 1.004
- Temperature: 24.6 C
- Rain probability: 0%
- Wind: 6.6 km/h (331 deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Atlanta Braves 3.80 - Philadelphia Phillies 3.73

### 3. Athletics +1.5
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.03
- Cover probability: 59.2%
- EV: 20.1%
- 1/4 Kelly: 4.9%
- Lineup: 未発表
- Lineup quality: -0.06
- Platoon proxy: +0.06
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.60
- Expected score: Toronto Blue Jays 3.77 - Athletics 2.83

### 4. New York Mets +1.5
- Game: New York Mets @ Miami Marlins
- Odds: 1.49
- Cover probability: 76.2%
- EV: 13.6%
- 1/4 Kelly: 6.9%
- Lineup: 未発表
- Lineup quality: +0.11
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: New York Mets 2.79 - Miami Marlins 2.70

### 5. Cleveland Guardians +1.5
- Game: Cleveland Guardians @ Baltimore Orioles
- Odds: 1.52
- Cover probability: 72.7%
- EV: 10.5%
- 1/4 Kelly: 5.1%
- Lineup: 未発表
- Lineup quality: +0.02
- Platoon proxy: +0.17
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 1.00
- Expected score: Cleveland Guardians 3.45 - Baltimore Orioles 3.42

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.