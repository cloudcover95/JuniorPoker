# BOM — every table part as buy / print / link

JuniorPoker does not vendor these SKUs. Prices move. Protocols matter.

## Cards

| Option | What | Air | Use |
|--------|------|-----|-----|
| Paper Bicycle-class | buy any poker deck | none | software-only table |
| ICODE SLIX boxed deck | buy (~54 PVC, 63×88, 13.56 MHz) | ISO 15693 / NFC T5 | seat coil, longer range |
| NTAG / 14443 boxed deck | buy (magic + OEM) | ISO 14443A | phone / ACR122U rub |
| OEM Alibaba/CXJ | wholesale MOQ | mixed | custom print |

Map UID→cid in local jsonl. Do not encode SPIFFE on the tag.

## Chips / pot

| Option | What |
|--------|------|
| Clay/ceramic | buy; no RFID |
| RFID casino tokens | buy 13.56 MHz; same tap path, later stacks |
| Print tokens | PLA + sticker NFC tag |

## Readers / antennas

| Option | Air | Notes |
|--------|-----|-------|
| ACR122U USB | 14443 | HID; operator process |
| PN532 UART | 14443 | Pi `/dev/ttyAMA0` later |
| RC522 SPI | 14443 | short range |
| ISO 15693 USB/module | 15693 | needed for SLIX decks |
| Seat PCB coil | — | one per bubble |
| Board coil | — | flop face-up, no rub |

Home: `open_serial: false`.

## Per-seat buttons + scroll wheel

Map to `juniorpoker.hid.action`. `inject: false`.

| Part | Buy | Print |
|------|-----|-------|
| Fold / check-call / raise | 3 arcade 30 mm | bezel later |
| Bet wheel | KY-040 encoder or mouse wheel | knob cap |
| MCU | Pro Micro / Pi Pico as USB HID | — |
| Macropad | Stream Deck / numpad | — |

If the seat plays a **commercial** room: official app on a small screen; human uses their UI. Do not pipe these buttons into an unofficial client.

## Collect / wash / sort

| Part | Print | Buy | Link (own license) |
|------|-------|-----|---------------------|
| Muck trough | `cad/trough.scad` | rail tray | — |
| Manual shuffler | — | Lotus-class retail | Printables shuffler v3 |
| Motor wash | — | — | Shuffle-o-matic (Pi+NEMA17) |
| Software wash | — | — | **this repo** `c/shuffle.c` |
| Shoe | print gate later | acrylic shoe | — |
| Sort bins | 4 pockets later | card tray | — |

## Motion (only if you build Shuffle-o-matic-class)

NEMA17 ≤40 mm, GT2 20t pulley/idler, MGN9 95/135, 6700ZZ, MG90S, N20 600 rpm. Their BOM, not ours.

## Compute / power

| Option | Role |
|--------|------|
| Raspberry Pi 4/5 4GB+ | under-table |
| SFF NUC / mini-PC | same profile |
| 12V brick + buck 5V | Pi |
| No listen on 0.0.0.0 | bind 127.0.0.1:18765 |

## Felt / UI

| Option | Role |
|--------|------|
| Print bubble bezels | seat lids |
| Acrylic speed cloth | buy |
| Seat screen | official-app kiosk only |
| Local HTML bubbles | roadmap |

## Software that stays ours

`Table.tap` · `hid.action` · `jp_shuffle` · combo-21 ABC · eval store. Trit does not rank the hand.
