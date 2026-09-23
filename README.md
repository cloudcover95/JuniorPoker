# JuniorPoker

MIT. JuniorCloud LLC / cloudcover95.
Local-first felt: C shuffle, Python table, cloud-bubble peek, RFID *interface*, trit pack of the shoe.
Not a casino platform. Not a USB driver. Not a Rust rewrite of 52 cards.

```bash
make -C c
PYTHONPATH=. python3 tests/test_table.py
PYTHONPATH=. python3 tests/test_rank.py
PYTHONPATH=. python3 scripts/table_prod.py --seats 6 --decks 2
PYTHONPATH=. python3 scripts/under_table_prod.py
PYTHONPATH=. python3 scripts/hw_prod.py
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
| Rank | combo-21 ABC ruling; no 130MB LUT |
| Trit | `trit_felt.pack(ids)` Winsor → i2s_hex |
| Bind | 127.0.0.1:18765 profiled, **not listening** |
| Pi / SFF | aarch64 `.so` same Makefile; `/dev/ttyAMA0` noted, not opened |
| License | MIT |

---

## BOM and table-part options

Full notes: `hw/BOM.md`. Print: `cad/trough.scad`.

### Structure / fab

| Part | Option A (print) | Option B (buy) | Integrates |
|------|------------------|----------------|------------|
| Muck trough | OpenSCAD trough | any rail tray | drop-in |
| Shoe / gate | print + MG90S later | retail shoe | software deal |
| Wash / shuffler | C wash on Pi | Shuffle-o-matic / Printables v3 (their license) | `jp_shuffle` still canonical |
| Sort bins | 4 pockets roadmap | card tray | later |
| Felt + bubble lids | print bezels | acrylic | peek UI |
| Under-table | Pi 4/5 4GB+ | Intel/AMD NUC SFF | `under_table.profile` |

### RFID (cards, chips, seats)

Industry tables often tag **chips** for bets; some rooms also tag **cards**. We treat both as *tags* that call `tap`.

| Part | Option | Notes |
|------|--------|--------|
| RFID playing cards | 13.56 MHz inlay in poker stock | one UID per card; map UID→cid in a local jsonl |
| RFID chips | 13.56 MHz tokens | pot/stacks later; not required for peek |
| Seat antenna | PCB coil under each bubble | which seat rubbed |
| Board antenna | one coil center | flop/turn/river face-up, no rub |
| Reader | PN532 / RC522 / ACR122U | operator process; Home does not open USB |
| Wiring | UART `/dev/ttyAMA0` or USB HID | `open_serial: false` in profile |

Software today: `Reader.tap(tag, seat)` → `rub`. No HID driver in-tree. Do not put SPIFFE on a tag.

### Fasteners / motion (if you build a motor wash)

NEMA17, GT2 20t, MGN9, 6700ZZ, MG90S, N20 — see Shuffle-o-matic BOM; we do not restock their cart.

---

## Instructions

1. Clone. `make -C c` (optional).
2. `PYTHONPATH=. python3 scripts/table_prod.py` — scene, peek before/after rub.
3. SFF/Pi under the rail, same script, loopback.
4. RFID later: reader process → `table.tap(tag, seat)`. Not from Home automations.
5. Rub before ranks. Other seats stay `**`.
6. Print trough: OpenSCAD → STL. Omega job `terrain-obj`, no UE5.

---

## Games data sheet

| Game | Status | Data |
|------|--------|------|
| Hold'em hole + board | **live** | hole[seat], board[], burns |
| Multi-deck shoe | **live** | decks 1–8 |
| Stakes / pot | **live** | stacks, pot, next |
| 7-card rank + ABC | **live** | combo-21, store `stores/eval_canon.json` |
| Stud / draw / Omaha | roadmap | same shoe + different hole n |
| Tournament clock | roadmap | not shipped |
| Networked seats | no | loopback only |

---

## Software capabilities

| Module | Role |
|--------|------|
| `c/shuffle.c` | `jp_shuffle` |
| `juniorpoker.table` | deal, rub, peek, tap |
| `juniorpoker.rank` / `ruling` | five / seven / ABC |
| `juniorpoker.rfid` | tag event |
| `juniorpoker.hw` | BOM + profile |
| `stores/eval_canon.json` | frozen 21 / 7462 facts |
| `cad/trough.scad` | print |

---

## Roadmap

1. UID→cid jsonl when a reader exists.
2. Omaha hole=4.
3. Local HTML bubbles.
4. Never: 0.0.0.0 felt, SPIFFE on a card tag, 130MB LUT pull, vendor STL paste.

local-first poker holdem rfid raspberry-pi openscad bitnet juniorcloud shuffle mit