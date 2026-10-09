# MLB AI Predictor Ver.26.0 Prediction Report

- Updated: 2026-10-09T01:32:31.565232+00:00
- API requests remaining: 428
- Simulation: 100,000 Poisson score simulations per game

## Moneyline Buy Ranking

No EV 5%+ Moneyline bets.
## Run Line Buy Ranking

No EV 5%+ Run Line bets.
## Model Notes

- Platoon proxy uses each hitter's batting side versus the probable starter's throwing hand.
- It is a conservative proxy, not a true split-stat model.
- Moneyline and Run Line probabilities come from 100,000 simulated scores per game.
- BUY threshold is EV 5% or higher.
- Outdoor-game weather is fetched from Open-Meteo at the scheduled game hour.
- Temperature, rain probability and wind speed affect expected runs conservatively.
- Wind direction is reported, but a park-axis model is not yet used; retractable-roof games are treated as neutral.
- BUY threshold is EV 5% or higher.