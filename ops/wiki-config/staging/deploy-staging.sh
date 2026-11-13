#!/bin/bash
# Deploy the wiki staging copy behind https://test.swccg.com/wiki/ . Run as root on the VPS.
# Touches production only by READING: copies of /opt/swccg-wiki files and a --single-transaction
# dump of the wiki DB. Writes only /opt/swccg-wiki-staging, its own docker project
# (swccg-wiki-staging: 4 containers, 3 volumes, 3 networks) and the test.swccg.com nginx vhost.
#
# Usage: deploy-staging.sh <bundle.tgz> <player-password-file>
set -euo pipefail
BUNDLE=$1; PLAYER_PW=$2
S=/opt/swccg-wiki-staging; PROD=/opt/swccg-wiki
VHOST=/etc/nginx/sites-available/test.swccg.com
TS=$(date +%Y%m%d-%H%M%S)
log() { echo "[$(date +%H:%M:%S)] $*"; }

log "preflight"
[ -e "$S" ] && { echo "$S exists: run rollback-staging.sh first"; exit 1; }
ss -ltn | grep -q '127.0.0.1:17013 ' && { echo "port 17013 busy"; exit 1; }
for n in $(docker network ls -q); do docker network inspect "$n" --format '{{range .IPAM.Config}}{{.Subnet}}{{end}}'; done | grep -qx '172.31.13.0/24' && { echo "subnet in use"; exit 1; }
grep -q '>>> wiki-staging' "$VHOST" && { echo "vhost already patched"; exit 1; }
[ "$(grep -c '^    location / {$' "$VHOST")" = 1 ] || { echo "vhost layout unexpected (need one '    location / {')"; exit 1; }
if docker exec swccg_wiki_db sh -c 'ps aux 2>/dev/null || ls /proc' | grep -q -e mariadb-dump -e mysqldump; then
  echo "a dump is running on the production wiki DB (backup?): not adding a second one now"; exit 1; fi

log "staging dir + copies of production files (read-only on production)"
mkdir -p "$S"/{copy/extensions,secrets/wiki,backup}
tar xzf "$BUNDLE" -C "$S"          # -> wiki-config/, gempauth/
cp -a "$PROD/chrome" "$PROD/SwccgChrome.php" "$PROD/flaggedrevs-settings.php" "$PROD/extra-settings.php" "$PROD/logo" "$S/copy/"
cp -a "$PROD/extensions/FlaggedRevs" "$S/copy/extensions/"

log "secrets (generated here, never printed)"
umask 077
r() { openssl rand -hex "$1"; }
WIKIDB=$(r 24); GEMPDB=$(r 24); HMAC=$(r 32)
printf 'MARIADB_ROOT_PASSWORD=%s\nMARIADB_DATABASE=wiki\nMARIADB_USER=wiki\nMARIADB_PASSWORD=%s\n' "$(r 24)" "$WIKIDB" > "$S/secrets/wiki-db.env"
printf 'MARIADB_ROOT_PASSWORD=%s\nMARIADB_USER=gemp\nMARIADB_PASSWORD=%s\n' "$(r 24)" "$GEMPDB" > "$S/secrets/gempdb.env"
printf 'GEMP_INTERNAL_AUTH_SECRET=%s\nMYSQL_USER=gemp\nMYSQL_PASSWORD=%s\n' "$HMAC" "$GEMPDB" > "$S/secrets/gempauth.env"
printf "<?php\n\$wgDBpassword = '%s';\n\$wgSecretKey = '%s';\n\$wgUpgradeKey = '%s';\n" "$WIKIDB" "$(r 32)" "$(r 8)" > "$S/secrets/wiki/staging-secrets.php"
printf "<?php\n\$wgGempAuthSecret = '%s';\n" "$HMAC" > "$S/secrets/wiki/gempauth-secret.php"
install -m 0644 "$PLAYER_PW" "$S/secrets/player-password"   # staging-only test player
chown -R root:33 "$S/secrets/wiki"; chmod 750 "$S/secrets/wiki"; chmod 640 "$S/secrets/wiki/"*
umask 022

log "LocalSettings.php = production copy + staging includes"
cp "$PROD/LocalSettings.php" "$S/LocalSettings.php"
cat >> "$S/LocalSettings.php" <<'PHP'

# --- staging (test.swccg.com) — appended by deploy-staging.sh -------------------------------
require_once "$IP/login-security.php";
require_once "$IP/dev-mail-logonly.php";     # log-only mailer: nothing is ever sent
require_once "$IP/staging-settings.php";
PHP
chown root:33 "$S/LocalSettings.php"; chmod 640 "$S/LocalSettings.php"
cp "$S/wiki-config/staging/docker-compose.staging.yml" "$S/docker-compose.yml"

log "images + databases"
docker pull -q mediawiki:1.43.11
cd "$S"
docker compose up -d db gempdb
for c in swccg_wiki_staging_db swccg_gemp_staging_db; do
  for _ in $(seq 60); do [ "$(docker inspect -f '{{.State.Health.Status}}' $c)" = healthy ] && break; sleep 2; done
  [ "$(docker inspect -f '{{.State.Health.Status}}' $c)" = healthy ] || { echo "$c not healthy"; exit 1; }
done

log "copy production wiki DB -> staging DB (--single-transaction, no objectcache rows)"
docker exec swccg_wiki_db sh -c 'exec mariadb-dump -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" --single-transaction --quick --no-tablespaces --ignore-table="$MYSQL_DATABASE.objectcache" "$MYSQL_DATABASE"' \
  | docker exec -i swccg_wiki_staging_db sh -c 'exec mariadb -uroot -p"$MARIADB_ROOT_PASSWORD" wiki'
docker exec swccg_wiki_db sh -c 'exec mariadb-dump -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" --no-data --no-tablespaces "$MYSQL_DATABASE" objectcache' \
  | docker exec -i swccg_wiki_staging_db sh -c 'exec mariadb -uroot -p"$MARIADB_ROOT_PASSWORD" wiki'

log "start wiki + gempauth"
docker compose up -d wiki gempauth
for _ in $(seq 60); do docker logs swccg_gempauth_staging 2>&1 | grep -q 'listener ready' && break; sleep 2; done
docker logs swccg_gempauth_staging 2>&1 | grep -E 'staging:|wiki-auth internal' || { docker logs --tail 40 swccg_gempauth_staging; exit 1; }

log "guard: the staging wiki talks to its own DB server only"
DBIP=$(docker exec swccg_wiki_staging getent hosts db | awk '{print $1}')
STAGEDB=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}' swccg_wiki_staging_db)
case " $STAGEDB " in *" $DBIP "*) echo "db -> $DBIP (swccg_wiki_staging_db)";; *) echo "db resolves to $DBIP, not the staging DB"; exit 1;; esac

log "update.php on the STAGING DB (1.43.9 -> 1.43.11 schema, OATHAuth tables)"
docker exec swccg_wiki_staging php maintenance/run.php update --quick | tail -3
docker exec swccg_wiki_staging grep MW_VERSION includes/Defines.php

log "existing editors without a confirmed email -> confirmed-editor (staging)"
docker exec swccg_wiki_staging php maintenance/run.php ./extensions/GempAuth/maintenance/grantConfirmedEditor.php --dry-run
docker exec swccg_wiki_staging php maintenance/run.php ./extensions/GempAuth/maintenance/grantConfirmedEditor.php

log "nginx: test.swccg.com vhost (backup first)"
cp -a "$VHOST" "$S/backup/test.swccg.com.$TS"
python3 - "$VHOST" "$S/wiki-config/staging/nginx-test-wiki-staging.conf" <<'PY'
import sys, re
vhost, snip = sys.argv[1], open(sys.argv[2]).read()
http_part = snip.split('# [http context, top of file]\n')[1].split('#\n# [inside')[0]
loc_part = snip.split('before "location / {"]\n')[1]
s = open(vhost).read()
marker = '    location / {\n'
assert s.count(marker) == 1, 'expected exactly one "location / {" in the vhost'
s = '# >>> wiki-staging (http)\n' + http_part + '# <<< wiki-staging (http)\n' + s
s = s.replace(marker, '    # >>> wiki-staging\n' + loc_part + '    # <<< wiki-staging\n\n' + marker)
open(vhost, 'w').write(s)
PY
if nginx -t 2>&1; then systemctl reload nginx; else cp -a "$S/backup/test.swccg.com.$TS" "$VHOST"; echo "nginx -t failed; vhost restored"; exit 1; fi

log "smoke"
curl -s -o /dev/null -w 'Main_Page %{http_code}\n' https://test.swccg.com/wiki/Main_Page
curl -s -o /dev/null -w 'GEMP test root %{http_code}\n' https://test.swccg.com/
ss -ltn | grep -c ':8090 ' | sed 's/^/host listeners on 8090: /'
log "done. Rollback: $S/wiki-config/staging/rollback-staging.sh"
