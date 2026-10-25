"""Hand edits for tr-batch-03 applied to the built package (Claude 2026-10-25).
python3 tr03_post.py /tmp/claude-0/tr-batch-03pkg"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import decktech_batch as b  # noqa: E402

pk = Path(sys.argv[1])
tsv = next(pk.glob("y-*.tsv"))
FIELD = ('<ref name="field99">[https://web.archive.org/web/19991128125001/http://www.decipher.com/calendars/event/'
         'mainevents/deciphercon/swworldchamp/finalists.html Finalists], Decipher (Wayback 28 November 1999)</ref>')


def path(title):
    return pk / "pages" / (title.replace(" ", "_").replace("/", "%2F") + ".wiki")


def edit(title, fn):
    p = path(title)
    if p.exists():
        t = p.read_text(encoding="utf-8")
    else:
        t = b.live_text(title)
        if t is None:
            print("MISSING", title)
            return
        with open(tsv, "a", encoding="utf-8") as f:
            f.write(f"{title}\tpages/{p.name}\n")
    n = fn(t)
    if n == t:
        print("UNCHANGED", title)
    p.write_text(n, encoding="utf-8")


def list_fix(t):
    reps = [
        ("| 1999-10 || [[1999 Seattle Open]] || 1999 (before 18 October) ||", "| 1999-10 || [[1999 Seattle Open]] || 17 October 1999 ||"),
        ("| 1999-09 || [[1999 Endor Regionals]] || September 1999 || — ||", "| 1999-09 || [[1999 Endor Regionals]] || 4 September 1999 || Embassy Suites, Portland Airport, Portland, Oregon ||"),
        ("| 1999-08 || [[1999 GenCon Open]] || August 1999 || — ||", "| 1999-08 || [[1999 GenCon Open]] || 7 August 1999 || Gen Con, Milwaukee, Wisconsin ||"),
        ("| 1999 || [[1999 Dagobah Regionals]] || 1999 || Dagobah region || [[Premiere - Endor]] || Unknown",
         "| 1999-09 || [[1999 Dagobah Regionals]] || 25 September 1999 || Tallahassee, Florida || [[Premiere - Endor]] || [[Jason Burrows]]"),
    ]
    for a, c in reps:
        if a not in t:
            print("list row not found:", a[:60])
        t = t.replace(a, c)
    return t


def seattle(t):
    return t.replace("* '''Dates:''' 1999 (before 18 October)",
                     "* '''Dates:''' 17 October 1999<ref name=\"tr-d82\" />", 1)


def horbey(t):
    return t.replace("[[You Can Either Profit By This / He Must Pay|Profit]]", "", 1)


def team99(t):
    return re.sub(r"\n\* The \[\[List of SWCCG tournaments\]\] row names the winners as Paul Todd Feldman, Maarten Logghe, Bastian Winkelhaus and Unknown;[^\n]*", "", t)


def worlds99(t):
    for reg, hub in (("Calamari", "1999 Calamari Regionals"), ("Dagobah", "1999 Dagobah Regionals"),
                     ("Endor", "1999 Endor Regionals"), ("Kashyyyk", "1999 Kashyyyk Regionals"),
                     ("Naboo", "1999 Naboo Regionals"), ("Tatooine", "1999 Tatooine Regionals"),
                     ("Outer Rim", "1999 Outer Rim Regionals"), ("Ralltiir", "1999 Ralltiir Regionals")):
        t = re.sub(rf"(\|\| ){reg} Regional$", rf"\1[[{hub}|{reg} Regional]]", t, flags=re.M)
    return t


def tatooine(t):
    return t.replace("\n\n== ", f"\n* '''Qualified for Worlds:''' [[Thaddeus Chenoweth]] (Decipher's 1999 finalists list){FIELD}\n\n== ", 1)


def naboo(t):
    return t.replace("\n\n== ", f"\n* '''Qualified for Worlds:''' [[Gary Carman]] (Decipher's 1999 finalists list){FIELD}\n\n== ", 1)


edit("List of SWCCG tournaments", list_fix)
edit("1999 Seattle Open", seattle)
edit("Joe Horbey", horbey)
edit("DecipherCon 1999 Team Event", team99)
edit("1999 Decipher World Championship", worlds99)
edit("1999 Tatooine Regionals", tatooine)
edit("1999 Naboo Regionals", naboo)
p = path("Swccg-discussion")
p.write_text("#REDIRECT [[Decipher swccg-discussion list archive]]\n", encoding="utf-8")
with open(tsv, "a", encoding="utf-8") as f:
    f.write(f"Swccg-discussion\tpages/{p.name}\n")

# batch-02 hubs created with an empty Winner line (builder fixed 2026-10-25)
for t in [l.split("\t")[0] for l in open(Path(__file__).resolve().parents[2] / "y-tr-batch-02.tsv", encoding="utf-8") if l.strip()]:
    if not t.startswith("2000 DecipherCon") and not t.startswith("DecipherCon 1999"):
        continue
    cur = b.live_text(t) or ""
    if re.search(r"^\* '''Winner:''' *$", cur, re.M):
        edit(t, lambda x: re.sub(r"\n\* '''Winner:''' *(?=\n)", "", x))
