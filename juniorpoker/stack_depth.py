"""Stack-depth helpers for JuniorPoker (additive, pure Python, no I/O).

effective_stack: smaller of two stacks.
stack_in_bb: stack measured in big blinds.
spr: stack-to-pot ratio (effective stack / pot).
depth_bucket: coarse label used by coaching tips.
"""


def effective_stack(hero, villain):
    if hero < 0 or villain < 0:
        raise ValueError("stacks must be non-negative")
    return min(hero, villain)


def stack_in_bb(stack, big_blind):
    if big_blind <= 0:
        raise ValueError("big_blind must be positive")
    if stack < 0:
        raise ValueError("stack must be non-negative")
    return stack / big_blind


def spr(effective, pot):
    if pot <= 0:
        raise ValueError("pot must be positive")
    if effective < 0:
        raise ValueError("effective stack must be non-negative")
    return effective / pot


def depth_bucket(bb):
    if bb < 0:
        raise ValueError("bb must be non-negative")
    if bb <= 15:
        return "push-fold"
    if bb <= 40:
        return "short"
    if bb <= 100:
        return "standard"
    return "deep"


def _self_check():
    assert effective_stack(500, 300) == 300
    assert stack_in_bb(300, 10) == 30.0
    assert spr(300, 60) == 5.0
    assert depth_bucket(10) == "push-fold"
    assert depth_bucket(30) == "short"
    assert depth_bucket(100) == "standard"
    assert depth_bucket(250) == "deep"
    for bad in ((lambda: stack_in_bb(1, 0)), (lambda: spr(1, 0)), (lambda: effective_stack(-1, 2))):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    return True


if __name__ == "__main__":
    print("self-check ok" if _self_check() else "self-check failed")
