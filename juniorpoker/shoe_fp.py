"""FIPS 202 SHA3-256 of the id list. Not trit."""
from __future__ import annotations

import hashlib
import struct

PREFIX = b"jp-shoe-v1\n"


def fingerprint(ids: list[int]) -> dict:
    h = hashlib.sha3_256()
    h.update(PREFIX)
    h.update(struct.pack(">I", len(ids)))
    for i in ids:
        h.update(struct.pack(">H", int(i) & 0xFFFF))
    digest = h.hexdigest()
    return {
        "alg": "SHA3-256",
        "fips": "202",
        "hex": digest,
        "n": len(ids),
        "prefix": "jp-shoe-v1",
        "length_extension": False,
    }


def same_shoe(a: list[int], b: list[int]) -> bool:
    return fingerprint(a)["hex"] == fingerprint(b)["hex"]
