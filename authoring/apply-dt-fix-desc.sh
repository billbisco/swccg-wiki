#!/bin/bash
# DeckTech batch dt-fix-desc: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-fix-desc.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-fix-desc ] && ls gemp-import-dt-fix-desc/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-fix-desc
  docker cp gemp-import-dt-fix-desc/. swccg_wiki:/tmp/gemp-import-dt-fix-desc/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-fix-desc GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-fix-desc || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-fix-desc.tsv "DeckTech dt-fix-desc"
echo APPLY-dt-fix-desc-DONE
