#!/bin/bash
# DeckTech batch dt-gemme: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-gemme.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-gemme ] && ls gemp-import-dt-gemme/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-gemme
  docker cp gemp-import-dt-gemme/. swccg_wiki:/tmp/gemp-import-dt-gemme/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-gemme GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-gemme || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-gemme.tsv "DeckTech dt-gemme"
echo APPLY-dt-gemme-DONE
