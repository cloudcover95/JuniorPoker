from juniorpoker.link import attach
from juniorpoker.games import get

assert get("holdem")["hole"] == 2
assert attach(0, "party", "x")["multi_seat_one_game"]
assert attach(1, "solo")["one_seat_one_game"]
assert attach(0, "felt")["casino_client"] is False
print("ok")
