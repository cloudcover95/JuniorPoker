from juniorpoker.rank import five, seven
from juniorpoker.ruling import abc


def _ids(*faces):
    from juniorpoker.cards import RANKS, SUITS

    out = []
    for f in faces:
        out.append(RANKS.index(f[0]) + 13 * SUITS.index(f[1]))
    return out


def test_royal():
    k = five(_ids("Ah", "Kh", "Qh", "Jh", "Th"))
    assert k[0] == 8


def test_abc_agree():
    hole = _ids("As", "Kd")
    board = _ids("Qh", "Jc", "Td", "2s", "3c")
    r = abc(hole, board)
    assert r["ok"] and r["cat"] == "straight"


if __name__ == "__main__":
    test_royal()
    test_abc_agree()
    print("ok")
