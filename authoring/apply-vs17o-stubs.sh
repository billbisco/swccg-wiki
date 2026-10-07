#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs17-original
STUBS=$ROOT/pages/vs17-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs17o-stubs-import

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

echo "== importImages VS17O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS17O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs17o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs17o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 17 (Original) Remaster slip faces from VirtualCards17.pdf" \
  --overwrite \
  /tmp/vs17o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 17 (Original)" "$HUBS/Virtual_Set_17_(Original).wiki" "VS17 Original: link all Remaster slip stubs"
edit 'A Jedi'\''s Cunning (V) (Virtual Set 17)' "$STUBS/A_Jedis_Cunning_(V)_(Virtual_Set_17).wiki" "VS17O stub 01"
edit 'A Jedi'\''s Plans (V) (Virtual Set 17)' "$STUBS/A_Jedis_Plans_(V)_(Virtual_Set_17).wiki" "VS17O stub 02"
edit 'An Unusual Amount Of Fear (V) (Virtual Set 17)' "$STUBS/An_Unusual_Amount_Of_Fear_(V)_(Virtual_Set_17).wiki" "VS17O stub 03"
edit 'Coruscant: Jedi Archives (V) (Virtual Set 17)' "$STUBS/Coruscant__Jedi_Archives_(V)_(Virtual_Set_17).wiki" "VS17O stub 04"
edit 'Elegant Lightsaber (V) (Virtual Set 17)' "$STUBS/Elegant_Lightsaber_(V)_(Virtual_Set_17).wiki" "VS17O stub 05"
edit 'Fallen Jedi (V) (Virtual Set 17)' "$STUBS/Fallen_Jedi_(V)_(Virtual_Set_17).wiki" "VS17O stub 06"
edit 'Jedi Advisor (V) (Virtual Set 17)' "$STUBS/Jedi_Advisor_(V)_(Virtual_Set_17).wiki" "VS17O stub 07"
edit 'Jedi Guardian (V) (Virtual Set 17)' "$STUBS/Jedi_Guardian_(V)_(Virtual_Set_17).wiki" "VS17O stub 08"
edit 'NOOOOOOOOOOOO! (V) (Virtual Set 17)' "$STUBS/NOOOOOOOOOOOO!_(V)_(Virtual_Set_17).wiki" "VS17O stub 09"
edit 'We'\''ll Handle This (V) / Duel Of The Fates (V) (Virtual Set 17)' "$STUBS/Well_Handle_This_(V)_-_Duel_Of_The_Fates_(V)_(Virtual_Set_17).wiki" "VS17O stub 10"
edit 'A Sith'\''s Plans (V) (Virtual Set 17)' "$STUBS/A_Siths_Plans_(V)_(Virtual_Set_17).wiki" "VS17O stub 11"
edit 'Black Leader (V) (Virtual Set 17)' "$STUBS/Black_Leader_(V)_(Virtual_Set_17).wiki" "VS17O stub 12"
edit 'Black Leader (V) (AI) (Virtual Set 17)' "$STUBS/Black_Leader_(V)_(AI)_(Virtual_Set_17).wiki" "VS17O stub 12ai"
edit 'Galen, Secret Apprentice (V) (Virtual Set 17)' "$STUBS/Galen,_Secret_Apprentice_(V)_(Virtual_Set_17).wiki" "VS17O stub 13"
edit 'Galen'\''s Fighter (V) (Virtual Set 17)' "$STUBS/Galens_Fighter_(V)_(Virtual_Set_17).wiki" "VS17O stub 14"
edit 'Galen'\''s Lightsaber (V) (Virtual Set 17)' "$STUBS/Galens_Lightsaber_(V)_(Virtual_Set_17).wiki" "VS17O stub 15"
edit 'Gift Of The Master (V) (Virtual Set 17)' "$STUBS/Gift_Of_The_Master_(V)_(Virtual_Set_17).wiki" "VS17O stub 16"
edit 'Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V) (Virtual Set 17)' "$STUBS/Hunt_Down_And_Destroy_The_Jedi_(V)_-_Their_Fire_Has_Gone_Out_Of_The_Universe_(V)_(Virtual_Set_17).wiki" "VS17O stub 17"
edit 'If The Trace Was Correct (V) (Virtual Set 17)' "$STUBS/If_The_Trace_Was_Correct_(V)_(Virtual_Set_17).wiki" "VS17O stub 18"
edit 'Imperial Stormtrooper (V) (Virtual Set 17)' "$STUBS/Imperial_Stormtrooper_(V)_(Virtual_Set_17).wiki" "VS17O stub 19"
edit 'The Force Unleashed (V) (Virtual Set 17)' "$STUBS/The_Force_Unleashed_(V)_(Virtual_Set_17).wiki" "VS17O stub 20"
edit 'TIE Fighter Construction Facility (V) (Virtual Set 17)' "$STUBS/TIE_Fighter_Construction_Facility_(V)_(Virtual_Set_17).wiki" "VS17O stub 21"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "== purgePage hub + stubs + samples =="
docker exec swccg_wiki php maintenance/run.php purgePage 'Virtual Set 17 (Original)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Main Page' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Category:Virtual Original sets' || true

docker exec swccg_wiki php maintenance/run.php purgePage 'A Jedi'\''s Cunning (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'A Jedi'\''s Plans (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'An Unusual Amount Of Fear (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Coruscant: Jedi Archives (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Elegant Lightsaber (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Fallen Jedi (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Jedi Advisor (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Jedi Guardian (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'NOOOOOOOOOOOO! (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'We'\''ll Handle This (V) / Duel Of The Fates (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'A Sith'\''s Plans (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Black Leader (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Black Leader (V) (AI) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Galen, Secret Apprentice (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Galen'\''s Fighter (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Galen'\''s Lightsaber (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Gift Of The Master (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Hunt Down And Destroy The Jedi (V) / Their Fire Has Gone Out Of The Universe (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'If The Trace Was Correct (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Imperial Stormtrooper (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'The Force Unleashed (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'TIE Fighter Construction Facility (V) (Virtual Set 17)' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-01-A_Jedis_Cunning.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-06-Fallen_Jedi.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-10-Well_Handle_This.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-12-Black_Leader.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-12-Black_Leader_AI.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-13-Galen_Secret_Apprentice.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-17-Hunt_Down_And_Destroy_The_Jedi.png' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:VS17O-21-TIE_Fighter_Construction_Facility.png' || true
echo VS17O_APPLY_DONE
