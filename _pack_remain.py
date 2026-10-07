#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "y2022-2024-remain.tsv"
full = ROOT / "y2022-2024-titles.tsv"
tar_path = ROOT / "y2022-2024-remain.tar"
missing = []
n = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(full, arcname=full.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    n += 3
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _title, rel = line.split("\t", 1)
        p = ROOT / rel.strip()
        if not p.exists():
            missing.append(rel)
            continue
        tar.add(p, arcname=rel.strip().replace("\\", "/"))
        n += 1
print("tar", tar_path)
print("files", n, "bytes", tar_path.stat().st_size)
print("tsv rows", sum(1 for x in tsv.read_text(encoding="utf-8").splitlines() if x.strip()))
print("missing", len(missing))
for m in missing[:20]:
    print(" MISSING", m)
