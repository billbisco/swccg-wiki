#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
XML="$ROOT/strategy-remaining.xml"

if [[ -f "$XML" ]]; then
  docker cp "$XML" swccg_wiki:/tmp/strategy-remaining.xml
  docker exec swccg_wiki php maintenance/run.php importDump /tmp/strategy-remaining.xml
fi

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
A Million Voices Crying Out
Aurra Sing
Darth Maul
Hidden Base / Systems Will Slip Through Your Fingers
EOF
echo strategy remaining import done
