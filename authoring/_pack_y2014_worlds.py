#!/usr/bin/env python3
"""Pack y2014-worlds.tgz from y2014-worlds-titles.tsv plus PDF scans."""
from __future__ import annotations

import shutil
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2014-worlds-titles.tsv"
OUT = ROOT / "y2014-worlds.tgz"
UPLOAD = ROOT / "encyclopedia" / "pc-2014-worlds" / "upload"
MEDIA = ROOT / "y2014-worlds-media"

NAME_MAP = {
    "2014_Worlds_Day_3.pdf": "2014 Worlds Day 3.pdf",
    "2014_Worlds_Day_2_Part_1.pdf": "2014 Worlds Day 2 Part 1.pdf",
    "2014_Worlds_Day_2_Part_2.pdf": "2014 Worlds Day 2 Part 2.pdf",
    "2014_Worlds_Day_2_Part_3.pdf": "2014 Worlds Day 2 Part 3.pdf",
    "2014_Worlds_Chris_Terwilliger_Y4.pdf": "2014 Worlds Chris Terwilliger Y4.pdf",
}

MEDIA.mkdir(parents=True, exist_ok=True)
for src_name, dest_name in NAME_MAP.items():
    src = UPLOAD / src_name
    if not src.exists():
        raise SystemExit(f"missing PDF {src}")
    shutil.copy2(src, MEDIA / dest_name)
    print("media", dest_name, src.stat().st_size)

from _prep_2014_scans import main as prep_scans  # noqa: E402

prep_scans()

rows: list[tuple[str, str]] = []
seen: dict[str, int] = {}
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

missing = []
ok = []
for title, rel in rows:
    p = ROOT / rel
    if not p.exists():
        missing.append(f"{title}\t{rel}")
        continue
    ok.append((title, rel))

TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
print("tsv", TSV, "n", len(ok), "missing", len(missing))
for m in missing:
    print("MISSING", m)

with tarfile.open(OUT, "w:gz") as tar:
    for _title, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(TSV, arcname="y2014-worlds-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2014-worlds.sh", arcname="apply-2014-worlds.sh")
    tar.add(MEDIA, arcname="y2014-worlds-media")
print("packed", OUT, "bytes", OUT.stat().st_size)
