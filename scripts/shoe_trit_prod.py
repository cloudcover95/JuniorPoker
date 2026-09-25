#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from juniorpoker.shuffle import shuffle
from juniorpoker.trit_felt import pack, pack_centered, pack_delta, trit_ham
from juniorpoker.sha3_felt import digest

a = list(range(52))
b = list(range(52))
shuffle(b, 7)
pa, pb = pack(a), pack(b)
ca, cb = pack_centered(a), pack_centered(b)
da, db = pack_delta(a), pack_delta(b)
print(json.dumps({
    "raw_ham": trit_ham(pa["trits"], pb["trits"]),
    "centered_ham": trit_ham(ca["trits"], cb["trits"]),
    "delta_ham": trit_ham(da["trits"], db["trits"]),
    "same_sha3": digest(a) == digest(b),
    "centered_hex_eq": ca["i2s_hex"] == cb["i2s_hex"],
}, indent=2))
