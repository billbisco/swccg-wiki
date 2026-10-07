"""Pack TSV-listed pages + apply script into a tar for VPS scp."""
from __future__ import annotations

import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "decipher-worlds-titles.tsv"
out = ROOT / "decipher-worlds.tar"
with tarfile.open(out, "w") as tar:
    tar.add(tsv, arcname="decipher-worlds-titles.tsv")
    tar.add(ROOT / "apply-decipher-worlds.sh", arcname="apply-decipher-worlds.sh")
    missing = []
    n = 0
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        title, rel = line.split("\t", 1)
        path = ROOT / rel
        if not path.is_file():
            missing.append(rel)
            continue
        tar.add(path, arcname=rel.replace("\\", "/"))
        n += 1
print("packed", n, "pages", out, "bytes", out.stat().st_size)
if missing:
    print("MISSING", len(missing))
    for m in missing:
        print(" ", m)
