#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
edit() {
  echo "edit $1"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$3" "$1" < "$2"
}
edit "Trandosite" "$ROOT/pages/Trandosite.wiki" "UK fan site (Rod Latham); Worlds 2000 board and 2000 interviews"
edit "Interviews" "$ROOT/pages/Interviews.wiki" "Index of published player interviews, starting with Trandosite 2000"
edit "Category:Interviews" "$ROOT/pages/Category_Interviews.wiki" "Interviews category"
edit "DeckTech" "$ROOT/pages/DeckTech.wiki" "See also Trandosite"
edit "Corellian Engineering Corporation (fan site)" "$ROOT/pages/Corellian_Engineering_Corporation_(fan_site).wiki" "See also Trandosite"
edit "Simon Moore" "$ROOT/pages/Simon_Moore.wiki" "Trandosite interview 8 April 2000"
edit "Mike Burgess" "$ROOT/pages/Mike_Burgess.wiki" "Trandosite interview 2 May 2000"
edit "Bastian Winkelhaus" "$ROOT/pages/Bastian_Winkelhaus.wiki" "Trandosite interview 26 May 2000"
edit "Markus Wüst" "$ROOT/pages/Markus_Wust.wiki" "Trandosite interview 9 June 2000"
edit "Peter Di Biasio" "$ROOT/pages/Peter_Di_Biasio.wiki" "Trandosite interview 20 July 2000"
edit "Philipp Jacobs" "$ROOT/pages/Philipp_Jacobs.wiki" "Trandosite interview 24 August 2000"
edit "Martin Akesson" "$ROOT/pages/Martin_Akesson.wiki" "Trandosite interview 31 August 2000"
edit "Ryan Hase" "$ROOT/pages/Ryan_Hase.wiki" "Trandosite interview 4 September 2000"
edit "Clint Hays" "$ROOT/pages/Clint_Hays.wiki" "Trandosite interview 8 September 2000"
edit "John Shields" "$ROOT/pages/John_Shields.wiki" "Trandosite interview 15 September 2000"
edit "Raphael Asselin" "$ROOT/pages/Raphael_Asselin.wiki" "Trandosite interview 21 September 2000"
edit "Steven Lewis" "$ROOT/pages/Steven_Lewis.wiki" "Trandosite interview 29 September 2000"
edit "Gary Carman" "$ROOT/pages/Gary_Carman.wiki" "Trandosite interview 29 September 2000"
edit "Rod Latham" "$ROOT/pages/Rod_Latham.wiki" "Trandosite webmaster; interview 8 October 2000"
edit "Yannick Lapointe" "$ROOT/pages/Yannick_Lapointe.wiki" "Trandosite interview 21 October 2000"
edit "Matt Sokol" "$ROOT/pages/Matt_Sokol.wiki" "Trandosite interview 25 October 2000"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
for p in Trandosite Interviews "Category:Interviews" "Matt Sokol" "Gary Carman" "Philipp Jacobs" "Raphael Asselin" "Category:Fan sites"; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$p" || true
done
echo DONE trandosite
