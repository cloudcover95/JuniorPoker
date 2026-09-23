from juniorpoker.actions import press
assert press(0, "fold")["ok"]
assert press(0, "raise", 200)["amt"] == 200
assert press(0, "fold")["remote_casino"] is False
print("ok")
