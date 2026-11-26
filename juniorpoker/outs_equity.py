"""Outs counting and rule-of-2-and-4 equity estimates (stdlib only).

Exact draw equity from the number of outs versus the common mental-math
approximation, so tools can report the approximation error.
"""
from __future__ import annotations

from math import comb


def exact_hit_prob(outs: int, unseen: int, cards_to_come: int) -> float:
    """P(at least one out arrives) drawing cards_to_come from unseen cards."""
    if not 0 <= outs <= unseen:
        raise ValueError("outs must be within 0..unseen")
    if not 0 <= cards_to_come <= unseen:
        raise ValueError("cards_to_come must be within 0..unseen")
    miss = comb(unseen - outs, cards_to_come) / comb(unseen, cards_to_come)
    return 1.0 - miss


def rule_of_2_and_4(outs: int, cards_to_come: int) -> float:
    """Approximation: 4% per out with two cards to come, 2% with one."""
    if cards_to_come not in (1, 2):
        raise ValueError("cards_to_come must be 1 or 2")
    return min(1.0, outs * (0.02 if cards_to_come == 1 else 0.04))


def flop_unseen() -> int:
    return 47


def turn_unseen() -> int:
    return 46


def approx_error(outs: int, cards_to_come: int) -> float:
    """Approximation minus exact, hold'em unseen count for the street."""
    unseen = flop_unseen() if cards_to_come == 2 else turn_unseen()
    return rule_of_2_and_4(outs, cards_to_come) - exact_hit_prob(outs, unseen, cards_to_come)


def _selftest() -> None:
    assert abs(exact_hit_prob(9, 47, 2) - 0.3497) < 1e-3  # flush draw on flop
    assert abs(exact_hit_prob(9, 46, 1) - 9 / 46) < 1e-12
    assert exact_hit_prob(0, 47, 2) == 0.0
    assert exact_hit_prob(47, 47, 1) == 1.0
    assert abs(rule_of_2_and_4(8, 2) - 0.32) < 1e-12
    assert abs(approx_error(8, 2)) < 0.02
    for bad in ((-1, 47, 1), (48, 47, 1), (1, 47, 48)):
        try:
            exact_hit_prob(*bad)
        except ValueError:
            continue
        raise AssertionError(bad)
    print("outs_equity selftest ok")


if __name__ == "__main__":
    _selftest()
