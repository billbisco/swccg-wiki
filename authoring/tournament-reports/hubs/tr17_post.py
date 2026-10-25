"""Hand edits for tr-batch-17 (Claude 2026-10-25). python3 tr17_post.py /tmp/claude-0/tr-batch-17pkg

d1671 (Steve Marshall, Phoenix 26 January 2001) was filed in batch 15 under the 13 January hub
"January 2001 Phoenix tournament". Batch 17 rebuilds it under "January 2001 Phoenix tournament (26 January)";
this removes the old d1671 rows from the 13 January hub and from every page that cited them."""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import decktech_batch as b  # noqa: E402

pk = Path(sys.argv[1])
tsv = next(pk.glob("y-*.tsv"))
OLD = "January 2001 Phoenix tournament"
API = "https://wiki.swccg.com/api.php?"
import tr_build as T  # noqa: E402
_d = json.load(open(Path(__file__).resolve().parents[1] / "decktech" / "d1671.json"))
_d.setdefault("id", "d1671")
REF = T.ref(_d)


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


def drop_rows(x, need_old):
    """Drop table rows citing tr-d1671 (on person pages only those linking the 13 January hub)."""
    keep = []
    for line in x.split("\n"):
        if line.startswith("|") and "tr-d1671" in line and (not need_old or f"[[{OLD}]]" in line):
            if keep and keep[-1] == "|-":
                keep.pop()
            continue
        keep.append(line)
    out = "\n".join(keep)
    if '<ref name="tr-d1671" />' in out and '<ref name="tr-d1671">' not in out:
        out = out.replace('<ref name="tr-d1671" />', REF, 1)  # hand the full ref to the first remaining use
    return out


def hub13(t):
    t = drop_rows(t, False)
    return re.sub(r"\n\* \[\[Steve Marshall Viper Turnss Dark Side Phoenix AZ 1-26 \(tournament report\)\]\][^\n]*", "", t)


edit(OLD, hub13)

# pages that link the old hub and cite d1671 (person pages)
r = json.load(urllib.request.urlopen(API + urllib.parse.urlencode({"action": "query", "list": "backlinks", "bltitle": OLD, "bllimit": 500, "format": "json", "formatversion": 2}), timeout=60))
for bl in r["query"]["backlinks"]:
    t = bl["title"]
    if t in (OLD, "List of SWCCG tournaments") or "(tournament report)" in t:
        continue
    p = pk / "pages" / (t.replace(" ", "_").replace("/", "%2F") + ".wiki")
    txt = p.read_text(encoding="utf-8") if p.exists() else b.live_text(t)
    if 'name="tr-d1671"' not in (txt or ""):
        continue

    edit(t, lambda x: drop_rows(x, True))
