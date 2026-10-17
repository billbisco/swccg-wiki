#!/bin/bash
# DeckTech batch dt-batch-31: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-batch-31.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-batch-31 ] && ls gemp-import-dt-batch-31/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-batch-31
  docker cp gemp-import-dt-batch-31/. swccg_wiki:/tmp/gemp-import-dt-batch-31/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-batch-31 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-batch-31 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-batch-31.tsv "DeckTech dt-batch-31"
echo APPLY-dt-batch-31-DONE
