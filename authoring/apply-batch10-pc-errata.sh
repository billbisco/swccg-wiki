#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch10-gifs

ARCHIVES=(
  Premiere-L-demotion-decipher-archive.gif
  Premiere-L-crashsitememorial-decipher-archive.gif
  CC-D-darkstrike-decipher-archive.gif
  Dagobah-L-descentintothedark-decipher-archive.gif
  Endor-L-deactivatetheshieldgenerator-decipher-archive.gif
  Endor-L-daughterofskywalker-decipher-archive.gif
  Hoth-D-crashlanding-decipher-archive.gif
  ANH-D-deathstartractorbeam-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-demotion.gif
  Premiere-L-crashsitememorial.gif
  CC-D-darkstrike.gif
  Dagobah-L-descentintothedark.gif
  Endor-L-deactivatetheshieldgenerator.gif
  Endor-L-daughterofskywalker.gif
  Hoth-D-crashlanding.gif
  ANH-D-deathstartractorbeam.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch10-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch10-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch10-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch10 (Demotion, Crash Site Memorial, Dark Strike, Descent Into The Dark, Deactivate The Shield Generator, Daughter Of Skywalker, Crash Landing, Death Star Tractor Beam); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch10-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch10-gifs
fi

edit "File:Premiere-L-demotion-decipher-archive.gif" "$PAGES/File_Premiere-L-demotion-decipher-archive.gif.wiki" "File: Decipher archive Original Demotion"
edit "File:Premiere-L-crashsitememorial-decipher-archive.gif" "$PAGES/File_Premiere-L-crashsitememorial-decipher-archive.gif.wiki" "File: Decipher archive Original Crash Site Memorial"
edit "File:CC-D-darkstrike-decipher-archive.gif" "$PAGES/File_CC-D-darkstrike-decipher-archive.gif.wiki" "File: Decipher archive Original Dark Strike"
edit "File:Dagobah-L-descentintothedark-decipher-archive.gif" "$PAGES/File_Dagobah-L-descentintothedark-decipher-archive.gif.wiki" "File: Decipher archive Original Descent Into The Dark"
edit "File:Endor-L-deactivatetheshieldgenerator-decipher-archive.gif" "$PAGES/File_Endor-L-deactivatetheshieldgenerator-decipher-archive.gif.wiki" "File: Decipher archive Original Deactivate The Shield Generator"
edit "File:Endor-L-daughterofskywalker-decipher-archive.gif" "$PAGES/File_Endor-L-daughterofskywalker-decipher-archive.gif.wiki" "File: Decipher archive Original Daughter Of Skywalker"
edit "File:Hoth-D-crashlanding-decipher-archive.gif" "$PAGES/File_Hoth-D-crashlanding-decipher-archive.gif.wiki" "File: Decipher archive Original Crash Landing"
edit "File:ANH-D-deathstartractorbeam-decipher-archive.gif" "$PAGES/File_ANH-D-deathstartractorbeam-decipher-archive.gif.wiki" "File: Decipher archive Original Death Star Tractor Beam"
edit "Demotion (Original)" "$PAGES/Demotion_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Demotion (PC Errata)" "$PAGES/Demotion_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Demotion" "$PAGES/Demotion.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Crash Site Memorial (Original)" "$PAGES/Crash_Site_Memorial_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Crash Site Memorial (PC Errata)" "$PAGES/Crash_Site_Memorial_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Crash Site Memorial" "$PAGES/Crash_Site_Memorial.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dark Strike (Original)" "$PAGES/Dark_Strike_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dark Strike (PC Errata)" "$PAGES/Dark_Strike_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dark Strike" "$PAGES/Dark_Strike.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Descent Into The Dark (Original)" "$PAGES/Descent_Into_The_Dark_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Descent Into The Dark (PC Errata)" "$PAGES/Descent_Into_The_Dark_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Descent Into The Dark" "$PAGES/Descent_Into_The_Dark.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Deactivate The Shield Generator (Original)" "$PAGES/Deactivate_The_Shield_Generator_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Deactivate The Shield Generator (PC Errata)" "$PAGES/Deactivate_The_Shield_Generator_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Deactivate The Shield Generator" "$PAGES/Deactivate_The_Shield_Generator.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Daughter Of Skywalker (Original)" "$PAGES/Daughter_Of_Skywalker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Daughter Of Skywalker (PC Errata)" "$PAGES/Daughter_Of_Skywalker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Daughter Of Skywalker" "$PAGES/Daughter_Of_Skywalker.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Crash Landing (Original)" "$PAGES/Crash_Landing_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Crash Landing (PC Errata)" "$PAGES/Crash_Landing_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Crash Landing" "$PAGES/Crash_Landing.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Death Star Tractor Beam (Original)" "$PAGES/Death_Star_Tractor_Beam_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Death Star Tractor Beam (PC Errata)" "$PAGES/Death_Star_Tractor_Beam_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Death Star Tractor Beam" "$PAGES/Death_Star_Tractor_Beam.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch10 (Demotion through Death Star Tractor Beam)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch10 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Demotion" \
  "Demotion (Original)" \
  "Demotion (PC Errata)" \
  "Crash Site Memorial" \
  "Crash Site Memorial (Original)" \
  "Crash Site Memorial (PC Errata)" \
  "Dark Strike" \
  "Dark Strike (Original)" \
  "Dark Strike (PC Errata)" \
  "Descent Into The Dark" \
  "Descent Into The Dark (Original)" \
  "Descent Into The Dark (PC Errata)" \
  "Deactivate The Shield Generator" \
  "Deactivate The Shield Generator (Original)" \
  "Deactivate The Shield Generator (PC Errata)" \
  "Daughter Of Skywalker" \
  "Daughter Of Skywalker (Original)" \
  "Daughter Of Skywalker (PC Errata)" \
  "Crash Landing" \
  "Crash Landing (Original)" \
  "Crash Landing (PC Errata)" \
  "Death Star Tractor Beam" \
  "Death Star Tractor Beam (Original)" \
  "Death Star Tractor Beam (PC Errata)" \
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
echo DONE_APPLY_BATCH10_PC_ERRATA
