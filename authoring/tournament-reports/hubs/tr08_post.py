"""Hand edits for tr-batch-08 on the built package (Claude 2026-10-25). python3 tr08_post.py /tmp/claude-0/tr-batch-08pkg"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import decktech_batch as b  # noqa: E402

pk = Path(sys.argv[1])
tsv = next(pk.glob("y-*.tsv"))


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


def houston(t):
    t = re.sub(r"\n\|-\n\| 1st \|\| \[\[Joe Horbey\]\]<ref name=\"tr-d988\" />[^\n]*", "", t, count=1)
    return t.replace("| 1st || Unknown. Decipher's Grand Slam 2000 results page records no Star Wars CCG winner.<ref name=\"gs00\" />",
                     "| 1st || [[Joe Horbey]]<ref name=\"tr-d988\" /> (from [[Justin Warren]]'s report; Decipher's Grand Slam 2000 results page records no Star Wars CCG winner<ref name=\"gs00\" />)")


def mtview(t):
    t = t.replace("* '''Format:''' [[Premiere - Death Star II]]<ref name=\"dt-7975\" />",
                  "* '''Format:''' [[Sealed Deck]] (a pre-release; Ceder's sealed deck is Endor and Death Star II cards)<ref name=\"dt-7975\" />")
    return t.replace("* '''Date:''' June 2000 (24 June 2000 per Ceder's report title)", "* '''Date:''' 24 June 2000<ref name=\"tr-d949\" />")


def lst(t):
    t = t.replace("| 2000-06 || [[2000 Death Star II Pre-Release (Mountain View)]] || June 2000 || Mountain View, California || [[Premiere - Death Star II]] || —",
                  "| 2000-06 || [[2000 Death Star II Pre-Release (Mountain View)]] || 24 June 2000 || Mountain View, California || [[Sealed Deck]] || —")
    return t.replace("| 2000-06 || [[2000 Coruscant Regionals]] || 17 June 2000 ||  || [[Premiere - Endor]] || ",
                     "| 2000-06 || [[2000 Coruscant Regionals]] || 17 June 2000 || Cedar Grove, New Jersey || [[Premiere - Endor]] || [[John Lolli]] and [[Patrick Ziagos]] (co-champions)")


edit("2000 Houston Grand Slam", houston)
edit("2000 Death Star II Pre-Release (Mountain View)", mtview)
edit("List of SWCCG tournaments", lst)
