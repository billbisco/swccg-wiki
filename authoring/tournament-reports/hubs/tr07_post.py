"""Hand edits for tr-batch-07 (Claude 2026-10-25): the UK Nationals date was written as ISO by batch 5."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import decktech_batch as b  # noqa: E402
pk = Path(sys.argv[1])
tsv = next(pk.glob("y-*.tsv"))


def edit(title, fn):
    p = pk / "pages" / (title.replace(" ", "_") + ".wiki")
    if p.exists():
        t = p.read_text(encoding="utf-8")
    else:
        t = b.live_text(title)
        open(tsv, "a", encoding="utf-8").write(f"{title}\tpages/{p.name}\n")
    n = fn(t)
    print(("edited " if n != t else "UNCHANGED ") + title)
    p.write_text(n, encoding="utf-8")


edit("2000 UK National Championship", lambda t: t.replace("* '''Date:''' 2000-04-02<ref", "* '''Date:''' 2 April 2000<ref", 1))
edit("List of SWCCG tournaments", lambda t: t.replace("| 2000 || [[2000 UK National Championship]] || 2000 || United Kingdom ||",
                                                     "| 2000-04 || [[2000 UK National Championship]] || 2 April 2000 || Warwick, England ||", 1))
