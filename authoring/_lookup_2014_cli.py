#!/usr/bin/env python3
"""Lookup 2014 Legacy Open dests. Usage:
  python wiki/_lookup_2014_cli.py Dark "Sense" 0
  python wiki/_lookup_2014_cli.py --file path.txt
File lines: side<TAB>name<TAB>0|1   (1 = (V) checked / written)
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from generate_2014_worlds import _lookup, visible_for, wikilink  # noqa: E402


def one(side: str, name: str, is_v: bool, prefer_sh: bool = False) -> None:
    dest = _lookup(name, side, is_v, prefer_sh=prefer_sh)
    shown = visible_for(dest, name, is_v) if dest else None
    link = wikilink(name, side, is_v, prefer_sh=prefer_sh)
    flag = "OK" if dest else "NO_DEST"
    print(f"{flag}\t{side}\t{int(is_v)}\t{name}\t{dest or ''}\t{shown or ''}\t{link}")


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[0] == "--file":
        path = Path(argv[1])
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                print("BAD", raw, file=sys.stderr)
                continue
            side, name = parts[0], parts[1]
            is_v = parts[2].strip() in ("1", "true", "True", "V", "(V)") if len(parts) > 2 else False
            prefer_sh = parts[3].strip() in ("1", "sh", "shield") if len(parts) > 3 else False
            one(side, name, is_v, prefer_sh=prefer_sh)
        return 0
    if len(argv) < 2:
        print("usage: _lookup_2014_cli.py Side Name [0|1] [sh]", file=sys.stderr)
        return 2
    side = argv[0]
    name = argv[1]
    is_v = argv[2] in ("1", "true", "True", "V") if len(argv) > 2 else False
    prefer_sh = len(argv) > 3 and argv[3] in ("1", "sh", "shield")
    one(side, name, is_v, prefer_sh=prefer_sh)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
