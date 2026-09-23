# Under-table BOM (drop-in modules)

MIT notes + links. We do not vendor Shuffle Master or copy Shuffle-o-matic STLs.

| Module | Solves | Fab | Compute |
|--------|--------|-----|---------|
| trough | collect mucked cards | print `cad/trough.scad` | none |
| shoe-gate | single-card feed | print + MG90S later | Pi GPIO later |
| wash | software shuffle | C `jp_shuffle` | Pi/SFF |
| sort-bin | 4 suit pockets | print, roadmap |
| felt-rfid | tap → rub | antenna later | `Table.tap` |
| sff | brain | Pi 4/5 or NUC | 127.0.0.1:18765 |

Open refs (own licenses): [Shuffle-o-matic](https://github.com/DDeGonge/Shuffle-o-matic) (Pi + NEMA17, hard), [Printables shuffler v3](https://www.printables.com/model/427943-playing-card-shuffler-v3).
