import json,re
from pathlib import Path
root=Path(__file__).parent;p=json.loads((root/'completion-progress.json').read_bytes());c=p['counts'];heads=json.loads((root/'published-heads.json').read_bytes());drafts=[]
for f in root.glob('batch*-new-packet.json'):
    if not (root/(f.name.replace('-new-packet.json','-new-receipts.jsonl'))).exists():drafts.extend(r['title'] for r in json.loads(f.read_bytes()))
text=f'''# Story 381 — publication progress, 14 November 2026

The initial census reconciled 314 regular foil slots: 114 Reflections I, 100 Reflections II, and 100 Reflections III. Sixteen articles existed initially and 298 English articles were initially missing. Current delivery: {c['created']} newly completed and fully verified; {c['published_pending_batch_verification']} additional new articles live with full-batch work pending; {c['draft_prepared_awaiting_preservation']} new article drafts prepared but not published; one additional existing article discovered and awaiting integration audit; {c['missing']} further articles not yet drafted. The entire story remains unfinished.

## Verified delivery

Seven batches of ten passed exact source, style lint, supported review, public current revision/Cite, reciprocal navigation, source conservation, original-image hash, source/archive and representative desktop/mobile checks. All seventy full-resolution wiki-original image versions have byte-verified Wayback captures and File-page Preservation links. The Vader shared navigator was retained and propagation checked on its existing members. Every changed backed-up page is linked in [published-pages.md](published-pages.md): {len(heads)} distinct pages.

The eighth batch's ten new articles, ten File descriptions/original binaries, ten signed Talk notes, and direct checklist links are live and checked (31 pages, exact source/review/public/Cite/image SHA). Its 45 family drafts are not saved yet: some inherited citations need the blocked primary snapshot. Its ten wiki-original image captures are pending. This partial check is explicitly not the whole-batch PASS file.

## Prepared work

All 113 initially missing Reflections I physical faces have been independently read. Batches 9–11 supply the final 33 unsaved Reflections I drafts; all have zero style/Cite flags and intact shared Card previews. Batch12 has nine new Reflections II drafts plus an independently read existing Don't Get Cocky foil to reuse; batch13 has ten more. New Reflections II drafts pass the same lint/template preview checks. No unverified gameplay IDs are assigned. Discovery/OCR alone is not approved transcription.

Printed differences remain distinct from later errata. The Redemption punctuation was checked against a second complete SWCA photograph and corrected to “have been modified”; no separate misprint is asserted. Locations retain side-specific text/Force icons, and named creature statistics and symbolic values remain explicit. Unpublished Light twin names and Artoo-Detoo were normalized before creation; the initial inventory is unchanged historical evidence. Existing card-family roots use their actual current titles (the two Death Star base pages use different expansion qualifiers).

## Preservation blocker and exact recovery

Wayback GET saves from the VPS and Bill's PC returned HTTP520 / “Job failed”. The public POST route returned HTTP429 explicitly identifying automated-traffic throttling; submissions were stopped. The documented authenticated VPS route returned HTTP401. No credentials were exposed. The old working captures remain recorded; current failures are not marked verified. Exact pending image versions and the retained source snapshot are queued in the source PR; no archive URL is invented. Original photographs are backed up in swccg-wiki-files.

Next publication step after archive recovery: capture and verify batch8's primary snapshot, repair/preview/publish its 45 family drafts, obtain byte-matching captures of its ten wiki originals, add File Preservation links and run full verify-batch.py batch8. Then publish prepared batches9–13 through the guarded pipeline, re-fetching current heads. Draft-only image identity packets intentionally cannot be uploaded: regenerate complete packets with upload-batch.py only after verified source snapshots exist. Inspect remaining II/III faces while publication is pending. Do not replay old revision guards against newer pages.

Retained VPS files: /opt/swccg-res/snapshots/psa/reflections381-batch8-primary-sources.html and reflections381-batch8-wiki-originals.html. Do not delete them without a checked capture. Gallery capture is an optimization only; every original binary still requires independent comparison. No deletion of wiki articles is required.

[Story #381](https://github.com/swccg-guild/work/issues/381); [source PR18](https://github.com/billbisco/swccg-wiki/pull/18); [shared evidence](https://github.com/swccg-guild/work/tree/main/evidence/381).
'''
last=max(int(re.match(r'batch(\d+)',f.name)[1]) for f in root.glob('batch*-new-packet.json'))
text=text.replace('batches9–13','batches9–'+str(last)).replace('batches 9–13','batches 9–'+str(last))
text=re.sub(r'Batch12 has nine new Reflections II drafts.*?No unverified gameplay IDs', 'The prepared Reflections II drafts now cover all remaining missing faces. Each has zero style/Cite flags and an intact shared Card preview. The additional existing Don’t Get Cocky article is retained for integration audit. No unverified gameplay IDs',text)
(root/'current-batch-report.md').write_text(text,encoding='utf8')
delivery=f'''## Current delivery

Inventory: 314 regular foil slots (114/100/100). Sixteen articles existed initially. Of the 298 initial gaps, {c['created']} new articles are fully completed and verified, ten more are live with preservation/family completion pending, {c['draft_prepared_awaiting_preservation']} have unsaved lint-clean/template-previewed drafts, and one additional existing article has been found for reuse. {c['missing']} more remain to draft. The story remains In Progress; AC2–AC5 are not yet met.

All 113 initially missing Reflections I faces have been read. Completed batches retain exact physical text/stats/icons, original photographs, byte-verified wiki-image captures, supported reviews, direct checklist links, reciprocal family navigation, source conservation and public/visual checks. The latest live batch's published subset was independently checked without falsely marking the full batch complete. Source originals for all remaining cards are backed up. No article deletion is required.

Current external blocker: Wayback GET saves returned520; its public POST returned429 explicitly throttling automated traffic, so submissions stopped. The documented authenticated VPS route returned401. Uncaptured staging files remain and exact image versions are queued. No credential change or approval is required from Bill to continue ordinary work. Next publication step after archive recovery: finish batch8's inherited-source snapshot,45 family links,10 wiki-original binary captures and File links, then its full QA; continue prepared batches9–13 and remaining II/III physical readings. Do not count drafts, queue acceptance or published-only pages as complete.

[Inventory, field evidence, current report and all changed-page links](https://github.com/swccg-guild/work/tree/main/evidence/381). [Source PR18](https://github.com/billbisco/swccg-wiki/pull/18). [Detailed current report](https://github.com/swccg-guild/work/blob/main/evidence/381/current-batch-report.md).
'''
delivery=delivery.replace('batches9–13','batches9–'+str(last))
live=(root/'story-live.md').read_text(encoding='utf-8-sig');assert live.count('## Current delivery')==1
(root/'story-current.md').write_text(re.sub(r'## Current delivery\n.*',lambda m:delivery,live,flags=re.S),encoding='utf8')
readme=(root/'README.md').read_text(encoding='utf8');match=re.search(r'First verified batch:|\d+ new articles completed',readme);assert match
(root/'README.md').write_text(readme[:match.start()]+f"{c['created']} new articles completed and verified; ten more live/pending; {c['draft_prepared_awaiting_preservation']} unsaved drafts. Whole story remains In Progress. See current-batch-report.md and completion-progress.json. Original sources live in swccg-wiki-files; draft-only image packets are not upload packets. Never claim pending image captures verified or replay obsolete revision guards.\n",encoding='utf8')
print(len(heads),'live pages backed up;',len(drafts),'unsaved drafts; current report and story body prepared')
