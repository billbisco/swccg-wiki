"""Put a person page's sections back in house order after the DeckTech/GPN builders append to it (2026-10-17).

Order: lead, content sections (Tournament Results, Decklists, …) with Miscellaneous decklists right after Decklists,
then See also, External links, Sources, one References block, categories. Duplicate See also / Sources sections are
merged; bullet links left under the Miscellaneous decklists table move to See also; extra References blocks go.
"""
from __future__ import annotations

import re

REF_BLOCK = re.compile(r"\{\{#if:1\|<nowiki />\n<h2>References</h2>\n<references />\}\}\n?")
REF_SECTION = re.compile(r"^== *References *==\n+<references */>\n?", re.M)
TAIL = ["See also", "External links", "Sources"]


def _merge_bullets(bodies: list[str]) -> str:
    out, seen = [], set()
    for b in bodies:
        for line in b.strip("\n").splitlines():
            key = line.strip()
            if not key:
                continue
            if key in seen and key.startswith("*"):
                continue
            seen.add(key)
            out.append(line)
    return "\n".join(out)


def tidy(text: str) -> str:
    had_refs = bool(REF_BLOCK.search(text) or REF_SECTION.search(text))
    cats = re.findall(r"^\[\[Category:[^\]]+\]\]$", text, re.M)
    body = re.sub(r"^\[\[Category:[^\]]+\]\]\n?", "", text, flags=re.M)
    body = REF_SECTION.sub("", REF_BLOCK.sub("", body))
    parts = re.split(r"^== *([^=\n]+?) *== *$", body, flags=re.M)
    lead, secs = parts[0].strip("\n"), []
    for i in range(1, len(parts), 2):
        secs.append((parts[i].strip(), parts[i + 1].strip("\n")))
    merged: dict[str, list[str]] = {}
    order: list[str] = []
    for name, b in secs:
        if name not in merged:
            order.append(name)
            merged[name] = []
        merged[name].append(b)
    if "Miscellaneous decklists" in merged:  # bullets after the table are See also links
        moved = []
        new = []
        for b in merged["Miscellaneous decklists"]:
            end = b.rfind("|}")
            if end >= 0 and b[end + 2:].strip():
                moved.append(b[end + 2:])
                b = b[:end + 2]
            new.append(b)
        merged["Miscellaneous decklists"] = new
        if moved:
            if "See also" not in merged:
                order.append("See also")
                merged["See also"] = []
            merged["See also"] += moved
    content = [n for n in order if n not in TAIL and n != "Miscellaneous decklists"]
    if "Miscellaneous decklists" in merged:
        at = content.index("Decklists") + 1 if "Decklists" in content else len(content)
        content.insert(at, "Miscellaneous decklists")
    final = content + [n for n in TAIL if n in merged]
    out = [lead] if lead else []
    for n in final:
        b = _merge_bullets(merged[n]) if n in ("See also", "Sources", "External links") else "\n\n".join(x for x in merged[n] if x.strip())
        out.append(f"== {n} ==\n\n{b}" if b else f"== {n} ==")
    text2 = "\n\n".join(out).rstrip("\n") + "\n"
    if had_refs:
        text2 += "\n{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n"
    if cats:
        text2 += "\n" + "\n".join(dict.fromkeys(cats)) + "\n"
    return text2
