#!/bin/bash
# DeckTech batch dt-ep1: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-ep1.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-ep1 ] && ls gemp-import-dt-ep1/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-ep1
  docker cp gemp-import-dt-ep1/. swccg_wiki:/tmp/gemp-import-dt-ep1/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-ep1 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-ep1 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-ep1.tsv "DeckTech dt-ep1"
echo APPLY-dt-ep1-DONE
