"""Kelly criterion bet sizing for even-money-style bets with a payout ratio (stdlib only)."""
from __future__ import annotations

import math


def kelly_fraction(p_win: float, b: float) -> float:
    """Optimal bankroll fraction for win prob p_win paying b-to-1; 0 if no edge."""
    if not 0.0 <= p_win <= 1.0 or b <= 0:
        raise ValueError("need 0<=p_win<=1 and b>0")
    return max(0.0, (p_win * (b + 1) - 1) / b)


def fractional_kelly(p_win: float, b: float, scale: float = 0.5) -> float:
    if not 0.0 < scale <= 1.0:
        raise ValueError("scale must be in (0,1]")
    return kelly_fraction(p_win, b) * scale


def growth_rate(p_win: float, b: float, f: float) -> float:
    """Expected log growth per bet when staking fraction f of bankroll."""
    if not 0.0 <= f < 1.0:
        raise ValueError("f must be in [0,1)")
    return p_win * math.log(1 + b * f) + (1 - p_win) * math.log(1 - f)


def _self_check() -> None:
    assert abs(kelly_fraction(0.6, 1.0) - 0.2) < 1e-12
    assert kelly_fraction(0.4, 1.0) == 0.0
    assert abs(fractional_kelly(0.6, 1.0, 0.5) - 0.1) < 1e-12
    p, b = 0.55, 1.5
    fs = kelly_fraction(p, b)
    g = growth_rate(p, b, fs)
    for d in (-0.05, -0.01, 0.01, 0.05):
        assert growth_rate(p, b, fs + d) < g
    assert growth_rate(p, b, 0.0) == 0.0
    print("self-check ok")


if __name__ == "__main__":
    _self_check()
