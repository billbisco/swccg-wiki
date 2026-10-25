"""Hand edits for tr-batch-12 on the built package (Claude 2026-10-25). python3 tr12_post.py /tmp/claude-0/tr-batch-12pkg
Late-2000 events whose reports show Jabba's Palace Sealed Deck objectives (My Kind Of Scum, Agents In The Court) are
Premiere - Jabba's Palace Sealed Deck, not Premiere - Death Star II."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import decktech_batch as b  # noqa: E402

pk = Path(sys.argv[1])
tsv = next(pk.glob("y-*.tsv"))
JP = "[[Premiere - Jabba's Palace Sealed Deck]]"


def edit(title, fn):
    p = pk / "pages" / (title.replace(" ", "_").replace("/", "%2F") + ".wiki")
    if p.exists():
        t = p.read_text(encoding="utf-8")
    else:
        t = b.live_text(title)
        open(tsv, "a", encoding="utf-8").write(f"{title}\tpages/{p.name}\n")
    n = fn(t)
    print(("edited " if n != t else "UNCHANGED ") + title)
    p.write_text(n, encoding="utf-8")


def hubfmt(ref):
    def f(t):
        return t.replace("* '''Format:''' [[Premiere - Death Star II]]",
                         f"* '''Format:''' {JP} (the reports' decks use its objectives){ref}", 1)
    return f


def mega(t):
    return t.replace("* '''Dates:''' 2000 (before 19 November)", "* '''Dates:''' 3–5 November 2000<ref name=\"tr-d1434\" />", 1)


def lst(t):
    t = t.replace("| 2000-11 || [[2000 Mega Weekend]] || 2000 (before 19 November) ||", "| 2000-11 || [[2000 Mega Weekend]] || 3–5 November 2000 ||", 1)
    for ev in ("2000 Coruscant Civil War", "2000 Mega Weekend"):
        t = re.sub(rf"^(\| [^\n]*\[\[{re.escape(ev)}\]\][^\n]*\|\| )\[\[Premiere - Death Star II\]\]", rf"\g<1>{JP}", t, count=1, flags=re.M)
    return t


edit("2000 Coruscant Civil War", hubfmt('<ref name="tr-d1417" />'))
edit("2000 Mega Weekend", hubfmt('<ref name="tr-d1441" />'))
edit("2000 Mega Weekend", mega)
edit("List of SWCCG tournaments", lst)
