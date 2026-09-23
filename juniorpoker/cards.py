RANKS = "A23456789TJQK"
SUITS = "cdhs"


def shoe(decks: int = 1) -> list[int]:
    d = max(1, min(8, int(decks)))
    return list(range(52 * d))


def face(cid: int) -> str:
    i = cid % 52
    return RANKS[i % 13] + SUITS[i // 13]
