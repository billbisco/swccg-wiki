#!/bin/bash
# DeckTech batch dt-batch-18: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-batch-18.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-batch-18 ] && ls gemp-import-dt-batch-18/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-batch-18
  docker cp gemp-import-dt-batch-18/. swccg_wiki:/tmp/gemp-import-dt-batch-18/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-batch-18 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-batch-18 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-batch-18.tsv "DeckTech dt-batch-18"
echo APPLY-dt-batch-18-DONE
