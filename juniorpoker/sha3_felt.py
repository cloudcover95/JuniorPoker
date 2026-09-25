"""SHA3-256 of exact ids. Trit stays the neighbor."""
from __future__ import annotations

import hashlib

from juniorpoker.trit_felt import pack


def digest(ids: list[int]) -> str:
    h = hashlib.sha3_256()
    h.update(bytes((i & 255) for i in ids))
    return h.hexdigest()


def pair(ids: list[int]) -> dict:
    t = pack(ids)
    return {
        "sha3_256": digest(ids),
        "i2s_hex": t["i2s_hex"],
        "n": len(ids),
        "roles": {"sha3": "exact", "trit": "neighbor"},
    }
