"""Hand edits for tr-batch-15 (Claude 2026-10-25): the I-10 Cup's vague date takes the reports' range (the builder now does this)."""
import sys
from pathlib import Path

pk = Path(sys.argv[1]) / "pages"


def edit(title, fn):
    p = pk / (title.replace(" ", "_") + ".wiki")
    t = p.read_text(encoding="utf-8")
    n = fn(t)
    print(("edited " if n != t else "UNCHANGED ") + title)
    p.write_text(n, encoding="utf-8")


edit("2001 I-10 Cup", lambda t: t.replace("* '''Dates:''' January 2001 (before 22 January)", "* '''Dates:''' 20–21 January 2001<ref name=\"tr-d1666\" />", 1))
edit("List of SWCCG tournaments", lambda t: t.replace("| 2001-01 || [[2001 I-10 Cup]] || January 2001 (before 22 January) || Arizona ||",
                                                     "| 2001-01 || [[2001 I-10 Cup]] || 20–21 January 2001 || Tucson and Chandler, Arizona ||", 1))
