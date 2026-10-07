#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch27-gifs

ARCHIVES=(
  Hoth-D-probeantennae-decipher-archive.gif
  Hoth-D-probedroid-decipher-archive.gif
  Hoth-D-probedroidlaser-decipher-archive.gif
  ANewHope-D-programtrap-decipher-archive.gif
  Premiere-D-preciseattack-decipher-archive.gif
  CloudCity-D-projectivetelepathy-decipher-archive.gif
  SpecialEdition-D-prideoftheempire-decipher-archive.gif
  Premiere-L-protontorpedoes-decipher-archive.gif
  JabbasPalace-L-pucumirthryss-decipher-archive.gif
  Hoth-L-powerharpoon-decipher-archive.gif
  Hoth-L-planetdefenderioncannon-decipher-archive.gif
)
HT_FILES=(
  Hoth-D-probeantennae.gif
  Hoth-D-probedroid.gif
  Hoth-D-probedroidlaser.gif
  ANH-D-programtrap.gif
  Premiere-D-preciseattack.gif
  CC-D-projectivetelepathy.gif
  SE-D-prideoftheempire.gif
  Premiere-L-protontorpedoes.gif
  JP-L-pucumirthryss.gif
  Hoth-L-powerharpoon.gif
  Hoth-L-planetdefenderioncannon.gif
)

strip_bom() {
  python3 - "$1" <<'INNER'
from pathlib import Path
import sys, re
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
m = re.search(r"\|notes=(.*?)(\n\|[a-z_]+=|\n\}\})", text, re.S)
if m and re.search(r"\[\[File:[^\]]*\.gif", m.group(1), re.I):
    raise SystemExit(f"FATAL: gif File embed in notes of {p.name}")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
INNER
}
edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}
ht_hex() {
  local HT_FILE="$1"
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -type f -name "'"$HT_FILE"'" | head -1); if [ -n "$f" ]; then sha1sum "$f" | awk "{print \$1}"; else echo MISSING; fi'
}

echo "== Holotable BEFORE =="
declare -a HT_BEFORE
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht"); echo "ht_before $ht=$h"
  test -n "$h" && test "$h" != "MISSING"
  HT_BEFORE+=("$h")
done

mkdir -p "$STAGE"; rm -f "$STAGE"/*
for a in "${ARCHIVES[@]}"; do
  test -f "$ROOT/set-card-art/$a"
  cp -f "$ROOT/set-card-art/$a" "$STAGE/$a"
done
for ht in "${HT_FILES[@]}"; do
  if [ -f "$STAGE/$ht" ]; then echo "REFUSING Holotable $ht"; exit 1; fi
done

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch27-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch27-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch27-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch27 (Probe Antennae through Planet Defender Ion Cannon); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch27-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch27-gifs
fi

edit "File:Hoth-D-probeantennae-decipher-archive.gif" "$PAGES/File_Hoth-D-probeantennae-decipher-archive.gif.wiki" "File: Decipher archive Original Probe Antennae"
edit "File:Hoth-D-probedroid-decipher-archive.gif" "$PAGES/File_Hoth-D-probedroid-decipher-archive.gif.wiki" "File: Decipher archive Original Probe Droid"
edit "File:Hoth-D-probedroidlaser-decipher-archive.gif" "$PAGES/File_Hoth-D-probedroidlaser-decipher-archive.gif.wiki" "File: Decipher archive Original Probe Droid Laser"
edit "File:ANewHope-D-programtrap-decipher-archive.gif" "$PAGES/File_ANewHope-D-programtrap-decipher-archive.gif.wiki" "File: Decipher archive Original Program Trap"
edit "File:Premiere-D-preciseattack-decipher-archive.gif" "$PAGES/File_Premiere-D-preciseattack-decipher-archive.gif.wiki" "File: Decipher archive Original Precise Attack"
edit "File:CloudCity-D-projectivetelepathy-decipher-archive.gif" "$PAGES/File_CloudCity-D-projectivetelepathy-decipher-archive.gif.wiki" "File: Decipher archive Original Projective Telepathy"
edit "File:SpecialEdition-D-prideoftheempire-decipher-archive.gif" "$PAGES/File_SpecialEdition-D-prideoftheempire-decipher-archive.gif.wiki" "File: Decipher archive Original Pride Of The Empire"
edit "File:Premiere-L-protontorpedoes-decipher-archive.gif" "$PAGES/File_Premiere-L-protontorpedoes-decipher-archive.gif.wiki" "File: Decipher archive Original Proton Torpedoes"
edit "File:JabbasPalace-L-pucumirthryss-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-pucumirthryss-decipher-archive.gif.wiki" "File: Decipher archive Original Pucumir Thryss"
edit "File:Hoth-L-powerharpoon-decipher-archive.gif" "$PAGES/File_Hoth-L-powerharpoon-decipher-archive.gif.wiki" "File: Decipher archive Original Power Harpoon"
edit "File:Hoth-L-planetdefenderioncannon-decipher-archive.gif" "$PAGES/File_Hoth-L-planetdefenderioncannon-decipher-archive.gif.wiki" "File: Decipher archive Original Planet Defender Ion Cannon"

edit "Probe Antennae (Original)" "$PAGES/Probe_Antennae_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Probe Antennae (PC Errata)" "$PAGES/Probe_Antennae_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Probe Antennae" "$PAGES/Probe_Antennae.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Probe Droid (Original)" "$PAGES/Probe_Droid_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Probe Droid (PC Errata)" "$PAGES/Probe_Droid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Probe Droid" "$PAGES/Probe_Droid.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Probe Droid Laser (Original)" "$PAGES/Probe_Droid_Laser_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Probe Droid Laser (PC Errata)" "$PAGES/Probe_Droid_Laser_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Probe Droid Laser" "$PAGES/Probe_Droid_Laser.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Program Trap (Original)" "$PAGES/Program_Trap_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Program Trap (PC Errata)" "$PAGES/Program_Trap_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Program Trap" "$PAGES/Program_Trap.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Precise Attack (Original)" "$PAGES/Precise_Attack_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Precise Attack (PC Errata)" "$PAGES/Precise_Attack_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Precise Attack" "$PAGES/Precise_Attack.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Projective Telepathy (Original)" "$PAGES/Projective_Telepathy_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Projective Telepathy (PC Errata)" "$PAGES/Projective_Telepathy_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Projective Telepathy" "$PAGES/Projective_Telepathy.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Pride Of The Empire (Original)" "$PAGES/Pride_Of_The_Empire_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Pride Of The Empire (PC Errata)" "$PAGES/Pride_Of_The_Empire_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Pride Of The Empire" "$PAGES/Pride_Of_The_Empire.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Proton Torpedoes (Original)" "$PAGES/Proton_Torpedoes_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Proton Torpedoes (PC Errata)" "$PAGES/Proton_Torpedoes_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Proton Torpedoes" "$PAGES/Proton_Torpedoes.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Pucumir Thryss (Original)" "$PAGES/Pucumir_Thryss_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Pucumir Thryss (PC Errata)" "$PAGES/Pucumir_Thryss_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Pucumir Thryss" "$PAGES/Pucumir_Thryss.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Power Harpoon (Original)" "$PAGES/Power_Harpoon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Power Harpoon (PC Errata)" "$PAGES/Power_Harpoon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Power Harpoon" "$PAGES/Power_Harpoon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Planet Defender Ion Cannon (Original)" "$PAGES/Planet_Defender_Ion_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Planet Defender Ion Cannon (PC Errata)" "$PAGES/Planet_Defender_Ion_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Planet Defender Ion Cannon" "$PAGES/Planet_Defender_Ion_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch27 (Probe Antennae through Planet Defender Ion Cannon)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch27 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Probe Antennae" \
  "Probe Antennae (Original)" \
  "Probe Antennae (PC Errata)" \
  "Probe Droid" \
  "Probe Droid (Original)" \
  "Probe Droid (PC Errata)" \
  "Probe Droid Laser" \
  "Probe Droid Laser (Original)" \
  "Probe Droid Laser (PC Errata)" \
  "Program Trap" \
  "Program Trap (Original)" \
  "Program Trap (PC Errata)" \
  "Precise Attack" \
  "Precise Attack (Original)" \
  "Precise Attack (PC Errata)" \
  "Projective Telepathy" \
  "Projective Telepathy (Original)" \
  "Projective Telepathy (PC Errata)" \
  "Pride Of The Empire" \
  "Pride Of The Empire (Original)" \
  "Pride Of The Empire (PC Errata)" \
  "Proton Torpedoes" \
  "Proton Torpedoes (Original)" \
  "Proton Torpedoes (PC Errata)" \
  "Pucumir Thryss" \
  "Pucumir Thryss (Original)" \
  "Pucumir Thryss (PC Errata)" \
  "Power Harpoon" \
  "Power Harpoon (Original)" \
  "Power Harpoon (PC Errata)" \
  "Planet Defender Ion Cannon" \
  "Planet Defender Ion Cannon (Original)" \
  "Planet Defender Ion Cannon (PC Errata)" \
  "Errata" \
  "PC Errata"
do
  echo "purge $t"; purge "$t"
done
for a in "${ARCHIVES[@]}"; do purge "File:$a"; done
for ht in "${HT_FILES[@]}"; do purge "File:$ht"; done

echo "== Holotable AFTER =="
i=0
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht"); echo "ht_after $ht=$h"
  test "$h" = "${HT_BEFORE[$i]}"
  i=$((i+1))
done
echo HOLOTABLE_OK
echo DONE_APPLY_BATCH27_PC_ERRATA
