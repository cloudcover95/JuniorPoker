"""Local game directory. Functions per title."""
from __future__ import annotations

GAMES = {
    "holdem": {"hole": 2, "board": 5, "burn": True, "rank": "seven"},
    "omaha": {"hole": 4, "board": 5, "burn": True, "rank": "seven", "live": False},
    "stud": {"hole": 7, "board": 0, "live": False},
}


def get(name: str) -> dict:
    g = GAMES.get((name or "holdem").lower())
    if not g:
        return {"ok": False, "name": name}
    return {"ok": True, "name": name.lower(), **g}


def list_games() -> list:
    return [{"name": k, **v} for k, v in GAMES.items()]
