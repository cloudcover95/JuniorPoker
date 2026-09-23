"""Seat → remote table. Our spec only. No casino client."""
from __future__ import annotations

MODES = ("felt", "party", "solo", "peer")


def attach(seat: int, mode: str = "felt", table_id: str | None = None) -> dict:
    mode = (mode or "felt").lower()
    if mode not in MODES:
        return {"ok": False, "mode": mode}
    remote = mode in ("party", "solo", "peer")
    return {
        "ok": True,
        "seat": seat,
        "mode": mode,
        "table_id": table_id or "local-felt",
        "remote": remote,
        "bind": "127.0.0.1",
        "casino_client": False,
        "multi_seat_one_game": mode == "party",
        "one_seat_one_game": mode == "solo",
        "peer_juniorpoker": mode == "peer",
    }
