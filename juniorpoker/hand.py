"""Hold'em streets + trit receipt when JuniorLLM is on path."""
from __future__ import annotations

from juniorpoker.table import Table


def _receipt(note: str) -> dict:
    try:
        from ports.receipt_cache import issue
    except ImportError:
        return {"ok": False, "offline": True}
    return issue(note)


class Hand:
    def __init__(self, table: Table | None = None) -> None:
        self.t = table or Table()
        self.street = "idle"
        self.folded: set[int] = set()
        self.receipt: dict = {}

    def start(self) -> dict:
        self.t.wash()
        self.t.deal_hole()
        self.street = "preflop"
        self.folded.clear()
        self.receipt = _receipt("poker preflop")
        return self.view()

    def fold(self, seat: int) -> dict:
        self.folded.add(seat)
        return self.view()

    def next_street(self) -> dict:
        if self.street == "preflop":
            self.t.flop()
            self.street = "flop"
        elif self.street == "flop":
            self.t.turn_or_river()
            self.street = "turn"
        elif self.street == "turn":
            self.t.turn_or_river()
            self.street = "river"
        elif self.street == "river":
            self.street = "showdown"
        self.receipt = _receipt(f"poker {self.street}")
        return self.view()

    def showdown(self, seat: int) -> dict:
        self.t.rub(seat)
        peek = self.t.peek(seat)
        return {**peek, "street": self.street, "folded": seat in self.folded}

    def view(self) -> dict:
        sc = self.t.scene()
        sc["street"] = self.street
        sc["folded"] = sorted(self.folded)
        sc["live"] = [s for s in range(self.t.seats) if s not in self.folded]
        sc["trit_ok"] = bool(self.receipt.get("ok"))
        sc["i2s"] = self.receipt.get("i2s_hex")
        return sc
