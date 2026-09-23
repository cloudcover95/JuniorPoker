"""Seats, deal, cloud-bubble rub-then-peek."""
from __future__ import annotations

from juniorpoker.cards import face
from juniorpoker.rfid import Reader
from juniorpoker.shuffle import shuffle


class Table:
    def __init__(self, seats: int = 6, decks: int = 1, seed: int = 1) -> None:
        self.seats = max(2, min(10, int(seats)))
        self.decks = decks
        self.seed = seed
        self.shoe: list[int] = []
        self.hole: dict[int, list[int]] = {i: [] for i in range(self.seats)}
        self.board: list[int] = []
        self.rubbed: set[tuple[int, int]] = set()
        self.rfid = Reader()
        self.button = 0

    def wash(self) -> None:
        self.shoe = shuffle(self.decks, self.seed)
        self.hole = {i: [] for i in range(self.seats)}
        self.board = []
        self.rubbed.clear()

    def _draw(self) -> int:
        if not self.shoe:
            self.wash()
        return self.shoe.pop()

    def deal_hole(self, n: int = 2) -> None:
        if not self.shoe:
            self.wash()
        for _ in range(n):
            for s in range(self.seats):
                self.hole[s].append(self._draw())

    def flop(self) -> None:
        self._draw()
        self.board.extend(self._draw() for _ in range(3))

    def turn_or_river(self) -> None:
        self._draw()
        self.board.append(self._draw())

    def rub(self, seat: int, cid: int | None = None) -> dict:
        cards = self.hole.get(seat) or []
        if cid is None:
            for c in cards:
                self.rubbed.add((seat, c))
            return {"seat": seat, "rubbed": len(cards), "bubble": "cloud"}
        if cid in cards:
            self.rubbed.add((seat, cid))
        return {"seat": seat, "cid": cid, "ok": (seat, cid) in self.rubbed}

    def peek(self, seat: int) -> dict:
        out = []
        for c in self.hole.get(seat) or []:
            if (seat, c) in self.rubbed:
                out.append(face(c))
            else:
                out.append("**")
        return {"seat": seat, "hole": out, "board": [face(c) for c in self.board]}

    def tap(self, tag: str, seat: int) -> dict:
        ev = self.rfid.tap(tag, seat)
        rub = self.rub(seat)
        return {**ev, **rub}

    def scene(self) -> dict:
        return {
            "seats": self.seats,
            "decks": self.decks,
            "button": self.button,
            "board": [face(c) for c in self.board],
            "bubbles": [{"seat": s, "hidden": ["**" for _ in self.hole[s]]} for s in range(self.seats)],
            "rfid_hw": self.rfid.live,
            "kernel": "c-or-python",
            "rust": False,
        }
