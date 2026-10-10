#!/bin/bash
# DeckTech batch dt-batch-07: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-batch-07.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-batch-07 ] && ls gemp-import-dt-batch-07/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-batch-07
  docker cp gemp-import-dt-batch-07/. swccg_wiki:/tmp/gemp-import-dt-batch-07/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-batch-07 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-batch-07 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-batch-07.tsv "DeckTech dt-batch-07"
echo APPLY-dt-batch-07-DONE
