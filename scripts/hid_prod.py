#!/usr/bin/env python3
import json
from juniorpoker.hid import action
from juniorpoker.stakes import Stakes

t = Stakes(seats=2, seed=1)
t.deal_hole()
print(json.dumps([action(t, 0, "wheel", 4), action(t, 0, "raise", 4)], indent=2))
