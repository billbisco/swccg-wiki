#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs10-original
STUBS=$ROOT/pages/vs10-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs10o-stubs-import

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

echo "== importImages VS10O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS10O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs10o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs10o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 10 (Original) Remaster slip faces from VirtualCards10.pdf" \
  --overwrite \
  /tmp/vs10o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 10 (Original)" "$HUBS/Virtual_Set_10_(Original).wiki" "VS10 Original: link all 14 Remaster slip stubs"
edit 'Chewie (V) (Virtual Set 10)' "$STUBS/Chewie_(V)_(Virtual_Set_10).wiki" "VS10O stub 01"
edit 'Evacuation Control (V) (Virtual Set 10)' "$STUBS/Evacuation_Control_(V)_(Virtual_Set_10).wiki" "VS10O stub 02"
edit 'Gold Leader In Gold 1 (V) (Virtual Set 10)' "$STUBS/Gold_Leader_In_Gold_1_(V)_(Virtual_Set_10).wiki" "VS10O stub 03"
edit 'Han Solo (V) (Virtual Set 10)' "$STUBS/Han_Solo_(V)_(Virtual_Set_10).wiki" "VS10O stub 04"
edit 'Luke (V) (Virtual Set 10)' "$STUBS/Luke_(V)_(Virtual_Set_10).wiki" "VS10O stub 05"
edit 'Mandalorian Mishap (V) (Virtual Set 10)' "$STUBS/Mandalorian_Mishap_(V)_(Virtual_Set_10).wiki" "VS10O stub 06"
edit 'Shocking Information (V) (Virtual Set 10)' "$STUBS/Shocking_Information_(V)_(Virtual_Set_10).wiki" "VS10O stub 07"
edit "Darth Vader's Lightsaber (V) (Virtual Set 10)" "$STUBS/Darth_Vaders_Lightsaber_(V)_(Virtual_Set_10).wiki" "VS10O stub 08"
edit 'Imperial Justice (V) (Virtual Set 10)' "$STUBS/Imperial_Justice_(V)_(Virtual_Set_10).wiki" "VS10O stub 09"
edit 'Insignificant Rebellion (V) (Virtual Set 10)' "$STUBS/Insignificant_Rebellion_(V)_(Virtual_Set_10).wiki" "VS10O stub 10"
edit 'Shocking Revelation (V) (Virtual Set 10)' "$STUBS/Shocking_Revelation_(V)_(Virtual_Set_10).wiki" "VS10O stub 11"
edit 'Vader (V) (Virtual Set 10)' "$STUBS/Vader_(V)_(Virtual_Set_10).wiki" "VS10O stub 12"
edit "Vader's Anger (V) (Virtual Set 10)" "$STUBS/Vaders_Anger_(V)_(Virtual_Set_10).wiki" "VS10O stub 13"
edit 'Veers (V) (Virtual Set 10)' "$STUBS/Veers_(V)_(Virtual_Set_10).wiki" "VS10O stub 14"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "== purgePage hub + stubs + samples =="
docker exec swccg_wiki php maintenance/run.php purgePage 'Virtual Set 10 (Original)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Main Page' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Category:Virtual Original sets' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Chewie (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Evacuation Control (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Gold Leader In Gold 1 (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Han Solo (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Luke (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Mandalorian Mishap (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Shocking Information (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage "Darth Vader's Lightsaber (V) (Virtual Set 10)" || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Imperial Justice (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Insignificant Rebellion (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Shocking Revelation (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Vader (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage "Vader's Anger (V) (Virtual Set 10)" || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Veers (V) (Virtual Set 10)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS10O-01-Chewie.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS10O-03-Gold_Leader_In_Gold_1.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS10O-08-Darth_Vaders_Lightsaber.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS10O-12-Vader.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS10O-14-Veers.png' || true
echo VS10O_APPLY_DONE
