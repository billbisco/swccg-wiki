#!/bin/bash
# Live end-to-end test: real GEMP private listener (AuthService, real DbPlayerDAO on a throwaway MariaDB with
# the update_password_hashing.sql migration applied) + real GempAuth on a MariaDB-backed MediaWiki.
# Dev box only. Never point it at production databases: it creates and drops its own.
#
# Usage: run-e2e.sh <swccg-gemp checkout> <MediaWiki dir with dev deps, extensions/GempAuth linked>
# Env:   MDB_BASE (default /tmp/gempauth-e2e), MDB_PORT (3337), AUTH_PORT (18090)
set -euo pipefail
GEMP=$(cd "$1" && pwd); MW=$(cd "$2" && pwd)
EXT=$(cd "$(dirname "$0")/../.." && pwd); CFG=$(cd "$EXT/../.." && pwd)
BASE=${MDB_BASE:-/tmp/gempauth-e2e}; PORT=${MDB_PORT:-3337}; AUTH_PORT=${AUTH_PORT:-18090}
SOCK=$BASE/sock; JPID=; MPID=
cleanup() {
  [ -n "$JPID" ] && kill "$JPID" 2>/dev/null && wait "$JPID" 2>/dev/null || true
  [ -n "$MPID" ] && kill "$MPID" 2>/dev/null && wait "$MPID" 2>/dev/null || true
  echo "cleanup: stopped listener and MariaDB"
}
trap cleanup EXIT
rm -rf "$BASE" && mkdir -p "$BASE/conf"
SQL() { mariadb --no-defaults -S "$SOCK" -uroot "$@"; }

echo "== MariaDB (throwaway, port $PORT)"
mariadb-install-db --no-defaults --datadir="$BASE/data" --auth-root-authentication-method=normal >"$BASE/mdb-init.log" 2>&1
/usr/sbin/mariadbd --no-defaults --datadir="$BASE/data" --socket="$SOCK" --port="$PORT" --bind-address=127.0.0.1 \
  --pid-file="$BASE/pid" --log-error="$BASE/mdb.log" & MPID=$!
for _ in $(seq 50); do [ -S "$SOCK" ] && break; sleep 0.2; done
SQL -e "CREATE USER 'e2e'@'%' IDENTIFIED BY 'e2e-pw'; GRANT ALL ON *.* TO 'e2e'@'%'; CREATE USER 'e2e'@'localhost' IDENTIFIED BY 'e2e-pw'; GRANT ALL ON *.* TO 'e2e'@'localhost';"

echo "== GEMP schema: pre-#284 creation script + update_password_hashing.sql"
BASEREV=$(git -C "$GEMP" merge-base HEAD origin/master)
git -C "$GEMP" show "$BASEREV:src/db-scripts/database_creation_script.sql" > "$BASE/schema-old.sql"
SQL < "$BASE/schema-old.sql"
SQL gemp-swccg -e "SHOW COLUMNS FROM player LIKE 'password'" | tail -1
SQL gemp-swccg < "$GEMP/src/db-scripts/update_password_hashing.sql"
SQL gemp-swccg -e "SHOW COLUMNS FROM player LIKE 'password'; SHOW TABLES LIKE 'player_password_reset'" | grep -v Field

echo "== Wiki: fresh MariaDB-backed install of $(basename "$MW")"
MW_CONFIG_FILE="$BASE/conf/LocalSettings.php" php "$MW/maintenance/run.php" install --dbtype mysql --dbserver "127.0.0.1:$PORT" --dbname e2ewiki --dbuser e2e \
  --dbpass e2e-pw --server http://localhost --scriptpath "" --confpath "$BASE/conf" \
  --pass "$(openssl rand -hex 16)" "SWCCG E2E" Admin >"$BASE/mw-install.log"
SECRET=$(openssl rand -hex 32)
cat > "$BASE/conf/e2e-settings.php" <<PHP
<?php
require "$BASE/conf/LocalSettings.php";
require_once "$MW/extra-settings.php";
require_once "$CFG/login-security.php";
require_once "$CFG/dev-mail-logonly.php";
\$wgGempAuthEndpoint = 'http://127.0.0.1:$AUTH_PORT/internal/v1/verify';
\$wgGempAuthSecret = getenv( 'GEMP_INTERNAL_AUTH_SECRET' );
// Isolate GEMP's behaviour: the wiki's own login throttle and bad-login captcha are tested in phpunit.
\$wgPasswordAttemptThrottle = [];
\$wgCaptchaTriggers['badlogin'] = false;
\$wgCaptchaTriggers['badloginperuser'] = false;
PHP
export GEMP_INTERNAL_AUTH_SECRET=$SECRET
MWRUN() { php "$MW/maintenance/run.php" --conf "$BASE/conf/e2e-settings.php" "$@"; }
MWRUN update --quick >"$BASE/mw-update.log"

echo "== GEMP: build and start the private listener"
( cd "$GEMP/src" && mvn -o -q -pl gemp-swccg-async -am test-compile -DskipTests \
  && mvn -o -q -pl gemp-swccg-async dependency:build-classpath -Dmdep.outputFile="$BASE/cp" -Dmdep.includeScope=test >/dev/null )
CP="$GEMP/src/gemp-swccg-async/target/test-classes:$GEMP/src/gemp-swccg-async/target/classes"
for m in gemp-swccg-server gemp-swccg-logic gemp-swccg-common gemp-swccg-cards; do
  [ -d "$GEMP/src/$m/target/classes" ] && CP="$CP:$GEMP/src/$m/target/classes"
done
CP="$CP:$(cat "$BASE/cp")"
cat > "$BASE/log4j2-e2e.xml" <<'XML'
<Configuration status="WARN"><Appenders><Console name="out" target="SYSTEM_OUT"><PatternLayout pattern="%d{ISO8601} %-5level %c{1} %msg%n"/></Console></Appenders>
<Loggers><Root level="info"><AppenderRef ref="out"/></Root></Loggers></Configuration>
XML
DB_CONTAINER_NAME="127.0.0.1:$PORT" MYSQL_DATABASE=gemp-swccg MYSQL_USER=e2e MYSQL_PASSWORD=e2e-pw \
  INTERNAL_AUTH_PORT=$AUTH_PORT java -Dlog4j2.configurationFile="$BASE/log4j2-e2e.xml" -cp "$CP" com.gempukku.swccgo.async.internal.e2e.WikiAuthE2EServer "$BASE/seed.json" \
  >"$BASE/gemp.log" 2>&1 & JPID=$!
for _ in $(seq 150); do grep -q "E2E listener ready" "$BASE/gemp.log" && break; kill -0 $JPID 2>/dev/null || { cat "$BASE/gemp.log"; exit 1; }; sleep 0.2; done
grep -q "E2E listener ready" "$BASE/gemp.log" || { tail -40 "$BASE/gemp.log"; exit 1; }
echo "listener up on 127.0.0.1:$AUTH_PORT (peer seen by GEMP is 127.0.0.1)"

FAILED=0
run_case() { MWRUN "$EXT/tests/e2e/GempAuthE2E.php" --case "$1" --ip "$2" --seed "$BASE/seed.json" --gemp-log "$BASE/gemp.log" || FAILED=$((FAILED+1)); }
run_case setup 203.0.113.49
run_case ok 203.0.113.50
run_case ok-again 203.0.113.51
run_case wrong 203.0.113.52
run_case blank 203.0.113.53
run_case reset 203.0.113.54
run_case admin-variant 203.0.113.55
run_case throttle-authservice 203.0.113.56
run_case throttle-endpoint 203.0.113.57
run_case legacy 2001:db8::58

echo "== GEMP DB after the run"
SQL gemp-swccg -N -e "SELECT name, LEFT(password, 14) FROM player WHERE name IN ('e2elegacy','e2eblank','e2ereset') ORDER BY name;
  SELECT CONCAT('reset codes left: ', COUNT(*)) FROM player_password_reset;"
LEG=$(SQL gemp-swccg -N -e "SELECT password FROM player WHERE name='e2elegacy'")
if [[ $LEG == pbkdf2-sha256\$* ]]; then echo "  PASS legacy SHA-256 hash upgraded to PBKDF2 on wiki login"; else echo "  FAIL legacy hash not upgraded"; FAILED=$((FAILED+1)); fi
if grep -q "Correct-Horse-9\|Wrong-Horse-9\|Gemp-Admin-pw1\|admin-local-pw\|$(jq -r .reset_code "$BASE/seed.json")" "$BASE/gemp.log"; then echo "  FAIL password in GEMP log"; FAILED=$((FAILED+1)); else echo "  PASS no password in GEMP log"; fi
echo "== GEMP decisions"; grep "wiki-auth: " "$BASE/gemp.log" | sed 's/^.*wiki-auth: /  /'
[ "$FAILED" -eq 0 ] && echo "E2E RESULT: ALL CASES PASSED" || { echo "E2E RESULT: $FAILED case(s) FAILED"; exit 1; }
