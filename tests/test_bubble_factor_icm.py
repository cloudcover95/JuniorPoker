"""Cross-check juniorpoker.bubble_factor against exact Malmuth-Harville ICM (stdlib only)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from juniorpoker.bubble_factor import bubble_factor, required_equity  # noqa: E402


def icm(stacks, payouts):
    n = len(stacks)
    eq = [0.0] * n

    def rec(alive, rem, p, place):
        if place >= len(payouts) or not alive:
            return
        for i in alive:
            pi = p * stacks[i] / rem
            eq[i] += pi * payouts[place]
            rec([j for j in alive if j != i], rem - stacks[i], pi, place + 1)

    rec(list(range(n)), float(sum(stacks)), 1.0, 0)
    return eq


def shove_equities(stacks, payouts, hero, villain):
    risk = min(stacks[hero], stacks[villain])
    win, lose = list(stacks), list(stacks)
    win[hero] += risk
    win[villain] -= risk
    lose[hero] -= risk
    lose[villain] += risk
    return icm(stacks, payouts)[hero], icm(win, payouts)[hero], icm(lose, payouts)[hero]


class BubbleFactorIcm(unittest.TestCase):
    def test_icm_sums_to_prize_pool(self):
        self.assertAlmostEqual(sum(icm([5000, 3000, 2000], [50, 30, 20])), 100.0, places=9)

    def test_winner_take_all_is_chip_ev(self):
        now, win, lose = shove_equities([4000, 3000, 3000], [100], 0, 1)
        self.assertAlmostEqual(bubble_factor(now, win, lose), 1.0, places=9)
        self.assertAlmostEqual(required_equity(1.0), 0.5, places=9)

    def test_bubble_raises_required_equity(self):
        now, win, lose = shove_equities([5000, 3000, 2000, 1000], [50, 30, 20], 1, 2)
        bf = bubble_factor(now, win, lose)
        self.assertGreater(bf, 1.0)
        self.assertGreater(required_equity(bf), 0.5)


if __name__ == "__main__":
    unittest.main()
