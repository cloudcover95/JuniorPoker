"""RFID interface. Hardware reader is operator later."""
from __future__ import annotations


class Reader:
    def __init__(self) -> None:
        self.live = False

    def tap(self, tag: str, seat: int) -> dict:
        return {"tag": tag, "seat": seat, "hw": self.live}
