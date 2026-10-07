#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
STAGE=/tmp/vs1o-composites-redo
rm -rf "$STAGE"; mkdir -p "$STAGE"
cp -f "$ROOT/images/original-vs1/vs1-composites/"VS1O-*-composite.png "$STAGE/"
echo "stage $(ls "$STAGE" | wc -l)"
docker exec swccg_wiki mkdir -p /tmp/vs1o-composites-redo
docker cp "$STAGE/." swccg_wiki:/tmp/vs1o-composites-redo/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="VS1O redo: title-stripped Premium panel + alpha; inset inside Decipher text area; borders preserved" \
  --overwrite \
  /tmp/vs1o-composites-redo
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -2
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Luke Skywalker (V) (Virtual Set 1 Original)
Bo Shek (V) (Virtual Set 1 Original)
Darth Vader (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)
Virtual Set 1 (Original)
File:VS1O-05-Luke-Skywalker-composite.png
File:VS1O-01-Bo-Shek-composite.png
File:VS1O-10-Darth-Vader-composite.png
EOF
python3 - <<'PY'
import urllib.request
for u in [
 "https://wiki.swccg.com/wiki/Special:FilePath/VS1O-05-Luke-Skywalker-composite.png",
 "https://wiki.swccg.com/wiki/Luke_Skywalker_(V)_(Virtual_Set_1_Original)",
 "https://wiki.swccg.com/wiki/Bo_Shek_(V)_(Virtual_Set_1_Original)",
 "https://wiki.swccg.com/wiki/Darth_Vader_(V)_(Virtual_Set_1_Original)",
]:
  r=urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=25)
  print(u, r.status, (r.headers.get('Content-Type') or '')[:40], r.headers.get('Content-Length'))
print('REDO DEPLOY DONE')
PY
