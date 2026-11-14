"""Risk-of-ruin and bankroll estimates for a poker winrate model.

Pure stdlib. Uses the Brownian-motion approximation:
    RoR = exp(-2 * winrate * bankroll / variance)
with winrate and variance expressed per the same unit (e.g. per 100 hands).
"""
from __future__ import annotations

import math


def risk_of_ruin(winrate: float, std_dev: float, bankroll: float) -> float:
    """Probability of ever losing the whole bankroll."""
    if std_dev <= 0:
        raise ValueError("std_dev must be positive")
    if bankroll < 0:
        raise ValueError("bankroll must be non-negative")
    if winrate <= 0:
        return 1.0
    return math.exp(-2.0 * winrate * bankroll / (std_dev ** 2))


def required_bankroll(winrate: float, std_dev: float, target_ror: float) -> float:
    """Bankroll needed to keep risk of ruin at or below target_ror."""
    if winrate <= 0:
        raise ValueError("winrate must be positive")
    if std_dev <= 0:
        raise ValueError("std_dev must be positive")
    if not 0 < target_ror < 1:
        raise ValueError("target_ror must be in (0, 1)")
    return -math.log(target_ror) * std_dev ** 2 / (2.0 * winrate)


def _self_check() -> None:
    assert risk_of_ruin(0, 80, 1000) == 1.0
    r = risk_of_ruin(5, 80, 3000)
    assert 0 < r < 1
    b = required_bankroll(5, 80, r)
    assert abs(b - 3000) < 1e-6
    assert risk_of_ruin(5, 80, 0) == 1.0
    try:
        required_bankroll(5, 80, 1.5)
    except ValueError:
        pass
    else:
        raise AssertionError


if __name__ == "__main__":
    _self_check()
    print("ok")
