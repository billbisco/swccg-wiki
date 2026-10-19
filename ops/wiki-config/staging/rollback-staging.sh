#!/bin/bash
# Remove the wiki staging copy completely. Run as root on the VPS. Production is not touched.
# The vhost is reverted by deleting only the "# >>> wiki-staging" ... "# <<< wiki-staging" blocks,
# so any other change made to the test.swccg.com vhost since the deploy is kept.
set -euo pipefail
S=/opt/swccg-wiki-staging; VHOST=/etc/nginx/sites-available/test.swccg.com
if grep -q '>>> wiki-staging' "$VHOST"; then
  cp -a "$VHOST" "/root/test.swccg.com.pre-staging-rollback.$(date +%Y%m%d-%H%M%S)"
  python3 - "$VHOST" <<'PY'
import re, sys
p = sys.argv[1]; s = open(p).read()
s = re.sub(r'[ \t]*# >>> wiki-staging[^\n]*\n.*?# <<< wiki-staging[^\n]*\n\n?', '', s, flags=re.S)
open(p, 'w').write(s)
PY
  nginx -t && systemctl reload nginx && echo "vhost: wiki-staging blocks removed, nginx reloaded"
fi
[ -f "$S/docker-compose.yml" ] && (cd "$S" && docker compose down -v --remove-orphans)
rm -rf "$S"
echo "staging removed (mediawiki:1.43.11 image kept; 'docker rmi mediawiki:1.43.11' drops it)"
