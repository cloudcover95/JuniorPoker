"""Invariants. Not a casino RNG cert."""
from __future__ import annotations

from juniorpoker.shuffle import shuffle
from juniorpoker.trit_felt import pack


def fy_ok(n: int = 52, seed: int = 7) -> dict:
    a = list(range(n))
    shuffle(a, seed)
    b = list(range(n))
    shuffle(b, seed)
    return {
        "set_ok": sorted(a) == list(range(n)),
        "replay_ok": a == b,
        "n": n,
        "lcg_mod_bias": True,
        "crypto": False,
    }


def trit_collapses(n: int = 52) -> dict:
    p = pack(list(range(n)))
    ones = sum(1 for t in p["trits"] if t == 1)
    return {"n": n, "plus_ones": ones, "collapses": ones >= n - 2, "not_a_perm_proof": True}
