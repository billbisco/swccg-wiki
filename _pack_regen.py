#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
titles = ROOT / "y2022-2024-titles.tsv"
redirs = ROOT / "y2022-2024-redirects.tsv"
combined = ROOT / "y2022-2024-regen.tsv"
lines = []
for p in (titles, redirs):
    lines.extend(x for x in p.read_text(encoding="utf-8").splitlines() if x.strip())
combined.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
tar_path = ROOT / "y2022-2024-regen.tar"
n = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(combined, arcname=combined.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    n += 2
    seen = set()
    for line in lines:
        _t, rel = line.split("\t", 1)
        rel = rel.strip()
        if rel in seen:
            continue
        seen.add(rel)
        p = ROOT / rel
        if p.exists():
            tar.add(p, arcname=rel.replace("\\", "/"))
            n += 1
    media = ROOT / "y2022-2024-media"
    if media.exists():
        for p in media.glob("*"):
            if p.is_file():
                tar.add(p, arcname=f"y2022-2024-media/{p.name}")
                n += 1
print("tar", tar_path, "files", n, "bytes", tar_path.stat().st_size, "tsv", len(lines))
