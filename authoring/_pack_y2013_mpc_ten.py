#!/usr/bin/env python3
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FULL = ROOT / "y2013-mpc-titles.tsv"
TSV = ROOT / "y2013-mpc-ten-titles.tsv"
OUT = ROOT / "y2013-mpc-ten.tgz"
MEDIA = ROOT / "y2013-mpc-media"
KEEP = {
    "2013 Match Play Championship p29 Matt Fink LS.png",
    "2013 Match Play Championship p30 Matt Fink DS.png",
    "2013 Match Play Championship p49 Aaron Kinser LS.png",
    "2013 Match Play Championship p50 Aaron Kinser DS.png",
    "2013 Match Play Championship p53 Tuan Le DS.png",
    "2013 Match Play Championship p54 Tuan Le LS.png",
    "2013 Match Play Championship p59 Josh Mack DS.png",
    "2013 Match Play Championship p60 Josh Mack LS.png",
    "2013 Match Play Championship p63 Aaron Nelson LS.png",
    "2013 Match Play Championship p64 Aaron Nelson DS.png",
    "2013 Match Play Championship p65 Cuong Nguyen DS.png",
    "2013 Match Play Championship p66 Cuong Nguyen LS.png",
    "2013 Match Play Championship p67 Chris O'Hara DS.png",
    "2013 Match Play Championship p68 Chris O'Hara LS.png",
    "2013 Match Play Championship p69 Matt Paragano DS.png",
    "2013 Match Play Championship p70 Matt Paragano LS.png",
    "2013 Match Play Championship p77 Mike Richards LS.png",
    "2013 Match Play Championship p78 Mike Richards DS.png",
    "2013 Match Play Championship p83 Rustin Sharer DS.png",
    "2013 Match Play Championship p84 Rustin Sharer LS.png",
}
PLAYERS = {
    "Matt Fink",
    "Aaron Kinser",
    "Tuan Le",
    "Josh Mack",
    "Aaron Nelson",
    "Cuong Nguyen",
    "Chris O'Hara",
    "Matt Paragano",
    "Mike Richards",
    "Rustin Sharer",
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
    tar.add(TSV, arcname="y2013-mpc-ten-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2013-mpc-ten.sh", arcname="apply-2013-mpc-ten.sh")
    if MEDIA.exists():
        for p in MEDIA.iterdir():
            if p.name in KEEP:
                tar.add(p, arcname=f"y2013-mpc-ten-media/{p.name}")
print("packed", OUT, OUT.stat().st_size)
