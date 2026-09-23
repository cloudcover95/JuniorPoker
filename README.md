# JuniorPoker

MIT. JuniorCloud LLC / cloudcover95.
Local-first felt: C shuffle, Python table, cloud-bubble peek, RFID *interface*, trit pack of the shoe.
Not a casino platform. Not a USB driver. Not a Rust rewrite of 52 cards.

```bash
make -C c
PYTHONPATH=. python3 tests/test_table.py
PYTHONPATH=. python3 scripts/table_prod.py --seats 6 --decks 2
PYTHONPATH=. python3 scripts/under_table_prod.py
```

Home: `python scripts/poker_prod.py` in JuniorHome.

---

## Table spec sheet

| Item | Spec |
|------|------|
| Seats | 2–10 (default 6) |
| Decks | 1–8 (default 1; use 2 for a shoe) |
| Cards | 52 × decks; id `0..52d-1`; face `A23456789TJQK` + `cdhs` |
| Shuffle | C `jp_shuffle` Fisher–Yates LCG seed; Python `random` if `.so` missing |
| Deal | hole n=2, burn+flop 3, burn+turn, burn+river |
| Peek | `**` until that seat `rub`s those hole ids |
| Bubble | per-seat cloud icon; rub = thumb on RFID or `Table.rub(seat)` |
| RFID | `Reader.tap(tag, seat)` → rub; `live=False` until hardware |
| Stakes | `Stakes.post(seat, amt)` stacks + pot + next |
| Trit | `trit_felt.pack(ids)` Winsor → i2s_hex; optional JuniorLLM handshake |
| Bind | 127.0.0.1:18765 profiled, **not listening** |
| Pi / SFF | aarch64 `.so` same Makefile; `/dev/ttyAMA0` noted, not opened |
| Rust | rail only; FFI not on shoe length |
| License | MIT |

---

## Instructions

1. Clone. `make -C c` (optional; fallback shuffle works).
2. `PYTHONPATH=. python3 scripts/table_prod.py` — scene JSON, then peek before/after rub seat 0.
3. Physical table: SFF or Pi under the rail, run the same script on loopback.
4. RFID later: reader process calls `table.tap(tag, seat)` when a tag hits a seat antenna. Do not open serial from Home automations.
5. Players must rub (tap) before the seat computer shows ranks. Other seats stay `**`.
6. Pack the shoe or hole for Home/OSai: `trit_felt.pack(sum(table.hole.values(), []))`.

---

## Games data sheet

| Game | Status | Data |
|------|--------|------|
| Hold'em hole + board | **live** | hole[seat], board[], burns |
| Multi-deck shoe | **live** | decks 1–8 |
| Stakes / pot | **live** | stacks, pot, next |
| Stud / draw / Omaha | roadmap | same shoe + different hole n |
| Tournament clock | roadmap | not shipped |
| Hand evaluator | roadmap | no ranking yet |
| Networked seats | no | loopback only |

Card encoding: `cid % 52` → rank + suit. Trit pack is a neighbor key, not a hand rank.

---

## Software capabilities

| Module | Role |
|--------|------|
| `c/shuffle.c` | `jp_shuffle(uint16_t*, n, seed)` |
| `juniorpoker.cards` | shoe + face |
| `juniorpoker.shuffle` | ctypes or Python |
| `juniorpoker.table` | deal, rub, peek, scene, tap |
| `juniorpoker.stakes` | stacks/pot |
| `juniorpoker.rfid` | tag event, no HID |
| `juniorpoker.trit_felt` | Winsor pack / optional handshake |
| `juniorpoker.under_table` | Pi/SFF profile |
| `scripts/table_prod.py` | CLI scene |
| `scripts/under_table_prod.py` | profile + pack |
| `tests/test_table.py` | rub-then-peek + blind other seat |

---

## Roadmap

1. Hand evaluator (stdlib), Omaha hole=4.
2. Operator RFID: serial/HID reader process, still loopback to the table.
3. Seat UI: local HTML bubbles (no D3 requirement).
4. OSai golden `poker.json` if JuniorLLM is present.
5. Rust kernel only if replay n ≥ 1e5.
6. Never: 0.0.0.0 felt, SPIFFE on a card tag, GGUF pull for shuffle.
