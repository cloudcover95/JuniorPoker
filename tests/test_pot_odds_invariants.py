"""Invariant tests for juniorpoker.pot_odds (additive, stdlib only)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from juniorpoker import pot_odds as po  # noqa: E402


def test_pot_odds_half_pot():
    assert abs(po.pot_odds(100, 50) - 3.0) < 1e-12


def test_mdf_plus_bluff_ratio():
    for pot, bet in [(100, 50), (100, 100), (30, 90)]:
        assert 0 < po.mdf(pot, bet) <= 1
        assert 0 < po.bluff_break_even(pot, bet) < 1


def test_call_ev_sign_matches_should_call():
    for eq in (0.1, 0.25, 0.4, 0.6, 0.9):
        ev = po.call_ev(eq, 100, 50)
        assert (ev >= -1e-12) == po.should_call(eq, 100, 50)


def test_break_even_is_zero_ev():
    be = po.break_even_equity(100, 50)
    assert abs(po.call_ev(be, 100, 50)) < 1e-9


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("test_pot_odds_invariants ok")
