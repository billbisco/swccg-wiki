#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch25-gifs

ARCHIVES=(
  Premiere-L-obiwanscape-decipher-archive.gif
  Hoth-D-ohswitchoff-decipher-archive.gif
  ANH-D-officerevax-decipher-archive.gif
  Premiere-D-observationholocam-decipher-archive.gif
  ReflectionsII-L-obiwansjournal-decipher-archive.gif
  Premiere-L-narrowescape-decipher-archive.gif
  Premiere-D-nevaryalnal-decipher-archive.gif
  ANH-D-monnok-decipher-archive.gif
  Hoth-D-mournfulroar-decipher-archive.gif
  JabbasPalace-L-moseisleyblaster-decipher-archive.gif
  JabbasPalace-D-moseisleyblaster-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-obiwanscape.gif
  Hoth-D-ohswitchoff.gif
  ANH-D-officerevax.gif
  Premiere-D-observationholocam.gif
  Ref2-L-obiwansjournal.gif
  Premiere-L-narrowescape.gif
  Premiere-D-nevaryalnal.gif
  ANH-D-monnok.gif
  Hoth-D-mournfulroar.gif
  JP-L-moseisleyblaster.gif
  JP-D-moseisleyblaster.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch25-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch25-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch25-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch25 (Obi-Wan's Cape through Mos Eisley Blaster dual); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch25-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch25-gifs
fi

edit "File:Premiere-L-obiwanscape-decipher-archive.gif" "$PAGES/File_Premiere-L-obiwanscape-decipher-archive.gif.wiki" "File: Decipher archive Original Obi-Wan's Cape"
edit "File:Hoth-D-ohswitchoff-decipher-archive.gif" "$PAGES/File_Hoth-D-ohswitchoff-decipher-archive.gif.wiki" "File: Decipher archive Original Oh, Switch Off"
edit "File:ANH-D-officerevax-decipher-archive.gif" "$PAGES/File_ANH-D-officerevax-decipher-archive.gif.wiki" "File: Decipher archive Original Officer Evax"
edit "File:Premiere-D-observationholocam-decipher-archive.gif" "$PAGES/File_Premiere-D-observationholocam-decipher-archive.gif.wiki" "File: Decipher archive Original Observation Holocam"
edit "File:ReflectionsII-L-obiwansjournal-decipher-archive.gif" "$PAGES/File_ReflectionsII-L-obiwansjournal-decipher-archive.gif.wiki" "File: Decipher archive Original Obi-Wan's Journal"
edit "File:Premiere-L-narrowescape-decipher-archive.gif" "$PAGES/File_Premiere-L-narrowescape-decipher-archive.gif.wiki" "File: Decipher archive Original Narrow Escape"
edit "File:Premiere-D-nevaryalnal-decipher-archive.gif" "$PAGES/File_Premiere-D-nevaryalnal-decipher-archive.gif.wiki" "File: Decipher archive Original Nevar Yalnal"
edit "File:ANH-D-monnok-decipher-archive.gif" "$PAGES/File_ANH-D-monnok-decipher-archive.gif.wiki" "File: Decipher archive Original Monnok"
edit "File:Hoth-D-mournfulroar-decipher-archive.gif" "$PAGES/File_Hoth-D-mournfulroar-decipher-archive.gif.wiki" "File: Decipher archive Original Mournful Roar"
edit "File:JabbasPalace-L-moseisleyblaster-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-moseisleyblaster-decipher-archive.gif.wiki" "File: Decipher archive Original Mos Eisley Blaster"
edit "File:JabbasPalace-D-moseisleyblaster-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-moseisleyblaster-decipher-archive.gif.wiki" "File: Decipher archive Original Mos Eisley Blaster (Dark)"
edit "Obi-Wan's Cape (Original)" "$PAGES/Obi-Wan's_Cape_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Obi-Wan's Cape (PC Errata)" "$PAGES/Obi-Wan's_Cape_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Obi-Wan's Cape" "$PAGES/Obi-Wan's_Cape.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Oh, Switch Off (Original)" "$PAGES/Oh,_Switch_Off_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Oh, Switch Off (PC Errata)" "$PAGES/Oh,_Switch_Off_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Oh, Switch Off" "$PAGES/Oh,_Switch_Off.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Officer Evax (Original)" "$PAGES/Officer_Evax_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Officer Evax (PC Errata)" "$PAGES/Officer_Evax_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Officer Evax" "$PAGES/Officer_Evax.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Observation Holocam (Original)" "$PAGES/Observation_Holocam_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Observation Holocam (PC Errata)" "$PAGES/Observation_Holocam_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Observation Holocam" "$PAGES/Observation_Holocam.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Obi-Wan's Journal (Original)" "$PAGES/Obi-Wan's_Journal_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Obi-Wan's Journal (PC Errata)" "$PAGES/Obi-Wan's_Journal_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Obi-Wan's Journal" "$PAGES/Obi-Wan's_Journal.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Narrow Escape (Original)" "$PAGES/Narrow_Escape_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Narrow Escape (PC Errata)" "$PAGES/Narrow_Escape_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Narrow Escape" "$PAGES/Narrow_Escape.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Nevar Yalnal (Original)" "$PAGES/Nevar_Yalnal_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Nevar Yalnal (PC Errata)" "$PAGES/Nevar_Yalnal_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Nevar Yalnal" "$PAGES/Nevar_Yalnal.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Monnok (Original)" "$PAGES/Monnok_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Monnok (PC Errata)" "$PAGES/Monnok_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Monnok" "$PAGES/Monnok.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Mournful Roar (Original)" "$PAGES/Mournful_Roar_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Mournful Roar (PC Errata)" "$PAGES/Mournful_Roar_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Mournful Roar" "$PAGES/Mournful_Roar.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Mos Eisley Blaster (Original)" "$PAGES/Mos_Eisley_Blaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Mos Eisley Blaster (PC Errata)" "$PAGES/Mos_Eisley_Blaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Mos Eisley Blaster" "$PAGES/Mos_Eisley_Blaster.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Mos Eisley Blaster (Dark) (Original)" "$PAGES/Mos_Eisley_Blaster_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Mos Eisley Blaster (Dark) (PC Errata)" "$PAGES/Mos_Eisley_Blaster_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Mos Eisley Blaster (Dark)" "$PAGES/Mos_Eisley_Blaster_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch25 (Obi-Wan's Cape through Mos Eisley Blaster dual)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch25 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Obi-Wan's Cape" \
  "Obi-Wan's Cape (Original)" \
  "Obi-Wan's Cape (PC Errata)" \
  "Oh, Switch Off" \
  "Oh, Switch Off (Original)" \
  "Oh, Switch Off (PC Errata)" \
  "Officer Evax" \
  "Officer Evax (Original)" \
  "Officer Evax (PC Errata)" \
  "Observation Holocam" \
  "Observation Holocam (Original)" \
  "Observation Holocam (PC Errata)" \
  "Obi-Wan's Journal" \
  "Obi-Wan's Journal (Original)" \
  "Obi-Wan's Journal (PC Errata)" \
  "Narrow Escape" \
  "Narrow Escape (Original)" \
  "Narrow Escape (PC Errata)" \
  "Nevar Yalnal" \
  "Nevar Yalnal (Original)" \
  "Nevar Yalnal (PC Errata)" \
  "Monnok" \
  "Monnok (Original)" \
  "Monnok (PC Errata)" \
  "Mournful Roar" \
  "Mournful Roar (Original)" \
  "Mournful Roar (PC Errata)" \
  "Mos Eisley Blaster" \
  "Mos Eisley Blaster (Original)" \
  "Mos Eisley Blaster (PC Errata)" \
  "Mos Eisley Blaster (Dark)" \
  "Mos Eisley Blaster (Dark) (Original)" \
  "Mos Eisley Blaster (Dark) (PC Errata)" \
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
echo DONE_APPLY_BATCH25_PC_ERRATA
