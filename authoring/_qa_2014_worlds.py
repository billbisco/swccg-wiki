#!/usr/bin/env python3
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_2014_worlds import wikilink, _lookup  # noqa: E402

checks = [
    ("Imperial Entanglements / No One To Stop Us This Time", "Dark", False, False),
    ("Mind What You Have Learned / Save You It Can (V)", "Light", True, False),
    ("Wookiee Slaving Operation / Indentured To The Empire", "Dark", False, False),
    ("Communing", "Light", False, False),
    ("Admiral Piett", "Dark", False, False),
    ("Admiral Motti (V)", "Dark", True, False),
    ("Imperial Decree", "Dark", False, False),
    ("Let The Wookiee Win", "Light", True, False),
    ("Let's Keep A Little Optimism Here", "Light", True, True),
    ("The Professor", "Light", True, True),
    ("Affect Mind", "Light", True, True),
    ("Jabba's Prize", "Light", True, True),
    ("Hoth: Defensive Perimeter", "Dark", False, False),
    ("Hoth: Ice Plains", "Dark", True, False),
    ("Hoth: Mountains", "Dark", False, False),
    ("Grimtaash", "Light", False, False),
    ("Tantive IV", "Light", False, False),
    ("Guardian's Lightsaber", "Light", True, False),
    ("There Is Good In Him / I Can Save Him", "Light", False, False),
    ("Imperial Occupation / Imperial Control", "Dark", True, False),
    ("Simple Tricks And Nonsense", "Light", False, True),
    ("Chasm", "Light", True, True),
]
print("lookup samples:")
for name, side, is_v, sh in checks:
    dest = _lookup(name, side, is_v, prefer_sh=sh)
    link = wikilink(name, side, is_v, prefer_sh=sh)
    print(f"  {name!r} v={is_v} sh={sh} -> {dest!r}")
    print(f"    {link}")

ROOT = Path(__file__).resolve().parent
decks = list((ROOT / "pages").glob("2014_Worlds_Day_*.wiki"))
forbid = {
    "Imperial Entanglements / No One To Stop Us This Time",
    "Mind What You Have Learned / Save You It Can (V)",
    "Mind What You Have Learned / Save You It Can",
    "Imperial Occupation / Imperial Control",
}
print("\n--- modern dual dests ---")
for p in decks:
    t = p.read_text(encoding="utf-8")
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", t):
        dest = m.group(1)
        if dest in forbid:
            print("BAD", p.name, dest)

print("\n--- blanks ---")
for p in decks:
    t = p.read_text(encoding="utf-8")
    blanks = [i for i, ln in enumerate(t.splitlines(), 1) if ln.strip() in ("# &nbsp;", "#")]
    if blanks:
        print(p.name, blanks)

print("\n--- ditto leftover ---")
for p in decks:
    t = p.read_text(encoding="utf-8")
    if '""' in t or "''" in t and '""' in t:
        print("DITTO", p.name)
