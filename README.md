# JuniorPoker

MIT. JuniorCloud LLC / cloudcover95.

Local Hold'em felt: C Fisher–Yates, Python table, rub-then-peek bubbles, combo-21 + ABC.
RFID is an **event** (`tap` → `rub`), `live=False` until a reader exists.
Trit on raw ids collapses; use `pack_centered` / `pack_delta` as a neighbor, SHA3-256 as the shoe fingerprint.
Not a casino platform, not a sequenced antenna pit, not a shuffler clone, not a USB driver, not a 130MB LUT.

GitHub About (paste): see `ABOUT.md`.

```bash
make -C c
PYTHONPATH=. python3 tests/test_table.py
PYTHONPATH=. python3 tests/test_rank.py
PYTHONPATH=. python3 tests/test_shuffle_proof.py
PYTHONPATH=. python3 tests/test_shoe_trit.py
PYTHONPATH=. python3 scripts/table_prod.py --seats 6 --decks 2
PYTHONPATH=. python3 scripts/sha3_felt_prod.py
PYTHONPATH=. python3 scripts/shoe_trit_prod.py
```

Home: `python scripts/poker_prod.py` in JuniorHome.

---

## What this is / is not

| Is | Is not |
|----|--------|
| Software wash + deal + peek | Licensed smart table |
| Cloud-bubble privacy (`**` until rub) | Hole-card surveillance matrix |
| Combo-21 + ABC store | TwoPlusTwo 130MB LUT |
| SHA3 exact shoe / trit neighbor | Trit as a hash or a ruling |
| Loopback party/peer | Official-room bot / casino_client |
| Printable trough + BOM options | SHFL motor wash |

Patent screen: `docs/PATENTS.md`. Originality: `docs/ORIGINAL.md`. Tech sheet: `docs/TECH_SHEET.md`.

---

## Table spec

| Item | Spec |
|------|------|
| Seats | 2–10 (default 6) |
| Decks | 1–8 |
| Shuffle | `jp_shuffle` LCG FY; Python if no `.so`. Not a RNG cert. |
| Deal | hole 2, burn+flop, burn+turn, burn+river |
| Peek | `**` until `rub(seat)` |
| RFID | `Reader.tap(tag, seat)` → rub; no HID in-tree |
| Rank | combo-21, ABC A=B=C |
| Trit | `pack_centered` / `pack_delta`; raw `pack` collapses on 0..51 |
| Exact id | `sha3_felt.digest` |
| Bind | 127.0.0.1:18765 profiled, not listening |
| License | MIT |

---

## BOM

`hw/BOM.md`. Print: `cad/trough.scad`. Boxed 13.56 MHz decks are a **buy option**, not a shipped driver.

---

## Roadmap

1. UID→cid jsonl when a reader exists.
2. Omaha hole=4.
3. Local HTML bubbles.
4. Never: 0.0.0.0 felt, casino inject, sequenced locating coils as product without FTO, vendor STL paste.
