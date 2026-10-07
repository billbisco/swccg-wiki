#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
UP=/tmp/decipher-rulebook-pdf-upload

echo "== importImages Decipher rulebooks + Icon Reference Sheet =="
docker exec swccg_wiki rm -rf /tmp/decipher-rulebook-pdf-upload || true
docker cp "$UP" swccg_wiki:/tmp/decipher-rulebook-pdf-upload
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Host Decipher rules PDFs + Virtual Icon Reference Sheet locally on wiki" \
  --overwrite \
  /tmp/decipher-rulebook-pdf-upload \
  || docker exec swccg_wiki php maintenance/importImages.php --user=Admin --overwrite /tmp/decipher-rulebook-pdf-upload || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  if [[ ! -f "$file" ]]; then
    echo "SKIP missing $file ($title)"
    return 0
  fi
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

SUMMARY='Host Decipher rules PDFs on wiki File:; rewire cites off res.starwarsccg.org; Icon Reference Sheet Feb 2024 local'

# Hub / core
edit "Rulebooks" "$PAGES/Rulebooks.wiki" "$SUMMARY"
edit "Errata" "$PAGES/Errata.wiki" "$SUMMARY"
edit "Decipher Glossary Supplement" "$PAGES/Decipher_Glossary_Supplement.wiki" "$SUMMARY"
edit "Decipher Glossary 2.0" "$PAGES/Decipher_Glossary_2.0.wiki" "$SUMMARY"
edit "Decipher Comprehensive Rules" "$PAGES/Decipher_Comprehensive_Rules.wiki" "$SUMMARY"
edit "Star Wars Customizable Card Game RULEBOOK 2.0" "$PAGES/Star_Wars_Customizable_Card_Game_RULEBOOK_2.0.wiki" "$SUMMARY"
edit "Enhanced Premiere Rulesheet" "$PAGES/Enhanced_Premiere_Rulesheet.wiki" "$SUMMARY"
edit "Endor Rulesheet" "$PAGES/Endor_Rulesheet.wiki" "$SUMMARY"
edit "Death Star II Rulesheet" "$PAGES/Death_Star_II_Rulesheet.wiki" "$SUMMARY"
edit "Reflections II Rulesheet" "$PAGES/Reflections_II_Rulesheet.wiki" "$SUMMARY"
edit "Reflections III Rulesheet" "$PAGES/Reflections_III_Rulesheet.wiki" "$SUMMARY"
edit "Tatooine Rulesheet" "$PAGES/Tatooine_Rulesheet.wiki" "$SUMMARY"
edit "Coruscant Rulesheet" "$PAGES/Coruscant_Rulesheet.wiki" "$SUMMARY"
edit "Theed Palace Rulesheet" "$PAGES/Theed_Palace_Rulesheet.wiki" "$SUMMARY"
edit "Virtual card icons" "$PAGES/icons/Virtual_card_icons.wiki" "$SUMMARY"
edit "Errata on Projective Telepathy" "$PAGES/Errata_on_Projective_Telepathy.wiki" "$SUMMARY"

# Errata card pages (Original/Errata/main)
for f in \
  Advosze Advosze_\(Errata\) Advosze_\(Original\) \
  Asteroid_Sanctuary Asteroid_Sanctuary_\(Errata\) Asteroid_Sanctuary_\(Original\) \
  AT-AT_Cannon AT-AT_Cannon_\(Errata\) AT-AT_Cannon_\(Original\) \
  Attack_Run Attack_Run_\(Errata\) Attack_Run_\(Original\) \
  Beru_Stew Beru_Stew_\(Errata\) Beru_Stew_\(Original\) \
  Desperate_Times Desperate_Times_\(Errata\) Desperate_Times_\(Original\) \
  Electrobinoculars Electrobinoculars_\(Errata\) Electrobinoculars_\(Original\) \
  Great_Warrior Great_Warrior_\(Errata\) Great_Warrior_\(Original\) \
  HoloNet_Transmission HoloNet_Transmission_\(Errata\) HoloNet_Transmission_\(Original\) \
  I\'d_Just_As_Soon_Kiss_A_Wookiee I\'d_Just_As_Soon_Kiss_A_Wookiee_\(Errata\) I\'d_Just_As_Soon_Kiss_A_Wookiee_\(Original\) \
  Imperial_Decree Imperial_Decree_\(Errata\) Imperial_Decree_\(Original\) \
  Innocent_Scoundrel Innocent_Scoundrel_\(Errata\) Innocent_Scoundrel_\(Original\) \
  It_Can_Wait It_Can_Wait_\(Errata\) It_Can_Wait_\(Original\) \
  Limited_Resources Limited_Resources_\(Errata\) Limited_Resources_\(Original\) \
  Luke_Skywalker Luke_Skywalker_\(Errata\) Luke_Skywalker_\(Original\) \
  Luke\'s_Cape Luke\'s_Cape_\(Errata\) Luke\'s_Cape_\(Original\) \
  Medium_Repeating_Blaster_Cannon Medium_Repeating_Blaster_Cannon_\(Errata\) Medium_Repeating_Blaster_Cannon_\(Original\) \
  Mirax_Terrik \
  Projective_Telepathy Projective_Telepathy_\(Errata\) Projective_Telepathy_\(Original\) \
  Responsibility_Of_Command Responsibility_Of_Command_\(Errata\) Responsibility_Of_Command_\(Original\) \
  Spaceport_Speeders Spaceport_Speeders_\(Errata\) Spaceport_Speeders_\(Original\) \
  Tallon_Roll Tallon_Roll_\(Errata\) Tallon_Roll_\(Original\) \
  Undercover Undercover_\(Errata\) Undercover_\(Original\) \
  Wioslea Wioslea_\(Errata\) Wioslea_\(Original\)
do
  file="$PAGES/${f}.wiki"
  # title: underscores to spaces, keep parentheses
  title="${f//_/ }"
  edit "$title" "$file" "$SUMMARY"
done

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge touched =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Rulebooks
Errata
Decipher Glossary Supplement
Decipher Glossary 2.0
Decipher Comprehensive Rules
Star Wars Customizable Card Game RULEBOOK 2.0
Enhanced Premiere Rulesheet
Endor Rulesheet
Death Star II Rulesheet
Reflections II Rulesheet
Reflections III Rulesheet
Tatooine Rulesheet
Coruscant Rulesheet
Theed Palace Rulesheet
Virtual card icons
Errata on Projective Telepathy
File:Decipher_Glossary_Supplement.pdf
File:Decipher_Glossary_1998.pdf
File:Decipher_Rulebook_2.0.pdf
File:Decipher_Enhanced_Premiere_Rulesheet.pdf
File:Decipher_Endor_Rulesheet.pdf
File:Decipher_Death_Star_II_Rulesheet.pdf
File:Decipher_Reflections_II_Rulesheet.pdf
File:Decipher_Reflections_III_Rulesheet.pdf
File:Decipher_Tatooine_Rulesheet.pdf
File:Decipher_Coruscant_Rulesheet.pdf
File:Decipher_ESB_Two_Player_Rules.pdf
File:Decipher_Theed_Palace_Rule_Cards.pdf
File:Icon_Reference_Sheet_Feb_2024.pdf
Main Page
EOF

echo "== verify files =="
docker exec swccg_wiki bash -c "find /var/www/html/images -name 'Decipher_*.pdf' -o -name 'Icon_Reference_Sheet_Feb_2024.pdf' 2>/dev/null | sort"
echo "apply-decipher-rulebooks-local done"