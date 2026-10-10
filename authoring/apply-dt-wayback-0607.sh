#!/bin/bash
# DeckTech batch dt-wayback-0607: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-wayback-0607.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-wayback-0607 ] && ls gemp-import-dt-wayback-0607/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-wayback-0607
  docker cp gemp-import-dt-wayback-0607/. swccg_wiki:/tmp/gemp-import-dt-wayback-0607/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-wayback-0607 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-wayback-0607 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-wayback-0607.tsv "DeckTech dt-wayback-0607"
echo APPLY-dt-wayback-0607-DONE
