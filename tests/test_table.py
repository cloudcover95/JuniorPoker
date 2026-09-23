from juniorpoker.table import Table


def test_rub_then_peek():
    t = Table(seats=2, decks=1, seed=7)
    t.deal_hole()
    hid = t.peek(0)
    assert hid["hole"] == ["**", "**"]
    t.rub(0)
    seen = t.peek(0)
    assert all(c != "**" for c in seen["hole"])


def test_other_seat_blind():
    t = Table(seats=2, decks=2, seed=3)
    t.deal_hole()
    t.rub(0)
    assert t.peek(1)["hole"] == ["**", "**"]


if __name__ == "__main__":
    test_rub_then_peek()
    test_other_seat_blind()
    print("ok")
