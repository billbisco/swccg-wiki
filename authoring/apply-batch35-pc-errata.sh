#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch35-gifs

ARCHIVES=(
  Dagobah-L-vinesnake-decipher-archive.gif
  Dagobah-D-vinesnake-decipher-archive.gif
  ANH-D-wehaveaprisoner-decipher-archive.gif
  ANH-L-wedgeantilles-decipher-archive.gif
  JabbasPalace-D-weequaymarksman-decipher-archive.gif
  Hoth-L-wesjanson-decipher-archive.gif
  JabbasPalace-D-wooof-decipher-archive.gif
  Dagobah-D-zuckuss-decipher-archive.gif
  EnhancedJabbasPalace-D-zuckussinmisthunter-decipher-archive.gif
  Dagobah-D-zuckusssnarerifle-decipher-archive.gif
)
HT_FILES=(
  Dagobah-L-vinesnake.gif
  Dagobah-D-vinesnake.gif
  ANH-D-wehaveaprisoner.gif
  ANH-L-wedgeantilles.gif
  JP-D-weequaymarksman.gif
  Hoth-L-wesjanson.gif
  JP-D-wooof.gif
  Dagobah-D-zuckuss.gif
  EJP-D-zuckussinmisthunter.gif
  Dagobah-D-zuckusssnarerifle.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch35-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch35-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch35-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch35 (Vine Snake through Zuckuss'\'' Snare Rifle); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch35-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch35-gifs
fi

edit "File:Dagobah-L-vinesnake-decipher-archive.gif" "$PAGES/File_Dagobah-L-vinesnake-decipher-archive.gif.wiki" "File: Decipher archive Original Vine Snake"
edit "File:Dagobah-D-vinesnake-decipher-archive.gif" "$PAGES/File_Dagobah-D-vinesnake-decipher-archive.gif.wiki" "File: Decipher archive Original Vine Snake (Dark)"
edit "File:ANH-D-wehaveaprisoner-decipher-archive.gif" "$PAGES/File_ANH-D-wehaveaprisoner-decipher-archive.gif.wiki" "File: Decipher archive Original We Have A Prisoner"
edit "File:ANH-L-wedgeantilles-decipher-archive.gif" "$PAGES/File_ANH-L-wedgeantilles-decipher-archive.gif.wiki" "File: Decipher archive Original Wedge Antilles"
edit "File:JabbasPalace-D-weequaymarksman-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-weequaymarksman-decipher-archive.gif.wiki" "File: Decipher archive Original Weequay Marksman"
edit "File:Hoth-L-wesjanson-decipher-archive.gif" "$PAGES/File_Hoth-L-wesjanson-decipher-archive.gif.wiki" "File: Decipher archive Original Wes Janson"
edit "File:JabbasPalace-D-wooof-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-wooof-decipher-archive.gif.wiki" "File: Decipher archive Original Wooof"
edit "File:Dagobah-D-zuckuss-decipher-archive.gif" "$PAGES/File_Dagobah-D-zuckuss-decipher-archive.gif.wiki" "File: Decipher archive Original Zuckuss"
edit "File:EnhancedJabbasPalace-D-zuckussinmisthunter-decipher-archive.gif" "$PAGES/File_EnhancedJabbasPalace-D-zuckussinmisthunter-decipher-archive.gif.wiki" "File: Decipher archive Original Zuckuss In Mist Hunter"
edit "File:Dagobah-D-zuckusssnarerifle-decipher-archive.gif" "$PAGES/File_Dagobah-D-zuckusssnarerifle-decipher-archive.gif.wiki" "File: Decipher archive Original Zuckuss' Snare Rifle"

edit "Vine Snake (Original)" "$PAGES/Vine_Snake_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vine Snake (PC Errata)" "$PAGES/Vine_Snake_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vine Snake" "$PAGES/Vine_Snake.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vine Snake (Dark) (Original)" "$PAGES/Vine_Snake_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vine Snake (Dark) (PC Errata)" "$PAGES/Vine_Snake_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vine Snake (Dark)" "$PAGES/Vine_Snake_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "We Have A Prisoner (Original)" "$PAGES/We_Have_A_Prisoner_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "We Have A Prisoner (PC Errata)" "$PAGES/We_Have_A_Prisoner_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "We Have A Prisoner" "$PAGES/We_Have_A_Prisoner.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wedge Antilles (Original)" "$PAGES/Wedge_Antilles_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wedge Antilles (PC Errata)" "$PAGES/Wedge_Antilles_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wedge Antilles" "$PAGES/Wedge_Antilles.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Weequay Marksman (Original)" "$PAGES/Weequay_Marksman_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Weequay Marksman (PC Errata)" "$PAGES/Weequay_Marksman_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Weequay Marksman" "$PAGES/Weequay_Marksman.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wes Janson (Original)" "$PAGES/Wes_Janson_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wes Janson (PC Errata)" "$PAGES/Wes_Janson_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wes Janson" "$PAGES/Wes_Janson.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wooof (Original)" "$PAGES/Wooof_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wooof (PC Errata)" "$PAGES/Wooof_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wooof" "$PAGES/Wooof.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Zuckuss (Original)" "$PAGES/Zuckuss_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Zuckuss (PC Errata)" "$PAGES/Zuckuss_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Zuckuss" "$PAGES/Zuckuss.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Zuckuss In Mist Hunter (Original)" "$PAGES/Zuckuss_In_Mist_Hunter_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Zuckuss In Mist Hunter (PC Errata)" "$PAGES/Zuckuss_In_Mist_Hunter_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Zuckuss In Mist Hunter" "$PAGES/Zuckuss_In_Mist_Hunter.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Zuckuss' Snare Rifle (Original)" "$PAGES/Zuckuss'_Snare_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Zuckuss' Snare Rifle (PC Errata)" "$PAGES/Zuckuss'_Snare_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Zuckuss' Snare Rifle" "$PAGES/Zuckuss'_Snare_Rifle.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch35 (Vine Snake through Zuckuss' Snare Rifle)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch35 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Vine Snake" \
  "Vine Snake (Original)" \
  "Vine Snake (PC Errata)" \
  "Vine Snake (Dark)" \
  "Vine Snake (Dark) (Original)" \
  "Vine Snake (Dark) (PC Errata)" \
  "We Have A Prisoner" \
  "We Have A Prisoner (Original)" \
  "We Have A Prisoner (PC Errata)" \
  "Wedge Antilles" \
  "Wedge Antilles (Original)" \
  "Wedge Antilles (PC Errata)" \
  "Weequay Marksman" \
  "Weequay Marksman (Original)" \
  "Weequay Marksman (PC Errata)" \
  "Wes Janson" \
  "Wes Janson (Original)" \
  "Wes Janson (PC Errata)" \
  "Wooof" \
  "Wooof (Original)" \
  "Wooof (PC Errata)" \
  "Zuckuss" \
  "Zuckuss (Original)" \
  "Zuckuss (PC Errata)" \
  "Zuckuss In Mist Hunter" \
  "Zuckuss In Mist Hunter (Original)" \
  "Zuckuss In Mist Hunter (PC Errata)" \
  "Zuckuss' Snare Rifle" \
  "Zuckuss' Snare Rifle (Original)" \
  "Zuckuss' Snare Rifle (PC Errata)" \
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
echo DONE_APPLY_BATCH35_PC_ERRATA
