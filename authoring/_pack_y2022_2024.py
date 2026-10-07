#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
tsv = ROOT / "y2022-2024-titles.tsv"
# include category stubs
extra = [
    ROOT / "pages" / "Category_2022.wiki",
    ROOT / "pages" / "Category_2023.wiki",
    ROOT / "pages" / "Category_2024.wiki",
    ROOT / "apply-tsv.sh",
]
tar_path = ROOT / "y2022-2024.tar"
n = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    for p in extra:
        if p.exists():
            tar.add(p, arcname=p.name if p.suffix == ".sh" else f"pages/{p.name}")
            n += 1
    for line in tsv.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _title, rel = line.split("\t", 1)
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
print("tar", tar_path, "files", n, "bytes", tar_path.stat().st_size)
