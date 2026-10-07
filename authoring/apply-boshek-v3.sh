#!/bin/bash
set -euo pipefail
docker exec swccg_wiki mkdir -p /tmp/vs1o-boshek
docker cp /tmp/VS1O-01-Bo-Shek-composite.png swccg_wiki:/tmp/vs1o-boshek/VS1O-01-Bo-Shek-composite.png
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="BoShek seamless-v3: expand left+down target_rect [36,683,699,978]; no fill_rgb" \
  --overwrite \
  /tmp/vs1o-boshek
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -2
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Bo Shek (V) (Virtual Set 1 Original)
File:VS1O-01-Bo-Shek-composite.png
EOF
python3 -c "
import urllib.request
u='https://wiki.swccg.com/wiki/Special:FilePath/VS1O-01-Bo-Shek-composite.png'
r=urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=25)
print(u, r.status, r.headers.get('Content-Length'))
print('BOSHEK V3 LIVE')
"
