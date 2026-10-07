#!/usr/bin/env python3
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2014-nats-titles.tsv"
OUT = ROOT / "y2014-nats.tgz"
MEDIA = ROOT / "y2014-nats-media"

rows = []
seen = {}
for line in TSV.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    title, rel = title.strip(), rel.strip().replace("\\", "/")
    if title in seen:
        rows[seen[title]] = (title, rel)
    else:
        seen[title] = len(rows)
        rows.append((title, rel))

missing, ok = [], []
for title, rel in rows:
    if not (ROOT / rel).exists():
        missing.append(f"{title}\t{rel}")
    else:
        ok.append((title, rel))
TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
print("tsv", TSV, "n", len(ok), "missing", len(missing))
for m in missing:
    print("MISSING", m)
with tarfile.open(OUT, "w:gz") as tar:
    for _title, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(TSV, arcname="y2014-nats-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2014-nats.sh", arcname="apply-2014-nats.sh")
    if MEDIA.exists():
        for p in MEDIA.iterdir():
            tar.add(p, arcname=f"y2014-nats-media/{p.name}")
print("packed", OUT, "bytes", OUT.stat().st_size)
