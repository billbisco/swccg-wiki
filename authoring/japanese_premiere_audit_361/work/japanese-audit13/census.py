import collections
import json
from pathlib import Path
import re
import sys

from bs4 import BeautifulSoup

sys.path.insert(0, "work/wiki-tools")
from style_lint import lint

root = Path("work/japanese-audit13")
live = json.loads((root / "live.json").read_bytes())
records = []

def plain(markup):
    return BeautifulSoup(markup, "html.parser").get_text(" ", strip=True)

for title, page in live.items():
    if title.startswith("Template:") or title == "Admiral Motti":
        continue
    revision = page["revisions"][0]
    text = revision["slots"]["main"]["content"]
    match = re.search(r"1301_(\d+)o?", text)
    assert match, title
    number = int(match[1])
    normalized = re.sub(r"<h2>(.*?)</h2>", r"== \1 ==", text)
    chunks = re.split(r"(?m)^==\s*(.*?)\s*==\s*\n", normalized)
    sections = dict(zip(chunks[1::2], chunks[2::2]))
    soup = BeautifulSoup(text, "html.parser")
    stats = {}
    for row in soup.select("table.card-infobox tr"):
        cells = row.find_all(["th", "td"], recursive=False)
        if len(cells) == 2:
            stats[plain(str(cells[0]))] = plain(str(cells[1]))
    for label, value in re.findall(r"(?m)^\* '''([^']+):''' (.*)$", text):
        stats.setdefault(label, value)
    files = list(dict.fromkeys(re.findall(r"\[\[File:([^|\]]+)", text)))
    issues = []
    for label in ["Title", "Card Text", "Lore", "Translation of Japanese Text"]:
        value = sections.get(label, "")
        if not value or re.search(r"not yet|awaits verification|awaiting verification|Not yet|yet to be|untranscribed", value):
            if label == "Lore" and "Location" in stats.get("Type", stats.get("Card type", "")):
                continue
            issues.append(label)
    if not files:
        issues.append("scan")
    if any("Video" in filename for filename in files):
        issues.append("scan edge completeness check")
    type_label = stats.get("Type", stats.get("Card type", ""))
    card_type = re.search(r"\[\[([^]|]+)", type_label)
    card_type = card_type[1] if card_type else plain(type_label)
    applicable = ["Destiny"]
    if "Location" in card_type:
        applicable = ["Dark icons", "Light icons"]
        if "System" in type_label:
            applicable.append("Parsec")
    elif any(kind in card_type for kind in ["Character", "Starship", "Vehicle", "Creature"]):
        applicable += ["Power", "Deploy", "Forfeit"]
        if "Character" in card_type and "Droid" not in type_label:
            applicable.append("Ability")
        if "Starfighter" in type_label:
            applicable += ["Maneuver", "Hyperspeed"]
        if "Capital" in type_label:
            applicable += ["Armor", "Hyperspeed"]
        if "Vehicle" in card_type:
            applicable.append("Landspeed")
    missing_stats = [label for label in applicable if not stats.get(label)]
    if missing_stats:
        issues.append("stats: " + ", ".join(missing_stats))
    if "Location" not in card_type and not stats.get("Icons") and not stats.get("Card type icon"):
        issues.append("symbol inventory check")
    flags = lint(text, title)[0]
    records.append(dict(title=title, number=number, printing_id=f"1301_{number}o", revid=revision["revid"], files=files,
                        stats=stats, sections=sections, issues=issues, lint_flags=flags,
                        shared_template=bool(re.search(r"\{\{\s*Card\s*[|\n]", text, re.I))))

assert len(records) == 324 and {row["number"] for row in records} == set(range(1, 325))
records.sort(key=lambda row: row["number"])
(root / "census.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
counts = collections.Counter(issue for row in records for issue in row["issues"])
print("324 distinct original printing IDs reconciled")
print("Shared Card template", sum(row["shared_template"] for row in records), "of", len(records))
print("Gaps or verification checks", dict(counts))
print("Pages with lint findings", sum(bool(row["lint_flags"]) for row in records))
for row in records:
    serious = [issue for issue in row["issues"] if issue in ["Title", "Card Text", "Lore", "Translation of Japanese Text", "scan"]]
    if serious:
        print(row["number"], row["title"], "; ".join(row["issues"]))
