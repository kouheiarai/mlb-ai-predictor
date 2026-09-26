# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-09-26T02:38:56.131984+00:00
- API requests remaining: 248
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

### 1. Los Angeles Angels
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 2.72
- AI probability: 65.3%
- EV: 77.5%
- 1/4 Kelly: 11.3%
- Lineup: 未発表
- Lineup quality: -0.22
- Platoon proxy: -0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Los Angeles Angels 4.25 - Seattle Mariners 2.80

### 2. Toronto Blue Jays
- Game: Cincinnati Reds @ Toronto Blue Jays
- Odds: 1.63
- AI probability: 76.8%
- EV: 25.2%
- 1/4 Kelly: 10.0%
- Lineup: 未発表
- Lineup quality: -0.14
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Cincinnati Reds 3.02 - Toronto Blue Jays 5.43

### 3. Washington Nationals
- Game: New York Mets @ Washington Nationals
- Odds: 2.16
- AI probability: 55.1%
- EV: 19.1%
- 1/4 Kelly: 4.1%
- Lineup: 未発表
- Lineup quality: +0.33
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.45 - Washington Nationals 2.84

### 4. San Francisco Giants
- Game: Los Angeles Dodgers @ San Francisco Giants
- Odds: 3.73
- AI probability: 31.2%
- EV: 16.4%
- 1/4 Kelly: 1.5%
- Lineup: 未発表
- Lineup quality: -0.31
- Platoon proxy: +0.00
- Weather run factor: 1.007
- Temperature: 18.5 C
- Rain probability: 5%
- Wind: 21.6 km/h (285 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Los Angeles Dodgers 3.45 - San Francisco Giants 2.32

### 5. Cleveland Guardians
- Game: Cleveland Guardians @ Kansas City Royals
- Odds: 1.79
- AI probability: 61.3%
- EV: 9.7%
- 1/4 Kelly: 3.1%
- Lineup: 未発表
- Lineup quality: +0.01
- Platoon proxy: +0.02
- Weather run factor: 1.004
- Temperature: 24.3 C
- Rain probability: 7%
- Wind: 7.6 km/h (82 deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Cleveland Guardians 4.24 - Kansas City Royals 3.35

### 6. Milwaukee Brewers
- Game: St. Louis Cardinals @ Milwaukee Brewers
- Odds: 1.56
- AI probability: 68.7%
- EV: 7.1%
- 1/4 Kelly: 3.2%
- Lineup: 未発表
- Lineup quality: +0.33
- Platoon proxy: +0.04
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: St. Louis Cardinals 2.27 - Milwaukee Brewers 3.51

## Run Line Buy Ranking

### 1. Los Angeles Angels +1.5
- Game: Los Angeles Angels @ Seattle Mariners
- Odds: 1.78
- Cover probability: 87.4%
- EV: 55.5%
- 1/4 Kelly: 17.8%
- Lineup: 未発表
- Lineup quality: -0.22
- Platoon proxy: -0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: Los Angeles Angels 4.25 - Seattle Mariners 2.80

### 2. Toronto Blue Jays -1.5
- Game: Cincinnati Reds @ Toronto Blue Jays
- Odds: 2.35
- Cover probability: 62.0%
- EV: 45.7%
- 1/4 Kelly: 8.5%
- Lineup: 未発表
- Lineup quality: -0.14
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.75
- Expected score: Cincinnati Reds 3.02 - Toronto Blue Jays 5.43

### 3. San Francisco Giants +1.5
- Game: Los Angeles Dodgers @ San Francisco Giants
- Odds: 2.47
- Cover probability: 56.9%
- EV: 40.5%
- 1/4 Kelly: 6.9%
- Lineup: 未発表
- Lineup quality: -0.31
- Platoon proxy: +0.00
- Weather run factor: 1.007
- Temperature: 18.5 C
- Rain probability: 5%
- Wind: 21.6 km/h (285 deg)
- Bullpen fatigue proxy: 0.20
- Expected score: Los Angeles Dodgers 3.45 - San Francisco Giants 2.32

### 4. Washington Nationals +1.5
- Game: New York Mets @ Washington Nationals
- Odds: 1.69
- Cover probability: 80.4%
- EV: 35.8%
- 1/4 Kelly: 13.0%
- Lineup: 未発表
- Lineup quality: +0.33
- Platoon proxy: +0.05
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.45
- Expected score: New York Mets 2.45 - Washington Nationals 2.84

### 5. Colorado Rockies +1.5
- Game: Colorado Rockies @ Chicago White Sox
- Odds: 1.9
- Cover probability: 55.9%
- EV: 6.2%
- 1/4 Kelly: 1.7%
- Lineup: 未発表
- Lineup quality: +0.50
- Platoon proxy: +0.07
- Weather run factor: 1.000
- Temperature: None C
- Rain probability: None%
- Wind: None km/h (None deg)
- Bullpen fatigue proxy: 0.55
- Expected score: Colorado Rockies 2.69 - Chicago White Sox 3.86

## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.