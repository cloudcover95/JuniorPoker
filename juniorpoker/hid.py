"""Per-seat buttons + wheel. Local table actions. Not a site clicker."""
from __future__ import annotations

from juniorpoker.stakes import Stakes

WHEEL_TICK = 25  # chips per detent


def action(table: Stakes, seat: int, kind: str, ticks: int = 0) -> dict:
    kind = (kind or "").lower()
    if kind == "fold":
        table.hole[seat] = []
        return {"seat": seat, "op": "fold", "inject": False}
    if kind == "check":
        return table.post(seat, 0) | {"op": "check", "inject": False}
    if kind == "call":
        return table.post(seat, min(WHEEL_TICK, table.stacks[seat])) | {"op": "call", "inject": False}
    if kind == "raise":
        amt = max(WHEEL_TICK, abs(int(ticks)) * WHEEL_TICK)
        return table.post(seat, amt) | {"op": "raise", "inject": False}
    if kind == "wheel":
        return {"seat": seat, "op": "wheel", "ticks": ticks, "preview": abs(ticks) * WHEEL_TICK, "inject": False}
    return {"ok": False, "kind": kind, "inject": False}
