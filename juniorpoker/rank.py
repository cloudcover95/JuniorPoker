"""5-card and Hold'em 7-card rank. Combinatorial, no 130MB table."""
from __future__ import annotations

from itertools import combinations

CAT = (
    "high",
    "pair",
    "two",
    "trips",
    "straight",
    "flush",
    "full",
    "quads",
    "straight-flush",
)
# A,2,3,...,K → 12,0,1,...,11
VAL = (12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)


def _r(cid: int) -> int:
    return VAL[cid % 13]


def _s(cid: int) -> int:
    return (cid % 52) // 13


def _straight(ranks: list[int]) -> int | None:
    u = sorted(set(ranks), reverse=True)
    if 12 in u:
        u.append(-1)
    run = 1
    for i in range(1, len(u)):
        if u[i - 1] - u[i] == 1:
            run += 1
            if run >= 5:
                return u[i] + 4
        elif u[i - 1] != u[i]:
            run = 1
    return None


def five(ids: list[int]) -> tuple:
    ranks = [_r(c) for c in ids]
    suits = [_s(c) for c in ids]
    flush = len(set(suits)) == 1
    st = _straight(ranks)
    counts: dict[int, int] = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    groups = sorted(((n, r) for r, n in counts.items()), reverse=True)
    if flush and st is not None:
        return (8, st)
    if groups[0][0] == 4:
        return (7, groups[0][1], groups[1][1])
    if groups[0][0] == 3 and len(groups) > 1 and groups[1][0] == 2:
        return (6, groups[0][1], groups[1][1])
    if flush:
        return (5, *sorted(ranks, reverse=True))
    if st is not None:
        return (4, st)
    if groups[0][0] == 3:
        return (3, groups[0][1], *sorted((r for n, r in groups[1:]), reverse=True))
    if groups[0][0] == 2 and len(groups) > 1 and groups[1][0] == 2:
        p = sorted((groups[0][1], groups[1][1]), reverse=True)
        return (2, p[0], p[1], groups[2][1])
    if groups[0][0] == 2:
        return (1, groups[0][1], *sorted((r for n, r in groups[1:]), reverse=True))
    return (0, *sorted(ranks, reverse=True))


def seven(ids: list[int]) -> tuple:
    best = None
    for combo in combinations(ids, 5):
        k = five(list(combo))
        if best is None or k > best:
            best = k
    return best or (0,)


def name(key: tuple) -> str:
    return CAT[key[0]] if key else "high"
