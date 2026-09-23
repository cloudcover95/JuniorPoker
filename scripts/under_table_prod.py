#!/usr/bin/env python3
import json
from juniorpoker.table import Table
from juniorpoker.trit_felt import pack
from juniorpoker.under_table import profile

t = Table(seats=6, decks=2, seed=2)
t.deal_hole()
print(json.dumps({"profile": profile(), "shoe_pack": pack(sum(t.hole.values(), [])), "scene": t.scene()}, indent=2))
