#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs7-original
STUBS=$ROOT/pages/vs7-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs7o-stubs-import

strip() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"  {p.name} nonascii={n}")
assert n==0, p
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip "$file"
  echo "edit: $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== importImages VS7O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS7O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs7o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs7o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 7 (Original) Remaster slip faces from VirtualCards7.pdf" \
  --overwrite \
  /tmp/vs7o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 7 (Original)" "$HUBS/Virtual_Set_7_(Original).wiki" "VS7 Original: link all 22 Remaster slip stubs"
edit 'Chewbacca, Protector (V) (Virtual Set 7)' "$STUBS/Chewbacca_Protector_(V)_(Virtual_Set_7).wiki" "VS7O stub 01"
edit 'Dash Rendar (V) (Virtual Set 7)' "$STUBS/Dash_Rendar_(V)_(Virtual_Set_7).wiki" "VS7O stub 02"
edit 'Gambler'\''s Luck (V) (Virtual Set 7)' "$STUBS/Gamblers_Luck_(V)_(Virtual_Set_7).wiki" "VS7O stub 03"
edit 'Impressive, Most Impressive (V) (Virtual Set 7)' "$STUBS/Impressive_Most_Impressive_(V)_(Virtual_Set_7).wiki" "VS7O stub 04"
edit 'Ke Chu Ke Kukuta? (V) (Virtual Set 7)' "$STUBS/Ke_Chu_Ke_Kukuta_(V)_(Virtual_Set_7).wiki" "VS7O stub 05"
edit 'LE-BO2D9 (Leebo) (V) (Virtual Set 7)' "$STUBS/LEBO2D9_(Leebo)_(V)_(Virtual_Set_7).wiki" "VS7O stub 06"
edit 'Mercenary Armor (V) (Virtual Set 7)' "$STUBS/Mercenary_Armor_(V)_(Virtual_Set_7).wiki" "VS7O stub 07"
edit 'Smuggler'\''s Blues (V) (Virtual Set 7)' "$STUBS/Smugglers_Blues_(V)_(Virtual_Set_7).wiki" "VS7O stub 08"
edit 'Tantive IV (V) (Virtual Set 7)' "$STUBS/Tantive_IV_(V)_(Virtual_Set_7).wiki" "VS7O stub 09"
edit 'Tawss Khaa (V) (Virtual Set 7)' "$STUBS/Tawss_Khaa_(V)_(Virtual_Set_7).wiki" "VS7O stub 10"
edit 'Uh-oh! (V) (Virtual Set 7)' "$STUBS/Uh_oh_(V)_(Virtual_Set_7).wiki" "VS7O stub 11"
edit 'Bane Malar (V) (Virtual Set 7)' "$STUBS/Bane_Malar_(V)_(Virtual_Set_7).wiki" "VS7O stub 12"
edit 'Brief Loss Of Control (V) (Virtual Set 7)' "$STUBS/Brief_Loss_Of_Control_(V)_(Virtual_Set_7).wiki" "VS7O stub 13"
edit 'Flagship Operations (V) (Virtual Set 7)' "$STUBS/Flagship_Operations_(V)_(Virtual_Set_7).wiki" "VS7O stub 14"
edit 'Frustration (V) (Virtual Set 7)' "$STUBS/Frustration_(V)_(Virtual_Set_7).wiki" "VS7O stub 15"
edit 'Guri (V) (Virtual Set 7)' "$STUBS/Guri_(V)_(Virtual_Set_7).wiki" "VS7O stub 16"
edit 'Information Exchange (V) (Virtual Set 7)' "$STUBS/Information_Exchange_(V)_(Virtual_Set_7).wiki" "VS7O stub 17"
edit 'Prince Xizor (V) (Virtual Set 7)' "$STUBS/Prince_Xizor_(V)_(Virtual_Set_7).wiki" "VS7O stub 18"
edit 'Slave I (V) (Virtual Set 7)' "$STUBS/Slave_I_(V)_(Virtual_Set_7).wiki" "VS7O stub 19"
edit 'Those Rebels Won'\''t Escape Us (V) (Virtual Set 7)' "$STUBS/Those_Rebels_Wont_Escape_Us_(V)_(Virtual_Set_7).wiki" "VS7O stub 20"
edit 'Unexpected Interruption (V) (Virtual Set 7)' "$STUBS/Unexpected_Interruption_(V)_(Virtual_Set_7).wiki" "VS7O stub 21"
edit 'Zuckuss (V) (Virtual Set 7)' "$STUBS/Zuckuss_(V)_(Virtual_Set_7).wiki" "VS7O stub 22"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin || true

echo "== purgePage hub + stubs + samples =="
docker exec swccg_wiki php maintenance/run.php purgePage 'Virtual Set 7 (Original)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Main Page' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Category:Virtual Original sets' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Chewbacca, Protector (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Dash Rendar (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Gambler'\''s Luck (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Impressive, Most Impressive (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Ke Chu Ke Kukuta? (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'LE-BO2D9 (Leebo) (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Mercenary Armor (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Smuggler'\''s Blues (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Tantive IV (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Tawss Khaa (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Uh-oh! (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Bane Malar (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Brief Loss Of Control (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Flagship Operations (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Frustration (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Guri (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Information Exchange (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Prince Xizor (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Slave I (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Those Rebels Won'\''t Escape Us (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Unexpected Interruption (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Zuckuss (V) (Virtual Set 7)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS7O-01-Chewbacca_Protector.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS7O-02-Dash_Rendar.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS7O-09-Tantive_IV.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS7O-16-Guri.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS7O-22-Zuckuss.png' || true
echo VS7O_APPLY_DONE
