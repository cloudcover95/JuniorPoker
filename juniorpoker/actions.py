"""Per-seat buttons. Local table only."""
from __future__ import annotations

ACT = ("fold", "check", "call", "raise", "allin")


def press(seat: int, act: str, amt: int = 0) -> dict:
    a = (act or "").lower()
    if a not in ACT:
        return {"ok": False, "act": act}
    return {"ok": True, "seat": seat, "act": a, "amt": max(0, int(amt)), "remote_casino": False}
