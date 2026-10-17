#!/bin/bash
# DeckTech batch dt-gemp-fix: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-gemp-fix.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-gemp-fix ] && ls gemp-import-dt-gemp-fix/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-gemp-fix
  docker cp gemp-import-dt-gemp-fix/. swccg_wiki:/tmp/gemp-import-dt-gemp-fix/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-gemp-fix GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-gemp-fix || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-gemp-fix.tsv "DeckTech dt-gemp-fix"
echo APPLY-dt-gemp-fix-DONE
