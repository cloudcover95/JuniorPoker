#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from juniorpoker.shuffle import shuffle
from juniorpoker.shoe_fp import fingerprint, same_shoe

a, b = list(range(52)), list(range(52))
shuffle(a, 7)
shuffle(b, 7)
c = list(range(52))
shuffle(c, 8)
print(json.dumps({"replay": same_shoe(a, b), "diff_seed": same_shoe(a, c), "fp": fingerprint(a)}, indent=2))
