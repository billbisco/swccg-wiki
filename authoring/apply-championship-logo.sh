#!/bin/bash
set -euo pipefail
echo '== importImages logo =='
docker exec swccg_wiki mkdir -p /tmp/retro-logo
docker cp /tmp/2026-Retro-GEMPC-Logo.png swccg_wiki:/tmp/retro-logo/2026-Retro-GEMPC-Logo.png
# importImages expects a directory of files
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment='Official 2026 Retro GEMPC event logo from PC forum overview t=86555 (postimg)' \
  --overwrite \
  /tmp/retro-logo || \
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment='Official 2026 Retro GEMPC event logo from PC forum overview t=86555 (postimg)' \
  /tmp/retro-logo

docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo '== edit File description =='
# Normalize
PAGE=/opt/swccg-wiki/pages/File_2026-Retro-GEMPC-Logo.png.wiki
python3 -c "
from pathlib import Path
p=Path('$PAGE')
t=p.read_bytes()
if t.startswith(b'\\xef\\xbb\\xbf'): t=t[3:]
p.write_text(t.decode('utf-8').replace('\\r\\n','\\n').replace('\\r','\\n'), encoding='utf-8', newline='\\n')
"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary='File description: 2026 Retro GEMPC event logo (forum t=86555)' 'File:2026-Retro-GEMPC-Logo.png' < "$PAGE"

echo '== edit championship page =='
CHAMP='/opt/swccg-wiki/pages/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki'
python3 -c "
from pathlib import Path
p=Path('''$CHAMP''')
t=p.read_bytes()
if t.startswith(b'\\xef\\xbb\\xbf'): t=t[3:]
p.write_text(t.decode('utf-8').replace('\\r\\n','\\n').replace('\\r','\\n'), encoding='utf-8', newline='\\n')
"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary='Add official event logo (lead thumb); source forum overview t=86555' '2026 Retro GEMP Match Play Championship (Premiere to DSII)' < "$CHAMP"

echo '== FlaggedRevs =='
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo '== purge =='
printf '%s\n' '2026 Retro GEMP Match Play Championship (Premiere to DSII)' 'File:2026-Retro-GEMPC-Logo.png' | docker exec -i swccg_wiki php maintenance/run.php purgePage

echo '== verify championship head =='
docker exec swccg_wiki php maintenance/run.php getText '2026 Retro GEMP Match Play Championship (Premiere to DSII)' | head -20
