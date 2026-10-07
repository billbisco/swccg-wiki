#!/usr/bin/env python3
"""Leftover pack: 2013 MPC Schwartz/Steve S. Username identity dests."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TSV = ROOT / "y2013-mpc-identity-titles.tsv"
OUT = ROOT / "y2013-mpc-identity.tgz"
ROWS = [
    (
        "2013 Match Play Championship",
        "pages/2013_Match_Play_Championship.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Matt Schmaltz LS Hidden Base",
        "pages/2013_Match_Play_Championship_Day_1_Matt_Schmaltz_LS_Hidden_Base.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Matt Schmaltz DS Imperial Occupation (V)",
        "pages/2013_Match_Play_Championship_Day_1_Matt_Schmaltz_DS_Imperial_Occupation_(V).wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Steve Skilton LS We'll Handle This",
        "pages/2013_Match_Play_Championship_Day_1_Steve_Skilton_LS_We'll_Handle_This.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Steve Skilton DS Contract Killers",
        "pages/2013_Match_Play_Championship_Day_1_Steve_Skilton_DS_Contract_Killers.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Schwartz LS Hidden Base",
        "pages/2013_Match_Play_Championship_Day_1_Schwartz_LS_Hidden_Base.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Schwartz DS Imperial Occupation (V)",
        "pages/2013_Match_Play_Championship_Day_1_Schwartz_DS_Imperial_Occupation_(V).wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Steve S. LS We'll Handle This",
        "pages/2013_Match_Play_Championship_Day_1_Steve_S._LS_We'll_Handle_This.wiki",
    ),
    (
        "2013 Match Play Championship Day 1 Steve S. DS Contract Killers",
        "pages/2013_Match_Play_Championship_Day_1_Steve_S._DS_Contract_Killers.wiki",
    ),
    ("Matt Schmaltz", "pages/player-stubs/Matt_Schmaltz.wiki"),
    ("Steve Skilton", "pages/player-stubs/Steve_Skilton.wiki"),
    ("Schwartz", "pages/player-stubs/Schwartz.wiki"),
    ("Steve S.", "pages/player-stubs/Steve_S..wiki"),
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
        tar.add(TSV, arcname="y2013-mpc-identity-titles.tsv")
        tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
        tar.add(
            ROOT / "apply-2013-mpc-identity.sh",
            arcname="apply-2013-mpc-identity.sh",
        )
    print("packed", OUT, OUT.stat().st_size, "n", len(ROWS))


if __name__ == "__main__":
    main()
