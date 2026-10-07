#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch7-gifs

ARCHIVES=(
  Hoth-D-blizzardwalker-decipher-archive.gif
  CC-L-civildisorder-decipher-archive.gif
  CC-D-chiefretwin-decipher-archive.gif
  CC-L-cloudcityblaster-decipher-archive.gif
  CC-D-cloudcityblaster-decipher-archive.gif
  ANH-D-comewithme-decipher-archive.gif
  Dagobah-D-commchief-decipher-archive.gif
  Dagobah-D-commanderbrandei-decipher-archive.gif
  Premiere-D-blasterscope-decipher-archive.gif
  Premiere-L-biggsdarklighter-decipher-archive.gif
  Premiere-L-boshek-decipher-archive.gif
)
HT_FILES=(
  Hoth-D-blizzardwalker.gif
  CC-L-civildisorder.gif
  CC-D-chiefretwin.gif
  CC-L-cloudcityblaster.gif
  CC-D-cloudcityblaster.gif
  ANH-D-comewithme.gif
  Dagobah-D-commchief.gif
  Dagobah-D-commanderbrandei.gif
  Premiere-D-blasterscope.gif
  Premiere-L-biggsdarklighter.gif
  Premiere-L-boshek.gif
)

strip_bom() {
  python3 - "$1" <<'PY'
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
PY
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch7-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch7-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch7-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch7 (Blizzard Walker, Civil Disorder, Chief Retwin, Cloud City Blaster Light+Dark, Come With Me, Comm Chief, Commander Brandei, Blaster Scope, Biggs Darklighter, BoShek); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch7-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch7-gifs
fi

edit "File:Hoth-D-blizzardwalker-decipher-archive.gif" "$PAGES/File_Hoth-D-blizzardwalker-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Blizzard Walker"
edit "File:CC-L-civildisorder-decipher-archive.gif" "$PAGES/File_CC-L-civildisorder-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Civil Disorder"
edit "File:CC-D-chiefretwin-decipher-archive.gif" "$PAGES/File_CC-D-chiefretwin-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Chief Retwin"
edit "File:CC-L-cloudcityblaster-decipher-archive.gif" "$PAGES/File_CC-L-cloudcityblaster-decipher-archive.gif.wiki" "File: Decipher Cloud City Light archive Original Cloud City Blaster"
edit "File:CC-D-cloudcityblaster-decipher-archive.gif" "$PAGES/File_CC-D-cloudcityblaster-decipher-archive.gif.wiki" "File: Decipher Cloud City Dark archive Original Cloud City Blaster (Dark)"
edit "File:ANH-D-comewithme-decipher-archive.gif" "$PAGES/File_ANH-D-comewithme-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Come With Me"
edit "File:Dagobah-D-commchief-decipher-archive.gif" "$PAGES/File_Dagobah-D-commchief-decipher-archive.gif.wiki" "File: Decipher Dagobah archive Original Comm Chief"
edit "File:Dagobah-D-commanderbrandei-decipher-archive.gif" "$PAGES/File_Dagobah-D-commanderbrandei-decipher-archive.gif.wiki" "File: Decipher Dagobah archive Original Commander Brandei"
edit "File:Premiere-D-blasterscope-decipher-archive.gif" "$PAGES/File_Premiere-D-blasterscope-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Blaster Scope"
edit "File:Premiere-L-biggsdarklighter-decipher-archive.gif" "$PAGES/File_Premiere-L-biggsdarklighter-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Biggs Darklighter"
edit "File:Premiere-L-boshek-decipher-archive.gif" "$PAGES/File_Premiere-L-boshek-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original BoShek"

edit "Blizzard Walker (Original)" "$PAGES/Blizzard_Walker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blizzard Walker (PC Errata)" "$PAGES/Blizzard_Walker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blizzard Walker" "$PAGES/Blizzard_Walker.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Civil Disorder (Original)" "$PAGES/Civil_Disorder_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Civil Disorder (PC Errata)" "$PAGES/Civil_Disorder_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Civil Disorder" "$PAGES/Civil_Disorder.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Chief Retwin (Original)" "$PAGES/Chief_Retwin_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Chief Retwin (PC Errata)" "$PAGES/Chief_Retwin_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Chief Retwin" "$PAGES/Chief_Retwin.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Cloud City Blaster (Original)" "$PAGES/Cloud_City_Blaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Cloud City Blaster (PC Errata)" "$PAGES/Cloud_City_Blaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Cloud City Blaster" "$PAGES/Cloud_City_Blaster.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Cloud City Blaster (Dark) (Original)" "$PAGES/Cloud_City_Blaster_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Cloud City Blaster (Dark) (PC Errata)" "$PAGES/Cloud_City_Blaster_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Cloud City Blaster (Dark)" "$PAGES/Cloud_City_Blaster_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Come With Me (Original)" "$PAGES/Come_With_Me_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Come With Me (PC Errata)" "$PAGES/Come_With_Me_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Come With Me" "$PAGES/Come_With_Me.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Comm Chief (Original)" "$PAGES/Comm_Chief_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Comm Chief (PC Errata)" "$PAGES/Comm_Chief_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Comm Chief" "$PAGES/Comm_Chief.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Commander Brandei (Original)" "$PAGES/Commander_Brandei_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commander Brandei (PC Errata)" "$PAGES/Commander_Brandei_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commander Brandei" "$PAGES/Commander_Brandei.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Blaster Scope (Original)" "$PAGES/Blaster_Scope_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blaster Scope (PC Errata)" "$PAGES/Blaster_Scope_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blaster Scope" "$PAGES/Blaster_Scope.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Biggs Darklighter (Original)" "$PAGES/Biggs_Darklighter_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Biggs Darklighter (PC Errata)" "$PAGES/Biggs_Darklighter_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Biggs Darklighter" "$PAGES/Biggs_Darklighter.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "BoShek (Original)" "$PAGES/BoShek_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "BoShek (PC Errata)" "$PAGES/BoShek_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "BoShek" "$PAGES/BoShek.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch7 (Blizzard Walker through BoShek)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch7 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Blizzard Walker" "Blizzard Walker (Original)" "Blizzard Walker (PC Errata)" \
  "Civil Disorder" "Civil Disorder (Original)" "Civil Disorder (PC Errata)" \
  "Chief Retwin" "Chief Retwin (Original)" "Chief Retwin (PC Errata)" \
  "Cloud City Blaster" "Cloud City Blaster (Original)" "Cloud City Blaster (PC Errata)" \
  "Cloud City Blaster (Dark)" "Cloud City Blaster (Dark) (Original)" "Cloud City Blaster (Dark) (PC Errata)" \
  "Come With Me" "Come With Me (Original)" "Come With Me (PC Errata)" \
  "Comm Chief" "Comm Chief (Original)" "Comm Chief (PC Errata)" \
  "Commander Brandei" "Commander Brandei (Original)" "Commander Brandei (PC Errata)" \
  "Blaster Scope" "Blaster Scope (Original)" "Blaster Scope (PC Errata)" \
  "Biggs Darklighter" "Biggs Darklighter (Original)" "Biggs Darklighter (PC Errata)" \
  "BoShek" "BoShek (Original)" "BoShek (PC Errata)" \
  Errata "PC Errata"
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
echo DONE_APPLY_BATCH7_PC_ERRATA

