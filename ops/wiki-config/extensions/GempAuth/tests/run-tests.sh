#!/bin/sh
# Reproduce the GempAuth test run on a dev box (no production access needed).
# Usage: tests/run-tests.sh 1.43.11   (or 1.43.9)
set -eu
V=${1:-1.43.11}
EXT=$(cd "$(dirname "$0")/.." && pwd)
CFG=$(cd "$EXT/../.." && pwd)            # ops/wiki-config
W=${WORK:-/tmp/gempauth-mw}
mkdir -p "$W" && cd "$W"
[ -d "mediawiki-$V" ] || curl -sSfL "https://releases.wikimedia.org/mediawiki/1.43/mediawiki-$V.tar.gz" | tar xz
cd "mediawiki-$V"
curl -sSfL "https://raw.githubusercontent.com/wikimedia/mediawiki/$V/phpunit.xml.dist" -o phpunit.xml.dist
# dev deps, keeping the bundled extensions' libraries (OATHAuth, AbuseFilter, ConfirmEdit)
printf '%s\n' '{ "extra": { "merge-plugin": { "include": [ "extensions/AbuseFilter/composer.json", "extensions/OATHAuth/composer.json", "extensions/ConfirmEdit/composer.json" ] } } }' > composer.local.json
composer update --no-interaction --no-progress -q
ln -sfn "$EXT" extensions/GempAuth
if [ ! -f LocalSettings.php ]; then
  php maintenance/run.php install --dbtype sqlite --dbpath "$W/data-$V" --server http://localhost --scriptpath "" \
    --pass "$(openssl rand -hex 16)" "SWCCG Test" Admin >/dev/null
  cp "$CFG/../../authoring/extra-settings.php" extra-settings.php
  cat >> LocalSettings.php <<PHP
require_once "\$IP/extra-settings.php";
require_once "$CFG/login-security.php";
require_once "$CFG/dev-mail-logonly.php";
\$wgEnableEmail = true;
\$wgGempAuthEndpoint = 'http://127.0.0.1:18090/internal/v1/verify';
\$wgGempAuthSecret = '0123456789abcdef0123456789abcdef'; // public test vector, not a real secret
PHP
  php maintenance/run.php update --quick >/dev/null
fi
php vendor/bin/phpunit extensions/GempAuth/tests/phpunit
