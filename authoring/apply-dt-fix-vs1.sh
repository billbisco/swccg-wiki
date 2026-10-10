#!/bin/bash
# DeckTech batch dt-fix-vs1: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-fix-vs1.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-fix-vs1 ] && ls gemp-import-dt-fix-vs1/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-fix-vs1
  docker cp gemp-import-dt-fix-vs1/. swccg_wiki:/tmp/gemp-import-dt-fix-vs1/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-fix-vs1 GEMP importable decklists" --extensions=txt /tmp/gemp-import-dt-fix-vs1 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-fix-vs1.tsv "DeckTech dt-fix-vs1"
echo APPLY-dt-fix-vs1-DONE
