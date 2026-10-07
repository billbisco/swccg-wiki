#!/usr/bin/env python3
"""Leftover pack: 2013 MPC hub + Day 1 decks after dest-note cleanup (no media)."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FULL = ROOT / "y2013-mpc-titles.tsv"
TSV = ROOT / "y2013-mpc-notes-titles.tsv"
OUT = ROOT / "y2013-mpc-notes.tgz"

rows = []
for line in FULL.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    title, rel = title.strip(), rel.strip().replace("\\", "/")
    if title == "2013 Match Play Championship" or title.startswith(
        "2013 Match Play Championship Day 1 "
    ):
        rows.append((title, rel))

missing = [f"{t}\t{r}" for t, r in rows if not (ROOT / r).exists()]
ok = [(t, r) for t, r in rows if (ROOT / r).exists()]
TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
print("tsv n", len(ok), "missing", missing)
with tarfile.open(OUT, "w:gz") as tar:
    for _t, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(TSV, arcname="y2013-mpc-notes-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2013-mpc-notes.sh", arcname="apply-2013-mpc-notes.sh")
print("packed", OUT, OUT.stat().st_size)
