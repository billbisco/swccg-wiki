"""Hand edits for tr-batch-11 on the built package (Claude 2026-10-25). python3 tr11_post.py /tmp/claude-0/tr-batch-11pkg
Winner lines for Grand Slam 2000 hubs whose infobox sits under == Format == (the builder now handles this)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import decktech_batch as b  # noqa: E402
import tr_world as W  # noqa: E402

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


def winner(rid, who, ev):
    def f(t):
        log = []
        n = W.hub_updates(t, {"id": rid}, [{"event": ev, "field": "winner", "value": who}], log)
        print(log)
        return n
    return f


edit("2000 Nashville Grand Slam", winner("d1227", "Chris Praskac", "2000 Nashville Grand Slam"))
edit("2000 Brussels Grand Slam", winner("d1133", "Martin Akesson", "2000 Brussels Grand Slam"))
