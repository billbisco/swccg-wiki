#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

mkdir -p "$ROOT/extensions"
if [ ! -f "$ROOT/extensions/FlaggedRevs/extension.json" ]; then
  rm -rf "$ROOT/extensions/FlaggedRevs"
  git clone --depth 1 --branch REL1_43 \
    https://github.com/wikimedia/mediawiki-extensions-FlaggedRevs.git \
    "$ROOT/extensions/FlaggedRevs"
fi

# nginx: serve /chrome/ on wiki + landing
python3 - <<'PY'
from pathlib import Path

chrome = """
    location /chrome/ {
        alias /opt/swccg-wiki/chrome/;
    }
"""

def ensure(path):
    p = Path(path)
    text = p.read_text()
    if "location /chrome/" in text:
        return
    needle = "    location / {"
    if needle not in text:
        raise SystemExit(f"no location / in {path}")
    p.write_text(text.replace(needle, chrome + "\n" + needle, 1))
    print("patched", path)

ensure("/etc/nginx/sites-enabled/wiki.swccg.com")
ensure("/etc/nginx/sites-enabled/swccg.com")
PY

cp "$ROOT/landing/index.html" /var/www/swccg.com/index.html

LS="$ROOT/LocalSettings.php"
if ! grep -q "SwccgChrome.php" "$LS"; then
  cat >> "$LS" <<'PHP'

# Shared swccg.com chrome
require_once "$IP/SwccgChrome.php";
$wgHooks['BeforePageDisplay'][] = 'SwccgChrome::onBeforePageDisplay';
$wgHooks['SiteNoticeAfter'][] = 'SwccgChrome::onSiteNoticeAfter';
$wgHooks['SkinAfterContent'][] = 'SwccgChrome::onSkinAfterContent';

# FlaggedRevs (pending revisions until trusted accepts)
require_once "$IP/flaggedrevs-settings.php";
PHP
fi

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d
nginx -t
systemctl reload nginx
docker exec swccg_wiki php maintenance/run.php update --quick

# Non-sysop user for pending-revision tests (password stays in .env).
# Never createAndPromote / changePassword Admin. Never --force an existing account.
set -a
# shellcheck disable=SC1091
source "$ROOT/.env"
set +a
if [ -z "${SUGGESTER_PASSWORD:-}" ]; then
  SUGGESTER_PASSWORD=$(openssl rand -hex 12)
  echo "SUGGESTER_PASSWORD=${SUGGESTER_PASSWORD}" >> "$ROOT/.env"
fi
if docker exec swccg_wiki php maintenance/run.php createAndPromote suggester "$SUGGESTER_PASSWORD"; then
  echo "created suggester (new account)"
else
  echo "suggester already exists; password not reset"
fi

echo "Chrome + FlaggedRevs applied."
curl -sI -m 10 https://wiki.swccg.com/ | head -8
curl -sI -m 10 https://swccg.com/chrome/chrome.css | head -8
