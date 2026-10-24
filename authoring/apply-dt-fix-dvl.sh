#!/bin/bash
# DeckTech batch dt-fix-dvl: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-dt-fix-dvl.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-dt-fix-dvl ] && ls gemp-import-dt-fix-dvl/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-dt-fix-dvl
  docker cp gemp-import-dt-fix-dvl/. swccg_wiki:/tmp/gemp-import-dt-fix-dvl/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="DeckTech dt-fix-dvl GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-dt-fix-dvl || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-dt-fix-dvl.tsv "DeckTech dt-fix-dvl"
echo APPLY-dt-fix-dvl-DONE
