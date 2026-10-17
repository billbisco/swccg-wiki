#!/bin/bash
# DeckTech batch dt-wb: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-wb.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-wb ] && ls gemp-import-dt-wb/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-wb
  docker cp gemp-import-dt-wb/. swccg_wiki:/tmp/gemp-import-dt-wb/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-wb GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-wb || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-wb.tsv "DeckTech dt-wb"
echo APPLY-dt-wb-DONE
