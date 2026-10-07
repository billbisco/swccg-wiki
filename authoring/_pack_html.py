#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "y2022-2024-html-titles.tsv"
tar_path = ROOT / "y2022-2024-html.tar"
n = 0
missing = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    n += 2
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _t, rel = line.split("\t", 1)
        p = ROOT / rel.strip()
        if not p.exists():
            missing += 1
            continue
        tar.add(p, arcname=rel.strip().replace("\\", "/"))
        n += 1
print("tar", tar_path, "files", n, "bytes", tar_path.stat().st_size, "missing", missing)
print("tsv", sum(1 for x in tsv.read_text(encoding="utf-8").splitlines() if x.strip()))
