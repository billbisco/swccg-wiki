#!/usr/bin/env python3
"""Leftover pack: 2013 MPC Smith last-name collision retarget."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-mpc-smith-titles.tsv"
OUT = ROOT / "y2013-mpc-smith.tgz"
ROWS = [
    (
        "2013 Match Play Championship",
        "pages/2013_Match_Play_Championship.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Smith LS Communing",
        "pages/2013_Match_Play_Championship_Day_1_Smith_LS_Communing.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Smith DS Kessel",
        "pages/2013_Match_Play_Championship_Day_1_Smith_DS_Kessel.wiki",
    ),
    (
        "Smith (2013 Match Play Championship)",
        "pages/player-stubs/Smith_(2013_Match_Play_Championship).wiki",
    ),
]


def main() -> None:
    missing = [f"{t}\t{r}" for t, r in ROWS if not (ROOT / r).exists()]
    if missing:
        raise SystemExit("missing " + "; ".join(missing))
    TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ROWS), encoding="utf-8", newline="\n"
    )
    with tarfile.open(OUT, "w:gz") as tar:
        for _t, rel in ROWS:
            tar.add(ROOT / rel, arcname=rel)
        tar.add(TSV, arcname="y2013-mpc-smith-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(ROOT / "apply-2013-mpc-smith.sh", arcname="apply-2013-mpc-smith.sh")
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS))


if __name__ == "__main__":
    main()
