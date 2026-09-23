#!/usr/bin/env python3
import json
from juniorpoker.store import canon, rows
from juniorpoker.ruling import abc
from juniorpoker.table import Table

t = Table(seats=2, decks=1, seed=5)
t.deal_hole(); t.flop(); t.turn_or_river(); t.turn_or_river()
print(json.dumps({"canon": canon(), "n_rows": len(rows()), "abc": abc(t.hole[0], t.board)}, indent=2))
