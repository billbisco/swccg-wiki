#!/usr/bin/env python3
"""Leftover pack: 2013 MPC incomplete-name Day 1 sheets + hub + stubs."""
from __future__ import annotations
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FULL = ROOT / "y2013-mpc-titles.tsv"
TSV = ROOT / "y2013-mpc-names-titles.tsv"
OUT = ROOT / "y2013-mpc-names.tgz"
MEDIA = ROOT / "y2013-mpc-media"
PLAYERS = {
    "Tony G",
    "Jeremy G",
    "Gogolen",
    "HARPSTER",
    "Stephen Kin",
    "Jared",
    "Pistone",
    "Schwartz",
    "Shannon",
    "Steve S.",
    "Smith",
    "Sokol",
    "BTwigg",
    "Mauer",
    "SAN",
    "Micah Wall",
    "Steve Wall",
    "Alex W",
    "WIRFS",
}
KEEP = {
    "2013 Match Play Championship p31 Tony G LS.png",
    "2013 Match Play Championship p32 Tony G DS.png",
    "2013 Match Play Championship p33 Jeremy G DS.png",
    "2013 Match Play Championship p34 Jeremy G LS.png",
    "2013 Match Play Championship p35 Gogolen LS.png",
    "2013 Match Play Championship p36 Gogolen DS.png",
    "2013 Match Play Championship p37 HARPSTER LS.png",
    "2013 Match Play Championship p38 HARPSTER DS.png",
    "2013 Match Play Championship p47 Stephen Kin LS.png",
    "2013 Match Play Championship p48 Stephen Kin DS.png",
    "2013 Match Play Championship p51 Jared DS.png",
    "2013 Match Play Championship p52 Jared LS.png",
    "2013 Match Play Championship p73 Pistone LS.png",
    "2013 Match Play Championship p74 Pistone DS.png",
    "2013 Match Play Championship p79 Schwartz LS.png",
    "2013 Match Play Championship p80 Schwartz DS.png",
    "2013 Match Play Championship p81 Shannon DS.png",
    "2013 Match Play Championship p82 Shannon LS.png",
    "2013 Match Play Championship p87 Steve S. LS.png",
    "2013 Match Play Championship p88 Steve S. DS.png",
    "2013 Match Play Championship p89 Smith DS.png",
    "2013 Match Play Championship p90 Smith LS.png",
    "2013 Match Play Championship p91 Sokol LS.png",
    "2013 Match Play Championship p92 Sokol DS.png",
    "2013 Match Play Championship p95 BTwigg DS.png",
    "2013 Match Play Championship p96 BTwigg LS.png",
    "2013 Match Play Championship p101 Mauer LS.png",
    "2013 Match Play Championship p102 Mauer DS.png",
    "2013 Match Play Championship p107 SAN LS.png",
    "2013 Match Play Championship p108 SAN DS.png",
    "2013 Match Play Championship p109 Micah Wall LS.png",
    "2013 Match Play Championship p110 Micah Wall DS.png",
    "2013 Match Play Championship p111 Steve Wall DS.png",
    "2013 Match Play Championship p112 Steve Wall LS.png",
    "2013 Match Play Championship p113 Alex W LS.png",
    "2013 Match Play Championship p114 Alex W DS.png",
    "2013 Match Play Championship p115 WIRFS DS.png",
    "2013 Match Play Championship p116 WIRFS LS.png",
}

rows = []
for line in FULL.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    title, rel = title.strip(), rel.strip().replace("\\", "/")
    keep = False
    if title == "2013 Match Play Championship":
        keep = True
    elif title in PLAYERS:
        keep = True
    elif title.startswith("2013 Match Play Championship Day 1 "):
        rest = title[len("2013 Match Play Championship Day 1 ") :]
        if any(rest.startswith(p + " ") for p in PLAYERS):
            keep = True
    if keep:
        rows.append((title, rel))

missing = [f"{t}\t{r}" for t, r in rows if not (ROOT / r).exists()]
ok = [(t, r) for t, r in rows if (ROOT / r).exists()]
TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
print("tsv n", len(ok), "missing", missing)
for t, r in ok:
    print(t, r)
with tarfile.open(OUT, "w:gz") as tar:
    for _t, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(TSV, arcname="y2013-mpc-names-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-2013-mpc-names.sh", arcname="apply-2013-mpc-names.sh")
    if MEDIA.exists():
        for p in MEDIA.iterdir():
            if p.name in KEEP:
                tar.add(p, arcname=f"y2013-mpc-names-media/{p.name}")
print("packed", OUT, OUT.stat().st_size)
