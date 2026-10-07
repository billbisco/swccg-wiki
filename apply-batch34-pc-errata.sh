#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch34-gifs

ARCHIVES=(
  CloudCity-D-trooperjerrolblendin-decipher-archive.gif
  JabbasPalace-L-vibroax-decipher-archive.gif
  JabbasPalace-D-vibroax-decipher-archive.gif
  Hoth-D-walkerbarrage-decipher-archive.gif
  Hoth-D-walloffire-decipher-archive.gif
  Premiere-L-warriorscourage-decipher-archive.gif
  Dagobah-D-warrantofficermkae-decipher-archive.gif
  Premiere-L-wioslea-decipher-archive.gif
  ANH-L-wookieeroar-decipher-archive.gif
  Dagobah-L-youdohaveyourmoments-decipher-archive.gif
  Hoth-L-zevsenesca-decipher-archive.gif
)
HT_FILES=(
  CC-D-trooperjerrolblendin.gif
  JP-L-vibroax.gif
  JP-D-vibroax.gif
  Hoth-D-walkerbarrage.gif
  Hoth-D-walloffire.gif
  Premiere-L-warriorscourage.gif
  Dagobah-D-warrantofficermkae.gif
  Premiere-L-wioslea.gif
  ANH-L-wookieeroar.gif
  Dagobah-L-youdohaveyourmoments.gif
  Hoth-L-zevsenesca.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch34-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch34-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch34-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch34 (Trooper Jerrol Blendin through Zev Senesca); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch34-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch34-gifs
fi

edit "File:CloudCity-D-trooperjerrolblendin-decipher-archive.gif" "$PAGES/File_CloudCity-D-trooperjerrolblendin-decipher-archive.gif.wiki" "File: Decipher archive Original Trooper Jerrol Blendin"
edit "File:JabbasPalace-L-vibroax-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-vibroax-decipher-archive.gif.wiki" "File: Decipher archive Original Vibro-Ax"
edit "File:JabbasPalace-D-vibroax-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-vibroax-decipher-archive.gif.wiki" "File: Decipher archive Original Vibro-Ax (Dark)"
edit "File:Hoth-D-walkerbarrage-decipher-archive.gif" "$PAGES/File_Hoth-D-walkerbarrage-decipher-archive.gif.wiki" "File: Decipher archive Original Walker Barrage"
edit "File:Hoth-D-walloffire-decipher-archive.gif" "$PAGES/File_Hoth-D-walloffire-decipher-archive.gif.wiki" "File: Decipher archive Original Wall Of Fire"
edit "File:Premiere-L-warriorscourage-decipher-archive.gif" "$PAGES/File_Premiere-L-warriorscourage-decipher-archive.gif.wiki" "File: Decipher archive Original Warrior's Courage"
edit "File:Dagobah-D-warrantofficermkae-decipher-archive.gif" "$PAGES/File_Dagobah-D-warrantofficermkae-decipher-archive.gif.wiki" "File: Decipher archive Original Warrant Officer M'Kae"
edit "File:Premiere-L-wioslea-decipher-archive.gif" "$PAGES/File_Premiere-L-wioslea-decipher-archive.gif.wiki" "File: Decipher archive Original Wioslea"
edit "File:ANH-L-wookieeroar-decipher-archive.gif" "$PAGES/File_ANH-L-wookieeroar-decipher-archive.gif.wiki" "File: Decipher archive Original Wookiee Roar"
edit "File:Dagobah-L-youdohaveyourmoments-decipher-archive.gif" "$PAGES/File_Dagobah-L-youdohaveyourmoments-decipher-archive.gif.wiki" "File: Decipher archive Original You Do Have Your Moments"
edit "File:Hoth-L-zevsenesca-decipher-archive.gif" "$PAGES/File_Hoth-L-zevsenesca-decipher-archive.gif.wiki" "File: Decipher archive Original Zev Senesca"

edit "Trooper Jerrol Blendin (Original)" "$PAGES/Trooper_Jerrol_Blendin_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Trooper Jerrol Blendin (PC Errata)" "$PAGES/Trooper_Jerrol_Blendin_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Trooper Jerrol Blendin" "$PAGES/Trooper_Jerrol_Blendin.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vibro-Ax (Original)" "$PAGES/Vibro-Ax_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vibro-Ax (PC Errata)" "$PAGES/Vibro-Ax_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vibro-Ax" "$PAGES/Vibro-Ax.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vibro-Ax (Dark) (Original)" "$PAGES/Vibro-Ax_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vibro-Ax (Dark) (PC Errata)" "$PAGES/Vibro-Ax_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vibro-Ax (Dark)" "$PAGES/Vibro-Ax_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Walker Barrage (Original)" "$PAGES/Walker_Barrage_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Walker Barrage (PC Errata)" "$PAGES/Walker_Barrage_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Walker Barrage" "$PAGES/Walker_Barrage.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wall Of Fire (Original)" "$PAGES/Wall_Of_Fire_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wall Of Fire (PC Errata)" "$PAGES/Wall_Of_Fire_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wall Of Fire" "$PAGES/Wall_Of_Fire.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Warrior's Courage (Original)" "$PAGES/Warrior's_Courage_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Warrior's Courage (PC Errata)" "$PAGES/Warrior's_Courage_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Warrior's Courage" "$PAGES/Warrior's_Courage.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Warrant Officer M'Kae (Original)" "$PAGES/Warrant_Officer_M'Kae_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Warrant Officer M'Kae (PC Errata)" "$PAGES/Warrant_Officer_M'Kae_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Warrant Officer M'Kae" "$PAGES/Warrant_Officer_M'Kae.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wioslea (Original)" "$PAGES/Wioslea_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wioslea (PC Errata)" "$PAGES/Wioslea_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wioslea" "$PAGES/Wioslea.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Wookiee Roar (Original)" "$PAGES/Wookiee_Roar_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Wookiee Roar (PC Errata)" "$PAGES/Wookiee_Roar_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Wookiee Roar" "$PAGES/Wookiee_Roar.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "You Do Have Your Moments (Original)" "$PAGES/You_Do_Have_Your_Moments_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "You Do Have Your Moments (PC Errata)" "$PAGES/You_Do_Have_Your_Moments_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "You Do Have Your Moments" "$PAGES/You_Do_Have_Your_Moments.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Zev Senesca (Original)" "$PAGES/Zev_Senesca_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Zev Senesca (PC Errata)" "$PAGES/Zev_Senesca_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Zev Senesca" "$PAGES/Zev_Senesca.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch34 (Trooper Jerrol Blendin through Zev Senesca)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch34 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Trooper Jerrol Blendin" \
  "Trooper Jerrol Blendin (Original)" \
  "Trooper Jerrol Blendin (PC Errata)" \
  "Vibro-Ax" \
  "Vibro-Ax (Original)" \
  "Vibro-Ax (PC Errata)" \
  "Vibro-Ax (Dark)" \
  "Vibro-Ax (Dark) (Original)" \
  "Vibro-Ax (Dark) (PC Errata)" \
  "Walker Barrage" \
  "Walker Barrage (Original)" \
  "Walker Barrage (PC Errata)" \
  "Wall Of Fire" \
  "Wall Of Fire (Original)" \
  "Wall Of Fire (PC Errata)" \
  "Warrior's Courage" \
  "Warrior's Courage (Original)" \
  "Warrior's Courage (PC Errata)" \
  "Warrant Officer M'Kae" \
  "Warrant Officer M'Kae (Original)" \
  "Warrant Officer M'Kae (PC Errata)" \
  "Wioslea" \
  "Wioslea (Original)" \
  "Wioslea (PC Errata)" \
  "Wookiee Roar" \
  "Wookiee Roar (Original)" \
  "Wookiee Roar (PC Errata)" \
  "You Do Have Your Moments" \
  "You Do Have Your Moments (Original)" \
  "You Do Have Your Moments (PC Errata)" \
  "Zev Senesca" \
  "Zev Senesca (Original)" \
  "Zev Senesca (PC Errata)" \
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
echo DONE_APPLY_BATCH34_PC_ERRATA
