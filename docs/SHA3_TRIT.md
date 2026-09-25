# SHA3 vs trit

SHA3-256 (FIPS 202, stdlib `hashlib`) is collision-resistant identity of the **byte string** of ids.
I2_S / Hamming is a 2-bit/trit neighborhood of a Winsor pack.

| | SHA3-256 | I2_S trit |
|--|----------|-----------|
| Same shoe, same seed | same digest | same hex |
| Two FY perms of 0..51 | **different** | often **same** (all +1) |
| Typo in a note | different | nearby Hamming |
| Blockchain / account | yes | no |
| Home cache key | exact replay | semantic replay |

Do not publish trit as a hash. Do not use SHA3 as a closeness metric.
