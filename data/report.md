# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-07T02:00:11.757952+00:00
- API requests remaining: 428
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Washington Nationals
- Game: Washington Nationals @ Los Angeles Dodgers
- Odds: 2.73
- AI probability: 61.0%
- EV: 66.6%
- 1/4 Kelly: 9.6%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Washington Nationals 3.53 - Los Angeles Dodgers 2.53

### 2. Atlanta Braves
- Game: Atlanta Braves @ Philadelphia Phillies
- Odds: 2.45
- AI probability: 49.2%
- EV: 20.6%
- 1/4 Kelly: 3.6%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.04
- Weather run factor: 1.007
- Temperature: 25.2 C
- Rain probability: 0%
- Wind: 8.7 km/h (353 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Atlanta Braves 3.77 - Philadelphia Phillies 3.70

### 3. Baltimore Orioles
- Game: Cleveland Guardians @ Baltimore Orioles
- Odds: 1.82
- AI probability: 64.8%
- EV: 17.9%
- 1/4 Kelly: 5.5%
- Lineup: 未発表
- Lineup quality: -0.02
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cleveland Guardians 3.36 - Baltimore Orioles 4.59

### 4. Athletics
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.74
- AI probability: 40.1%
- EV: 9.9%
- 1/4 Kelly: 1.4%
- Lineup: 未発表
- Lineup quality: -0.03
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.43 - Athletics 2.84

### 5. New York Mets
- Game: New York Mets @ Miami Marlins
- Odds: 2.02
- AI probability: 52.8%
- EV: 6.6%
- 1/4 Kelly: 1.6%
- Lineup: 未発表
- Lineup quality: +0.06
- Platoon proxy: +0.02
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.83 - Miami Marlins 2.61

## Run Line Buy Ranking

### 1. Washington Nationals +1.5
- Game: Washington Nationals @ Los Angeles Dodgers
- Odds: 1.81
- Cover probability: 85.5%
- EV: 54.7%
- 1/4 Kelly: 16.9%
- Lineup: 未発表
- Lineup quality: +0.00
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Washington Nationals 3.53 - Los Angeles Dodgers 2.53

### 2. Athletics +1.5
- Game: Toronto Blue Jays @ Athletics
- Odds: 2.04
- Cover probability: 64.7%
- EV: 32.0%
- 1/4 Kelly: 7.7%
- Lineup: 未発表
- Lineup quality: -0.03
- Platoon proxy: +0.00
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Toronto Blue Jays 3.43 - Athletics 2.84

### 3. Baltimore Orioles -1.5
- Game: Cleveland Guardians @ Baltimore Orioles
- Odds: 2.68
- Cover probability: 45.7%
- EV: 22.4%
- 1/4 Kelly: 3.3%
- Lineup: 未発表
- Lineup quality: -0.02
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Cleveland Guardians 3.36 - Baltimore Orioles 4.59

### 4. Atlanta Braves +1.5
- Game: Atlanta Braves @ Philadelphia Phillies
- Odds: 1.67
- Cover probability: 72.3%
- EV: 20.8%
- 1/4 Kelly: 7.8%
- Lineup: 未発表
- Lineup quality: +0.26
- Platoon proxy: +0.04
- Weather run factor: 1.007
- Temperature: 25.2 C
- Rain probability: 0%
- Wind: 8.7 km/h (353 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Atlanta Braves 3.77 - Philadelphia Phillies 3.70

### 5. New York Mets +1.5
- Game: New York Mets @ Miami Marlins
- Odds: 1.49
- Cover probability: 78.0%
- EV: 16.2%
- 1/4 Kelly: 8.3%
- Lineup: 未発表
- Lineup quality: +0.06
- Platoon proxy: +0.02
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.83 - Miami Marlins 2.61

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.