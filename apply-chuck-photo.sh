#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
COMMENT="Chuck Kallenbach photo from BoardMatt interview https://www.youtube.com/watch?v=00zEbUKIGRQ"

docker exec swccg_wiki mkdir -p /tmp/chuck-photo
docker cp "$ROOT/encyclopedia/upload/Chuck_Kallenbach.png" swccg_wiki:/tmp/chuck-photo/Chuck_Kallenbach.png
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/chuck-photo \
  || docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/chuck-photo

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Chuck Kallenbach' \
  < "$ROOT/pages/Chuck_Kallenbach.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'File:Chuck_Kallenbach.png' \
  < "$ROOT/pages/File_Chuck_Kallenbach.wiki"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Chuck Kallenbach' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'File:Chuck_Kallenbach.png' || true
echo DONE chuck-photo
