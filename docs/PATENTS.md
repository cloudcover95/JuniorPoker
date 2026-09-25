# Patent screen (not legal advice, not FTO)

Counsel required before selling a table that reads RFID cards or chips on a felt with per-seat antennas.

## Hot families (casino floor)

- Shuffle Master / SHFL / Bally / SG Gaming / LNW: shoes, shufflers, smart tables, chip RFID + optical card read. Enpat RFID buy-in for table play tracking.
- Sequenced antenna arrays locating RFID chips on blackjack/poker tables (e.g. US7561053 / US7852223 lineage).
- Walker Digital Table Systems: RFID-enabled table games, inferring transactions from tag reads.
- Angel Group and others: tagged cards + table management.
- Smart table *card hand identification* (Shuffle Master US7114718 class).
- Wireless monitoring of card games / wagers (US7950661 class).

Mechanical casino shufflers sit in a thicket that has been *litigated*, including antitrust/sham-suit history. Do not ship a Shuffle Master look-alike.

## Our tree vs that thicket

| Ours | Overlap |
|------|---------|
| C Fisher–Yates + Python table | **low** — software random + combo-21 |
| Printable muck trough SCAD | **low** — tray geometry |
| Cloud-bubble *software* peek (`**` until rub) | **medium** if sold with per-seat RFID antennas that identify hole cards |
| Buy boxed RFID decks + UID→cid jsonl | **medium** — using commodity cards is fine; a *system* that polls the felt and names hands is the claim zone |
| Sequenced seat coils + board coil locating every tag | **high** if we implement that |
| Casino chip accounting / bet-spot inference | **high** — we do not ship |
| Linking official-room clients / bot inject | **out** — ToS, not just patents |
| Linking Shuffle-o-matic STLs | **their** MIT; still do not commercialize a motor wash that copies SHFL claims |

## Posture

Home / MIT source: keep `Reader.live=False`, software wash canonical, RFID is tap→rub not a tracking matrix.
Productize only after a real FTO on the antenna + hand-ID claims in the target country.
