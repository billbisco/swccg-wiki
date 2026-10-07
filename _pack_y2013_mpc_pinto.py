#!/usr/bin/env python3
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-mpc-pinto-titles.tsv"
OUT = ROOT / "y2013-mpc-pinto.tgz"
MEDIA = ROOT / "y2013-mpc-media"
KEEP = {
    "2013 Match Play Championship p71 Joe Pinto LS.png",
    "2013 Match Play Championship p72 Joe Pinto DS.png",
}

rows = []
for line in TSV.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    rows.append((title.strip(), rel.strip().replace("\\", "/")))
missing = [f"{t}\t{r}" for t, r in rows if not (ROOT / r).exists()]
ok = [(t, r) for t, r in rows if (ROOT / r).exists()]
print("tsv n", len(ok), "missing", missing)
with tarfile.open(OUT, "w:gz") as tar:
    for _t, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(TSV, arcname="y2013-mpc-pinto-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2013-mpc-pinto.sh", arcname="apply-2013-mpc-pinto.sh")
    if MEDIA.exists():
        for p in MEDIA.iterdir():
            if p.name in KEEP:
                tar.add(p, arcname=f"y2013-mpc-pinto-media/{p.name}")
print("packed", OUT, OUT.stat().st_size)
