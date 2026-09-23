"""Standalone Winsor-style pack of card ids. Optional JuniorLLM handshake."""
from __future__ import annotations


def pack(ids: list[int]) -> dict:
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


def note_pack(note: str) -> dict:
    try:
        from ports.gaia_proto import handshake

        env = handshake(note, job="dash-viewport")
        return {"via": "juniorllm", "i2s_hex": (env.get("note") or {}).get("i2s_hex"), "schema_ok": env.get("schema_ok")}
    except Exception:
        return {"via": "felt", **pack([ord(c) for c in (note or "felt")[:32]])}
