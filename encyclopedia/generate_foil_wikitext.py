"""Emit compact foil-list wikitext from encyclopedia foil_index.json."""
import json
from collections import defaultdict
from pathlib import Path

rows = json.loads(Path("wiki/encyclopedia/foil_index.json").read_text(encoding="utf-8"))

SET_MAP = {
    "Reflections A Collector's Bounty": "ref1",
    "Reflections II Expanding the Galazy": "ref2",
    "Reflections III": "ref3",
    "Rebel Leader Pack": "promo",
}

RARITY_ORDER = ["Ultra Rare Foil", "Super Rare Foil", "Very Rare Foil", "Tournament Foil"]
SIDE_ORDER = ["Light", "Dark"]


def wiki_title(title: str) -> str:
    t = title.replace("•", "").strip()
    t = t.replace("  ", " ")
    return t


def emit(key: str) -> str:
    items = [r for r in rows if SET_MAP.get(r["set"]) == key]
    by = defaultdict(list)
    for r in items:
        by[(r["side"], r["rarity"])].append(wiki_title(r["title"]))
    parts = []
    for side in SIDE_ORDER:
        parts.append(f"=== {side} Side ===")
        for rar in RARITY_ORDER:
            titles = sorted(set(by[(side, rar)]))
            if not titles:
                continue
            short = rar.replace(" Foil", "")
            parts.append(f"'''''{short}''''' ({len(titles)})")
            parts.append(", ".join(f"[[{t}]]" for t in titles))
            parts.append("")
    return "\n".join(parts).rstrip() + "\n"


out = Path("wiki/encyclopedia")
(out / "foils_ref1.wiki").write_text(emit("ref1"), encoding="utf-8")
(out / "foils_ref2.wiki").write_text(emit("ref2"), encoding="utf-8")
(out / "foils_ref3.wiki").write_text(emit("ref3"), encoding="utf-8")
(out / "foils_promo.wiki").write_text(emit("promo"), encoding="utf-8")
for name in ("foils_ref1.wiki", "foils_ref2.wiki", "foils_ref3.wiki", "foils_promo.wiki"):
    p = out / name
    print(name, p.stat().st_size, "lines", p.read_text(encoding="utf-8").count("\n"))
