#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch30-gifs

ARCHIVES=(
  Premiere-L-sandcrawler-decipher-archive.gif
  Premiere-L-saitorrkalfas-decipher-archive.gif
  Hoth-D-selfdestructmechanism-decipher-archive.gif
  CloudCity-D-shatteredhope-decipher-archive.gif
  Hoth-L-shawnvaldez-decipher-archive.gif
  Dagobah-D-shotinthedark-decipher-archive.gif
  SpecialEdition-D-sienarfleetsystems-decipher-archive.gif
  Hoth-L-snowspeeder-decipher-archive.gif
  Hoth-D-snowtrooper-decipher-archive.gif
  Premiere-L-solohan-decipher-archive.gif
  CloudCity-D-specialdelivery-decipher-archive.gif
  Premiere-D-stormtrooperbackpack-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-sandcrawler.gif
  Premiere-D-sandcrawler.gif
  Premiere-L-saitorrkalfas.gif
  Hoth-D-selfdestructmechanism.gif
  CC-D-shatteredhope.gif
  Hoth-L-shawnvaldez.gif
  Dagobah-D-shotinthedark.gif
  SE-D-sienarfleetsystems.gif
  Hoth-L-snowspeeder.gif
  Hoth-D-snowtrooper.gif
  Premiere-L-solohan.gif
  CC-D-specialdelivery.gif
  Premiere-D-stormtrooperbackpack.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch30-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch30-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch30-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch30 (Sandcrawler Light+Dark through Stormtrooper Backpack); flush crop + flood bleach #FFF. DO NOT replace Holotable. Dark Sandcrawler Original uses shared Light archive this pass."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch30-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch30-gifs
fi

edit "File:Premiere-L-sandcrawler-decipher-archive.gif" "$PAGES/File_Premiere-L-sandcrawler-decipher-archive.gif.wiki" "File: Decipher archive Original Sandcrawler (shared Light for Dark too)"
edit "File:Premiere-L-saitorrkalfas-decipher-archive.gif" "$PAGES/File_Premiere-L-saitorrkalfas-decipher-archive.gif.wiki" "File: Decipher archive Original Sai'torr Kal Fas"
edit "File:Hoth-D-selfdestructmechanism-decipher-archive.gif" "$PAGES/File_Hoth-D-selfdestructmechanism-decipher-archive.gif.wiki" "File: Decipher archive Original Self-Destruct Mechanism"
edit "File:CloudCity-D-shatteredhope-decipher-archive.gif" "$PAGES/File_CloudCity-D-shatteredhope-decipher-archive.gif.wiki" "File: Decipher archive Original Shattered Hope"
edit "File:Hoth-L-shawnvaldez-decipher-archive.gif" "$PAGES/File_Hoth-L-shawnvaldez-decipher-archive.gif.wiki" "File: Decipher archive Original Shawn Valdez"
edit "File:Dagobah-D-shotinthedark-decipher-archive.gif" "$PAGES/File_Dagobah-D-shotinthedark-decipher-archive.gif.wiki" "File: Decipher archive Original Shot In The Dark"
edit "File:SpecialEdition-D-sienarfleetsystems-decipher-archive.gif" "$PAGES/File_SpecialEdition-D-sienarfleetsystems-decipher-archive.gif.wiki" "File: Decipher archive Original Sienar Fleet Systems"
edit "File:Hoth-L-snowspeeder-decipher-archive.gif" "$PAGES/File_Hoth-L-snowspeeder-decipher-archive.gif.wiki" "File: Decipher archive Original Snowspeeder"
edit "File:Hoth-D-snowtrooper-decipher-archive.gif" "$PAGES/File_Hoth-D-snowtrooper-decipher-archive.gif.wiki" "File: Decipher archive Original Snowtrooper"
edit "File:Premiere-L-solohan-decipher-archive.gif" "$PAGES/File_Premiere-L-solohan-decipher-archive.gif.wiki" "File: Decipher archive Original Solo Han"
edit "File:CloudCity-D-specialdelivery-decipher-archive.gif" "$PAGES/File_CloudCity-D-specialdelivery-decipher-archive.gif.wiki" "File: Decipher archive Original Special Delivery"
edit "File:Premiere-D-stormtrooperbackpack-decipher-archive.gif" "$PAGES/File_Premiere-D-stormtrooperbackpack-decipher-archive.gif.wiki" "File: Decipher archive Original Stormtrooper Backpack"

edit "Sandcrawler (Original)" "$PAGES/Sandcrawler_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Sandcrawler (PC Errata)" "$PAGES/Sandcrawler_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Sandcrawler" "$PAGES/Sandcrawler.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Sandcrawler (Dark) (Original)" "$PAGES/Sandcrawler_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original (shared Light face)"
edit "Sandcrawler (Dark) (PC Errata)" "$PAGES/Sandcrawler_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Sandcrawler (Dark)" "$PAGES/Sandcrawler_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Sai'torr Kal Fas (Original)" "$PAGES/Sai'torr_Kal_Fas_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Sai'torr Kal Fas (PC Errata)" "$PAGES/Sai'torr_Kal_Fas_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Sai'torr Kal Fas" "$PAGES/Sai'torr_Kal_Fas.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Self-Destruct Mechanism (Original)" "$PAGES/Self-Destruct_Mechanism_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Self-Destruct Mechanism (PC Errata)" "$PAGES/Self-Destruct_Mechanism_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Self-Destruct Mechanism" "$PAGES/Self-Destruct_Mechanism.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Shattered Hope (Original)" "$PAGES/Shattered_Hope_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Shattered Hope (PC Errata)" "$PAGES/Shattered_Hope_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Shattered Hope" "$PAGES/Shattered_Hope.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Shawn Valdez (Original)" "$PAGES/Shawn_Valdez_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Shawn Valdez (PC Errata)" "$PAGES/Shawn_Valdez_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Shawn Valdez" "$PAGES/Shawn_Valdez.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Shot In The Dark (Original)" "$PAGES/Shot_In_The_Dark_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Shot In The Dark (PC Errata)" "$PAGES/Shot_In_The_Dark_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Shot In The Dark" "$PAGES/Shot_In_The_Dark.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Sienar Fleet Systems (Original)" "$PAGES/Sienar_Fleet_Systems_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Sienar Fleet Systems (PC Errata)" "$PAGES/Sienar_Fleet_Systems_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Sienar Fleet Systems" "$PAGES/Sienar_Fleet_Systems.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Snowspeeder (Original)" "$PAGES/Snowspeeder_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Snowspeeder (PC Errata)" "$PAGES/Snowspeeder_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Snowspeeder" "$PAGES/Snowspeeder.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Snowtrooper (Original)" "$PAGES/Snowtrooper_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Snowtrooper (PC Errata)" "$PAGES/Snowtrooper_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Snowtrooper" "$PAGES/Snowtrooper.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Solo Han (Original)" "$PAGES/Solo_Han_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Solo Han (PC Errata)" "$PAGES/Solo_Han_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Solo Han" "$PAGES/Solo_Han.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Special Delivery (Original)" "$PAGES/Special_Delivery_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Special Delivery (PC Errata)" "$PAGES/Special_Delivery_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Special Delivery" "$PAGES/Special_Delivery.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Stormtrooper Backpack (Original)" "$PAGES/Stormtrooper_Backpack_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Stormtrooper Backpack (PC Errata)" "$PAGES/Stormtrooper_Backpack_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Stormtrooper Backpack" "$PAGES/Stormtrooper_Backpack.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch30 (Sandcrawler Light+Dark through Stormtrooper Backpack)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch30 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Sandcrawler" \
  "Sandcrawler (Original)" \
  "Sandcrawler (PC Errata)" \
  "Sandcrawler (Dark)" \
  "Sandcrawler (Dark) (Original)" \
  "Sandcrawler (Dark) (PC Errata)" \
  "Sai'torr Kal Fas" \
  "Sai'torr Kal Fas (Original)" \
  "Sai'torr Kal Fas (PC Errata)" \
  "Self-Destruct Mechanism" \
  "Self-Destruct Mechanism (Original)" \
  "Self-Destruct Mechanism (PC Errata)" \
  "Shattered Hope" \
  "Shattered Hope (Original)" \
  "Shattered Hope (PC Errata)" \
  "Shawn Valdez" \
  "Shawn Valdez (Original)" \
  "Shawn Valdez (PC Errata)" \
  "Shot In The Dark" \
  "Shot In The Dark (Original)" \
  "Shot In The Dark (PC Errata)" \
  "Sienar Fleet Systems" \
  "Sienar Fleet Systems (Original)" \
  "Sienar Fleet Systems (PC Errata)" \
  "Snowspeeder" \
  "Snowspeeder (Original)" \
  "Snowspeeder (PC Errata)" \
  "Snowtrooper" \
  "Snowtrooper (Original)" \
  "Snowtrooper (PC Errata)" \
  "Solo Han" \
  "Solo Han (Original)" \
  "Solo Han (PC Errata)" \
  "Special Delivery" \
  "Special Delivery (Original)" \
  "Special Delivery (PC Errata)" \
  "Stormtrooper Backpack" \
  "Stormtrooper Backpack (Original)" \
  "Stormtrooper Backpack (PC Errata)" \
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
echo DONE_APPLY_BATCH30_PC_ERRATA
