#!/bin/bash
# DeckTech batch dt-batch-80: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-batch-80.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-batch-80 ] && ls gemp-import-dt-batch-80/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-batch-80
  docker cp gemp-import-dt-batch-80/. swccg_wiki:/tmp/gemp-import-dt-batch-80/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-batch-80 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-batch-80 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-batch-80.tsv "DeckTech dt-batch-80"
echo APPLY-dt-batch-80-DONE
