#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from juniorpoker.shuffle_proof import fy_ok, trit_collapses
print(json.dumps({"fy": fy_ok(), "trit": trit_collapses()}, indent=2))
