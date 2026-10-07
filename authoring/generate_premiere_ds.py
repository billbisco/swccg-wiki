#!/usr/bin/env python3
"""Generate Premiere Dark Side card pages. Shared names use Title (Dark)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_premiere_ls_rest as g

OUT = g.ROOT / "pages" / "ds-cards"
CONCEPTS = {
    "Interrupt",
    "Used Interrupt",
    "Lost Interrupt",
    "Effect",
    "Utinni Effect",
    "Character",
    "Device",
    "Weapon",
    "Starship",
    "Vehicle",
    "Location",
    "Site",
    "System",
    "Light",
    "Dark",
    "Rebel",
    "Imperial",
    "Alien",
    "Droid",
    "Used",
    "Lost",
    "Character Weapon",
    "Starship Weapon",
    "Automated Weapon",
    "Artillery Weapon",
    "Vehicle Weapon",
    "Starfighter",
    "Capital",
    "Transport",
    "Creature Vehicle",
}


def image_map():
    text = g.THUMBS.read_text(encoding="utf-8")
    m = {}
    for fn, uid in re.findall(
        r"\[\[File:(Premiere-D-[a-z0-9]+\.gif)\|200px\|link=Card:(1_\d+)\]\]",
        text,
    ):
        m[uid] = fn
    return m


def wiki_title(printed: str, occupied: set[str]) -> str:
    if printed not in occupied:
        return printed
    return f"{printed} (Dark)"


def main():
    db = g.load_db()
    imgs = image_map()
    ls_titles = {c["title"] for c in db if c.get("side") == "LIGHT"}
    occupied = set(ls_titles) | CONCEPTS | {
        "2X-3KPR (Tooex)",
        "Tooex",
        "2X-3KPR",
        "Premiere Limited",
        "Rarity",
    }
    cards = [c for c in db if c.get("side") == "DARK"]
    cards.sort(key=lambda c: int(c["cardId"].split("_")[1]))
    titles_for_link = [c["title"] for c in db if c.get("side") in ("LIGHT", "DARK")]
    linker = g.Linker(titles_for_link)
    wiki_titles = [wiki_title(c["title"], occupied) for c in cards]
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for i, c in enumerate(cards):
        printed = c["title"]
        page = wiki_titles[i]
        prev_t = wiki_titles[i - 1] if i else ""
        next_t = wiki_titles[i + 1] if i + 1 < len(wiki_titles) else ""
        img = imgs.get(c["cardId"], "")
        hatnote = ""
        if page != printed:
            hatnote = f"For the Light Side card, see [[{printed}]]."
        text = g.page_for(
            c,
            prev_t,
            next_t,
            img,
            linker,
            side="Dark",
            list_url=g.DECIPHER_DS,
            hatnote=hatnote,
        )
        path = OUT / f"{c['cardId']}.wiki"
        path.write_text(text, encoding="utf-8")
        written.append((page, c["cardId"], path, printed))
    print("wrote", len(written), "to", OUT)
    (OUT / "index.tsv").write_text(
        "\n".join(f"{uid}\t{page}\t{path.name}" for page, uid, path, _p in written)
        + "\n",
        encoding="utf-8",
    )
    occupied2 = set(occupied) | {page for page, *_ in written}
    alias_rows = []
    for page, uid, _path, printed in written:
        for alias in g.aliases_for(printed):
            if alias and alias not in occupied2:
                alias_rows.append((alias, page))
                occupied2.add(alias)
        if page != printed and printed not in occupied2:
            # do not steal the Light page
            pass
    (OUT / "aliases.tsv").write_text(
        "\n".join(f"{alias}\t{dest}" for alias, dest in alias_rows) + "\n",
        encoding="utf-8",
    )
    print("aliases", len(alias_rows))
    print("disambiguated", sum(1 for page, _u, _p, printed in written if page != printed))


if __name__ == "__main__":
    main()
