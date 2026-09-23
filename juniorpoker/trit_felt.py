"""Felt → Home note. Shuffle stays C. Trit is the receipt, not the RNG."""
from __future__ import annotations

from juniorpoker.cards import face
from juniorpoker.table import Table


def note(t: Table, seat: int | None = None) -> str:
    board = "".join(face(c) for c in t.board) or "pre"
    if seat is None:
        return f"poker table {t.seats}s {t.decks}d btn{t.button} {board}"
    return f"poker seat {seat} {board}"


def pack(t: Table, seat: int | None = None) -> dict:
    n = note(t, seat)
    row = {"note": n, "seats": t.seats, "decks": t.decks, "rfid_hw": t.rfid.live}
    try:
        from ports.gaia_proto import handshake
        from ports.cache_secure import put

        hs = handshake(n, job="dash-viewport")
        cr = put(n)
        row.update(
            {
                "gamma": (hs.get("note") or {}).get("gamma"),
                "i2s_hex": (hs.get("note") or {}).get("i2s_hex"),
                "schema_ok": hs.get("schema_ok"),
                "collision": cr.get("collision"),
                "trit": True,
            }
        )
    except ImportError:
        row["trit"] = False
    return row
