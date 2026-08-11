"""Regression tests for the run model's scoring scale.

Two bugs shipped a slate whose average total was 6.4 runs against a real-world
~9, which turned every totals pick into an Under with an impossible edge:

  1. team_metrics pulled *player* season splits from /v1/stats and stored the
     last player processed for each team, so runs_per_game read ~0.55 instead
     of ~4.5 and pinned offense_factor to its lower clamp.
  2. bullpen fatigue is a one-sided 0..1 score whose neutral point is 0.55, but
     expected_runs treated 0 as neutral, adding a flat ~6.6% to every game.

Both were invisible in any single prediction and only showed up in aggregate,
so these tests assert on aggregate behaviour.

    python -m unittest test_run_model -v
"""

from __future__ import annotations

import unittest

from bullpen import NEUTRAL_FATIGUE_SCORE
from predictor import LEAGUE_RUNS_PER_TEAM, expected_runs
from team_metrics import (
    MLB_TEAMS,
    PLAUSIBLE_LEAGUE_RUNS_PER_GAME,
    TeamMetricsError,
    validate_metrics,
)

NEUTRAL = {
    "opponent_starter_quality": 0.0,
    "opponent_bullpen_fatigue": NEUTRAL_FATIGUE_SCORE,
    "recent_form": 0.5,
    "lineup_adjustment": 0.0,
    "platoon_adjustment": 0.0,
    "park_factor": 1.0,
    "weather_run_factor": 1.0,
}


def league_average_team(**overrides):
    kwargs = dict(NEUTRAL)
    kwargs.update(overrides)
    return expected_runs(
        {"runs_per_game": LEAGUE_RUNS_PER_TEAM},
        {"team_pitching_era": 4.20},
        kwargs["opponent_starter_quality"],
        kwargs["opponent_bullpen_fatigue"],
        kwargs["recent_form"],
        kwargs["lineup_adjustment"],
        kwargs["platoon_adjustment"],
        kwargs["park_factor"],
        kwargs["weather_run_factor"],
        home=kwargs.get("home", False),
    )


def fake_metrics(runs_per_game: float, era: float = 4.20, teams: int = MLB_TEAMS):
    return {
        f"Team {i}": {"runs_per_game": runs_per_game, "team_pitching_era": era}
        for i in range(teams)
    }


class ScoringScaleTest(unittest.TestCase):
    def test_league_average_matchup_scores_about_league_average(self):
        """The whole model hangs off this: neutral inputs must return ~4.4."""
        lam = league_average_team()
        self.assertAlmostEqual(lam, LEAGUE_RUNS_PER_TEAM, delta=0.15)

    def test_neutral_game_total_matches_real_mlb(self):
        total = league_average_team(home=False) + league_average_team(home=True)
        # Real MLB games average roughly 9 runs; 6.4 was the shipped bug.
        self.assertGreater(total, 8.0)
        self.assertLess(total, 10.0)

    def test_offense_factor_is_not_pinned_to_its_clamp(self):
        """A league-average offense must not sit on the lower bound.

        This is what the player-splits bug did: every team looked like it
        scored 0.55 runs a game, so every offense clamped to 0.70.
        """
        average = league_average_team()
        weakest = expected_runs(
            {"runs_per_game": LEAGUE_RUNS_PER_TEAM * 0.75},
            {"team_pitching_era": 4.20},
            *[NEUTRAL[k] for k in (
                "opponent_starter_quality", "opponent_bullpen_fatigue",
                "recent_form", "lineup_adjustment", "platoon_adjustment",
                "park_factor", "weather_run_factor")],
            home=False,
        )
        self.assertLess(weakest, average, "a weak offense must score less than average")


class BullpenFatigueCenteringTest(unittest.TestCase):
    def test_ordinary_schedule_is_neutral(self):
        """A normally-rested bullpen must not inflate the opponent's runs."""
        neutral = league_average_team(opponent_bullpen_fatigue=NEUTRAL_FATIGUE_SCORE)
        self.assertAlmostEqual(neutral, LEAGUE_RUNS_PER_TEAM, delta=0.15)

    def test_tired_bullpen_concedes_more_than_rested_one(self):
        rested = league_average_team(opponent_bullpen_fatigue=0.0)
        tired = league_average_team(opponent_bullpen_fatigue=1.0)
        self.assertLess(rested, tired)

    def test_rested_bullpen_can_lower_the_total(self):
        """The old one-sided clamp made this impossible."""
        rested = league_average_team(opponent_bullpen_fatigue=0.0)
        neutral = league_average_team(opponent_bullpen_fatigue=NEUTRAL_FATIGUE_SCORE)
        self.assertLess(rested, neutral)


class DirectionalityTest(unittest.TestCase):
    def test_better_starter_suppresses_runs(self):
        self.assertLess(
            league_average_team(opponent_starter_quality=1.0),
            league_average_team(opponent_starter_quality=-1.0),
        )

    def test_hitters_park_raises_runs(self):
        self.assertGreater(
            league_average_team(park_factor=1.12),
            league_average_team(park_factor=0.96),
        )

    def test_home_team_scores_slightly_more(self):
        self.assertGreater(league_average_team(home=True), league_average_team(home=False))


class MetricsValidationTest(unittest.TestCase):
    def test_healthy_feed_passes(self):
        validate_metrics(fake_metrics(4.5))

    def test_player_level_feed_is_rejected(self):
        """The exact shape of the shipped bug: per-player runs per game."""
        with self.assertRaises(TeamMetricsError):
            validate_metrics(fake_metrics(0.55))

    def test_partial_feed_is_rejected(self):
        with self.assertRaises(TeamMetricsError):
            validate_metrics(fake_metrics(4.5, teams=12))

    def test_absurd_scoring_is_rejected(self):
        low, high = PLAUSIBLE_LEAGUE_RUNS_PER_GAME
        with self.assertRaises(TeamMetricsError):
            validate_metrics(fake_metrics(high + 1.0))

    def test_absurd_era_is_rejected(self):
        with self.assertRaises(TeamMetricsError):
            validate_metrics(fake_metrics(4.5, era=0.4))


class OutputGuardTest(unittest.TestCase):
    def test_validator_rejects_a_depressed_slate(self):
        from validate_outputs import check_scoring_is_plausible

        broken = {
            "all_predictions": {
                "moneyline": [
                    {"away_expected_runs": 2.4, "home_expected_runs": 2.7},
                    {"away_expected_runs": 3.1, "home_expected_runs": 2.9},
                ]
            }
        }
        with self.assertRaises(RuntimeError):
            check_scoring_is_plausible(broken)

    def test_validator_accepts_a_healthy_slate(self):
        from validate_outputs import check_scoring_is_plausible

        healthy = {
            "all_predictions": {
                "moneyline": [
                    {"away_expected_runs": 4.4, "home_expected_runs": 4.6},
                    {"away_expected_runs": 4.1, "home_expected_runs": 5.0},
                ]
            }
        }
        check_scoring_is_plausible(healthy)


if __name__ == "__main__":
    unittest.main()
