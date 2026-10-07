#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch14-gifs

ARCHIVES=(
  JabbasPalace-L-fallenportal-decipher-archive.gif
  Dagobah-D-flagship-decipher-archive.gif
  Endor-L-firefight-decipher-archive.gif
  JabbasPalace-D-fozec-decipher-archive.gif
  Hoth-D-frozendinner-decipher-archive.gif
  Hoth-D-fx10effexten-decipher-archive.gif
  Hoth-L-fx7effexseven-decipher-archive.gif
  Premiere-L-fullthrottle-decipher-archive.gif
  JabbasPalace-D-gailid-decipher-archive.gif
  JabbasPalace-D-gamorreanax-decipher-archive.gif
  Hoth-D-generalveers-decipher-archive.gif
  ANH-L-grapplinghook-decipher-archive.gif
)
HT_FILES=(
  JP-L-fallenportal.gif
  Dagobah-D-flagship.gif
  Endor-L-firefight.gif
  JP-D-fozec.gif
  Hoth-D-frozendinner.gif
  Hoth-D-fx10effexten.gif
  Hoth-L-fx7effexseven.gif
  Premiere-L-fullthrottle.gif
  JP-D-gailid.gif
  JP-D-gamorreanax.gif
  Hoth-D-generalveers.gif
  ANH-L-grapplinghook.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch14-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch14-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch14-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch14 (Fallen Portal through Grappling Hook); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch14-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch14-gifs
fi

edit "File:JabbasPalace-L-fallenportal-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-fallenportal-decipher-archive.gif.wiki" "File: Decipher archive Original Fallen Portal"
edit "File:Dagobah-D-flagship-decipher-archive.gif" "$PAGES/File_Dagobah-D-flagship-decipher-archive.gif.wiki" "File: Decipher archive Original Flagship"
edit "File:Endor-L-firefight-decipher-archive.gif" "$PAGES/File_Endor-L-firefight-decipher-archive.gif.wiki" "File: Decipher archive Original Firefight"
edit "File:JabbasPalace-D-fozec-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-fozec-decipher-archive.gif.wiki" "File: Decipher archive Original Fozec"
edit "File:Hoth-D-frozendinner-decipher-archive.gif" "$PAGES/File_Hoth-D-frozendinner-decipher-archive.gif.wiki" "File: Decipher archive Original Frozen Dinner"
edit "File:Hoth-D-fx10effexten-decipher-archive.gif" "$PAGES/File_Hoth-D-fx10effexten-decipher-archive.gif.wiki" "File: Decipher archive Original FX-10 (Effex-ten)"
edit "File:Hoth-L-fx7effexseven-decipher-archive.gif" "$PAGES/File_Hoth-L-fx7effexseven-decipher-archive.gif.wiki" "File: Decipher archive Original FX-7 (Effex-Seven)"
edit "File:Premiere-L-fullthrottle-decipher-archive.gif" "$PAGES/File_Premiere-L-fullthrottle-decipher-archive.gif.wiki" "File: Decipher archive Original Full Throttle"
edit "File:JabbasPalace-D-gailid-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-gailid-decipher-archive.gif.wiki" "File: Decipher archive Original Gailid"
edit "File:JabbasPalace-D-gamorreanax-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-gamorreanax-decipher-archive.gif.wiki" "File: Decipher archive Original Gamorrean Ax"
edit "File:Hoth-D-generalveers-decipher-archive.gif" "$PAGES/File_Hoth-D-generalveers-decipher-archive.gif.wiki" "File: Decipher archive Original General Veers"
edit "File:ANH-L-grapplinghook-decipher-archive.gif" "$PAGES/File_ANH-L-grapplinghook-decipher-archive.gif.wiki" "File: Decipher archive Original Grappling Hook"

edit "Fallen Portal (Original)" "$PAGES/Fallen_Portal_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Fallen Portal (PC Errata)" "$PAGES/Fallen_Portal_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Fallen Portal" "$PAGES/Fallen_Portal.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Flagship (Original)" "$PAGES/Flagship_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Flagship (PC Errata)" "$PAGES/Flagship_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Flagship" "$PAGES/Flagship.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Firefight (Original)" "$PAGES/Firefight_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Firefight (PC Errata)" "$PAGES/Firefight_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Firefight" "$PAGES/Firefight.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Fozec (Original)" "$PAGES/Fozec_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Fozec (PC Errata)" "$PAGES/Fozec_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Fozec" "$PAGES/Fozec.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Frozen Dinner (Original)" "$PAGES/Frozen_Dinner_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Frozen Dinner (PC Errata)" "$PAGES/Frozen_Dinner_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Frozen Dinner" "$PAGES/Frozen_Dinner.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "FX-10 (Effex-ten) (Original)" "$PAGES/FX-10_(Effex-ten)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "FX-10 (Effex-ten) (PC Errata)" "$PAGES/FX-10_(Effex-ten)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "FX-10 (Effex-ten)" "$PAGES/FX-10_(Effex-ten).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "FX-7 (Effex-Seven) (Original)" "$PAGES/FX-7_(Effex-Seven)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "FX-7 (Effex-Seven) (PC Errata)" "$PAGES/FX-7_(Effex-Seven)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "FX-7 (Effex-Seven)" "$PAGES/FX-7_(Effex-Seven).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Full Throttle (Original)" "$PAGES/Full_Throttle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Full Throttle (PC Errata)" "$PAGES/Full_Throttle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Full Throttle" "$PAGES/Full_Throttle.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Gailid (Original)" "$PAGES/Gailid_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gailid (PC Errata)" "$PAGES/Gailid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gailid" "$PAGES/Gailid.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Gamorrean Ax (Original)" "$PAGES/Gamorrean_Ax_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gamorrean Ax (PC Errata)" "$PAGES/Gamorrean_Ax_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gamorrean Ax" "$PAGES/Gamorrean_Ax.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "General Veers (Original)" "$PAGES/General_Veers_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "General Veers (PC Errata)" "$PAGES/General_Veers_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "General Veers" "$PAGES/General_Veers.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Grappling Hook (Original)" "$PAGES/Grappling_Hook_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Grappling Hook (PC Errata)" "$PAGES/Grappling_Hook_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Grappling Hook" "$PAGES/Grappling_Hook.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch14 (Fallen Portal through Grappling Hook)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch14 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Fallen Portal" "Fallen Portal (Original)" "Fallen Portal (PC Errata)" \
  "Flagship" "Flagship (Original)" "Flagship (PC Errata)" \
  "Firefight" "Firefight (Original)" "Firefight (PC Errata)" \
  "Fozec" "Fozec (Original)" "Fozec (PC Errata)" \
  "Frozen Dinner" "Frozen Dinner (Original)" "Frozen Dinner (PC Errata)" \
  "FX-10 (Effex-ten)" "FX-10 (Effex-ten) (Original)" "FX-10 (Effex-ten) (PC Errata)" \
  "FX-7 (Effex-Seven)" "FX-7 (Effex-Seven) (Original)" "FX-7 (Effex-Seven) (PC Errata)" \
  "Full Throttle" "Full Throttle (Original)" "Full Throttle (PC Errata)" \
  "Gailid" "Gailid (Original)" "Gailid (PC Errata)" \
  "Gamorrean Ax" "Gamorrean Ax (Original)" "Gamorrean Ax (PC Errata)" \
  "General Veers" "General Veers (Original)" "General Veers (PC Errata)" \
  "Grappling Hook" "Grappling Hook (Original)" "Grappling Hook (PC Errata)" \
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
echo DONE_APPLY_BATCH14_PC_ERRATA
