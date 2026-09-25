# Fisher–Yates vs trit

`jp_shuffle` is modern FY: for i = n-1 .. 1, swap a[i] with a[j], j in 0..i.
Induction: the suffix of length k is a uniform random k-subset, ordered uniformly.
Invariant: the set of values is unchanged. Replay: same seed ⇒ same perm.

RNG is LCG `s = 1664525 s + 1013904223` (Numerical Recipes), then `s % (i+1)`.
That modulo is **biased** when 2^32 is not a multiple of i+1. Fine for a home shoe, not a casino RNG cert.
Not cryptographic. Not a proof that trit packed.

## Trit does not prove the wash

`trit_felt.pack` Winsor-clips then `round(x/γ) → {-1,0,1}`.
Card ids are `0..51` (or `0..52d-1`), all ≥ 0. γ ≈ mean(|id|) ~ 25. Almost every trit is `+1`.
Two different shoes therefore share nearly the same I2_S hex. Hamming(π,σ) ≈ 0 even when π ≠ σ.

Use trit as a **Home note key**, not as a permutation certificate.
To fingerprint a shoe, hash the id list (SHA3/BLAKE2 already on the suite) or pack **centered** ids (`id - mean`) so signs split.

```
FY proof: set preserved + seed replay
Trit proof: neighbor notes, not S_n
```
