from __future__ import annotations

import json
from pathlib import Path

from juniorpoker.under_table import profile

ROOT = Path(__file__).resolve().parents[1]


def stack() -> dict:
    mods = json.loads((ROOT / "hw" / "modules.json").read_text(encoding="utf-8"))
    return {"profile": profile(), "modules": mods, "trough": str(ROOT / "cad" / "trough.scad")}
