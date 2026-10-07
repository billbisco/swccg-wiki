#!/bin/bash
set -euo pipefail
cd /opt/swccg-wiki
tar -xf legacy-pre.tar
docker exec swccg_wiki mkdir -p /tmp/legacy-pre
docker cp /opt/swccg-wiki/legacy-pre/. swccg_wiki:/tmp/legacy-pre/
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="Legacy pre-reset virtual card art" /tmp/legacy-pre || true
docker cp /opt/swccg-wiki/legacy-pre.xml swccg_wiki:/tmp/legacy-pre.xml
docker exec swccg_wiki php maintenance/run.php importDump /tmp/legacy-pre.xml
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Virtual Block 9
Anakin Skywalker, Padawan Learner (Virtual Block 9)
Virtual Block 1
Virtual Shields
Main Page
EOF
echo legacy-pre done
