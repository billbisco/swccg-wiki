#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

if ! grep -q "wgDefaultSkin" "$ROOT/extra-settings.php" || ! grep -q "vector';" "$ROOT/extra-settings.php"; then
  cat >> "$ROOT/extra-settings.php" <<'PHP'

# LOTR-wiki-style left sidebar (Vector legacy, not Vector 2022)
$wgDefaultSkin = "vector";
$wgDefaultUserOptions["vector-limited-width"] = 0;
PHP
fi

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d

import_page() {
  local title="$1"
  local file="$2"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Front page / card versions" "$title" < "$file"
}

import_page "Template:Card" "$PAGES/Template_Card.wiki"
import_page "Card:1_109" "$PAGES/Card_1_109.wiki"
import_page "Card versions" "$PAGES/Card_versions.wiki"
import_page "Main Page" "$PAGES/Main_Page.wiki"
import_page "MediaWiki:Sidebar" "$PAGES/MediaWiki_Sidebar.wiki"
import_page "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki"

stub() {
  local title="$1"
  local body="$2"
  printf '%s\n' "$body" | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="stub" "$title"
}

stub "Star Wars CCG" "'''Star Wars Customizable Card Game''' was published by Decipher from 1995 to 2001. This wiki covers that history first. Later Players Committee errata and virtual cards are labeled as later layers. Construction stub. See [[Main Page]]."
stub "Getting Started" "New to the game: [[How to play]], [[Starter Decks]], [[Card Type]], [[Phase]], then [[GEMP|play online]]. Construction stub."
stub "Starter Decks" "Decipher starter and two-player products. Construction stub. See [[Premiere]] and [[Premium sets]]."
stub "Card Type" "SWCCG card types: [[Character]], [[Creature]], [[Location]], [[Starship]], [[Vehicle]], [[Interrupt]], [[Effect]], [[Weapon]], [[Device]], [[Objective]], [[Epic Event]], [[Admiral's Order]], [[Jedi Test]], [[Podracer]], [[Defensive Shield]]. Construction stub."
stub "Card Layout" "How to read a SWCCG card: destiny, power, ability, deploy, forfeit, icons, lore, game text. Construction stub."
stub "Side" "Light Side and Dark Side. Construction stub."
stub "Phase" "A turn: Activate, Control, Deploy, Battle, Move, Draw. Construction stub."
stub "Formats" "Decipher-era constructed and sealed, plus later PC Standard and other labeled formats. This site hosts PC Standard as one format among others. Construction stub."
stub "PC Errata" "Players Committee errata are '''separate card pages''' (card_uid suffix <code>-PC</code>), linked from the original printing. They are not Decipher text. Construction stub. See [[Card versions]]."
stub "Rulebooks" "Redirect target for Official Rulebooks. See [[Rules]]."
stub "Decipher Rulebook" "Last widely used Decipher Rulebook (confirm edition at ingest; often cited as v2.0, November 1998). Transcription is WP-W7. Construction stub."
stub "Decipher Current Rulings Document" "Last Decipher CRD. Construction stub. Archive the PDF before quoting."
stub "Players Committee Advanced Rulebook" "Current PC Advanced Rulebook. Labeled as a later layer. Construction stub."
stub "Tournament Guidelines" "Tournament procedure. Construction stub."
stub "Current Virtual Sets" "PC virtual sets from the 2014 Reset onward (Set 0, Set 1, …). Badge: Players Committee / Virtual. Construction stub."
stub "Virtual Legacy" "PC virtual cards 2002 through the 2014 Reset. Not current Standard. Construction stub."
stub "Premium sets" "Jedi Pack, anthologies, Enhanced sets, OTSD, two-player, etc. Construction stub."
stub "Reflections" "Reflections I, II, III (Decipher). Construction stub."
stub "A New Hope" "Decipher expansion. Construction stub. See [[Sets]]."
stub "Hoth" "Decipher expansion. Construction stub."
stub "Dagobah" "Decipher expansion. Construction stub."
stub "Cloud City" "Decipher expansion. Construction stub."
stub "Jabba's Palace" "Decipher expansion. Construction stub."
stub "Special Edition" "Decipher expansion. Construction stub."
stub "Endor" "Decipher expansion. Construction stub."
stub "Death Star II" "Decipher expansion. Construction stub."
stub "Tatooine" "Decipher expansion. Construction stub."
stub "Coruscant" "Decipher expansion. Construction stub."
stub "Theed Palace" "Decipher expansion. Construction stub."

for t in Character Creature Location Starship Vehicle Interrupt Effect Weapon Device Objective "Epic Event" "Admiral's Order" "Jedi Test" Podracer "Defensive Shield" Destiny Power Ability Deploy Forfeit Icons Lore "Game text" "Life Force" "Reserve Deck" "Force Pile" "Used Pile" "Lost Pile" Hand "Activate Phase" "Control Phase" "Deploy Phase" "Battle Phase" "Move Phase" "Draw Phase" "Force drain" "Force loss" Battle Attrition "Immunity to attrition" Presence React Captive Uniqueness Persona Errata Play; do
  stub "$t" "Construction stub. See [[Main Page]] and [[Card Type]] / [[Phase]] / [[Game text]]."
done

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
echo "Front page + stubs done."
curl -sI -m 10 "https://wiki.swccg.com/wiki/Main_Page" | head -8
