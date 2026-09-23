#!/usr/bin/env python3
import json
from juniorpoker.hand import Hand

h = Hand()
print(json.dumps(h.start(), indent=2))
h.next_street()
h.fold(5)
print(json.dumps(h.next_street(), indent=2))
print(json.dumps(h.showdown(0), indent=2))
