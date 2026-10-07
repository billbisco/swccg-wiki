#!/usr/bin/env python3
"""Inventory Username strings in transcribe NOTE fields."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "encyclopedia"


def notes(text: str) -> dict[str, str]:
    out = {}
    for name in ("LS_NOTE", "DS_NOTE", "NOTE", "PUBLIC_NOTE"):
        m = re.search(
            rf"{name}\s*=\s*(\((?:.|\n)*?\)|\"\"\"(?:.|\n)*?\"\"\"|\"[^\"]*\"|'[^']*')",
            text,
        )
        if m:
            out[name] = m.group(1)
    return out


def usernames(blob: str) -> list[str]:
    found = []
    for pat in (
        r"Username\s+([A-Za-z0-9@._\-]+)",
        r"username\s+([A-Za-z0-9@._\-]+)",
        r"Username:\s*([A-Za-z0-9@._\-]+)",
    ):
        found.extend(re.findall(pat, blob))
    return found


def main() -> None:
    files = sorted(ROOT.rglob("transcribe_*.py"))
    print("files", len(files))
    missing = []
    for p in files:
        t = p.read_text(encoding="utf-8")
        n = notes(t)
        blob = " ".join(n.values())
        u = usernames(blob)
        player = re.search(r'^PLAYER\s*=\s*"([^"]+)"', t, re.M)
        pl = player.group(1) if player else "?"
        if u:
            print(f"HAS {pl}\t{p.name}\t{u}")
        else:
            missing.append((pl, p.name))
    print("MISSING", len(missing))
    for pl, name in missing:
        print(f"MISS {pl}\t{name}")


if __name__ == "__main__":
    main()
