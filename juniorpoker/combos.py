"""Starting-hand combo counting with card removal (blockers).

Standard library only. Hands use shorthand like "AA", "AKs", "AKo", "AK";
known cards use two-char strings like "As", "Kd". Additive module for JuniorPoker.
"""

from __future__ import annotations

from itertools import combinations

RANKS = "23456789TJQKA"
SUITS = "cdhs"


def _parse(hand: str) -> tuple[str, str, str]:
    h = hand.strip()
    if len(h) not in (2, 3):
        raise ValueError(f"bad hand: {hand!r}")
    r1, r2 = h[0].upper(), h[1].upper()
    kind = h[2].lower() if len(h) == 3 else ""
    if r1 not in RANKS or r2 not in RANKS or kind not in ("", "s", "o"):
        raise ValueError(f"bad hand: {hand!r}")
    if r1 == r2 and kind:
        raise ValueError(f"pairs take no suit marker: {hand!r}")
    return r1, r2, kind


def hand_combos(hand: str, dead: tuple[str, ...] | list[str] = ()) -> list[tuple[str, str]]:
    """All concrete two-card combos for a hand class, minus any using dead cards."""
    r1, r2, kind = _parse(hand)
    dead_set = {c[0].upper() + c[1].lower() for c in dead}
    out: list[tuple[str, str]] = []
    if r1 == r2:
        for s1, s2 in combinations(SUITS, 2):
            out.append((r1 + s1, r2 + s2))
    else:
        for s1 in SUITS:
            for s2 in SUITS:
                if kind == "s" and s1 != s2:
                    continue
                if kind == "o" and s1 == s2:
                    continue
                out.append((r1 + s1, r2 + s2))
    return [c for c in out if c[0] not in dead_set and c[1] not in dead_set]


def combo_count(hand: str, dead: tuple[str, ...] | list[str] = ()) -> int:
    return len(hand_combos(hand, dead))


def range_combos(hands: list[str], dead: tuple[str, ...] | list[str] = ()) -> int:
    """Total combos across a list of hand classes after card removal."""
    return sum(combo_count(h, dead) for h in hands)


if __name__ == "__main__":
    for h in ("AA", "AKs", "AKo", "AK"):
        print(h, combo_count(h), "with As dead:", combo_count(h, ["As"]))
