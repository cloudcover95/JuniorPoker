from __future__ import annotations

import json
from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "stores"


def canon() -> dict:
    return json.loads((DIR / "eval_canon.json").read_text(encoding="utf-8"))


def rows() -> list:
    p = DIR / "eval_canon.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
