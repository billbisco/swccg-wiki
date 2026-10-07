#!/bin/bash
set -euo pipefail
docker exec swccg_wiki rm -rf /tmp/vs1o-batch
docker cp /tmp/vs1o-batch swccg_wiki:/tmp/vs1o-batch
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="VS1O seamless-v5 batch: BoShek-method chrome stretch + icon alpha holes; no fill_rgb" \
  --overwrite \
  /tmp/vs1o-batch
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)
Gold 1 (V) (Virtual Set 1 Original)
Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)
Luke Skywalker (V) (Virtual Set 1 Original)
Sai'torr Kal Fas (V) (Virtual Set 1 Original)
Assault Rifle (V) (Virtual Set 1 Original)
Black 2 (V) (Virtual Set 1 Original)
Blaster Rack (V) (Virtual Set 1 Original)
Darth Vader (V) (Virtual Set 1 Original)
Prophetess (V) (Virtual Set 1 Original)
Virtual Set 1 (Original)
File:VS1O-02-Fusion-Generator-Supply-Tanks-LS-composite.png
File:VS1O-03-Gold-1-composite.png
File:VS1O-04-Hans-Heavy-Blaster-Pistol-composite.png
File:VS1O-05-Luke-Skywalker-composite.png
File:VS1O-06-Saitorr-Kal-Fas-composite.png
File:VS1O-07-Assault-Rifle-composite.png
File:VS1O-08-Black-2-composite.png
File:VS1O-09-Blaster-Rack-composite.png
File:VS1O-10-Darth-Vader-composite.png
File:VS1O-11-Fusion-Generator-Supply-Tanks-DS-composite.png
File:VS1O-12-Prophetess-composite.png
EOF
python3 - <<'PY'
import urllib.request
files=[
"VS1O-02-Fusion-Generator-Supply-Tanks-LS-composite.png",
"VS1O-03-Gold-1-composite.png",
"VS1O-05-Luke-Skywalker-composite.png",
"VS1O-07-Assault-Rifle-composite.png",
"VS1O-08-Black-2-composite.png",
"VS1O-09-Blaster-Rack-composite.png",
"VS1O-10-Darth-Vader-composite.png",
"VS1O-12-Prophetess-composite.png",
]
for f in files:
  u=f"https://wiki.swccg.com/wiki/Special:FilePath/{f}"
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=25)
  print(f, r.status, r.headers.get("Content-Length"))
print("BATCH11 LIVE")
PY
