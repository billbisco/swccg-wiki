"""Generate the dated coverage report from the final live census."""
import collections,csv,json
from pathlib import Path
from urllib.parse import quote
root=Path(__file__).parent
rows=json.loads((root/'census.json').read_bytes())
prior={r['Canonical title']:r for r in csv.DictReader((root/'prior-indexed-face-coverage.csv').open(encoding='utf-8-sig'))}
url=lambda t:'https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe='')
gaps=[r for r in rows if r['gaps']]
parts=['# Remaining Japanese evidence — 13 November 2026\n',
'The 469-printing census has 47 missing usable faces and nine untranscribed A New Hope cards. The other 38 are Premiere introductory white-border printings with existing text but no acceptable portrait. All 162 Hoth cards now have a face and native sections. Existing transcriptions are not a blanket linguistic or full-edge scan certification. `coverage.csv` and `census.json` record every printing, including the 422 with a face.\n',
'## Counts by product\n\n| Product | Audited | Missing face | Native/translation gap |\n|---|---:|---:|---:|\n']
for s in sorted({r['set'] for r in rows}):
    group=[r for r in rows if r['set']==s]
    parts.append('| '+s+' | '+str(len(group))+' | '+str(sum('scan' in r['gaps'] for r in group))+' | '+str(sum('printed_title' in r['gaps'] for r in group))+' |\n')
parts+=['\n## Named unresolved rows\n\nThe 38 unfilled uniqueness fields are also confined to missing-face printings. A blank icon field on a missing-face article remains unknown. Elsewhere, the 124 inspected icon candidates include 41 cards with no lower-box gameplay icon to add. No droid Ability, TIE hyperdrive, location Lore or printed blank Leia game box is invented. EG-4’s printed star is a valid destiny value.\n\n',
'| Article / printing ID | Missing fields | Source limit and next lead |\n|---|---|---|\n']
for r in gaps:
    p=r['params'];old=prior.get(r['title'],{})
    native='printed_title' in r['gaps']
    limit=('No verified Japanese face in the reused collector inventory or fresh source search. Recover an actual Japanese A New Hope face; verify the card, not its listing/holder label.' if native else 'No acceptable edition-confirmed 1997 Japanese white-border portrait. Earlier SKU/photo leads are placeholders or marked images; obtain a clean physical photograph of this printing, not an ESB or black-border substitute.')
    trail='; '.join(old.get(k,'') for k in ['Sources in this pass','Partial or inaccessible leads'] if old.get(k))
    if trail:limit+=' Earlier index: '+trail
    missing=list(r['gaps'])
    if not r['uniqueness']:missing.append('uniqueness')
    if not r['icons']:missing.append('icons (unverified)')
    parts.append('| ['+r['title']+']('+url(r['title'])+') / `'+p.get('gemp_id','')+'` | '+', '.join(missing)+' | '+limit.replace('|',' / ')+' |\n')
parts.append('''
## Searches and rejected leads

- Reused #226/#274’s expanded collector index, per-card face ledger, named 37-card two-player gap list and Hoth video-frame results. One additional currently blank Premiere two-player portrait brings the live total to 38. These older search records are historical evidence, not a claim that every seller was freshly revisited.
- Fresh [PSA gallery 127305](https://www.psacard.com/psasetregistry/starwarscollector-1/imagegallery/127305) yielded the original 2-1B photograph. Recovered nine more original JPEG candidates from the prior registry inventory; eight resolve stubs. Candidate six is **I'm On The Leader**, although its PSA holder says Evader. Its correctly named File and the corrected version-two source snapshot preserve that discrepancy; Evader remains unresolved.
- [SWCCG Store’s Japanese Monnok listing](https://www.swccgstore.com/SWCCG-Monnok-Jap-p/jap0363.htm) displays an English card: inspected and rejected. Retail category titles are not printing evidence. Japanese A New Hope category discovery did not supply the other missing faces.
- [Motti Seeker eBay lead](https://www.ebay.com/itm/175133384414) returned 403 directly; the documented VPS FlareSolverr route returned an ErrorPage with no image. No usable source was extracted; no persistent session was created.
- [CCG Obsession Japanese A New Hope catalog](https://ccgobsession.com/product_set.php?pi=79) returned menu/table headings without card items. Category One Games discovery and public searches did not recover edition-confirmed missing portraits; previous two-player SKU placeholders are retained as leads.
- Existing Hoth rare-box video was already frame-inspected in the earlier work and does not resolve the remaining A New Hope faces. No English image, another Japanese edition, artificial reconstruction, or marked seller portrait was substituted.

## Preservation and continuation

All ten newly uploaded originals are unchanged JPEGs, SHA-checked against the wiki and shared image backup. Both source snapshots and all ten wiki-image captures were replayed and byte-verified; retry logs retain the initial archive rate limits. Staging HTML was removed after verification. The corrected [nine-face snapshot](https://web.archive.org/web/20261113165759/https://swccg.com/snapshots/psa/japanese-nine-faces-369-v2.html) includes the original bytes and correct identities. The earlier mislabeled snapshot is retained in provenance, not used as the corrected citation.

Next useful evidence is an actual edition-confirmed face for one of the named rows. Recheck its native title, marker, subtype, printed text and all corner/icon statistics together; preserve the original and source capture, then publish with fresh revision guards. Seller contact has not been undertaken. The unresolved research is separate from the completed bounded audit; no claim is made that all Japanese cards are fully sourced.
''')
(root/'remaining-evidence.md').write_text(''.join(parts),encoding='utf8')
(root/'recommendations.md').write_text('''# Japanese integration recommendations

The shared Card template is now in use for all 793 Japanese cards and the oversized promotion (#287). The 469-card follow-up demonstrates why that needed to precede the remaining repairs: each new fact has one shared display path, and original images can be oriented without replacing their bytes.

1. **Make evidence state explicit per field.** Distinguish verified value, verified printed blank, inapplicable and unknown. A page with headings or a citation-only parameter should not count as transcribed. Keep a printing-specific source/field ledger and separate scan presence from full-face/edge quality. Leia’s blank box and EG-4’s star should not be completeness errors.
2. **Keep native text, literal translation and counterpart comparison separate.** Do not generate Japanese from English. Preserve unusual printed wording, repeated FX-7 lore and icon multiplicity. If a rules interpretation differs from a literal translation, label and source it separately. The physical face overrules seller and grading-holder labels, as the recovered I'm On The Leader photograph demonstrates.
3. **Use one verified record for article and checklist values.** A structured CardData or Lua record can later supply card infoboxes and set-list title/text/thumbnail cells. Start with a small sandbox pilot and compare output before a migration; do not create a second independently maintained Japanese database. Preserve established printing IDs, explicit counterpart/version links and edition-specific scans.
4. **Improve discovery without conflating printings.** Index native titles as aliases/search terms; when the same Japanese title belongs to several products, lead to a printing selector or disambiguation rather than silently merging their pages. Product, border, finish and text state remain explicit identity dimensions.
5. **Render verified symbols consistently.** Preserve repeated Pilot, Scomp and Nav Computer symbols; do not infer them from lore or permanent pilots. A shared icon renderer and typed stat schema should support creature Ferocity and special movement fields, preventing duplicate Power/Ferocity rows. The analogous English Dianoga/Wampa Power entries merit a separately scoped source check.
6. **Continue source acquisition separately from formatting.** The remaining 47 portraits and nine native stubs need physical evidence, not another template rewrite. Keep originals and archived sources, use display-only orientation, and track clean-portrait quality separately. No new deletions or card-identity renames are required by this audit; the wrongly named File was moved with a redirect.

#286’s shared set-symbol lookup/transparency work and #283’s CardMaker integration remain separate stories. This pass uses the existing explicit `set_icon` interface and does not claim either future integration is implemented. A later checklist-data pilot is a recommendation, not an unapproved bulk rewrite.
''',encoding='utf8')
(root/'README.md').write_text('''# Japanese card audit — #369

Completed bounded audit, 13 November 2026, following #287. Census: 469 printings; 252 card articles repaired, two set checklists updated. Ten original photographs preserved (nine newly resolve missing faces; one correctly identified additional photograph supports an existing card). The shared Card template gains optional display-only orientation for sideways originals; its default path preserves English output.

`verification-summary.json`, `source-verification.json` and `public-verification.json` record 485 live source checks and 268 changed public pages. All are reviewed, lint/Cite zero; ten uploaded image SHA1s match. Ghhhk and Hypo retain concurrent family-version edits, with all audit fields exact. Twelve final desktop/mobile screenshots, three old-revision examples and 50 identical English controls supplement these checks.

`coverage.csv`/`census.json` cover every printing; `remaining-evidence.md` names 47 missing faces and nine untranscribed cards. `recommendations.md` separates completed shared-template work from future data/discovery opportunities. `published-pages.md` links every changed page. Field readings, source manifests, before heads, guarded publication receipts and original-byte archive receipts are included. Re-running mutation scripts is unnecessary.

Publication source: [PR17](https://github.com/billbisco/swccg-wiki/pull/17). Story: [#369](https://github.com/swccg-guild/work/issues/369). Shared evidence: [evidence/369](https://github.com/swccg-guild/work/tree/main/evidence/369). Reproduction requires Python requests, beautifulsoup4, Pillow, mwparserfromhell; browser captures additionally require Playwright and Chrome. `census.py` runs offline; `verify.py` is read-only. Publishing/uploading requires the documented own bot credential on gemp, held in memory only. Preserve the directory layout in the authoring bundle.
''',encoding='utf8')
(root/'pr-body.md').write_text('''Japanese card articles had missing face-backed fields after their shared infobox migration. This completes the 469-printing audit: repairs 252 cards, updates the A New Hope/Hoth checklists, preserves ten original JPEGs, and adds optional display-only image orientation to the shared Card template. Existing English rendering follows the unchanged default branch.

Verified additions include nine newly recovered faces and native text/translations, 180 previously unrecorded uniqueness values, 86 icon rows, location Force icons, creature Ferocity/special movement corrections and explicit printed blank game boxes. The PSA photograph labeled Evader actually depicts I'm On The Leader; the File was moved with a redirect and Evader remains unresolved.

Validation: 485 current source/review/lint checks; 268 anonymous public pages current and Cite zero; ten original image hashes; twelve final desktop/mobile captures plus three before examples; 50 English controls identical. Ghhhk and Hypo retain concurrent family-version edits; every audit field still matches. Source snapshots and ten image captures are byte-verified, and original files are backed up unchanged.

The dated census names the remaining 47 missing faces (38 Premiere two-player, nine A New Hope) and nine native stubs. Existing transcriptions have not received blanket linguistic certification. Reports, guarded tools, readings, source manifests and exact live source backups are included under `authoring/japanese_other369/`; integration recommendations remain separately scoped.

Refs swccg-guild/work#369. Evidence: https://github.com/swccg-guild/work/tree/main/evidence/369
''',encoding='utf8')
print('Coverage, source limits, recommendations and completion artifacts generated')
