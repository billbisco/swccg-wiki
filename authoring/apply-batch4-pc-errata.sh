#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch4-gifs

ARCHIVES=(
  JP-L-artoo-decipher-archive.gif
  Premiere-D-assaultrifle-decipher-archive.gif
  Hoth-L-anakinslightsaber-decipher-archive.gif
  ANH-D-astromechshortage-decipher-archive.gif
  Hoth-L-bactatank-decipher-archive.gif
  Hoth-L-atgarlasercannon-decipher-archive.gif
  CC-D-atmosphericassault-decipher-archive.gif
  SE-D-banthaherd-decipher-archive.gif
  Premiere-D-banisskeeg-decipher-archive.gif
)
HT_FILES=(
  JP-L-artoo.gif
  Premiere-D-assaultrifle.gif
  Hoth-L-anakinslightsaber.gif
  ANH-D-astromechshortage.gif
  Hoth-L-bactatank.gif
  Hoth-L-atgarlasercannon.gif
  CC-D-atmosphericassault.gif
  SE-D-banthaherd.gif
  Premiere-D-banisskeeg.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch4-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch4-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch4-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch4 (Artoo, Assault Rifle, Anakin Lightsaber, Astromech Shortage, Bacta Tank, Atgar Laser Cannon, Atmospheric Assault, Bantha Herd, Baniss Keeg); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch4-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch4-gifs
fi

edit "File:JP-L-artoo-decipher-archive.gif" "$PAGES/File_JP-L-artoo-decipher-archive.gif.wiki" "File: Decipher Jabba archive Original Artoo"
edit "File:Premiere-D-assaultrifle-decipher-archive.gif" "$PAGES/File_Premiere-D-assaultrifle-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Assault Rifle"
edit "File:Hoth-L-anakinslightsaber-decipher-archive.gif" "$PAGES/File_Hoth-L-anakinslightsaber-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Anakin's Lightsaber"
edit "File:ANH-D-astromechshortage-decipher-archive.gif" "$PAGES/File_ANH-D-astromechshortage-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Astromech Shortage"
edit "File:Hoth-L-bactatank-decipher-archive.gif" "$PAGES/File_Hoth-L-bactatank-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Bacta Tank"
edit "File:Hoth-L-atgarlasercannon-decipher-archive.gif" "$PAGES/File_Hoth-L-atgarlasercannon-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Atgar Laser Cannon"
edit "File:CC-D-atmosphericassault-decipher-archive.gif" "$PAGES/File_CC-D-atmosphericassault-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Atmospheric Assault"
edit "File:SE-D-banthaherd-decipher-archive.gif" "$PAGES/File_SE-D-banthaherd-decipher-archive.gif.wiki" "File: Decipher Special Edition archive Original Bantha Herd"
edit "File:Premiere-D-banisskeeg-decipher-archive.gif" "$PAGES/File_Premiere-D-banisskeeg-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Baniss Keeg"

edit "Artoo (Jabba's Palace) (Original)" "$PAGES/Artoo_(Jabba's_Palace)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Artoo (Jabba's Palace) (PC Errata)" "$PAGES/Artoo_(Jabba's_Palace)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Artoo (Jabba's Palace)" "$PAGES/Artoo_(Jabba's_Palace).wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Assault Rifle (Original)" "$PAGES/Assault_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Assault Rifle (PC Errata)" "$PAGES/Assault_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Assault Rifle" "$PAGES/Assault_Rifle.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Anakin's Lightsaber (Original)" "$PAGES/Anakin's_Lightsaber_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Anakin's Lightsaber (PC Errata)" "$PAGES/Anakin's_Lightsaber_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Anakin's Lightsaber" "$PAGES/Anakin's_Lightsaber.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Astromech Shortage (Original)" "$PAGES/Astromech_Shortage_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Astromech Shortage (PC Errata)" "$PAGES/Astromech_Shortage_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Astromech Shortage" "$PAGES/Astromech_Shortage.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Bacta Tank (Original)" "$PAGES/Bacta_Tank_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Bacta Tank (PC Errata)" "$PAGES/Bacta_Tank_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Bacta Tank" "$PAGES/Bacta_Tank.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Atgar Laser Cannon (Original)" "$PAGES/Atgar_Laser_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Atgar Laser Cannon (PC Errata)" "$PAGES/Atgar_Laser_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Atgar Laser Cannon" "$PAGES/Atgar_Laser_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Atmospheric Assault (Original)" "$PAGES/Atmospheric_Assault_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Atmospheric Assault (PC Errata)" "$PAGES/Atmospheric_Assault_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Atmospheric Assault" "$PAGES/Atmospheric_Assault.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Bantha Herd (Original)" "$PAGES/Bantha_Herd_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Bantha Herd (PC Errata)" "$PAGES/Bantha_Herd_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Bantha Herd" "$PAGES/Bantha_Herd.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Baniss Keeg (Original)" "$PAGES/Baniss_Keeg_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Baniss Keeg (PC Errata)" "$PAGES/Baniss_Keeg_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Baniss Keeg" "$PAGES/Baniss_Keeg.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch4 (Artoo through Baniss Keeg)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch4 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Artoo (Jabba's Palace)" "Artoo (Jabba's Palace) (Original)" "Artoo (Jabba's Palace) (PC Errata)" \
  "Assault Rifle" "Assault Rifle (Original)" "Assault Rifle (PC Errata)" \
  "Anakin's Lightsaber" "Anakin's Lightsaber (Original)" "Anakin's Lightsaber (PC Errata)" \
  "Astromech Shortage" "Astromech Shortage (Original)" "Astromech Shortage (PC Errata)" \
  "Bacta Tank" "Bacta Tank (Original)" "Bacta Tank (PC Errata)" \
  "Atgar Laser Cannon" "Atgar Laser Cannon (Original)" "Atgar Laser Cannon (PC Errata)" \
  "Atmospheric Assault" "Atmospheric Assault (Original)" "Atmospheric Assault (PC Errata)" \
  "Bantha Herd" "Bantha Herd (Original)" "Bantha Herd (PC Errata)" \
  "Baniss Keeg" "Baniss Keeg (Original)" "Baniss Keeg (PC Errata)" \
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
echo DONE_APPLY_BATCH4_PC_ERRATA
