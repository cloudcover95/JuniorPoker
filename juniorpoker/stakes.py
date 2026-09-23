from __future__ import annotations

from juniorpoker.table import Table


class Stakes(Table):
    def __init__(self, seats: int = 6, decks: int = 1, seed: int = 1, stack: int = 10000) -> None:
        super().__init__(seats, decks, seed)
        self.stack0 = stack
        self.stacks = {i: stack for i in range(self.seats)}
        self.pot = 0
        self.acted = 0

    def post(self, seat: int, amt: int) -> dict:
        amt = max(0, min(self.stacks[seat], amt))
        self.stacks[seat] -= amt
        self.pot += amt
        self.acted = (seat + 1) % self.seats
        return {"seat": seat, "amt": amt, "pot": self.pot, "next": self.acted}
