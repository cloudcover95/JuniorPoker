"""SFF / Pi profile. No GPIO open. Loopback only."""
from __future__ import annotations

import os
from pathlib import Path


def profile() -> dict:
    machine = os.uname().machine if hasattr(os, "uname") else "unknown"
    pi = machine.startswith("arm") or machine.startswith("aarch")
    serial = Path("/dev/ttyAMA0")
    return {
        "bind": "127.0.0.1",
        "port": 18765,
        "listen": False,
        "gpio": False,
        "rfid_dev": str(serial) if serial.exists() else None,
        "pi_likely": pi,
        "sff": True,
        "open_serial": False,
    }
