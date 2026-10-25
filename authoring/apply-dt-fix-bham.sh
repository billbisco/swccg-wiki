#!/bin/bash
# DeckTech batch dt-fix-bham: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-fix-bham.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-fix-bham ] && ls gemp-import-dt-fix-bham/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-fix-bham
  docker cp gemp-import-dt-fix-bham/. swccg_wiki:/tmp/gemp-import-dt-fix-bham/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-fix-bham GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-fix-bham || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-fix-bham.tsv "DeckTech dt-fix-bham"
echo APPLY-dt-fix-bham-DONE
