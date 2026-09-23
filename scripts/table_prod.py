#!/usr/bin/env python3
import argparse
import json

from juniorpoker.table import Table

p = argparse.ArgumentParser()
p.add_argument("--seats", type=int, default=6)
p.add_argument("--decks", type=int, default=1)
p.add_argument("--seed", type=int, default=1)
a = p.parse_args()
t = Table(seats=a.seats, decks=a.decks, seed=a.seed)
t.deal_hole()
t.flop()
print(json.dumps(t.scene(), indent=2))
print(json.dumps(t.peek(0), indent=2))
print(json.dumps(t.rub(0), indent=2))
print(json.dumps(t.peek(0), indent=2))
