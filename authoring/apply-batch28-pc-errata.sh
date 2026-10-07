#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch28-gifs

ARCHIVES=(
  CloudCity-L-punchit-decipher-archive.gif
  Dagobah-D-punishingone-decipher-archive.gif
  CloudCity-L-putthatdown-decipher-archive.gif
  Premiere-L-quadlasercannon-decipher-archive.gif
  ANH-D-r2q2-decipher-archive.gif
  SpecialEdition-L-r3t2-decipher-archive.gif
  ANH-D-r3t6-decipher-archive.gif
  Premiere-L-r4e1-decipher-archive.gif
  Premiere-D-r4m9-decipher-archive.gif
  JabbasPalace-L-raycryjerd-decipher-archive.gif
  Dagobah-L-rebelflightsuit-decipher-archive.gif
  Premiere-L-rebelguard-decipher-archive.gif
)
HT_FILES=(
  CC-L-punchit.gif
  Dagobah-D-punishingone.gif
  CC-L-putthatdown.gif
  Premiere-L-quadlasercannon.gif
  ANH-D-r2q2.gif
  SE-L-r3t2.gif
  ANH-D-r3t6.gif
  Premiere-L-r4e1.gif
  Premiere-D-r4m9.gif
  JP-L-raycryjerd.gif
  Dagobah-L-rebelflightsuit.gif
  Premiere-L-rebelguard.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch28-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch28-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch28-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch28 (Punch It! through Rebel Guard); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch28-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch28-gifs
fi

edit "File:CloudCity-L-punchit-decipher-archive.gif" "$PAGES/File_CloudCity-L-punchit-decipher-archive.gif.wiki" "File: Decipher archive Original Punch It!"
edit "File:Dagobah-D-punishingone-decipher-archive.gif" "$PAGES/File_Dagobah-D-punishingone-decipher-archive.gif.wiki" "File: Decipher archive Original Punishing One"
edit "File:CloudCity-L-putthatdown-decipher-archive.gif" "$PAGES/File_CloudCity-L-putthatdown-decipher-archive.gif.wiki" "File: Decipher archive Original Put That Down"
edit "File:Premiere-L-quadlasercannon-decipher-archive.gif" "$PAGES/File_Premiere-L-quadlasercannon-decipher-archive.gif.wiki" "File: Decipher archive Original Quad Laser Cannon"
edit "File:ANH-D-r2q2-decipher-archive.gif" "$PAGES/File_ANH-D-r2q2-decipher-archive.gif.wiki" "File: Decipher archive Original R2-Q2 (Artoo-Kyootoo)"
edit "File:SpecialEdition-L-r3t2-decipher-archive.gif" "$PAGES/File_SpecialEdition-L-r3t2-decipher-archive.gif.wiki" "File: Decipher archive Original R3-T2 (Arthree-Teetoo)"
edit "File:ANH-D-r3t6-decipher-archive.gif" "$PAGES/File_ANH-D-r3t6-decipher-archive.gif.wiki" "File: Decipher archive Original R3-T6 (Arthree-Teesix)"
edit "File:Premiere-L-r4e1-decipher-archive.gif" "$PAGES/File_Premiere-L-r4e1-decipher-archive.gif.wiki" "File: Decipher archive Original R4-E1 (Arfour-Eeone)"
edit "File:Premiere-D-r4m9-decipher-archive.gif" "$PAGES/File_Premiere-D-r4m9-decipher-archive.gif.wiki" "File: Decipher archive Original R4-M9 (Arfour-Emmnine)"
edit "File:JabbasPalace-L-raycryjerd-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-raycryjerd-decipher-archive.gif.wiki" "File: Decipher archive Original Rayc Ryjerd"
edit "File:Dagobah-L-rebelflightsuit-decipher-archive.gif" "$PAGES/File_Dagobah-L-rebelflightsuit-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Flight Suit"
edit "File:Premiere-L-rebelguard-decipher-archive.gif" "$PAGES/File_Premiere-L-rebelguard-decipher-archive.gif.wiki" "File: Decipher archive Original Rebel Guard"

edit "Punch It! (Original)" "$PAGES/Punch_It!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Punch It! (PC Errata)" "$PAGES/Punch_It!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Punch It!" "$PAGES/Punch_It!.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Punishing One (Original)" "$PAGES/Punishing_One_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Punishing One (PC Errata)" "$PAGES/Punishing_One_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Punishing One" "$PAGES/Punishing_One.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Put That Down (Original)" "$PAGES/Put_That_Down_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Put That Down (PC Errata)" "$PAGES/Put_That_Down_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Put That Down" "$PAGES/Put_That_Down.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Quad Laser Cannon (Original)" "$PAGES/Quad_Laser_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Quad Laser Cannon (PC Errata)" "$PAGES/Quad_Laser_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Quad Laser Cannon" "$PAGES/Quad_Laser_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "R2-Q2 (Artoo-Kyootoo) (Original)" "$PAGES/R2-Q2_(Artoo-Kyootoo)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "R2-Q2 (Artoo-Kyootoo) (PC Errata)" "$PAGES/R2-Q2_(Artoo-Kyootoo)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "R2-Q2 (Artoo-Kyootoo)" "$PAGES/R2-Q2_(Artoo-Kyootoo).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "R3-T2 (Arthree-Teetoo) (Original)" "$PAGES/R3-T2_(Arthree-Teetoo)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "R3-T2 (Arthree-Teetoo) (PC Errata)" "$PAGES/R3-T2_(Arthree-Teetoo)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "R3-T2 (Arthree-Teetoo)" "$PAGES/R3-T2_(Arthree-Teetoo).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "R3-T6 (Arthree-Teesix) (Original)" "$PAGES/R3-T6_(Arthree-Teesix)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "R3-T6 (Arthree-Teesix) (PC Errata)" "$PAGES/R3-T6_(Arthree-Teesix)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "R3-T6 (Arthree-Teesix)" "$PAGES/R3-T6_(Arthree-Teesix).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "R4-E1 (Arfour-Eeone) (Original)" "$PAGES/R4-E1_(Arfour-Eeone)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "R4-E1 (Arfour-Eeone) (PC Errata)" "$PAGES/R4-E1_(Arfour-Eeone)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "R4-E1 (Arfour-Eeone)" "$PAGES/R4-E1_(Arfour-Eeone).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "R4-M9 (Arfour-Emmnine) (Original)" "$PAGES/R4-M9_(Arfour-Emmnine)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "R4-M9 (Arfour-Emmnine) (PC Errata)" "$PAGES/R4-M9_(Arfour-Emmnine)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "R4-M9 (Arfour-Emmnine)" "$PAGES/R4-M9_(Arfour-Emmnine).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rayc Ryjerd (Original)" "$PAGES/Rayc_Ryjerd_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rayc Ryjerd (PC Errata)" "$PAGES/Rayc_Ryjerd_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rayc Ryjerd" "$PAGES/Rayc_Ryjerd.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Flight Suit (Original)" "$PAGES/Rebel_Flight_Suit_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Flight Suit (PC Errata)" "$PAGES/Rebel_Flight_Suit_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Flight Suit" "$PAGES/Rebel_Flight_Suit.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Rebel Guard (Original)" "$PAGES/Rebel_Guard_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Rebel Guard (PC Errata)" "$PAGES/Rebel_Guard_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Rebel Guard" "$PAGES/Rebel_Guard.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch28 (Punch It! through Rebel Guard)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch28 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Punch It!" \
  "Punch It! (Original)" \
  "Punch It! (PC Errata)" \
  "Punishing One" \
  "Punishing One (Original)" \
  "Punishing One (PC Errata)" \
  "Put That Down" \
  "Put That Down (Original)" \
  "Put That Down (PC Errata)" \
  "Quad Laser Cannon" \
  "Quad Laser Cannon (Original)" \
  "Quad Laser Cannon (PC Errata)" \
  "R2-Q2 (Artoo-Kyootoo)" \
  "R2-Q2 (Artoo-Kyootoo) (Original)" \
  "R2-Q2 (Artoo-Kyootoo) (PC Errata)" \
  "R3-T2 (Arthree-Teetoo)" \
  "R3-T2 (Arthree-Teetoo) (Original)" \
  "R3-T2 (Arthree-Teetoo) (PC Errata)" \
  "R3-T6 (Arthree-Teesix)" \
  "R3-T6 (Arthree-Teesix) (Original)" \
  "R3-T6 (Arthree-Teesix) (PC Errata)" \
  "R4-E1 (Arfour-Eeone)" \
  "R4-E1 (Arfour-Eeone) (Original)" \
  "R4-E1 (Arfour-Eeone) (PC Errata)" \
  "R4-M9 (Arfour-Emmnine)" \
  "R4-M9 (Arfour-Emmnine) (Original)" \
  "R4-M9 (Arfour-Emmnine) (PC Errata)" \
  "Rayc Ryjerd" \
  "Rayc Ryjerd (Original)" \
  "Rayc Ryjerd (PC Errata)" \
  "Rebel Flight Suit" \
  "Rebel Flight Suit (Original)" \
  "Rebel Flight Suit (PC Errata)" \
  "Rebel Guard" \
  "Rebel Guard (Original)" \
  "Rebel Guard (PC Errata)" \
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
echo DONE_APPLY_BATCH28_PC_ERRATA
