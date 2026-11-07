"""Independent Chip Model (Malmuth-Harville) tournament equity.

Pure-Python, no dependencies. Converts chip stacks into $-equity given a
payout structure, so juniors can see why chips lose value near the bubble.
"""
from __future__ import annotations

from functools import lru_cache
from typing import Sequence


def icm_equity(stacks: Sequence[float], payouts: Sequence[float]) -> list[float]:
    """Return each player's expected payout under Malmuth-Harville ICM."""
    if not stacks:
        return []
    if any(s < 0 for s in stacks):
        raise ValueError("stacks must be non-negative")
    if any(p < 0 for p in payouts):
        raise ValueError("payouts must be non-negative")
    total = float(sum(stacks))
    if total <= 0:
        raise ValueError("total chips must be positive")
    n = len(stacks)
    pays = tuple(float(p) for p in payouts[:n])
    st = tuple(float(s) for s in stacks)

    @lru_cache(maxsize=None)
    def finish_probs(remaining: frozenset, place: int) -> tuple:
        # Returns per-player expected value from `place` onward, given
        # `remaining` players still unplaced.
        ev = [0.0] * n
        if place >= len(pays) or not remaining:
            return tuple(ev)
        rem_total = sum(st[i] for i in remaining)
        if rem_total <= 0:
            return tuple(ev)
        for i in remaining:
            p = st[i] / rem_total
            if p == 0:
                continue
            ev[i] += p * pays[place]
            sub = finish_probs(remaining - {i}, place + 1)
            for j in range(n):
                ev[j] += p * sub[j]
        return tuple(ev)

    return list(finish_probs(frozenset(range(n)), 0))


def bubble_factor(stacks: Sequence[float], payouts: Sequence[float],
                  hero: int, villain: int) -> float:
    """$-loss of losing an all-in to `villain` divided by $-gain of winning it."""
    eq0 = icm_equity(stacks, payouts)[hero]
    risk = min(stacks[hero], stacks[villain])
    win = list(stacks); win[hero] += risk; win[villain] -= risk
    lose = list(stacks); lose[hero] -= risk; lose[villain] += risk
    gain = icm_equity(win, payouts)[hero] - eq0
    loss = eq0 - icm_equity(lose, payouts)[hero]
    if gain <= 0:
        raise ValueError("no ICM gain available for hero in this spot")
    return loss / gain


def _self_check() -> None:
    eq = icm_equity([5000, 3000, 2000], [50, 30, 20])
    assert abs(sum(eq) - 100) < 1e-9, eq
    assert eq[0] > eq[1] > eq[2]
    # Equal stacks split equally.
    eq2 = icm_equity([1000] * 4, [60, 40])
    assert all(abs(e - 25) < 1e-9 for e in eq2), eq2
    # Winner-take-all equals chip share.
    eq3 = icm_equity([700, 300], [100])
    assert abs(eq3[0] - 70) < 1e-9 and abs(eq3[1] - 30) < 1e-9
    # Busted player gets nothing beyond places that must be paid out.
    eq4 = icm_equity([500, 500, 0], [70, 30])
    assert abs(eq4[2]) < 1e-9 and abs(eq4[0] - 50) < 1e-9
    # Bubble factor > 1 with a pay jump.
    bf = bubble_factor([4000, 3000, 2000, 1000], [50, 30, 20], 1, 0)
    assert bf > 1.0, bf
    print("icm_equity self-check OK", [round(x, 3) for x in eq], round(bf, 3))


if __name__ == "__main__":
    _self_check()
