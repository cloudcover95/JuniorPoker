# JuniorPoker tech sheet

| Layer | Spec |
|-------|------|
| License | MIT |
| Seats | 2–10 |
| Shoe | 1–8 decks, ids `0..52d-1` |
| Shuffle | `c/jp_shuffle` LCG Fisher–Yates; Python if no `.so` |
| Peek | `**` until `rub(seat[, cid])` |
| RFID | interface only; UID→cid jsonl later |
| Rank | combo-21, ABC A=B=C |
| Store | `stores/eval_canon.json` frozen 21 / 7462 |
| Trit | `trit_felt.pack` — not a ruling |
| Link | felt / party / solo / peer |
| HID | fold check call raise wheel, inject false |
| Bind | 127.0.0.1:18765 profiled, not listening |
| Compute | Pi 4/5 or SFF; T0 Python, T1 optional .so |
| Fab | `cad/trough.scad` |
| Home | `scripts/poker_prod.py`, OSai poker-* goldens |

Stack claim: local felt + Home note protocol. Not a licensed smart table.
