#!/bin/bash
# GPN batch gpn-fix-01: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-gpn-fix-01.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${EDIT_USER:-Admin}"
if [ -d gemp-import-gpn-fix-01 ] && ls gemp-import-gpn-fix-01/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-gpn-fix-01
  docker cp gemp-import-gpn-fix-01/. swccg_wiki:/tmp/gemp-import-gpn-fix-01/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \
    --comment="GPN gpn-fix-01 GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-gpn-fix-01 || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-gpn-fix-01.tsv "GPN gpn-fix-01"
echo APPLY-gpn-fix-01-DONE
