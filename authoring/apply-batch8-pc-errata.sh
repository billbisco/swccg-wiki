#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch8-gifs

ARCHIVES=(
  CloudCity-L-captainhansolo-decipher-archive.gif
  Premiere-L-collision-decipher-archive.gif
  Hoth-L-commanderlukeskywalker-decipher-archive.gif
  Dagobah-D-commandernemet-decipher-archive.gif
  Premiere-D-commanderpraji-decipher-archive.gif
  CloudCity-D-commanderdesanne-decipher-archive.gif
  ANH-L-commandervandenwillard-decipher-archive.gif
  Hoth-L-concussiongrenade-decipher-archive.gif
  ANH-D-conquest-decipher-archive.gif
  Premiere-L-combinedattack-decipher-archive.gif
  ANH-L-commencerecharging-decipher-archive.gif
  Hoth-D-comscandetection-decipher-archive.gif
  ANH-L-corellia-decipher-archive.gif
)
HT_FILES=(
  CC-L-captainhansolo.gif
  Premiere-L-collision.gif
  Hoth-L-commanderlukeskywalker.gif
  Dagobah-D-commandernemet.gif
  Premiere-D-commanderpraji.gif
  CC-D-commanderdesanne.gif
  ANH-L-commandervandenwillard.gif
  Hoth-L-concussiongrenade.gif
  ANH-D-conquest.gif
  Premiere-L-combinedattack.gif
  ANH-L-commencerecharging.gif
  Hoth-D-comscandetection.gif
  ANH-L-corellia.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch8-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch8-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch8-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch8 (Captain Han Solo, Collision!, Commander Luke Skywalker, Commander Nemet, Commander Praji, Commander Desanne, Commander Vanden Willard, Concussion Grenade, Conquest, Combined Attack, Commence Recharging, ComScan Detection, Corellia); flush crop + flood bleach #FFF. DO NOT replace Holotable. Combined Attack HT already on wiki — archive only.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch8-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch8-gifs
fi

edit "File:CloudCity-L-captainhansolo-decipher-archive.gif" "$PAGES/File_CloudCity-L-captainhansolo-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Captain Han Solo"
edit "File:Premiere-L-collision-decipher-archive.gif" "$PAGES/File_Premiere-L-collision-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Collision!"
edit "File:Hoth-L-commanderlukeskywalker-decipher-archive.gif" "$PAGES/File_Hoth-L-commanderlukeskywalker-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Commander Luke Skywalker"
edit "File:Dagobah-D-commandernemet-decipher-archive.gif" "$PAGES/File_Dagobah-D-commandernemet-decipher-archive.gif.wiki" "File: Decipher Dagobah archive Original Commander Nemet"
edit "File:Premiere-D-commanderpraji-decipher-archive.gif" "$PAGES/File_Premiere-D-commanderpraji-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Commander Praji"
edit "File:CloudCity-D-commanderdesanne-decipher-archive.gif" "$PAGES/File_CloudCity-D-commanderdesanne-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Commander Desanne"
edit "File:ANH-L-commandervandenwillard-decipher-archive.gif" "$PAGES/File_ANH-L-commandervandenwillard-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Commander Vanden Willard"
edit "File:Hoth-L-concussiongrenade-decipher-archive.gif" "$PAGES/File_Hoth-L-concussiongrenade-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Concussion Grenade"
edit "File:ANH-D-conquest-decipher-archive.gif" "$PAGES/File_ANH-D-conquest-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Conquest"
edit "File:Premiere-L-combinedattack-decipher-archive.gif" "$PAGES/File_Premiere-L-combinedattack-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Combined Attack"
edit "File:ANH-L-commencerecharging-decipher-archive.gif" "$PAGES/File_ANH-L-commencerecharging-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Commence Recharging"
edit "File:Hoth-D-comscandetection-decipher-archive.gif" "$PAGES/File_Hoth-D-comscandetection-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original ComScan Detection"
edit "File:ANH-L-corellia-decipher-archive.gif" "$PAGES/File_ANH-L-corellia-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Corellia"

edit "Captain Han Solo (Original)" "$PAGES/Captain_Han_Solo_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Captain Han Solo (PC Errata)" "$PAGES/Captain_Han_Solo_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Captain Han Solo" "$PAGES/Captain_Han_Solo.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Collision! (Original)" "$PAGES/Collision!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Collision! (PC Errata)" "$PAGES/Collision!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Collision!" "$PAGES/Collision!.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Commander Luke Skywalker (Original)" "$PAGES/Commander_Luke_Skywalker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commander Luke Skywalker (PC Errata)" "$PAGES/Commander_Luke_Skywalker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commander Luke Skywalker" "$PAGES/Commander_Luke_Skywalker.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Commander Nemet (Original)" "$PAGES/Commander_Nemet_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commander Nemet (PC Errata)" "$PAGES/Commander_Nemet_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commander Nemet" "$PAGES/Commander_Nemet.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Commander Praji (Original)" "$PAGES/Commander_Praji_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commander Praji (PC Errata)" "$PAGES/Commander_Praji_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commander Praji" "$PAGES/Commander_Praji.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Commander Desanne (Original)" "$PAGES/Commander_Desanne_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commander Desanne (PC Errata)" "$PAGES/Commander_Desanne_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commander Desanne" "$PAGES/Commander_Desanne.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Commander Vanden Willard (Original)" "$PAGES/Commander_Vanden_Willard_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commander Vanden Willard (PC Errata)" "$PAGES/Commander_Vanden_Willard_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commander Vanden Willard" "$PAGES/Commander_Vanden_Willard.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Concussion Grenade (Original)" "$PAGES/Concussion_Grenade_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Concussion Grenade (PC Errata)" "$PAGES/Concussion_Grenade_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Concussion Grenade" "$PAGES/Concussion_Grenade.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Conquest (Original)" "$PAGES/Conquest_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Conquest (PC Errata)" "$PAGES/Conquest_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Conquest" "$PAGES/Conquest.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Combined Attack (Original)" "$PAGES/Combined_Attack_(Original).wiki" "PC Errata seed CREATE: printed Decipher archive Original (article was missing)"
edit "Combined Attack (PC Errata)" "$PAGES/Combined_Attack_(PC_Errata).wiki" "PC Errata seed CREATE: AR 2023 Appendix A + Holotable (article was missing)"
edit "Combined Attack" "$PAGES/Combined_Attack.wiki" "CREATE bare Combined Attack; Decipher print; archive face; link PC Errata (was missing)"

edit "Commence Recharging (Original)" "$PAGES/Commence_Recharging_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Commence Recharging (PC Errata)" "$PAGES/Commence_Recharging_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Commence Recharging" "$PAGES/Commence_Recharging.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "ComScan Detection (Original)" "$PAGES/ComScan_Detection_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "ComScan Detection (PC Errata)" "$PAGES/ComScan_Detection_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "ComScan Detection" "$PAGES/ComScan_Detection.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Corellia (Original)" "$PAGES/Corellia_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Corellia (PC Errata)" "$PAGES/Corellia_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Corellia" "$PAGES/Corellia.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch8 (Captain Han Solo through Corellia)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch8 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Captain Han Solo" "Captain Han Solo (Original)" "Captain Han Solo (PC Errata)" \
  "Collision!" "Collision! (Original)" "Collision! (PC Errata)" \
  "Commander Luke Skywalker" "Commander Luke Skywalker (Original)" "Commander Luke Skywalker (PC Errata)" \
  "Commander Nemet" "Commander Nemet (Original)" "Commander Nemet (PC Errata)" \
  "Commander Praji" "Commander Praji (Original)" "Commander Praji (PC Errata)" \
  "Commander Desanne" "Commander Desanne (Original)" "Commander Desanne (PC Errata)" \
  "Commander Vanden Willard" "Commander Vanden Willard (Original)" "Commander Vanden Willard (PC Errata)" \
  "Concussion Grenade" "Concussion Grenade (Original)" "Concussion Grenade (PC Errata)" \
  "Conquest" "Conquest (Original)" "Conquest (PC Errata)" \
  "Combined Attack" "Combined Attack (Original)" "Combined Attack (PC Errata)" \
  "Commence Recharging" "Commence Recharging (Original)" "Commence Recharging (PC Errata)" \
  "ComScan Detection" "ComScan Detection (Original)" "ComScan Detection (PC Errata)" \
  "Corellia" "Corellia (Original)" "Corellia (PC Errata)" \
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
echo DONE_APPLY_BATCH8_PC_ERRATA
