"""Lossless File-description layout migration; no source facts or links are removed.

This is a draft producer, not a publisher or an editorial/source-verification gate.
Ambiguous paragraphs and opaque templates stay intact and get a repair disposition.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

HEADING = re.compile(r"^(?P<marks>={2,6})[ \t]*(?P<label>.*?)[ \t]*(?P=marks)[ \t]*$", re.M)
CATEGORY = re.compile(r"\[\[Category:[^\]]*\]\]", re.I)
PROTECTED = re.compile(r"<!--[\s\S]*?-->|<(nowiki|pre|syntaxhighlight|source)\b[^>]*>[\s\S]*?</\1\s*>|<nowiki\s*/>", re.I)
SOURCE_PREFIX = r"(?:Source(?:[ \t]+and[ \t]+credit)?[ \t]*:|'''Source(?:[ \t]+and[ \t]+credit)?[ \t]*(?::'''|'''[ \t]*:))"
SOURCE_BOUNDARY = re.compile(r"^[ \t]*(?:\*[ \t]*)?(?:" + SOURCE_PREFIX + r"[ \t]*\S|Photo provided by[ \t]+\S)", re.I | re.M)
RENAMES = {"summary": "Description", "source": "Source and credit", "sources": "Source and credit"}


def _masked(text: str) -> str:
    """Mask comments/code and balanced template bodies while retaining offsets."""
    chars = list(text)
    for match in PROTECTED.finditer(text):
        for pos in range(match.start(), match.end()):
            if chars[pos] not in "\r\n":
                chars[pos] = " "
    masked = "".join(chars)
    depth = 0
    pos = 0
    while pos < len(masked) - 1:
        pair = masked[pos:pos + 2]
        if pair == "{{":
            depth += 1
            chars[pos:pos + 2] = "  "
            pos += 2
        elif pair == "}}" and depth:
            depth -= 1
            chars[pos:pos + 2] = "  "
            pos += 2
        else:
            if depth and chars[pos] not in "\r\n":
                chars[pos] = " "
            pos += 1
    if depth and chars and chars[-1] not in "\r\n":
        chars[-1] = " "
    return "".join(chars)


def _headings(text: str) -> list[re.Match]:
    return [m for m in HEADING.finditer(_masked(text)) if len(m["marks"]) == 2]


def _substantive(text: str) -> bool:
    return bool(CATEGORY.sub("", _masked(text)).strip())


def _section_content(text: str, match: re.Match) -> str:
    following = HEADING.search(_masked(text), match.end())
    return text[match.end():following.start() if following else len(text)]


def structural_issues(text: str) -> list[str]:
    """Structural observations only; strict Wiki lint remains a separate gate."""
    headings = _headings(text)
    names = [m["label"].strip().casefold() for m in headings]
    issues = []
    if "description" not in names:
        issues.append("missing_description_section")
    if "source and credit" not in names:
        issues.append("missing_source_and_credit_section")
    if any(name in RENAMES for name in names):
        issues.append("legacy_section_heading")
    if any(names.count(name) > 1 for name in ["description", "source and credit"]):
        issues.append("duplicate_standard_heading")
    if any(not _substantive(_section_content(text, m)) for m in headings):
        issues.append("empty_section")
    if "{{" in text and not _substantive(text):
        issues.append("opaque_template_description")
    return issues


def _payload(text: str) -> str:
    """All non-heading payload characters in their original order, sans whitespace."""
    chars = list(text)
    for m in _headings(text):
        chars[m.start():m.end()] = " " * (m.end() - m.start())
    return re.sub(r"\s", "", "".join(chars))


def normalize(text: str) -> dict:
    original = text
    before = structural_issues(text)
    if re.match(r"\s*#redirect\b", text, re.I):
        return {
            "text": text, "changed": False, "operations": [],
            "issues_before": before, "issues_after": before, "new_issues": [],
            "all_payload_characters_retained": True, "all_urls_retained_in_order": True,
            "source_disposition": "file_redirect_not_a_description",
        }
    operations = []
    heads = _headings(text)
    names = [m["label"].strip().casefold() for m in heads]
    replacements = []
    for m in heads:
        target = RENAMES.get(m["label"].strip().casefold())
        if not target:
            continue
        # Do not merge competing sections or turn existing empty fields into the standard.
        aliases = [name for name in names if RENAMES.get(name, name).casefold() == target.casefold()]
        if len(aliases) != 1 or not _substantive(_section_content(text, m)):
            continue
        replacements.append((m.start(), m.end(), "== " + target + " =="))
        operations.append("rename_heading:" + m["label"].strip() + "->" + target)
    for start, end, replacement in reversed(replacements):
        text = text[:start] + replacement + text[end:]

    heads = _headings(text)
    names = [m["label"].strip().casefold() for m in heads]
    # An explicit source line can also follow a real Description/Summary subject.
    descriptions = [m for m in heads if m["label"].strip().casefold() == "description"]
    if len(descriptions) == 1 and "source and credit" not in names:
        description = descriptions[0]
        body = _section_content(text, description)
        boundary = SOURCE_BOUNDARY.search(_masked(body))
        if boundary and _substantive(body[:boundary.start()]):
            index = description.end() + boundary.start()
            text = text[:index] + "== Source and credit ==\n\n" + text[index:]
            operations.append("insert_source_heading_at_explicit_boundary")
            heads = _headings(text)
            names = [m["label"].strip().casefold() for m in heads]
    first = heads[0].start() if heads else len(text)
    prelude = text[:first]
    masked_prelude = _masked(prelude)
    boundary = SOURCE_BOUNDARY.search(masked_prelude)
    if boundary and "source and credit" not in names:
        index = boundary.start()
        source = prelude[index:]
        # A first-line source gives no subject; retain it without fabricating Description.
        if _substantive(source):
            prefix = prelude[:index]
            insert = "== Source and credit ==\n\n"
            text = prefix + insert + text[index:]
            operations.append("insert_source_heading_at_explicit_boundary")
            first = index
            prelude = prefix
    if "description" not in names and _substantive(prelude):
        # Bare URLs and source-only labels are not descriptions of an image's subject.
        visible = CATEGORY.sub("", _masked(prelude)).strip()
        if not re.match(r"(?:https?://|(?:\*[ \t]*)?" + SOURCE_PREFIX + r"|Photo provided by\b)", visible, re.I):
            text = "== Description ==\n\n" + text
            operations.append("insert_description_heading_over_existing_subject")

    after = structural_issues(text)
    assert _payload(original) == _payload(text), "Substantive payload changed; hold the draft"
    urls = lambda value: re.findall(r"https?://[^\s<>\]\"']+", value)
    assert urls(original) == urls(text), "Source URL sequence changed; hold the draft"
    return {
        "text": text,
        "changed": text != original,
        "operations": operations,
        "issues_before": before,
        "issues_after": after,
        "new_issues": sorted(set(after) - set(before)),
        "all_payload_characters_retained": True,
        "all_urls_retained_in_order": True,
        "source_disposition": "standard_section_present" if "missing_source_and_credit_section" not in after else "source_boundary_or_missing_information_needs_review",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    flags = Counter()
    with args.inventory.open(encoding="utf8") as source, (args.output / "drafts.jsonl").open("w", encoding="utf8", newline="\n") as drafts:
        for line in source:
            row = json.loads(line)
            if not row.get("image"):
                counts["non_image_excluded"] += 1
                continue
            counts["images"] += 1
            result = normalize(row.get("text", ""))
            counts["changed" if result["changed"] else "unchanged"] += 1
            counts["new_structural_issues"] += len(result["new_issues"])
            counts["with_source_section_after"] += "missing_source_and_credit_section" not in result["issues_after"]
            counts["with_description_section_after"] += "missing_description_section" not in result["issues_after"]
            flags.update(result["issues_after"])
            record = {"title": row["title"], "revision": row.get("revision"), "before_sha256": hashlib.sha256(row.get("text", "").encode()).hexdigest(), **result}
            drafts.write(json.dumps(record, ensure_ascii=False) + "\n")
    summary = {"inventory": str(args.inventory), "counts": dict(counts), "structural_issues_after": dict(flags), "scope": "Pure lossless layout drafts; not a strict editorial/source-verification or publication PASS"}
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
