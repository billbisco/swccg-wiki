#!/usr/bin/env python3
"""Pack TSV-listed wiki files into outrider-teams.tgz."""
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "outrider-teams-titles.tsv"
out = ROOT / "outrider-teams.tgz"
missing = []
with tarfile.open(out, "w:gz") as tar:
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _title, rel = line.split("\t", 1)
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        tar.add(path, arcname=rel.replace("\\", "/"))
    tar.add(tsv, arcname="outrider-teams-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-outrider-teams.sh", arcname="apply-outrider-teams.sh")
print("packed", out, "missing", missing)
