#!/bin/bash
# Persist MediaWiki login sessions in MariaDB. extra-settings.php is bind-mounted.
# Never change Admin's password.
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

echo "== extra-settings session lines =="
grep -n 'wgSessionCacheType\|wgObjectCacheSessionExpiry\|wgExtendedLoginCookieExpiration' \
  "$ROOT/extra-settings.php"

echo "== reload PHP (graceful; full restart only if graceful fails) =="
if docker exec swccg_wiki apachectl graceful; then
  echo "apachectl graceful ok"
elif docker exec swccg_wiki apache2ctl graceful; then
  echo "apache2ctl graceful ok"
else
  echo "graceful failed; docker restart swccg_wiki"
  docker restart swccg_wiki
fi
sleep 3

echo "== live SessionCacheType (CACHE_DB == 1) =="
echo 'echo "SessionCacheType="; var_export( $wgSessionCacheType ); echo "\nObjectCacheSessionExpiry="; var_export( $wgObjectCacheSessionExpiry ); echo "\n";' \
  | docker exec -i swccg_wiki php maintenance/run.php eval

echo "== repair Admin user_token if InvalidateUserSessions left INVALID_TOKEN =="
python3 "$ROOT/repair-admin-session-token.py"

echo "== Admin login vs .env (no password printed, no reset) =="
python3 "$ROOT/verify-admin-login.py"

echo "== session must survive docker restart =="
python3 "$ROOT/verify-admin-login.py" --survive-restart

echo "SESSION_PERSIST_OK"
