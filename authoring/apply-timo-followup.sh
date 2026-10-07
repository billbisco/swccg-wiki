#!/bin/bash
# Timo follow-up: landscape CardLink zoom, CardLink on alt decks, GEMP download upload.
# VPS only; no git remote. Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

EPOCH=$(cat "$PAGES/formats-tournament/followup-epoch.txt")
echo "CacheEpoch target $EPOCH"

python3 - <<'PY'
from pathlib import Path
import re
p = Path('/opt/swccg-wiki/extra-settings.php')
t = p.read_text(encoding='utf-8')
epoch = Path('/opt/swccg-wiki/pages/formats-tournament/followup-epoch.txt').read_text(encoding='utf-8').strip()
t2, n = re.subn(r"\$wgCacheEpoch\s*=\s*'[^']*';", "$wgCacheEpoch = '%s';" % epoch, t, count=1)
if not n:
    raise SystemExit('CacheEpoch not found')
p.write_text(t2, encoding='utf-8')
print('CacheEpoch set', epoch)
PY

edit() {
  local title="$1"; local file="$2"; local summary="$3"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

# Upload single-deck GEMP file (exact bytes from Fixed zip)
UP=/tmp/timo-gemp-upload
rm -rf "$UP"
mkdir -p "$UP"
cp "$PAGES/formats-tournament/26RMPC_Dusel_DS_ROps.txt" "$UP/26RMPC Dusel DS ROps.txt"
docker exec swccg_wiki rm -rf /tmp/timo-gemp-upload || true
docker cp "$UP" swccg_wiki:/tmp/timo-gemp-upload
echo "== importImages GEMP deck txt =="
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="GEMP import: 26RMPC Dusel DS ROps.txt from 2026 Retro Gempc Fixed.zip (forum t=86979 file.php?id=22918)" \
  --overwrite \
  /tmp/timo-gemp-upload || \
docker exec swccg_wiki php maintenance/importImages.php --user=Admin --overwrite /tmp/timo-gemp-upload || true

edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki" "CardLink zoom: landscape sites keep natural aspect (no portrait clamp scrunch)"
edit "MediaWiki:Common.js" "$PAGES/MediaWiki_Common.js.wiki" "CardLink zoom: size popup from naturalWidth/Height; landscape class for sites"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations.wiki" "GEMP download link; CardLink objective; cite forum Fixed zip"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)" "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(picture_layout).wiki" "CardLink hover on every card name; GEMP download"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)" "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(two-column_layout).wiki" "CardLink hover on every card name; GEMP download"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
python3 - <<'PY'
import subprocess
titles = [
  'MediaWiki:Common.js',
  'MediaWiki:Common.css',
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations',
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)',
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)',
  'File:26RMPC Dusel DS ROps.txt',
  'Main Page',
]
proc = subprocess.run(
  ["docker", "exec", "-i", "swccg_wiki", "php", "maintenance/run.php", "purgePage"],
  input="\n".join(titles)+"\n", text=True)
print('purge exit', proc.returncode)
PY

echo "== docker restart swccg_wiki =="
docker restart swccg_wiki
sleep 5

echo timo-followup applied
