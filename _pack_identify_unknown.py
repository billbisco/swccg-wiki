#!/usr/bin/env python3
"""Pack leftover TSV + wikitext for identify-unknown apply."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "identify-unknown-titles.tsv"
OUT = ROOT / "identify-unknown.tgz"


def main() -> None:
    rows = []
    for line in TSV.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        title, rel = line.split("\t", 1)
        rows.append((title, rel))
    missing = [p for _t, p in rows if not (ROOT / p).exists()]
    if missing:
        raise SystemExit("missing " + "; ".join(missing))
    with tarfile.open(OUT, "w:gz") as tar:
        seen = set()
        for _t, rel in rows:
            if rel in seen:
                continue
            seen.add(rel)
            tar.add(ROOT / rel, arcname=rel)
        tar.add(TSV, arcname="identify-unknown-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(ROOT / "apply-identify-unknown.sh", arcname="apply-identify-unknown.sh")
    print("packed", OUT, OUT.stat().st_size, "n", len(rows))


if __name__ == "__main__":
    main()
