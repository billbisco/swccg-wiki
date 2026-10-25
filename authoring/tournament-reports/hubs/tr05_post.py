"""Hand edits for tr-batch-05 on the built package (Claude 2026-10-25). python3 tr05_post.py /tmp/claude-0/tr-batch-05pkg"""
import sys
from pathlib import Path

pk = Path(sys.argv[1]) / "pages"


def edit(title, fn):
    p = pk / (title.replace(" ", "_") + ".wiki")
    t = p.read_text(encoding="utf-8")
    n = fn(t)
    print(("edited " if n != t else "UNCHANGED ") + title)
    p.write_text(n, encoding="utf-8")


def lst(t):
    t = t.replace("| 2000-04 || [[2000 Georgia State Championship]] || 25 March 2000 ||", "| 2000-03 || [[2000 Georgia State Championship]] || 25 March 2000 ||")
    t = t.replace("| 2000-03 || [[2000 Illinois State Championship]] || 1 April 2000 ||", "| 2000-04 || [[2000 Illinois State Championship]] || 1 April 2000 ||")
    return t


def boston(t):
    return t.replace("| 1st || Unknown. Decipher's Grand Slam 2000 results page records no Star Wars CCG winner.<ref name=\"gs00\" />",
                     "| 1st || [[Matt Sokol]]<ref name=\"tr-d496\" /> (from [[Michael Hawley]]'s report; Decipher's Grand Slam 2000 results page records no Star Wars CCG winner<ref name=\"gs00\" />)")


edit("List of SWCCG tournaments", lst)
edit("2000 Boston Grand Slam", boston)
