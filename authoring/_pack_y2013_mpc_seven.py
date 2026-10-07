#!/usr/bin/env python3
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FULL = ROOT / "y2013-mpc-titles.tsv"
TSV = ROOT / "y2013-mpc-seven-titles.tsv"
OUT = ROOT / "y2013-mpc-seven.tgz"
MEDIA = ROOT / "y2013-mpc-media"
KEEP = {
    "2013 Match Play Championship p27 Mike D'Ambrosio DS.png",
    "2013 Match Play Championship p28 Mike D'Ambrosio LS.png",
    "2013 Match Play Championship p57 Scott Lingrell DS.png",
    "2013 Match Play Championship p58 Scott Lingrell LS.png",
    "2013 Match Play Championship p75 Nick Reisch LS.png",
    "2013 Match Play Championship p76 Nick Reisch DS.png",
    "2013 Match Play Championship p85 Greg Shaw DS.png",
    "2013 Match Play Championship p86 Greg Shaw LS.png",
    "2013 Match Play Championship p93 Peter Tenneson LS.png",
    "2013 Match Play Championship p94 Peter Tenneson DS.png",
    "2013 Match Play Championship p97 Michael Thomas LS.png",
    "2013 Match Play Championship p98 Michael Thomas DS.png",
    "2013 Match Play Championship p103 John Veasey LS.png",
    "2013 Match Play Championship p104 John Veasey DS.png",
}
PLAYERS = {
    "Mike D'Ambrosio",
    "Scott Lingrell",
    "Nick Reisch",
    "Greg Shaw",
    "Peter Tenneson",
    "Michael Thomas",
    "John Veasey",
}

rows = []
for line in FULL.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    title, rel = title.strip(), rel.strip().replace("\\", "/")
    keep = False
    if title == "2013 Match Play Championship":
        keep = True
    elif title in PLAYERS:
        keep = True
    elif title.startswith("2013 Match Play Championship Day 1 "):
        rest = title[len("2013 Match Play Championship Day 1 ") :]
        if any(rest.startswith(p + " ") for p in PLAYERS):
            keep = True
    if keep:
        rows.append((title, rel))

missing = [f"{t}\t{r}" for t, r in rows if not (ROOT / r).exists()]
ok = [(t, r) for t, r in rows if (ROOT / r).exists()]
TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
print("tsv n", len(ok), "missing", missing)
for t, r in ok:
    print(t, r)
with tarfile.open(OUT, "w:gz") as tar:
    for _t, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(TSV, arcname="y2013-mpc-seven-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2013-mpc-seven.sh", arcname="apply-2013-mpc-seven.sh")
    if MEDIA.exists():
        for p in MEDIA.iterdir():
            if p.name in KEEP:
                tar.add(p, arcname=f"y2013-mpc-seven-media/{p.name}")
print("packed", OUT, OUT.stat().st_size)
