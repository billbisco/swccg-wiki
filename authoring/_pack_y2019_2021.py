#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "y2019-2021-titles.tsv"
tar_path = ROOT / "y2019-2021-qp2.tgz"
n = 0
missing = 0
with tarfile.open(tar_path, "w:gz") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(ROOT / "apply-2019-2021.sh", arcname="apply-2019-2021.sh")
    n += 2
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _t, rel = line.split("\t", 1)
        rel = rel.strip().replace("\\", "/")
        p = ROOT / rel
        if not p.exists():
            missing += 1
            print("MISSING", p)
            continue
        tar.add(p, arcname=rel)
        n += 1
print("tar", tar_path, "entries", n, "bytes", tar_path.stat().st_size, "missing", missing)
print("tsv", sum(1 for x in tsv.read_text(encoding="utf-8").splitlines() if x.strip()))
