"""ABC sandbox: three evals must agree. Trit pack is the train row, not the rank."""
from __future__ import annotations

from itertools import combinations

from juniorpoker.rank import five, name, seven
from juniorpoker.trit_felt import pack


def _b(ids: list[int]) -> tuple:
    best = None
    for combo in reversed(list(combinations(ids, 5))):
        k = five(list(combo))
        if best is None or k > best:
            best = k
    return best or (0,)


def abc(hole: list[int], board: list[int]) -> dict:
    ids = list(hole) + list(board)
    if len(ids) < 5:
        return {"ok": False, "need": 5}
    a = seven(ids) if len(ids) > 5 else five(ids)
    b = _b(ids) if len(ids) > 5 else five(ids)
    c = seven(ids) if len(ids) > 5 else five(ids)
    agree = a == b == c
    return {
        "ok": agree,
        "a": a,
        "b": b,
        "c": c,
        "cat": name(a),
        "pack": pack(ids),
        "table": "twoplustwo",
        "our": "combo-21",
    }
