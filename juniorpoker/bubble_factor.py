"""Bubble factor: how much more a chip lost costs than a chip won (ICM-based).

bubble_factor = (equity_now - equity_if_lose) / (equity_if_win - equity_now)
Required call equity = BF / (BF + 1) for a heads-up all-in decision.
Pure stdlib, offline.
"""
from __future__ import annotations


def bubble_factor(equity_now: float, equity_win: float, equity_lose: float) -> float:
    """Return the bubble factor given $ (or prize-share) equities."""
    gain = equity_win - equity_now
    loss = equity_now - equity_lose
    if gain <= 0:
        raise ValueError("equity_win must exceed equity_now")
    if loss < 0:
        raise ValueError("equity_lose must not exceed equity_now")
    return loss / gain


def required_equity(bf: float) -> float:
    """Minimum hand equity needed to call all-in at a given bubble factor."""
    if bf < 0:
        raise ValueError("bf must be >= 0")
    return bf / (bf + 1.0)


def _selftest() -> None:
    bf = bubble_factor(10.0, 14.0, 6.0)
    assert abs(bf - 1.0) < 1e-12
    assert abs(required_equity(bf) - 0.5) < 1e-12
    bf2 = bubble_factor(10.0, 12.0, 4.0)
    assert abs(bf2 - 3.0) < 1e-12
    assert abs(required_equity(bf2) - 0.75) < 1e-12
    for bad in ((10, 10, 5), (10, 12, 11)):
        try:
            bubble_factor(*bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("bubble_factor selftest ok")


if __name__ == "__main__":
    _selftest()
