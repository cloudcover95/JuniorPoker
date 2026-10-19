"""Pot odds, break-even equity, and minimum defense frequency helpers.

Pure-Python, no dependencies, no network, no I/O. Additive utility for
JuniorPoker decision tooling.

Definitions (chip amounts are non-negative numbers):
    pot      -- chips in the pot before the bet being faced (includes blinds/antes)
    bet      -- size of the bet the player is facing
    call     -- amount the player must put in to continue (usually == bet)

    pot_odds(pot, bet)          -> ratio "pot : call" as a float (e.g. 3.0 means 3:1)
    break_even_equity(pot, bet) -> fraction of the time a call must win to break even
    mdf(pot, bet)               -> minimum defense frequency vs. a bet of that size
    bluff_break_even(pot, bet)  -> how often a pure bluff must work to break even
    call_ev(equity, pot, bet)   -> chip EV of calling with a given equity
"""

from __future__ import annotations

__all__ = [
    "pot_odds",
    "break_even_equity",
    "mdf",
    "bluff_break_even",
    "call_ev",
    "should_call",
]


def _check(pot: float, bet: float) -> None:
    if pot < 0 or bet < 0:
        raise ValueError("pot and bet must be non-negative")
    if pot + bet == 0:
        raise ValueError("pot and bet cannot both be zero")


def pot_odds(pot: float, bet: float) -> float:
    """Return the reward-to-risk ratio for calling: (pot + bet) / bet."""
    _check(pot, bet)
    if bet == 0:
        raise ValueError("no bet to call; pot odds are undefined")
    return (pot + bet) / bet


def break_even_equity(pot: float, bet: float) -> float:
    """Equity a call needs to break even: call / (pot + bet + call)."""
    _check(pot, bet)
    return bet / (pot + 2 * bet)


def mdf(pot: float, bet: float) -> float:
    """Minimum defense frequency: pot / (pot + bet)."""
    _check(pot, bet)
    return pot / (pot + bet)


def bluff_break_even(pot: float, bet: float) -> float:
    """Fold frequency a pure bluff needs to break even: bet / (pot + bet)."""
    _check(pot, bet)
    return bet / (pot + bet)


def call_ev(equity: float, pot: float, bet: float) -> float:
    """Chip EV of calling: win (pot + bet) with `equity`, lose `bet` otherwise."""
    _check(pot, bet)
    if not 0.0 <= equity <= 1.0:
        raise ValueError("equity must be between 0 and 1")
    return equity * (pot + bet) - (1.0 - equity) * bet


def should_call(equity: float, pot: float, bet: float) -> bool:
    """True when calling is at least break-even in chip EV."""
    return call_ev(equity, pot, bet) >= -1e-12


def _self_check() -> None:
    close = lambda a, b: abs(a - b) < 1e-9  # noqa: E731
    # Half-pot bet: 100 pot, 50 bet -> 3:1 odds, need 25%, MDF 66.7%, bluff 33.3%
    assert close(pot_odds(100, 50), 3.0)
    assert close(break_even_equity(100, 50), 0.25)
    assert close(mdf(100, 50), 2 / 3)
    assert close(bluff_break_even(100, 50), 1 / 3)
    # Pot-size bet: need 1/3 equity, MDF 50%
    assert close(break_even_equity(100, 100), 1 / 3)
    assert close(mdf(100, 100), 0.5)
    # EV at break-even equity is zero; consistency between helpers
    for pot, bet in [(100, 50), (100, 100), (60, 200), (10, 1)]:
        be = break_even_equity(pot, bet)
        assert close(call_ev(be, pot, bet), 0.0)
        assert should_call(be + 0.01, pot, bet)
        assert not should_call(be - 0.01, pot, bet)
        assert close(mdf(pot, bet) + bluff_break_even(pot, bet), 1.0)
    for bad in [(-1, 5), (5, -1), (0, 0)]:
        try:
            mdf(*bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for %r" % (bad,))
    try:
        pot_odds(100, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for zero bet")


if __name__ == "__main__":
    _self_check()
    print("pot_odds self-check OK")
