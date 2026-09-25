# SHA3 shoe fingerprint

FIPS 202 Keccak sponge. SHA3-256: rate 1088, capacity 512, 256-bit collision target.
Sponge does not have SHA-2 length extension. Python `hashlib.sha3_256` is stdlib.

Domain: `jp-shoe-v1` + big-endian count + uint16 ids.
Two FY seeds ⇒ two hexes. Same seed replay ⇒ same hex.
Trit I2_S is still the Home neighbor key. Do not substitute.
