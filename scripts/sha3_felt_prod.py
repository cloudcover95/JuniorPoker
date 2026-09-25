#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from juniorpoker.sha3_felt import pair
from juniorpoker.shuffle import shuffle

a = list(range(52))
b = list(range(52))
shuffle(b, 7)
print(json.dumps({"ordered": pair(a), "shuffled": pair(b), "same_sha3": pair(a)["sha3_256"] == pair(b)["sha3_256"]}, indent=2))
