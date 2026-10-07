#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch21-gifs

ARCHIVES=(
  Hoth-L-k3pokaythreepio-decipher-archive.gif
  Premiere-L-kalfalnlcndros-decipher-archive.gif
  CloudCity-L-kebyc-decipher-archive.gif
  DeathStarII-L-keirsantage-decipher-archive.gif
  Premiere-D-ketmaliss-decipher-archive.gif
  JabbasPalace-D-kithaba-decipher-archive.gif
  Dagobah-D-knowledgeanddefense-decipher-archive.gif
  Premiere-L-lukeskywalker-decipher-archive.gif
  Premiere-L-lightsaberproficiency-decipher-archive.gif
  Premiere-L-leiassportingblaster-decipher-archive.gif
  ANewHope-L-letthewookieewin-decipher-archive.gif
  CloudCity-L-landocalrissian-decipher-archive.gif
)
HT_FILES=(
  Hoth-L-k3pokaythreepio.gif
  Premiere-L-kalfalnlcndros.gif
  CC-L-kebyc.gif
  DS2-L-keirsantage.gif
  Premiere-D-ketmaliss.gif
  JP-D-kithaba.gif
  Dagobah-D-knowledgeanddefense.gif
  Premiere-L-lukeskywalker.gif
  Premiere-L-lightsaberproficiency.gif
  Premiere-L-leiassportingblaster.gif
  ANH-L-letthewookieewin.gif
  CC-L-landocalrissian.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch21-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch21-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch21-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch21 (K-3PO through Lando Calrissian Light); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch21-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch21-gifs
fi

edit "File:Hoth-L-k3pokaythreepio-decipher-archive.gif" "$PAGES/File_Hoth-L-k3pokaythreepio-decipher-archive.gif.wiki" "File: Decipher archive Original K-3PO (Kay-Threepio)"
edit "File:Premiere-L-kalfalnlcndros-decipher-archive.gif" "$PAGES/File_Premiere-L-kalfalnlcndros-decipher-archive.gif.wiki" "File: Decipher archive Original Kal'Falnl C'ndros"
edit "File:CloudCity-L-kebyc-decipher-archive.gif" "$PAGES/File_CloudCity-L-kebyc-decipher-archive.gif.wiki" "File: Decipher archive Original Kebyc"
edit "File:DeathStarII-L-keirsantage-decipher-archive.gif" "$PAGES/File_DeathStarII-L-keirsantage-decipher-archive.gif.wiki" "File: Decipher archive Original Keir Santage"
edit "File:Premiere-D-ketmaliss-decipher-archive.gif" "$PAGES/File_Premiere-D-ketmaliss-decipher-archive.gif.wiki" "File: Decipher archive Original Ket Maliss"
edit "File:JabbasPalace-D-kithaba-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-kithaba-decipher-archive.gif.wiki" "File: Decipher archive Original Kithaba"
edit "File:Dagobah-D-knowledgeanddefense-decipher-archive.gif" "$PAGES/File_Dagobah-D-knowledgeanddefense-decipher-archive.gif.wiki" "File: Decipher archive Original Knowledge And Defense"
edit "File:Premiere-L-lukeskywalker-decipher-archive.gif" "$PAGES/File_Premiere-L-lukeskywalker-decipher-archive.gif.wiki" "File: Decipher archive Original Luke Skywalker"
edit "File:Premiere-L-lightsaberproficiency-decipher-archive.gif" "$PAGES/File_Premiere-L-lightsaberproficiency-decipher-archive.gif.wiki" "File: Decipher archive Original Lightsaber Proficiency"
edit "File:Premiere-L-leiassportingblaster-decipher-archive.gif" "$PAGES/File_Premiere-L-leiassportingblaster-decipher-archive.gif.wiki" "File: Decipher archive Original Leia's Sporting Blaster"
edit "File:ANewHope-L-letthewookieewin-decipher-archive.gif" "$PAGES/File_ANewHope-L-letthewookieewin-decipher-archive.gif.wiki" "File: Decipher archive Original Let The Wookiee Win"
edit "File:CloudCity-L-landocalrissian-decipher-archive.gif" "$PAGES/File_CloudCity-L-landocalrissian-decipher-archive.gif.wiki" "File: Decipher archive Original Lando Calrissian"
edit "K-3PO (Kay-Threepio) (Original)" "$PAGES/K-3PO_(Kay-Threepio)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "K-3PO (Kay-Threepio) (PC Errata)" "$PAGES/K-3PO_(Kay-Threepio)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "K-3PO (Kay-Threepio)" "$PAGES/K-3PO_(Kay-Threepio).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Kal'Falnl C'ndros (Original)" "$PAGES/Kal'Falnl_C'ndros_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Kal'Falnl C'ndros (PC Errata)" "$PAGES/Kal'Falnl_C'ndros_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Kal'Falnl C'ndros" "$PAGES/Kal'Falnl_C'ndros.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Kebyc (Original)" "$PAGES/Kebyc_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Kebyc (PC Errata)" "$PAGES/Kebyc_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Kebyc" "$PAGES/Kebyc.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Keir Santage (Original)" "$PAGES/Keir_Santage_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Keir Santage (PC Errata)" "$PAGES/Keir_Santage_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Keir Santage" "$PAGES/Keir_Santage.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ket Maliss (Original)" "$PAGES/Ket_Maliss_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ket Maliss (PC Errata)" "$PAGES/Ket_Maliss_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ket Maliss" "$PAGES/Ket_Maliss.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Kithaba (Original)" "$PAGES/Kithaba_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Kithaba (PC Errata)" "$PAGES/Kithaba_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Kithaba" "$PAGES/Kithaba.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Knowledge And Defense (Original)" "$PAGES/Knowledge_And_Defense_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Knowledge And Defense (PC Errata)" "$PAGES/Knowledge_And_Defense_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Knowledge And Defense" "$PAGES/Knowledge_And_Defense.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Luke Skywalker (Original)" "$PAGES/Luke_Skywalker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Luke Skywalker (PC Errata)" "$PAGES/Luke_Skywalker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Luke Skywalker" "$PAGES/Luke_Skywalker.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lightsaber Proficiency (Original)" "$PAGES/Lightsaber_Proficiency_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lightsaber Proficiency (PC Errata)" "$PAGES/Lightsaber_Proficiency_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lightsaber Proficiency" "$PAGES/Lightsaber_Proficiency.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Leia's Sporting Blaster (Original)" "$PAGES/Leia's_Sporting_Blaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Leia's Sporting Blaster (PC Errata)" "$PAGES/Leia's_Sporting_Blaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Leia's Sporting Blaster" "$PAGES/Leia's_Sporting_Blaster.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Let The Wookiee Win (Original)" "$PAGES/Let_The_Wookiee_Win_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Let The Wookiee Win (PC Errata)" "$PAGES/Let_The_Wookiee_Win_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Let The Wookiee Win" "$PAGES/Let_The_Wookiee_Win.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lando Calrissian (Original)" "$PAGES/Lando_Calrissian_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lando Calrissian (PC Errata)" "$PAGES/Lando_Calrissian_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lando Calrissian" "$PAGES/Lando_Calrissian.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch21 (K-3PO through Lando Calrissian)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch21 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "K-3PO (Kay-Threepio)" \
  "K-3PO (Kay-Threepio) (Original)" \
  "K-3PO (Kay-Threepio) (PC Errata)" \
  "Kal'Falnl C'ndros" \
  "Kal'Falnl C'ndros (Original)" \
  "Kal'Falnl C'ndros (PC Errata)" \
  "Kebyc" \
  "Kebyc (Original)" \
  "Kebyc (PC Errata)" \
  "Keir Santage" \
  "Keir Santage (Original)" \
  "Keir Santage (PC Errata)" \
  "Ket Maliss" \
  "Ket Maliss (Original)" \
  "Ket Maliss (PC Errata)" \
  "Kithaba" \
  "Kithaba (Original)" \
  "Kithaba (PC Errata)" \
  "Knowledge And Defense" \
  "Knowledge And Defense (Original)" \
  "Knowledge And Defense (PC Errata)" \
  "Luke Skywalker" \
  "Luke Skywalker (Original)" \
  "Luke Skywalker (PC Errata)" \
  "Lightsaber Proficiency" \
  "Lightsaber Proficiency (Original)" \
  "Lightsaber Proficiency (PC Errata)" \
  "Leia's Sporting Blaster" \
  "Leia's Sporting Blaster (Original)" \
  "Leia's Sporting Blaster (PC Errata)" \
  "Let The Wookiee Win" \
  "Let The Wookiee Win (Original)" \
  "Let The Wookiee Win (PC Errata)" \
  "Lando Calrissian" \
  "Lando Calrissian (Original)" \
  "Lando Calrissian (PC Errata)" \
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
echo DONE_APPLY_BATCH21_PC_ERRATA
