#!/usr/bin/env python3
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = [
    ("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"),
    ("2022 U.S. National Championship", "pages/2022_U.S._National_Championship.wiki"),
    ("2022 Endor Grand Prix", "pages/2022_Endor_Grand_Prix.wiki"),
    ("2022 Sixth Annual GEMPC", "pages/2022_Sixth_Annual_GEMPC.wiki"),
    ("2024 European Championship", "pages/2024_European_Championship.wiki"),
    ("2022 US Nationals Logan Pietig DS BHBM", "pages/2022_US_Nationals_Logan_Pietig_DS_BHBM.wiki"),
    ("2022 US Nationals Logan Pietig LS Pyre", "pages/2022_US_Nationals_Logan_Pietig_LS_Pyre.wiki"),
    ("2022 US Nationals Cory Lauer DS CCT", "pages/2022_US_Nationals_Cory_Lauer_DS_CCT.wiki"),
    ("2022 US Nationals Cory Lauer LS QMC", "pages/2022_US_Nationals_Cory_Lauer_LS_QMC.wiki"),
    ("2022 US Nationals Will Scinocca DS SYCFA", "pages/2022_US_Nationals_Will_Scinocca_DS_SYCFA.wiki"),
    ("2022 US Nationals Will Scinocca LS Y4O", "pages/2022_US_Nationals_Will_Scinocca_LS_Y4O.wiki"),
    ("2022 US Nationals Stephen Fulner DS Combat", "pages/2022_US_Nationals_Stephen_Fulner_DS_Combat.wiki"),
    ("2022 EGP Cal Alrdred LS Yoda Comm", "pages/2022_EGP_Cal_Alrdred_LS_Yoda_Comm.wiki"),
    ("2022 GEMPC Lavinge DS AOBS", "pages/2022_GEMPC_Lavinge_DS_AOBS.wiki"),
    ("2024 European Championship Eric Spijskma LS zero hour", "pages/2024_European_Championship_Eric_Spijskma_LS_zero_hour.wiki"),
]
for name in [
    "Stephen Fulner",
    "Adam Schellberg",
    "Dan Drentlaw",
    "Eric Nelson",
    "Thang Le",
    "Stewart Yoo",
    "Ben Herold",
    "Fulner",
    "Cal Alrdred",
    "Huo 2022 Nats",
    "Huo 2022 Nats No Idea",
    "Miyashiro Nats 22",
    "Olson Nationals",
    "Kessling Old Allies Nationals",
    "Koenig Nationals Karl Koenig",
    "Eric Spijskma",
    "Schellberg",
    "Drentlaw",
    "Yoo",
    "Herold",
    "William Scinocca",
]:
    rows.append((name, f"pages/player-stubs/{name.replace(' ', '_')}.wiki"))

tsv = ROOT / "y2022-remaining-players.tsv"
tsv.write_text("\n".join(f"{t}\t{r}" for t, r in rows) + "\n", encoding="utf-8", newline="\n")
print("tsv", len(rows))
missing = [r for t, r in rows if not (ROOT / r).exists()]
for m in missing:
    print("MISSING", m)

tar_path = ROOT / "y2022-remaining-players.tar"
n = 0
with tarfile.open(tar_path, "w") as tar:
    tar.add(tsv, arcname=tsv.name)
    tar.add(ROOT / "apply-tsv.sh", arcname="apply-tsv.sh")
    tar.add(ROOT / "apply-y2022-remaining-players.sh", arcname="apply-y2022-remaining-players.sh")
    n += 3
    for t, rel in rows:
        p = ROOT / rel
        tar.add(p, arcname=rel.replace("\\", "/"))
        n += 1
print("tar", tar_path, "files", n, "bytes", tar_path.stat().st_size)
