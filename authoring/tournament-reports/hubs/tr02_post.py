"""Hand edits for tr-batch-02 applied to the built package (Claude 2026-10-25).
python3 tr02_post.py /tmp/claude-0/tr-batch-02pkg"""
import re
import sys
from pathlib import Path

pk = Path(sys.argv[1]) / "pages"


def edit(title, fn):
    p = pk / (title.replace(" ", "_") + ".wiki")
    t = p.read_text(encoding="utf-8")
    n = fn(t)
    if n == t:
        print("UNCHANGED", title)
    p.write_text(n, encoding="utf-8")


J = "Jabba's Palace Sealed Deck"
SCHED = {  # (date, time) -> hub
    ("5 October", "12:00"): f"2000 DecipherCon {J} (5 October)",
    ("6 October", "18:00"): f"2000 DecipherCon {J} (6 October)",
    ("7 October", "10:00"): f"2000 DecipherCon {J} (7 October)",
    ("7 October", "18:00"): f"2000 DecipherCon {J} (7 October)",
    ("6 October", "21:00"): "2000 DecipherCon Japanese Sealed Deck (6 October)",
    ("7 October", "20:00"): "2000 DecipherCon Japanese Sealed Deck (7 October)",
    ("6 October", "09:00"): "2000 DecipherCon Reflections Booster Draft (6 October)",
    ("6 October", "19:00"): "2000 DecipherCon Highlander",
    ("7 October", "12:00"): "2000 DecipherCon Easy Come, Easy Go Sealed Deck",
    ("7 October", "14:00"): "2000 DecipherCon Race for Alderaan",
    ("8 October", "10:00"): "2000 DecipherCon Team Event",
    ("8 October", "12:00"): "2000 DecipherCon Kibitzing",
}
UNSCHED = [
    "2000 DecipherCon IRC 8-Man",
    "2000 DecipherCon 8-Man (Friday, Clay Ramey)",
    "2000 DecipherCon 8-Man (Friday, Brian Terwilliger)",
    "2000 DecipherCon 8-Man (Saturday, Charles Hickey)",
    "2000 DecipherCon Squadron Member Secret Squirrel",
]


def dcon2000(t):
    t = re.sub(r"\n== Side events ==\n.*?(?=\n== )", "\n", t, flags=re.S)
    for (day, tm), hub in SCHED.items():
        m = re.search(rf"^\| {day} \|\| {tm} \|\| ([^\n\[]+)$", t, re.M)
        if not m:
            print("no schedule row", day, tm)
            continue
        name = m.group(1)
        base = re.match(r"(.*?)( \(\$\d+\))?$", name)
        t = t[:m.start(1)] + f"[[{hub}|{base.group(1)}]]{base.group(2) or ''}" + t[m.end(1):]
    k = t.find("|}", t.find("== Star Wars side events =="))
    add = ("\n\nPlayers' tournament reports also describe events that were not on the printed schedule: "
           + ", ".join(f"[[{h}]]" for h in UNSCHED) + ".")
    return t[:k + 2] + add + t[k + 2:]


def list_fix(t):
    t = t.replace("| 1999-11 || [[DecipherCon 1999 Team Event]] || November 1999 || Virginia Beach, Virginia || [[Premiere - Endor]] || [[Paul Todd Feldman]], [[Maarten Logghe]], [[Bastian Winkelhaus]] and Unknown",
                  "| 1999-11 || [[DecipherCon 1999 Team Event]] || 14 November 1999 || Virginia Beach, Virginia || [[Premiere - Endor]] || [[Martin Akesson]], [[Paul Todd Feldman]], [[Koen Meijssen]] and [[Yannick Lapointe]]")
    t = t.replace("| 1999-11 || [[DecipherCon 1999 Progressive Sealed Deck]] || November 1999 || Virginia Beach, Virginia || || Unknown",
                  "| 1999-11 || [[DecipherCon 1999 Progressive Sealed Deck]] || 11 November 1999 || Virginia Beach, Virginia || || [[Martin Akesson]]")
    return t


def progressive(t):
    t = t.replace("|-\n| 1st || Unknown\n", "")
    return t.replace("recorded no overall winner.<ref name=\"dc99sw22_1\">",
                     "recorded no overall winner; [[Martin Akesson]]'s own report says he won it, beating [[Aldrin Long]] in the final.<ref name=\"tr-d163\" /><ref name=\"dc99sw22_1\">", 1)


edit("DecipherCon 2000", dcon2000)
edit("List of SWCCG tournaments", list_fix)
edit("DecipherCon 1999 Progressive Sealed Deck", progressive)
