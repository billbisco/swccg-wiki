#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch29-gifs

ARCHIVES=(
  Premiere-L-rebelpilot-decipher-archive.gif
  Premiere-L-rebelplanners-decipher-archive.gif
  Hoth-L-rebelscout-decipher-archive.gif
  ANH-L-rebelsquadleader-decipher-archive.gif
  ANH-L-rebeltech-decipher-archive.gif
  OTSD-L-rebeltrooperrecruit-decipher-archive.gif
  Premiere-L-redleader-decipher-archive.gif
  Premiere-L-rycarryjerd-decipher-archive.gif
  DeathStarII-D-saber4-decipher-archive.gif
  SpecialEdition-L-sandspeeder-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-rebelpilot.gif
  Premiere-L-rebelplanners.gif
  Hoth-L-rebelscout.gif
  ANH-L-rebelsquadleader.gif
  ANH-L-rebeltech.gif
  OTSD-L-rebeltrooperrecruit.gif
  Premiere-L-redleader.gif
  Premiere-L-rycarryjerd.gif
  DS2-D-saber4.gif
  SE-L-sandspeeder.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch29-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch29-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch29-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch29 (Rebel Pilot through Sandspeeder); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch29-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch29-gifs
fi

edit "File:Premiere-L-rebelpilot-decipher-archive.gif" "$PAGES/File_Premiere-L-rebelpilot-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Pilot"
edit "File:Premiere-L-rebelplanners-decipher-archive.gif" "$PAGES/File_Premiere-L-rebelplanners-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Planners"
edit "File:Hoth-L-rebelscout-decipher-archive.gif" "$PAGES/File_Hoth-L-rebelscout-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Scout"
edit "File:ANH-L-rebelsquadleader-decipher-archive.gif" "$PAGES/File_ANH-L-rebelsquadleader-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Squad Leader"
edit "File:ANH-L-rebeltech-decipher-archive.gif" "$PAGES/File_ANH-L-rebeltech-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Tech"
edit "File:OTSD-L-rebeltrooperrecruit-decipher-archive.gif" "$PAGES/File_OTSD-L-rebeltrooperrecruit-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Trooper Recruit"
edit "File:Premiere-L-redleader-decipher-archive.gif" "$PAGES/File_Premiere-L-redleader-decipher-archive.gif.wiki" "File: Decipher archive Original Red Leader"
edit "File:Premiere-L-rycarryjerd-decipher-archive.gif" "$PAGES/File_Premiere-L-rycarryjerd-decipher-archive.gif.wiki" "File: Decipher archive Original Rycar Ryjerd"
edit "File:DeathStarII-D-saber4-decipher-archive.gif" "$PAGES/File_DeathStarII-D-saber4-decipher-archive.gif.wiki" "File: Decipher archive Original Saber 4"
edit "File:SpecialEdition-L-sandspeeder-decipher-archive.gif" "$PAGES/File_SpecialEdition-L-sandspeeder-decipher-archive.gif.wiki" "File: Decipher archive Original Sandspeeder"

edit "Rebel Pilot (Original)" "$PAGES/Rebel_Pilot_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Pilot (PC Errata)" "$PAGES/Rebel_Pilot_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Pilot" "$PAGES/Rebel_Pilot.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Planners (Original)" "$PAGES/Rebel_Planners_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Planners (PC Errata)" "$PAGES/Rebel_Planners_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Planners" "$PAGES/Rebel_Planners.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Scout (Original)" "$PAGES/Rebel_Scout_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Scout (PC Errata)" "$PAGES/Rebel_Scout_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Scout" "$PAGES/Rebel_Scout.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Squad Leader (Original)" "$PAGES/Rebel_Squad_Leader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Squad Leader (PC Errata)" "$PAGES/Rebel_Squad_Leader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Squad Leader" "$PAGES/Rebel_Squad_Leader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Tech (Original)" "$PAGES/Rebel_Tech_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Tech (PC Errata)" "$PAGES/Rebel_Tech_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Tech" "$PAGES/Rebel_Tech.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Trooper Recruit (Original)" "$PAGES/Rebel_Trooper_Recruit_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Trooper Recruit (PC Errata)" "$PAGES/Rebel_Trooper_Recruit_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Trooper Recruit" "$PAGES/Rebel_Trooper_Recruit.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Red Leader (Original)" "$PAGES/Red_Leader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Red Leader (PC Errata)" "$PAGES/Red_Leader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Red Leader" "$PAGES/Red_Leader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rycar Ryjerd (Original)" "$PAGES/Rycar_Ryjerd_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rycar Ryjerd (PC Errata)" "$PAGES/Rycar_Ryjerd_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rycar Ryjerd" "$PAGES/Rycar_Ryjerd.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Saber 4 (Original)" "$PAGES/Saber_4_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Saber 4 (PC Errata)" "$PAGES/Saber_4_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Saber 4" "$PAGES/Saber_4.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Sandspeeder (Original)" "$PAGES/Sandspeeder_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Sandspeeder (PC Errata)" "$PAGES/Sandspeeder_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Sandspeeder" "$PAGES/Sandspeeder.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch29 (Rebel Pilot through Sandspeeder)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch29 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Rebel Pilot" \
  "Rebel Pilot (Original)" \
  "Rebel Pilot (PC Errata)" \
  "Rebel Planners" \
  "Rebel Planners (Original)" \
  "Rebel Planners (PC Errata)" \
  "Rebel Scout" \
  "Rebel Scout (Original)" \
  "Rebel Scout (PC Errata)" \
  "Rebel Squad Leader" \
  "Rebel Squad Leader (Original)" \
  "Rebel Squad Leader (PC Errata)" \
  "Rebel Tech" \
  "Rebel Tech (Original)" \
  "Rebel Tech (PC Errata)" \
  "Rebel Trooper Recruit" \
  "Rebel Trooper Recruit (Original)" \
  "Rebel Trooper Recruit (PC Errata)" \
  "Red Leader" \
  "Red Leader (Original)" \
  "Red Leader (PC Errata)" \
  "Rycar Ryjerd" \
  "Rycar Ryjerd (Original)" \
  "Rycar Ryjerd (PC Errata)" \
  "Saber 4" \
  "Saber 4 (Original)" \
  "Saber 4 (PC Errata)" \
  "Sandspeeder" \
  "Sandspeeder (Original)" \
  "Sandspeeder (PC Errata)" \
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
echo DONE_APPLY_BATCH29_PC_ERRATA
