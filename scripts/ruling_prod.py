#!/usr/bin/env python3
import json
from juniorpoker.table import Table
from juniorpoker.ruling import abc

t = Table(seats=2, decks=1, seed=11)
t.deal_hole()
t.flop()
t.turn_or_river()
t.turn_or_river()
row = abc(t.hole[0], t.board)
print(json.dumps(row, indent=2))
