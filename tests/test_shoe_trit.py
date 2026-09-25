from juniorpoker.shuffle import shuffle
from juniorpoker.trit_felt import pack, pack_centered, pack_delta, trit_ham
from juniorpoker.sha3_felt import digest

a = list(range(52))
b = list(range(52))
shuffle(b, 7)
assert digest(a) != digest(b)
assert trit_ham(pack_centered(a)["trits"], pack_centered(b)["trits"]) > 0
assert trit_ham(pack_delta(a)["trits"], pack_delta(b)["trits"]) > 0
# raw pack may collapse; do not require ham > 0
_ = pack(a)
print("ok")
