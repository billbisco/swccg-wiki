"""Hand edits for tr-batch-09 on the built package (Claude 2026-10-25). python3 tr09_post.py /tmp/claude-0/tr-batch-09pkg"""
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


def lst(t):
    return t.replace("| 2000-07 || [[2000 Origins Open]] || 15 July 2000 ||  ||",
                     "| 2000-07 || [[2000 Origins Open]] || 15 July 2000 || Origins, Columbus, Ohio ||")


edit("List of SWCCG tournaments", lst)
