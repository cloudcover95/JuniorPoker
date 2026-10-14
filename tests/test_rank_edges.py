"""Edge cases for juniorpoker.rank: wheel, kickers, 7-card best-of selection."""
from juniorpoker.rank import five, seven


def _ids(*faces):
    from juniorpoker.cards import RANKS, SUITS

    return [RANKS.index(f[0]) + 13 * SUITS.index(f[1]) for f in faces]


def test_wheel_is_straight_below_six_high():
    wheel = five(_ids("Ah", "2d", "3c", "4s", "5h"))
    six = five(_ids("2h", "3d", "4c", "5s", "6h"))
    assert wheel[0] == 4 and six[0] == 4
    assert six > wheel


def test_kicker_breaks_pair_tie():
    a = five(_ids("Ah", "Ad", "Kc", "7s", "2h"))
    b = five(_ids("As", "Ac", "Qc", "7d", "2d"))
    assert a[0] == b[0] == 1 and a > b


def test_seven_picks_flush_over_straight():
    k = seven(_ids("2h", "7h", "9h", "Jh", "Kh", "Tc", "8d"))
    assert k[0] == 5


def test_seven_full_house_from_two_trips():
    k = seven(_ids("Kh", "Kd", "Ks", "4c", "4d", "4h", "9s"))
    assert k[0] == 6


if __name__ == "__main__":
    for f in list(globals().values()):
        if callable(f) and getattr(f, "__name__", "").startswith("test_"):
            f()
    print("ok")
