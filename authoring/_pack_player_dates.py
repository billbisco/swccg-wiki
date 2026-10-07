#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "player-dates-titles.tsv"
tar_path = ROOT / "player-dates.tar"
n = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    n += 2
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _title, rel = line.split("\t", 1)
        rel = rel.replace("\\", "/").strip()
        p = ROOT / rel
        if p.exists():
            tar.add(p, arcname=rel)
            n += 1
print("tar", tar_path, "files", n, "bytes", tar_path.stat().st_size)
