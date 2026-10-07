#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vc-original-packs
STAGE=/tmp/vc-packs-import

echo "== importImages VirtualCards Remaster packs/symbols =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vc-packs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vc-packs-import/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Original Remaster packs/symbols from Wayback VirtualCards*.pdf (Dec 2006 re-edit family)" \
  --overwrite \
  /tmp/vc-packs-import || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -5

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 1 (Original)
Virtual Set 2 (Original)
Virtual Set 3 (Original)
Virtual Set 4 (Original)
Virtual Set 5 (Original)
Virtual Set 6 (Original)
Virtual Set 7 (Original)
Virtual Set 8 (Original)
Virtual Set 9 (Original)
Virtual Set 10 (Original)
Virtual Set 11 (Original)
Virtual Set 12 (Original)
Virtual Set 13 (Original)
Virtual Set 16 (Original)
Main Page
Virtual Sets (2002-2009)
File:VS2O-pack.png
File:VS2O-set-symbol.png
File:Set-VS2O-title.png
PURGE

python3 - <<'PY'
import urllib.request
sets=[1,2,3,4,5,6,7,8,9,10,11,12,13,16]
pass_n=0; fail=[]
for n in sets:
  ok_all=True
  for name in [f'VS{n}O-pack.png', f'VS{n}O-set-symbol.png', f'Set-VS{n}O-title.png']:
    u=f'https://wiki.swccg.com/wiki/Special:FilePath/{name}'
    try:
      r=urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=30)
      ok=(r.status==200)
    except Exception:
      ok=False
    print(('PASS' if ok else 'FAIL'), name)
    ok_all=ok_all and ok
  hub=f'https://wiki.swccg.com/wiki/Virtual_Set_{n}_(Original)'
  try:
    r=urllib.request.urlopen(urllib.request.Request(hub, method='HEAD'), timeout=30)
    hok=(r.status==200)
  except Exception:
    hok=False
  print(('PASS' if hok else 'FAIL'), hub)
  if ok_all and hok: pass_n+=1
  else: fail.append(n)
print(f'VC PACKS {pass_n}/14 sets PASS fail={fail}')
print('VC ORIGINAL PACKS APPLY OK')
PY
