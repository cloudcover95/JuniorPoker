from juniorpoker.shuffle_proof import fy_ok, trit_collapses

r = fy_ok()
assert r["set_ok"] and r["replay_ok"]
assert trit_collapses()["not_a_perm_proof"]
print("ok")
