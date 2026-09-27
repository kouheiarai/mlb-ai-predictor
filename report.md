# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-27T02:36:16.794523+00:00
- API requests remaining: 239
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Angels
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 2.58
- AI probability: 67.0%
- EV: 72.9%
- 1/4 Kelly: 11.5%
- Lineup: 未発表
- Lineup quality: -0.17
- Platoon proxy: -0.05
- Weather run factor: 0.992
- Temperature: 15.2 C
- Rain probability: 0%
- Wind: 13.9 km/h (10 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Los Angeles Angels 4.26 - Seattle Mariners 2.69

### 2. Tampa Bay Rays
- Game: Tampa Bay Rays @ Philadelphia Phillies
- Odds: 2.14
- AI probability: 52.7%
- EV: 12.8%
- 1/4 Kelly: 2.8%
- Lineup: 未発表
- Lineup quality: +0.40
- Platoon proxy: -0.00
- Weather run factor: 1.009
- Temperature: 17.2 C
- Rain probability: 35%
- Wind: 27.0 km/h (31 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Tampa Bay Rays 3.68 - Philadelphia Phillies 3.40

### 3. Atlanta Braves
- Game: Atlanta Braves @ Miami Marlins
- Odds: 1.93
- AI probability: 56.1%
- EV: 8.2%
- 1/4 Kelly: 2.2%
- Lineup: 未発表
- Lineup quality: +0.20
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.65
- Expected score: Atlanta Braves 3.24 - Miami Marlins 2.79

### 4. Washington Nationals
- Game: New York Mets @ Washington Nationals
- Odds: 1.96
- AI probability: 54.0%
- EV: 5.9%
- 1/4 Kelly: 1.5%
- Lineup: 未発表
- Lineup quality: +0.32
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.50 - Washington Nationals 2.77

## Run Line Buy Ranking

### 1. Los Angeles Angels +1.5
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 1.7
- Cover probability: 88.4%
- EV: 50.3%
- 1/4 Kelly: 18.0%
- Lineup: 未発表
- Lineup quality: -0.17
- Platoon proxy: -0.05
- Weather run factor: 0.992
- Temperature: 15.2 C
- Rain probability: 0%
- Wind: 13.9 km/h (10 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Los Angeles Angels 4.26 - Seattle Mariners 2.69

### 2. Washington Nationals +1.5
- Game: New York Mets @ Washington Nationals
- Odds: 1.56
- Cover probability: 79.0%
- EV: 23.2%
- 1/4 Kelly: 10.4%
- Lineup: 未発表
- Lineup quality: +0.32
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.50 - Washington Nationals 2.77

### 3. Detroit Tigers +1.5
- Game: Pittsburgh Pirates @ Detroit Tigers
- Odds: 1.68
- Cover probability: 70.2%
- EV: 18.0%
- 1/4 Kelly: 6.6%
- Lineup: 未発表
- Lineup quality: +0.47
- Platoon proxy: +0.00
- Weather run factor: 1.011
- Temperature: 24.1 C
- Rain probability: 0%
- Wind: 14.6 km/h (10 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Pittsburgh Pirates 3.31 - Detroit Tigers 3.10

### 4. Tampa Bay Rays +1.5
- Game: Tampa Bay Rays @ Philadelphia Phillies
- Odds: 1.51
- Cover probability: 75.8%
- EV: 14.5%
- 1/4 Kelly: 7.1%
- Lineup: 未発表
- Lineup quality: +0.40
- Platoon proxy: -0.00
- Weather run factor: 1.009
- Temperature: 17.2 C
- Rain probability: 35%
- Wind: 27.0 km/h (31 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Tampa Bay Rays 3.68 - Philadelphia Phillies 3.40

### 5. Miami Marlins +1.5
- Game: Atlanta Braves @ Miami Marlins
- Odds: 1.59
- Cover probability: 67.3%
- EV: 7.0%
- 1/4 Kelly: 2.9%
- Lineup: 未発表
- Lineup quality: +0.03
- Platoon proxy: -0.09
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Atlanta Braves 3.24 - Miami Marlins 2.79

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.