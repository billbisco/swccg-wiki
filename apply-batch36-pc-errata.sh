#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch36-gifs

ARCHIVES=(
  JabbasPalace-L-vultazaene-decipher-archive.gif
  Hoth-L-wyronserper-decipher-archive.gif
  Dagobah-L-whatisthybiddingmymaster-decipher-archive.gif
  Hoth-L-wed1016techiedroid-decipher-archive.gif
  Premiere-L-wed9m1banthadroid-decipher-archive.gif
  Premiere-D-wed151662treadwelldroid-decipher-archive.gif
)
HT_FILES=(
  JP-L-vultazaene.gif
  Hoth-L-wyronserper.gif
  Dagobah-L-whatisthybiddingmymaster.gif
  Hoth-L-wed1016techiedroid.gif
  Premiere-L-wed9m1banthadroid.gif
  Premiere-D-wed151662treadwelldroid.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch36-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch36-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch36-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch36 (Vul Tazaene through WED15-I662 '\''Treadwell'\'' Droid); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch36-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch36-gifs
fi

edit "File:JabbasPalace-L-vultazaene-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-vultazaene-decipher-archive.gif.wiki" "File: Decipher archive Original Vul Tazaene"
edit "File:Hoth-L-wyronserper-decipher-archive.gif" "$PAGES/File_Hoth-L-wyronserper-decipher-archive.gif.wiki" "File: Decipher archive Original Wyron Serper"
edit "File:Dagobah-L-whatisthybiddingmymaster-decipher-archive.gif" "$PAGES/File_Dagobah-L-whatisthybiddingmymaster-decipher-archive.gif.wiki" "File: Decipher archive Original What Is Thy Bidding, My Master?"
edit "File:Hoth-L-wed1016techiedroid-decipher-archive.gif" "$PAGES/File_Hoth-L-wed1016techiedroid-decipher-archive.gif.wiki" "File: Decipher archive Original WED-1016 'Techie' Droid"
edit "File:Premiere-L-wed9m1banthadroid-decipher-archive.gif" "$PAGES/File_Premiere-L-wed9m1banthadroid-decipher-archive.gif.wiki" "File: Decipher archive Original WED-9-M1 'Bantha' Droid"
edit "File:Premiere-D-wed151662treadwelldroid-decipher-archive.gif" "$PAGES/File_Premiere-D-wed151662treadwelldroid-decipher-archive.gif.wiki" "File: Decipher archive Original WED15-I662 'Treadwell' Droid"

edit "Vul Tazaene (Original)" "$PAGES/Vul_Tazaene_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vul Tazaene (PC Errata)" "$PAGES/Vul_Tazaene_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vul Tazaene" "$PAGES/Vul_Tazaene.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wyron Serper (Original)" "$PAGES/Wyron_Serper_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wyron Serper (PC Errata)" "$PAGES/Wyron_Serper_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wyron Serper" "$PAGES/Wyron_Serper.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "What Is Thy Bidding, My Master? (Original)" "$PAGES/What_Is_Thy_Bidding,_My_Master?_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "What Is Thy Bidding, My Master? (PC Errata)" "$PAGES/What_Is_Thy_Bidding,_My_Master?_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "What Is Thy Bidding, My Master?" "$PAGES/What_Is_Thy_Bidding,_My_Master?.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "WED-1016 'Techie' Droid (Original)" "$PAGES/WED-1016_'Techie'_Droid_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "WED-1016 'Techie' Droid (PC Errata)" "$PAGES/WED-1016_'Techie'_Droid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "WED-1016 'Techie' Droid" "$PAGES/WED-1016_'Techie'_Droid.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "WED-9-M1 'Bantha' Droid (Original)" "$PAGES/WED-9-M1_'Bantha'_Droid_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "WED-9-M1 'Bantha' Droid (PC Errata)" "$PAGES/WED-9-M1_'Bantha'_Droid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "WED-9-M1 'Bantha' Droid" "$PAGES/WED-9-M1_'Bantha'_Droid.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "WED15-I662 'Treadwell' Droid (Original)" "$PAGES/WED15-I662_'Treadwell'_Droid_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "WED15-I662 'Treadwell' Droid (PC Errata)" "$PAGES/WED15-I662_'Treadwell'_Droid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "WED15-I662 'Treadwell' Droid" "$PAGES/WED15-I662_'Treadwell'_Droid.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch36 (Vul Tazaene through WED15-I662 'Treadwell' Droid)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch36 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Vul Tazaene" \
  "Vul Tazaene (Original)" \
  "Vul Tazaene (PC Errata)" \
  "Wyron Serper" \
  "Wyron Serper (Original)" \
  "Wyron Serper (PC Errata)" \
  "What Is Thy Bidding, My Master?" \
  "What Is Thy Bidding, My Master? (Original)" \
  "What Is Thy Bidding, My Master? (PC Errata)" \
  "WED-1016 'Techie' Droid" \
  "WED-1016 'Techie' Droid (Original)" \
  "WED-1016 'Techie' Droid (PC Errata)" \
  "WED-9-M1 'Bantha' Droid" \
  "WED-9-M1 'Bantha' Droid (Original)" \
  "WED-9-M1 'Bantha' Droid (PC Errata)" \
  "WED15-I662 'Treadwell' Droid" \
  "WED15-I662 'Treadwell' Droid (Original)" \
  "WED15-I662 'Treadwell' Droid (PC Errata)" \
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
echo DONE_APPLY_BATCH36_PC_ERRATA
