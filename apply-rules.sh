#!/bin/bash
set -euo pipefail
python3 - <<'PY'
import subprocess
from pathlib import Path

def edit(title, data, summary):
    print("edit", title, flush=True)
    subprocess.run(
        [
            "docker", "exec", "-i", "swccg_wiki",
            "php", "maintenance/run.php", "edit",
            "--user=Admin", f"--summary={summary}",
            title,
        ],
        input=data if isinstance(data, bytes) else data.encode("utf-8"),
        check=True,
    )

pages = Path("/opt/swccg-wiki/pages")
names = {
    "Rules.wiki": "Rules",
    "Rulebooks.wiki": "Rulebooks",
    "Star_Wars_Customizable_Card_Game_RULEBOOK_2.0.wiki": "Star Wars Customizable Card Game RULEBOOK 2.0",
    "Decipher_Rulebook_2.0.wiki": "Decipher Rulebook 2.0",
    "Decipher_Glossary_2.0.wiki": "Decipher Glossary 2.0",
    "Decipher_Glossary_Supplement.wiki": "Decipher Glossary Supplement",
    "Decipher_Comprehensive_Rules.wiki": "Decipher Comprehensive Rules",
    "Players_Committee_Advanced_Rulebook.wiki": "Players Committee Advanced Rulebook",
    "Enhanced_Premiere_Rulesheet.wiki": "Enhanced Premiere Rulesheet",
    "Endor_Rulesheet.wiki": "Endor Rulesheet",
    "Death_Star_II_Rulesheet.wiki": "Death Star II Rulesheet",
    "Reflections_II_Rulesheet.wiki": "Reflections II Rulesheet",
    "Tatooine_Rulesheet.wiki": "Tatooine Rulesheet",
    "Coruscant_Rulesheet.wiki": "Coruscant Rulesheet",
    "Reflections_III_Rulesheet.wiki": "Reflections III Rulesheet",
    "Theed_Palace_Rulesheet.wiki": "Theed Palace Rulesheet",
    "How_to_play.wiki": "How to play",
    "Main_Page.wiki": "Main Page",
}
for fn, title in names.items():
    path = pages / fn
    if path.exists():
        edit(title, path.read_bytes(), "Decipher and PC rulebook pages")
for path in sorted((pages / "concepts").glob("*.wiki")):
    title = path.stem.replace("_", " ")
    edit(title, path.read_bytes(), "icon stub from Rulebook 2.0")
print("rules pages edited")
PY
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Rules
Rulebooks
Star Wars Customizable Card Game RULEBOOK 2.0
Decipher Rulebook 2.0
Decipher Glossary 2.0
Decipher Glossary Supplement
Decipher Comprehensive Rules
Players Committee Advanced Rulebook
How to play
Main Page
EOF
echo rules pages applied
