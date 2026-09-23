from __future__ import annotations

import ctypes
import os
from pathlib import Path

from juniorpoker.cards import shoe


def _lib():
    p = Path(__file__).resolve().parents[1] / "c" / "libjp_shuffle.so"
    if not p.is_file():
        return None
    lib = ctypes.CDLL(str(p))
    lib.jp_shuffle.argtypes = [ctypes.POINTER(ctypes.c_uint16), ctypes.c_int, ctypes.c_uint32]
    return lib


def shuffle(decks: int = 1, seed: int = 1) -> list[int]:
    ids = shoe(decks)
    lib = _lib()
    if lib is None:
        import random

        rng = random.Random(seed)
        rng.shuffle(ids)
        return ids
    n = len(ids)
    buf = (ctypes.c_uint16 * n)(*ids)
    lib.jp_shuffle(buf, n, ctypes.c_uint32(seed & 0xFFFFFFFF))
    return [int(buf[i]) for i in range(n)]
