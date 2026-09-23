#!/usr/bin/env python3
import json
from juniorpoker.games import list_games
from juniorpoker.link import attach
print(json.dumps({"games": list_games(), "party": attach(0, "party", "home-1"), "solo": attach(3, "solo", "other-1")}, indent=2))
