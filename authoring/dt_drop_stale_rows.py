"""Drop table rows that still show a deck under an old format after era_format relabels it (2026-10-22).

  python3 dt_drop_stale_rows.py TSV [PKGDIR]

A rebuilt player page / catalog keeps the live row (old format) and adds the new one; this removes the row whose
format cell differs from the deck's current format, on every page listed in TSV (and its copy in PKGDIR)."""
import json, re, sys
from pathlib import Path
import decktech_batch as db

fmt = {}
for f in db.DECKS.glob("*.json"):
    d = json.loads(f.read_text(encoding="utf-8"))
    fmt[db.dest_title(d)] = d.get("format")
tsv, pkg = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)
total = 0
for line in Path(tsv).read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, path = line.split("\t")[:2]
    for p in [Path(path)] + ([Path(pkg) / path] if pkg else []):
        if not p.exists():
            continue
        out, n = [], 0
        for row in p.read_text(encoding="utf-8").split("\n"):
            m = re.search(r"\|\| \[\[(Premiere - [^\]|]+|Episode I[^\]|]*)\]\] \|\| \[\[([^\]|]+)", row)
            if row.startswith("|") and m and m.group(2) in fmt and fmt[m.group(2)] and fmt[m.group(2)] != m.group(1):
                n += 1
                if out and out[-1] == "|-":
                    out.pop()
                continue
            # a format page's decklist bullet for a deck now filed under another format
            b = re.match(r"\* \[\[([^\]|]+)\]\]", row)
            if title.startswith(("Premiere - ", "Episode I")) and b and fmt.get(b.group(1)) and fmt[b.group(1)] != title:
                n += 1
                continue
            out.append(row)
        if n:
            p.write_text("\n".join(out), encoding="utf-8")
            if p == Path(path):
                total += n
print("stale format rows dropped:", total)
