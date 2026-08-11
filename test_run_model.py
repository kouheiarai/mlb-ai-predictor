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
from predictor import (
    LEAGUE_RUNS_PER_TEAM,
    RUN_DISPERSION,
    draw_runs,
    expected_runs,
    expected_value,
    quarter_kelly,
    simulate_total_probability,
)
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


class RunDistributionTest(unittest.TestCase):
    """Runs are over-dispersed; a Poisson draw made both tails far too thin."""

    @classmethod
    def setUpClass(cls):
        import numpy as np

        rng = np.random.default_rng(11)
        cls.np = np
        cls.away = draw_runs(rng, 4.487, 300_000)
        cls.home = draw_runs(rng, 4.487, 300_000)
        cls.totals = cls.away + cls.home

    def test_mean_is_preserved(self):
        self.assertAlmostEqual(float(self.away.mean()), 4.487, delta=0.05)

    def test_variance_matches_the_measured_dispersion(self):
        ratio = float(self.away.var() / self.away.mean())
        self.assertAlmostEqual(ratio, RUN_DISPERSION, delta=0.1)

    def test_game_totals_keep_the_same_dispersion(self):
        """Sharing p keeps the sum negative binomial rather than smearing it."""
        ratio = float(self.totals.var() / self.totals.mean())
        self.assertAlmostEqual(ratio, RUN_DISPERSION, delta=0.1)

    def test_low_scoring_games_are_not_vanishingly_rare(self):
        """A 3-run game happens ~6.8% of the time; Poisson claimed 1.5%."""
        share = float((self.totals == 3).mean())
        self.assertGreater(share, 0.035)

    def test_blowouts_are_not_vanishingly_rare(self):
        """20-run games are ~0.7% in reality and 0.06% under Poisson."""
        share = float((self.totals >= 20).mean())
        self.assertGreater(share, 0.01)


class PushAccountingTest(unittest.TestCase):
    """A whole-number total returns the stake; that is not a loss."""

    def test_push_raises_expected_value(self):
        without = expected_value(0.45, 2.0)
        with_push = expected_value(0.45, 2.0, 0.13)
        self.assertAlmostEqual(with_push - without, 0.13, places=9)

    def test_expected_value_matches_the_payout_definition(self):
        win, push, odds = 0.45, 0.13, 2.0
        lose = 1.0 - win - push
        manual = win * (odds - 1.0) + push * 0.0 - lose
        self.assertAlmostEqual(expected_value(win, odds, push), manual, places=9)

    def test_no_push_is_unchanged(self):
        self.assertAlmostEqual(expected_value(0.55, 1.9), expected_value(0.55, 1.9, 0.0))

    def test_kelly_conditions_on_the_bet_resolving(self):
        """Ignoring the push understates the stake, because it inflates 'lose'."""
        naive = quarter_kelly(0.45, 2.2)
        aware = quarter_kelly(0.45, 2.2, 0.13)
        self.assertGreater(aware, naive)

    def test_kelly_never_goes_negative(self):
        self.assertEqual(quarter_kelly(0.10, 1.5, 0.05), 0.0)

    def test_total_probabilities_form_a_distribution(self):
        over, under, push = simulate_total_probability("t", 4.5, 4.5, 8.0)
        self.assertAlmostEqual(over + under + push, 1.0, places=6)
        self.assertGreater(push, 0.05, "a whole-number line must be able to push")

    def test_half_line_cannot_push(self):
        over, under, push = simulate_total_probability("t", 4.5, 4.5, 8.5)
        self.assertAlmostEqual(push, 0.0, places=6)
        self.assertAlmostEqual(over + under, 1.0, places=6)


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
