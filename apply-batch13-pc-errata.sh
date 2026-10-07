#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch13-gifs

ARCHIVES=(
  Hoth-D-ewebblaster-decipher-archive.gif
  Endor-L-endorscouttrooper-decipher-archive.gif
  Hoth-D-exposure-decipher-archive.gif
  Premiere-D-evacuate-decipher-archive.gif
  Premiere-D-fearwillkeeptheminline-decipher-archive.gif
  Dagobah-D-fieldpromotion-decipher-archive.gif
  Dagobah-D-failureatthecave-decipher-archive.gif
  DS2-L-firstofficerthaneespi-decipher-archive.gif
  Hoth-L-fallback-decipher-archive.gif
)
HT_FILES=(
  Hoth-D-ewebblaster.gif
  Endor-L-endorscouttrooper.gif
  Hoth-D-exposure.gif
  Premiere-D-evacuate.gif
  Premiere-D-fearwillkeeptheminline.gif
  Dagobah-D-fieldpromotion.gif
  Dagobah-D-failureatthecave.gif
  DS2-L-firstofficerthaneespi.gif
  Hoth-L-fallback.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch13-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch13-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch13-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch13 (E-web Blaster through Fall Back!); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch13-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch13-gifs
fi

edit "File:Hoth-D-ewebblaster-decipher-archive.gif" "$PAGES/File_Hoth-D-ewebblaster-decipher-archive.gif.wiki" "File: Decipher archive Original E-web Blaster"
edit "File:Endor-L-endorscouttrooper-decipher-archive.gif" "$PAGES/File_Endor-L-endorscouttrooper-decipher-archive.gif.wiki" "File: Decipher archive Original Endor Scout Trooper"
edit "File:Hoth-D-exposure-decipher-archive.gif" "$PAGES/File_Hoth-D-exposure-decipher-archive.gif.wiki" "File: Decipher archive Original Exposure"
edit "File:Premiere-D-evacuate-decipher-archive.gif" "$PAGES/File_Premiere-D-evacuate-decipher-archive.gif.wiki" "File: Decipher archive Original Evacuate?"
edit "File:Premiere-D-fearwillkeeptheminline-decipher-archive.gif" "$PAGES/File_Premiere-D-fearwillkeeptheminline-decipher-archive.gif.wiki" "File: Decipher archive Original Fear Will Keep Them In Line"
edit "File:Dagobah-D-fieldpromotion-decipher-archive.gif" "$PAGES/File_Dagobah-D-fieldpromotion-decipher-archive.gif.wiki" "File: Decipher archive Original Field Promotion"
edit "File:Dagobah-D-failureatthecave-decipher-archive.gif" "$PAGES/File_Dagobah-D-failureatthecave-decipher-archive.gif.wiki" "File: Decipher archive Original Failure At The Cave"
edit "File:DS2-L-firstofficerthaneespi-decipher-archive.gif" "$PAGES/File_DS2-L-firstofficerthaneespi-decipher-archive.gif.wiki" "File: Decipher archive Original First Officer Thaneespi"
edit "File:Hoth-L-fallback-decipher-archive.gif" "$PAGES/File_Hoth-L-fallback-decipher-archive.gif.wiki" "File: Decipher archive Original Fall Back!"

edit "E-web Blaster (Original)" "$PAGES/E-web_Blaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "E-web Blaster (PC Errata)" "$PAGES/E-web_Blaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "E-web Blaster" "$PAGES/E-web_Blaster.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Endor Scout Trooper (Original)" "$PAGES/Endor_Scout_Trooper_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Endor Scout Trooper (PC Errata)" "$PAGES/Endor_Scout_Trooper_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Endor Scout Trooper" "$PAGES/Endor_Scout_Trooper.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Exposure (Original)" "$PAGES/Exposure_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Exposure (PC Errata)" "$PAGES/Exposure_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Exposure" "$PAGES/Exposure.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Evacuate? (Original)" "$PAGES/Evacuate?_(Original).wiki" "PC Errata seed: printed Decipher archive Original (create)"
edit "Evacuate? (PC Errata)" "$PAGES/Evacuate?_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable (create)"
edit "Evacuate?" "$PAGES/Evacuate?.wiki" "Create bare + Decipher print; archive face; link PC Errata"
edit "Fear Will Keep Them In Line (Original)" "$PAGES/Fear_Will_Keep_Them_In_Line_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Fear Will Keep Them In Line (PC Errata)" "$PAGES/Fear_Will_Keep_Them_In_Line_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Fear Will Keep Them In Line" "$PAGES/Fear_Will_Keep_Them_In_Line.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Field Promotion (Original)" "$PAGES/Field_Promotion_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Field Promotion (PC Errata)" "$PAGES/Field_Promotion_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Field Promotion" "$PAGES/Field_Promotion.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Failure At The Cave (Original)" "$PAGES/Failure_At_The_Cave_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Failure At The Cave (PC Errata)" "$PAGES/Failure_At_The_Cave_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Failure At The Cave" "$PAGES/Failure_At_The_Cave.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "First Officer Thaneespi (Original)" "$PAGES/First_Officer_Thaneespi_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "First Officer Thaneespi (PC Errata)" "$PAGES/First_Officer_Thaneespi_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "First Officer Thaneespi" "$PAGES/First_Officer_Thaneespi.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Fall Back! (Original)" "$PAGES/Fall_Back!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Fall Back! (PC Errata)" "$PAGES/Fall_Back!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Fall Back!" "$PAGES/Fall_Back!.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch13 (E-web Blaster through Fall Back!)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch13 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "E-web Blaster" "E-web Blaster (Original)" "E-web Blaster (PC Errata)" \
  "Endor Scout Trooper" "Endor Scout Trooper (Original)" "Endor Scout Trooper (PC Errata)" \
  "Exposure" "Exposure (Original)" "Exposure (PC Errata)" \
  "Evacuate?" "Evacuate? (Original)" "Evacuate? (PC Errata)" \
  "Fear Will Keep Them In Line" "Fear Will Keep Them In Line (Original)" "Fear Will Keep Them In Line (PC Errata)" \
  "Field Promotion" "Field Promotion (Original)" "Field Promotion (PC Errata)" \
  "Failure At The Cave" "Failure At The Cave (Original)" "Failure At The Cave (PC Errata)" \
  "First Officer Thaneespi" "First Officer Thaneespi (Original)" "First Officer Thaneespi (PC Errata)" \
  "Fall Back!" "Fall Back! (Original)" "Fall Back! (PC Errata)" \
  "Errata" "PC Errata"
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
echo DONE_APPLY_BATCH13_PC_ERRATA
