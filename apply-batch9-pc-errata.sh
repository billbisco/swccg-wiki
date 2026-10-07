#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch9-gifs

ARCHIVES=(
  Endor-L-corporaljanse-decipher-archive.gif
  CC-L-chasmwalkway-decipher-archive.gif
  CC-D-chasmwalkway-decipher-archive.gif
  ANH-D-dannikjerriko-decipher-archive.gif
  ANH-D-danzborin-decipher-archive.gif
  Premiere-D-darkjedilightsaber-decipher-archive.gif
  Premiere-D-darthvader-decipher-archive.gif
  Premiere-D-darkhours-decipher-archive.gif
  Hoth-D-deathsquadron-decipher-archive.gif
  Dagobah-D-dengar-decipher-archive.gif
  Dagobah-D-dengarsblastercarbine-decipher-archive.gif
  JP-D-dengarsmodifiedriotgun-decipher-archive.gif
  Hoth-L-derekhobbieklivian-decipher-archive.gif
)
HT_FILES=(
  Endor-L-corporaljanse.gif
  CC-L-cloudcitychasmwalkway.gif
  CC-D-cloudcitychasmwalkway.gif
  ANH-D-dannikjerriko.gif
  ANH-D-danzborin.gif
  Premiere-D-darkjedilightsaber.gif
  Premiere-D-darthvader.gif
  Premiere-D-darkhours.gif
  Hoth-D-deathsquadron.gif
  Dagobah-D-dengar.gif
  Dagobah-D-dengarsblastercarbine.gif
  JP-D-dengarsmodifiedriotgun.gif
  Hoth-L-derekhobbieklivian.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch9-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch9-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch9-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch9 (Corporal Janse, Cloud City: Chasm Walkway Light+Dark, Dannik Jerriko, Danz Borin, Dark Jedi Lightsaber, Darth Vader, Dark Hours, Death Squadron, Dengar, Dengar's Blaster Carbine, Dengar's Modified Riot Gun, Derek 'Hobbie' Klivian); flush crop + flood bleach #FFF. DO NOT replace Holotable. Chasm Light from 2004 Decipher backup (Wayback CDX miss)."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch9-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch9-gifs
fi

edit "File:Endor-L-corporaljanse-decipher-archive.gif" "$PAGES/File_Endor-L-corporaljanse-decipher-archive.gif.wiki" "File: Decipher archive Original Corporal Janse"
edit "File:CC-L-chasmwalkway-decipher-archive.gif" "$PAGES/File_CC-L-chasmwalkway-decipher-archive.gif.wiki" "File: Decipher archive Original Cloud City: Chasm Walkway"
edit "File:CC-D-chasmwalkway-decipher-archive.gif" "$PAGES/File_CC-D-chasmwalkway-decipher-archive.gif.wiki" "File: Decipher archive Original Cloud City: Chasm Walkway (Dark)"
edit "File:ANH-D-dannikjerriko-decipher-archive.gif" "$PAGES/File_ANH-D-dannikjerriko-decipher-archive.gif.wiki" "File: Decipher archive Original Dannik Jerriko"
edit "File:ANH-D-danzborin-decipher-archive.gif" "$PAGES/File_ANH-D-danzborin-decipher-archive.gif.wiki" "File: Decipher archive Original Danz Borin"
edit "File:Premiere-D-darkjedilightsaber-decipher-archive.gif" "$PAGES/File_Premiere-D-darkjedilightsaber-decipher-archive.gif.wiki" "File: Decipher archive Original Dark Jedi Lightsaber"
edit "File:Premiere-D-darthvader-decipher-archive.gif" "$PAGES/File_Premiere-D-darthvader-decipher-archive.gif.wiki" "File: Decipher archive Original Darth Vader"
edit "File:Premiere-D-darkhours-decipher-archive.gif" "$PAGES/File_Premiere-D-darkhours-decipher-archive.gif.wiki" "File: Decipher archive Original Dark Hours"
edit "File:Hoth-D-deathsquadron-decipher-archive.gif" "$PAGES/File_Hoth-D-deathsquadron-decipher-archive.gif.wiki" "File: Decipher archive Original Death Squadron"
edit "File:Dagobah-D-dengar-decipher-archive.gif" "$PAGES/File_Dagobah-D-dengar-decipher-archive.gif.wiki" "File: Decipher archive Original Dengar"
edit "File:Dagobah-D-dengarsblastercarbine-decipher-archive.gif" "$PAGES/File_Dagobah-D-dengarsblastercarbine-decipher-archive.gif.wiki" "File: Decipher archive Original Dengar's Blaster Carbine"
edit "File:JP-D-dengarsmodifiedriotgun-decipher-archive.gif" "$PAGES/File_JP-D-dengarsmodifiedriotgun-decipher-archive.gif.wiki" "File: Decipher archive Original Dengar's Modified Riot Gun"
edit "File:Hoth-L-derekhobbieklivian-decipher-archive.gif" "$PAGES/File_Hoth-L-derekhobbieklivian-decipher-archive.gif.wiki" "File: Decipher archive Original Derek 'Hobbie' Klivian"
edit "Corporal Janse (Original)" "$PAGES/Corporal_Janse_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Corporal Janse (PC Errata)" "$PAGES/Corporal_Janse_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Corporal Janse" "$PAGES/Corporal_Janse.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Cloud City: Chasm Walkway (Original)" "$PAGES/Cloud_City:_Chasm_Walkway_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Cloud City: Chasm Walkway (PC Errata)" "$PAGES/Cloud_City:_Chasm_Walkway_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Cloud City: Chasm Walkway" "$PAGES/Cloud_City:_Chasm_Walkway.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Cloud City: Chasm Walkway (Dark) (Original)" "$PAGES/Cloud_City:_Chasm_Walkway_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Cloud City: Chasm Walkway (Dark) (PC Errata)" "$PAGES/Cloud_City:_Chasm_Walkway_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Cloud City: Chasm Walkway (Dark)" "$PAGES/Cloud_City:_Chasm_Walkway_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dannik Jerriko (Original)" "$PAGES/Dannik_Jerriko_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dannik Jerriko (PC Errata)" "$PAGES/Dannik_Jerriko_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dannik Jerriko" "$PAGES/Dannik_Jerriko.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Danz Borin (Original)" "$PAGES/Danz_Borin_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Danz Borin (PC Errata)" "$PAGES/Danz_Borin_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Danz Borin" "$PAGES/Danz_Borin.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dark Jedi Lightsaber (Original)" "$PAGES/Dark_Jedi_Lightsaber_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dark Jedi Lightsaber (PC Errata)" "$PAGES/Dark_Jedi_Lightsaber_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dark Jedi Lightsaber" "$PAGES/Dark_Jedi_Lightsaber.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Darth Vader (Original)" "$PAGES/Darth_Vader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Darth Vader (PC Errata)" "$PAGES/Darth_Vader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Darth Vader" "$PAGES/Darth_Vader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dark Hours (Original)" "$PAGES/Dark_Hours_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dark Hours (PC Errata)" "$PAGES/Dark_Hours_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dark Hours" "$PAGES/Dark_Hours.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Death Squadron (Original)" "$PAGES/Death_Squadron_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Death Squadron (PC Errata)" "$PAGES/Death_Squadron_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Death Squadron" "$PAGES/Death_Squadron.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dengar (Original)" "$PAGES/Dengar_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dengar (PC Errata)" "$PAGES/Dengar_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dengar" "$PAGES/Dengar.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dengar's Blaster Carbine (Original)" "$PAGES/Dengar's_Blaster_Carbine_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dengar's Blaster Carbine (PC Errata)" "$PAGES/Dengar's_Blaster_Carbine_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dengar's Blaster Carbine" "$PAGES/Dengar's_Blaster_Carbine.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dengar's Modified Riot Gun (Original)" "$PAGES/Dengar's_Modified_Riot_Gun_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dengar's Modified Riot Gun (PC Errata)" "$PAGES/Dengar's_Modified_Riot_Gun_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dengar's Modified Riot Gun" "$PAGES/Dengar's_Modified_Riot_Gun.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Derek 'Hobbie' Klivian (Original)" "$PAGES/Derek_'Hobbie'_Klivian_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Derek 'Hobbie' Klivian (PC Errata)" "$PAGES/Derek_'Hobbie'_Klivian_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Derek 'Hobbie' Klivian" "$PAGES/Derek_'Hobbie'_Klivian.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch9 (Corporal Janse through Derek Hobbie; Chasm Walkway Light+Dark)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch9 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Corporal Janse" \
  "Corporal Janse (Original)" \
  "Corporal Janse (PC Errata)" \
  "Cloud City: Chasm Walkway" \
  "Cloud City: Chasm Walkway (Original)" \
  "Cloud City: Chasm Walkway (PC Errata)" \
  "Cloud City: Chasm Walkway (Dark)" \
  "Cloud City: Chasm Walkway (Dark) (Original)" \
  "Cloud City: Chasm Walkway (Dark) (PC Errata)" \
  "Dannik Jerriko" \
  "Dannik Jerriko (Original)" \
  "Dannik Jerriko (PC Errata)" \
  "Danz Borin" \
  "Danz Borin (Original)" \
  "Danz Borin (PC Errata)" \
  "Dark Jedi Lightsaber" \
  "Dark Jedi Lightsaber (Original)" \
  "Dark Jedi Lightsaber (PC Errata)" \
  "Darth Vader" \
  "Darth Vader (Original)" \
  "Darth Vader (PC Errata)" \
  "Dark Hours" \
  "Dark Hours (Original)" \
  "Dark Hours (PC Errata)" \
  "Death Squadron" \
  "Death Squadron (Original)" \
  "Death Squadron (PC Errata)" \
  "Dengar" \
  "Dengar (Original)" \
  "Dengar (PC Errata)" \
  "Dengar's Blaster Carbine" \
  "Dengar's Blaster Carbine (Original)" \
  "Dengar's Blaster Carbine (PC Errata)" \
  "Dengar's Modified Riot Gun" \
  "Dengar's Modified Riot Gun (Original)" \
  "Dengar's Modified Riot Gun (PC Errata)" \
  "Derek 'Hobbie' Klivian" \
  "Derek 'Hobbie' Klivian (Original)" \
  "Derek 'Hobbie' Klivian (PC Errata)" \
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
echo DONE_APPLY_BATCH9_PC_ERRATA
