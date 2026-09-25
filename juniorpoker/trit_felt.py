"""Winsor pack. pack() is notes. pack_centered / pack_delta are shoes."""
from __future__ import annotations


def pack(ids: list[int] | list[float]) -> dict:
    xs = [float(i) for i in ids] or [0.0]
    a = sorted(abs(x) for x in xs)
    tau = a[max(0, int(0.95 * (len(a) - 1)))]
    tau = tau or 1.0
    clipped = [min(max(x, -tau), tau) for x in xs]
    g = sum(abs(x) for x in clipped) / len(clipped)
    g = g or 1.0
    trits = []
    for x in clipped:
        q = round(x / g)
        trits.append(1 if q > 0 else (-1 if q < 0 else 0))
    bits = 0
    for t in trits:
        bits = (bits << 2) | (t + 1)
    return {"gamma": round(g, 6), "trits": trits, "i2s_hex": format(bits, "x"), "n": len(trits)}


def pack_centered(ids: list[int]) -> dict:
    """x' = id - mean(id). Signs split. Still not a hash."""
    xs = [float(i) for i in ids] or [0.0]
    mu = sum(xs) / len(xs)
    out = pack([x - mu for x in xs])
    out["mean"] = round(mu, 6)
    out["mode"] = "centered"
    out["collision_resistant"] = False
    return out


def pack_delta(ids: list[int]) -> dict:
    """Unwrap: sign of consecutive steps. Order-sensitive walk."""
    if not ids:
        return pack([])
    walk = [0.0]
    for i in range(1, len(ids)):
        walk.append(float(ids[i] - ids[i - 1]))
    out = pack(walk)
    out["mode"] = "delta"
    out["collision_resistant"] = False
    return out


def trit_ham(a: list[int], b: list[int]) -> int:
    n = min(len(a), len(b))
    return sum(x != y for x, y in zip(a[:n], b[:n])) + abs(len(a) - len(b))


def note_pack(note: str) -> dict:
    try:
        from ports.gaia_proto import handshake

        env = handshake(note, job="dash-viewport")
        return {"via": "juniorllm", "i2s_hex": (env.get("note") or {}).get("i2s_hex"), "schema_ok": env.get("schema_ok")}
    except Exception:
        return {"via": "felt", **pack([ord(c) for c in (note or "felt")[:32]])}
