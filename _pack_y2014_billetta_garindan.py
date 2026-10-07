#!/usr/bin/env python3
"""Leftover pack: 2014 Worlds Day 2 Brian Billetta DS Gyriadan -> Garindan."""
from __future__ import annotations

import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2014-billetta-garindan-titles.tsv"
OUT = ROOT / "y2014-billetta-garindan.tgz"
ROWS = [
    (
        "2014 Worlds Day 2 Brian Billetta DS Hunt Down",
        "pages/2014_Worlds_Day_2_Brian_Billetta_DS_Hunt_Down.wiki",
    ),
]


def main() -> None:
    missing = []
    ok = []
    for title, rel in ROWS:
        p = ROOT / rel
        if not p.exists():
            missing.append(f"{title}\t{rel}")
            continue
        ok.append((title, rel))
    if missing:
        raise SystemExit("MISSING\n" + "\n".join(missing))
    TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
    print("tsv", TSV, "n", len(ok))
    with tarfile.open(OUT, "w:gz") as tar:
        for _title, rel in ok:
            tar.add(ROOT / rel, arcname=rel)
        tar.add(TSV, arcname="y2014-billetta-garindan-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(ROOT / "apply-2014-billetta-garindan.sh", arcname="apply-2014-billetta-garindan.sh")
    print("packed", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
