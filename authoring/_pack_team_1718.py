#!/usr/bin/env python3
"""Build team-1718-titles.tsv and pack team-1718.tgz."""
from __future__ import annotations

import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "y2017-2018-titles.tsv"
OUT_TSV = ROOT / "team-1718-titles.tsv"
OUT_TGZ = ROOT / "team-1718.tgz"

EXTRA = [
    ("Team USA", "pages/Team_USA.wiki"),
    ("Team Europe", "pages/Team_Europe.wiki"),
    ("Team North America", "pages/Team_North_America.wiki"),
    ("Category:Teams", "pages/Category_Teams.wiki"),
    ("Category:2017", "pages/Category_2017.wiki"),
    ("Category:2018", "pages/Category_2018.wiki"),
    ("2019 Outrider Cup", "pages/2019_Outrider_Cup.wiki"),
    ("2021 Outrider Cup", "pages/2021_Outrider_Cup.wiki"),
    ("2023 Outrider Cup III", "pages/2023_Outrider_Cup_III.wiki"),
    ("2026 Outrider Cup IV", "pages/2026_Outrider_Cup_IV.wiki"),
    ("2023 Online Retro Event", "pages/2023_Online_Retro_Event.wiki"),
    ("Timo Dusel", "pages/player-stubs/Timo_Dusel.wiki"),
    ("Joe Horbey", "pages/player-stubs/Joe_Horbey.wiki"),
    ("Ian Monteith", "pages/player-stubs/Ian_Monteith.wiki"),
    ("Jonny Chu", "pages/player-stubs/Jonny_Chu.wiki"),
    ("Paul Todd Feldman", "pages/player-stubs/Paul_Todd_Feldman.wiki"),
    ("Sean Luhks", "pages/player-stubs/Sean_Luhks.wiki"),
    ("Andy Talaga", "pages/player-stubs/Andy_Talaga.wiki"),
    ("Thomas Nguyen", "pages/player-stubs/Thomas_Nguyen.wiki"),
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("European Championships", "pages/European_Championships.wiki"),
]

rows: list[tuple[str, str]] = []
seen: dict[str, int] = {}
for line in BASE.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, rel = line.split("\t", 1)
    title, rel = title.strip(), rel.strip().replace("\\", "/")
    if title in seen:
        rows[seen[title]] = (title, rel)
    else:
        seen[title] = len(rows)
        rows.append((title, rel))
for title, rel in EXTRA:
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

OUT_TSV.write_text("".join(f"{t}\t{r}\n" for t, r in ok), encoding="utf-8", newline="\n")
print("tsv", OUT_TSV, "n", len(ok), "missing", len(missing))
for m in missing:
    print("MISSING", m)

with tarfile.open(OUT_TGZ, "w:gz") as tar:
    for _title, rel in ok:
        tar.add(ROOT / rel, arcname=rel)
    tar.add(OUT_TSV, arcname="team-1718-titles.tsv")
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-team-1718.sh", arcname="apply-team-1718.sh")
print("packed", OUT_TGZ, "bytes", OUT_TGZ.stat().st_size)
