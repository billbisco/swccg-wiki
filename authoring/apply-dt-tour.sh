#!/bin/bash
# DeckTech batch dt-tour: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-tour.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-tour ] && ls gemp-import-dt-tour/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-tour
  docker cp gemp-import-dt-tour/. swccg_wiki:/tmp/gemp-import-dt-tour/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-tour GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-tour || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-tour.tsv "DeckTech dt-tour"
echo APPLY-dt-tour-DONE
