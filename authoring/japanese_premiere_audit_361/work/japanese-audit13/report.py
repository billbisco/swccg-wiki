from datetime import datetime,timedelta,timezone
import json
from pathlib import Path
import re

root=Path('work/japanese-audit13')
manifest=json.loads((root/'final-manifest.json').read_bytes())
rows=json.loads((root/'payload.json').read_bytes())['rows']
heads=json.loads((root/'checked-heads.json').read_bytes())
checks=json.loads((root/'verification.json').read_bytes())
assert len(manifest)==324 and len(rows)==len(checks)==167
assert not json.loads((root/'remaining-field-gaps.json').read_bytes())
old=json.loads((root/'live.json').read_bytes())
for card in manifest:
    title=card['title']
    before=old[title]['revisions'][0]['slots']['main']['content']
    after=heads[title]['revisions'][0]['slots']['main']['content']
    a=re.search(r'<tr><th>Versions</th><td>(.*?)</td></tr>',before,re.S)
    b=re.search(r'<tr><th>Versions</th><td>(.*?)</td></tr>',after,re.S)
    if title=='Reactor Terminal (Japanese)':
        assert before.replace('<br.\n</table>','</td></tr>\n</table>')==after
        assert re.findall(r'\[\[.*?\]\]|<code>.*?</code>',before)==re.findall(r'\[\[.*?\]\]|<code>.*?</code>',after)
    else:
        assert a and b and a[1]==b[1],title
    assert after.count('<table')==after.count('</table>'),title
    assert all(after.count('<'+tag+'>')==after.count('</'+tag+'>') for tag in ['tr','td','th']),title
    assert '<code>'+card['printing_id']+'</code>' in after or card['printing_id'] in after,title
    assert '[[Premiere (Japanese)' in after,title
set_text=heads['Premiere (Japanese)']['revisions'][0]['slots']['main']['content']
assert all('link='+card['title']+']]' in set_text for card in manifest)
assert set_text.count('!! Parsec !! Game text')==2
(root/'navigation-check.json').write_text(json.dumps(dict(printing_ids=324,family_version_rows_unchanged=323,family_version_rows_markup_repaired_without_link_loss=1,card_set_navigation=324,set_card_image_links=324,location_parsec_headers=2,balanced_card_tables=324),indent=2),encoding='utf8')
links={r['title']:r for r in checks}
readme='''# Japanese Premiere audit and verified repairs — Story #361

Completed a coverage audit of all 324 regular Japanese Premiere printings. Published repairs on **164 card articles, the set checklist, and two File descriptions** (167 pages). All changed public reviewed pages match their guarded final text, have zero lint/Cite errors, and retain functioning images.

## Results

- Completed sixteen Japanese game-text/lore entries and their English translations; added missing game/lore translations on Ponda Baba, Overload, Physical Choke and Precise Attack, and title-translation labels on LIN-V8K/Pops.
- Completed Ellorrs Madak's truncated Japanese text and three opposite-side location blocks.
- Corrected four Effect classifications, printed character/ship/vehicle/location symbols, Jawa's variable deploy, Talz's three asterisks and applicable stats. All 37 locations have numeric Force-icon counts; ten systems have verified parsec values. Removed unprinted destiny/deploy defaults from locations.
- Added complete original R4-E1/Tanbris photos without overwriting old frames; verified a source snapshot and both uploaded JPEG Wayback captures byte for byte.
- Fixed 34 bare set-video citations using an opened archived **watch page** and separate preserved card-frame links. This does not claim the archived watch page preserves playable video.
- Reconciled the checklist and retained 323 existing Versions rows verbatim and repaired Reactor Terminal’s malformed row without losing any printing link. No card article was deleted, renamed, merged or newly minted.

## Limits and integration work

[Remaining evidence](remaining-evidence.md) distinguishes coverage from proofreading. Existing fields are present, but this is not a fresh word-for-word certification of every older transcription or a comprehensive subtype rereading. The 135 video-derived filenames form a candidate list for edge inspection/replacement, not 135 proven incomplete scans. Chief Bast's lower-edge uncertainty is stated on the article. Source-verified visible icons are retained without inventing absent symbols or numeric zeros.

All 324 pages still use manual infoboxes. [Recommendations](recommendations.md) are supplied to existing story #287, owned by Alpha1/DatacardGrok; that template migration is not completed by this story. It must rebase its content/category baselines on these revisions.

## Evidence and reproduction

- [324-card manifest](final-manifest.json), [coverage CSV](coverage.csv), [remaining field gaps](remaining-field-gaps.json), [public verification](verification.json), and `navigation-check.json`.
- `changes.diff`, `phase2.diff`, `phase3.diff`, source readings, archive replay hashes, upload/edit receipts, and before/after/diff/desktop/mobile screenshots.
- Reproducible scripts and captured inputs are backed up under `billbisco/swccg-wiki/authoring/japanese_premiere_audit_361/`. From that bundle's root, read-only verification is `python work/japanese-audit13/verify.py` then `python work/japanese-audit13/final-audit.py`. Scripts require Python, requests, BeautifulSoup and Pillow; local screenshots additionally use Playwright and Chrome. Source acquisition uses the documented VPS FlareSolverr endpoint and closes only its own sessions.
- Historical build/publish packets are evidence, **not an instruction to replay stale revisions**. Rebase from live heads before any future write. Publication uses Memory Core ChatGPT's own VPS credential in memory, `bot=1`, revision/hash checks and both edit timestamps. No secrets are committed.

## Editing-method deviation

The legacy card sources use raw HTML headings with no editable section indices; an API rvsection=0 read returns the entire card (section-boundaries.json). The publisher used scoped whole-page writes for changes spanning these infoboxes/body blocks, and an explicit section=0 write for Reactor Terminal. It guarded every write with the exact prior revision and full-text SHA-256 as well as basetimestamp/starttimestamp, stopped on any mismatch, and verified exact final content and preserved family rows afterward. No other editor's concurrent revision was overwritten. This is recorded explicitly rather than claiming the section-edit procedure was used.

## All changed live pages

| Page | Final reviewed revision |
|---|---:|
'''
for row in rows:
    item=links[row['title']]
    readme+=f"| [{row['title']}]({item['url']}) | {item['revid']} |\n"
(root/'README.md').write_text(readme,encoding='utf8')
now=datetime.now(timezone(timedelta(hours=-4))).strftime('%Y-%m-%d %H:%M')
report=f'''PASS-REPORT v1 — ticket #361 — agent: ChatGPT — {now} (UTC-4)
| AC | Result | Evidence |
|---|---|---|
| AC1 Complete 324-printing evidence manifest and applicable-field summary | PASS | [final-manifest.json](https://github.com/swccg-guild/work/blob/main/evidence/361/final-manifest.json), coverage.csv; 324 unique IDs, 324 current images, per-field coverage and verification states |
| AC2 Source-verified repairs and explicit evidence limits | PASS | readings.json, phase3.diff, remaining-evidence.md; 16 full text entries, 4 further game/lore translations, 3 location side blocks, corrected symbols/stats and two recovered complete faces. Remaining coverage limits are listed individually; no English values silently replace Japanese evidence. |
| AC3 Reviewed public repairs, lint, images and navigation | PASS | verification.json: 167/167 final public reviewed pages match guarded text, lint 0 and Cite 0; 323 unchanged Versions rows plus one closing-tag repair with all links/IDs retained, 324 reciprocal checklist links, balanced card tables, 2 correct parsec headers. New source/JPEG replays byte-checked. Editing-method deviation documented below. |
| AC4 Concrete integration recommendations, coordinated on existing #287 | PASS | [recommendations.md](https://github.com/swccg-guild/work/blob/main/evidence/361/recommendations.md); existing owner retained, fresh-baseline requirements and edge-case fixtures supplied |
| AC5 Shared evidence, wiki text/scripts, images and handoff | PASS | evidence/361, wiki/image backup commits recorded alongside this report, and the refreshed team wiki handoff |
Overall: PASS
Visual diff: evidence/361/before.webp · evidence/361/after.webp · evidence/361/diff.webp

Public wiki edits are deployed and reviewed. The wiki has no separate Test server; pre-publication MediaWiki previews and a five-card live sample preceded the larger batches. No server configuration or gameplay changes. No peer review was requested.

**Editing method:** whole-page writes were used for changes spanning infoboxes and multiple text sections, rather than the board's section-edit parameter. Every write had an exact revision + full-content hash guard and both timestamps; final source and family rows were checked. No concurrent editor revision was overwritten. This procedural variance is disclosed; it is not represented as a section edit.

**Scope limit:** PASS certifies the coverage audit and verified repairs in #361, not a complete retranslation of every existing article, proof that all 135 video-derived images are complete, or completion of #287. Chief Bast's lower edge remains specifically unresolved. No deletions are needed for this batch.

MemoryCoreChatGPT
'''
(root/'pass-report.md').write_text(report,encoding='utf8')
(root/'design-log.md').write_text('''# #361 — Japanese Premiere coverage and integration

## 2026-11-13 — Complete verifiable source gaps; preserve printing identity

**Decision.** Audit all 324 regular Japanese Premiere articles, repair omissions and contradictions supported by their printed faces, and coordinate generic infobox support through existing #287. Separate coverage, independent verification and full-face completeness in the manifest.

**Why.** Manual infoboxes do not inherit Template:Card changes. Empty sections, truncated native text, wrong Effect types, parsec-as-destiny and imported zero defaults demonstrated that completeness cannot be inferred from article or image existence. Four further Translation sections held only a title; component-level checks were added.

**Alternatives.** Do not copy English rules into a Japanese historical printing, infer missing numeric zero values, rebuild another owner's template migration, or replace archive originals with reconstructions. Preserve photographer/source links and original bytes; keep playable-video preservation distinct from archived watch-page metadata.

**Who / Status.** Bill requested the full audit and integration recommendations; MemoryCoreChatGPT executed #361. #287 remains Alpha1/DatacardGrok's assigned migration. Recommendations and updated baselines are evidence/361/recommendations.md and final-manifest.json.

**Implementation-method variance.** Multi-section page repairs used whole-page API writes with exact prior revision and full-content SHA-256 guards plus both timestamps, instead of the board's section-edit parameter. This is disclosed in the report. Exact final source and preserved family links and IDs were verified; no concurrent editor revision was overwritten.

**Verification.** 324 unique printings, no missing presence/applicable-stat/translation-component fields, 167 changed public reviewed pages with lint/Cite 0, intact images and family/checklist links, original-photo replay hashes and Japanese-capable local desktop/mobile screenshots. Remaining evidence limits are explicit, including Chief Bast's cropped lower edge and the 135 video-image candidates. This does not certify a full linguistic proofreading or finish #287.
''',encoding='utf8')
print('Report, navigation proof and 167 live page links written')
