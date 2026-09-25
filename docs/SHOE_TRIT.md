# Shoe trit maps

`pack(ids)` on raw 0..51 collapses (all +). Do not use it as a wash key.

| Mode | Map | Sees order? | Hash? |
|------|-----|-------------|-------|
| pack | id | no (collapse) | no |
| pack_centered | id − mean | yes (sequence of signs) | no |
| pack_delta | sign(id_i − id_{i−1}) | yes (walk) | no |
| sha3_256 | bytes of ids | exact | yes |

Centered: mean of a full shoe is fixed, so card 0 is always negative and card 51 always positive. Hamming between two FY shoes = positions where the two orders put opposite sides of the mean.
Delta: unwraps the permutation as a path. Adjacent swaps flip one or two steps.

SHA3 stays identity. Trit Hamming stays neighbor.
