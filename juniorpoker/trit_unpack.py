"""Efficient I2_S unpack + packed flips. Pollinated into JuniorPoker.

Does not replace juniorpoker.trit_felt.pack. Import pack from trit_felt;
use this module for unpack / flip only.
"""
from __future__ import annotations


def unpack_i2s(bits: int, n: int) -> list[int]:
    if n <= 0:
        return []
    codes = [0] * n
    tmp = int(bits)
    for i in range(n - 1, -1, -1):
        codes[i] = (tmp & 3) - 1
        tmp >>= 2
    return codes


def unpack(blob: dict) -> list[int]:
    if blob.get("i2s_hex") and blob.get("n"):
        return unpack_i2s(int(blob["i2s_hex"], 16), int(blob["n"]))
    return [int(t) for t in (blob.get("trits") or [])]


def flip_packed(bits: int, n: int, index: int) -> int:
    if n <= 0 or index < 0 or index >= n:
        return int(bits)
    shift = 2 * (n - 1 - index)
    code = (int(bits) >> shift) & 3
    if code == 1:
        return int(bits)
    new_code = 2 if code == 0 else 0
    mask = ~(3 << shift)
    return (int(bits) & mask) | (new_code << shift)
