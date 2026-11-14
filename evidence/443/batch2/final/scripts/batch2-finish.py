from b2common import *
from urllib.parse import quote
proof=read('live-proof.json');browser=read('browser-checks.json');assert browser['result']=='PASS'and read('rollback-probe.json')['activation_restored']=='PASS';assert proof['exact_live_revisions']==53 and proof['all36_originals_checked']
def url(t):return'https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe="():/'")
lines=['# Story 443: Original Virtual Set1 cohort delivery','', 'All changed pages, independently checked against the exact saved revisions:','']
for r in proof['pages']:lines.append('- ['+r['title']+']('+url(r['title'])+') — revision '+str(r['revision']))
(B/'published-pages.md').write_bytes(('\n'.join(lines)+'\n').encode())
review='''# Own review: Original Virtual Set 1 rollout and primary image credits

MemoryCoreChatGPT, 14 November 2026. Bill approved the remaining nine after the three examples, and explicitly clarified Archive.org reading/downloads are allowed; uploads and Save Page Now remain paused.

Delivered the twelve actual later English PC-E2 publication articles, retained the three review examples and updated their hub. Eight unchanged historical GIF uploads join the four already present. All 36 image File descriptions now identify the source role: historical PC composite or recovered Holotable member, original archived publisher PDF/slip, and pinned CardMaker reconstruction recipe. Eleven full-card payloads match the 2007 PC archive index digests. Three image replays have checked actual payload receipts (including retained #419 checks); the others still need replay verification after read rate limits. Sai'torr has no identified individual PC GIF capture and honestly cites the exact recovered distribution image plus the original archived PDF. Do not convert an index digest match into a claim of replay verification. Source credits and preservation of the wiki upload are separate.

All nine additional historical faces, remasters and publisher slips were visually compared for title, lore, game text, uniqueness, statistics and printed icons. ▲/▼, pilot values and immunity symbols were checked, not silently expanded into another text state. Existing article gameplay text, card IDs, errata histories and Versions navigation were conserved. Source bullets were consolidated rather than duplicated. The source PDF has two pages; all twelve slips are on page2. No remaster or original image bytes were changed.

| Story AC | Cohort result / remaining global scope |
|---|---|
| AC1 | All12 actual articles pass desktop1440/phone390 geometry, card→slip→26px desktop/36px phone pair→Info. Decipher/other sets remain future work. |
| AC2 | 15 behavior tests cover eligibility and failure matrix; this cohort contains12 visually audited matching pairs. Other single/missing/mismatched inventories remain outside this delivery. |
| AC3 | Twelve explicit state/language mappings, canonical-content conservation and36 exact original hashes/timestamps/bytes pass. No other publication or language substituted. |
| AC4 | Guest saved defaults and per-card isolation pass across navigation/reload in both live contexts. Native account/private-cache behavior reused from the unchanged tested preference implementation. Real human cross-device/sign-in transitions remain future coverage. |
| AC5 | Existing fallback fixtures pass; actual rollback to prior cohort preserves native content and restores exact manifest. |
| AC6 | Actual French interface with English card text/image and translated button click passes. The first generated test incorrectly decoded UTF-8; that failure receipt is retained, builder corrected and French check rerun in a fresh isolated browser. No app bug or translated-card rollout was invented. |
| AC7 | All24 live desktop/phone card checks, keyboard, selected semantics, stable stage/slip/text and no overflow pass. Shared thumbnail/hover resolution remains future work. |
| AC8 | Source PR58 merged/deployed;53 exact live revisions and52 required stable reviews verified;36 originals rechecked; actual rollback passed. Strict raw ARCHIVE31/non-ARCHIVE0; exact pending-publication gates pass, external preservation remains unfinished. |

Own source review found no unresolved cohort issue. Application change is only the16-title allowlist/twelve-card mapping and rollout documentation; engine, preference code, shared Card/Versions templates and site configuration are unchanged. SHA-bound backup packets are independently read back, with the final live revision backup separate from drafts. API edits were own-bot, revision guarded, bot=1; upload descriptions and stable reviews checked. File origins are linked directly from cards and File pages, with copies labeled by role. No desktop capture/input used; isolated browser closed. No active own jobs remain after evidence publication. Do not replay already-applied drafts.

Whole Story443 remains open: other Original sets and Decipher inventory, set-thumbnail/hover preference integration, real translated-card and cross-user/device coverage are unfinished. No archive upload or saver restart occurred. #382 owns broader inventory/preservation; this is a36-file provenance correction, not a claimed whole-wiki structural repair.
'''
(B/'own-review.md').write_bytes(review.encode())
save('cohort-results.json',{'ticket':443,'cohort':'Original Virtual Set1 PC-E2','cohort_result':'PASS','cards_enabled':12,'newly_audited_cards':9,'changed_wiki_pages':53,'required_stable_reviews_verified':52,'exact_image_versions_verified':36,'source_pr':58,'source_merge':'e8bedfd7ed9931d37477e0fb6dbd21c9ce9d244b','behavior_tests':15,'desktop_and_phone_checks':24,'French_check':'PASS','rollback':'PASS','raw_archive_findings':31,'non_archive_findings':0,'archive_uploads':0,'archive_reads_allowed':True,'external_preservation_complete':False,'whole_story_complete':False,'active_jobs':[]})
names=['own-review.md','cohort-results.json','published-pages.md','source-accuracy.json','inventory.json','recipes.json','archive-checks.json','preview-checks.json','live-proof.json','live-backup-receipts.json','browser-checks.json','browser-checks-failed-label.json','deploy.json','cache-purge.json','rollback-probe.json','backup-image-source-assets.json','backup-drafts-sources-r2.json','backup-deduplicated-drafts.json','backup-exact-live.json','uploads-r3-manifest.json','uploads-r3-approval.json','pages-manifest.json','pages-approval.json','pages-registry-export.json','uploads-r3-registry-export.json','new-upload-originals-registry.json']
names += [x.name for x in B.glob('pages-*.report.json')]+[x.name for x in B.glob('uploads-r3-*.report.json')]+[x.name for x in B.glob('headless-*.jpg')]
files={'evidence/443/batch2/final/'+n:(B/n).read_bytes()for n in names}
for x in ROOT.glob('batch2-*.py'):files['evidence/443/batch2/final/scripts/'+x.name]=x.read_bytes()
for n in['b2common.py','batch2-browser.cjs','batch2-language-check.cjs']:files['evidence/443/batch2/final/scripts/'+n]=(ROOT/n).read_bytes()
evidencepin=pin('billbisco/swccg-wiki','final-evidence',files);save('final-index.json',{'evidence':evidencepin['repository']+'/tree/'+evidencepin['commit']+'/evidence/443/batch2/final','live_backup':'https://github.com/billbisco/swccg-wiki/commit/'+read('backup-exact-live.json')['commit'],'images':'https://github.com/billbisco/swccg-wiki-files/commit/'+read('backup-image-source-assets.json')['commit']})
shared={n:data for n,data in files.items()if n.split('/')[-1]in['own-review.md','cohort-results.json','published-pages.md','browser-checks.json','rollback-probe.json','headless-fusion-light-mobile-original.jpg','headless-gold1-desktop-remastered.jpg','headless-saitorr-mobile-remastered.jpg','headless-boshek-french-ui.jpg']}
shared['evidence/443/batch2/final/final-index.json']=(B/'final-index.json').read_bytes()
path='docs/design-log/443-wiki-image-rendition-rollout.md';current=gh('repos/swccg-guild/work/contents/'+path+'?ref=main');old=base64.b64decode(current['content'])
entry='''

### 2026-11-14 — expand the approved cohort and repair primary image credits
- **Decision:** Bill approved the remaining nine after reviewing the three examples. Enable all twelve actual later English OVS1 PC-E2 articles, retain the three samples and update their hub; leave other sets, set thumbnails and hover resolution outside this cohort.
- **Source correction:** Link historical PC image captures/archived original PDF and pinned reconstruction recipes directly, separately from wiki copies and independent backups. Eleven payloads match PC archive index digests; index equality is not replay verification. Sai'torr has no identified individual GIF capture, so cite its exact recovered Holotable member and archived PC slip. Correct duplicate source bullets and PDF page location. This scoped36-File repair does not claim the whole-wiki structural source task is done.
- **Policy correction:** Bill explicitly meant NO UPLOADS to Archive.org. Viewing, downloading and historical searches are allowed. Preserve saver/timer/authentication safeguards; pending metadata/backup is not an external capture. Updated registry continuations and Story443 supersede older all-request wording.
- **Verification:** 15 behavior tests;24 desktop/phone card checks; real French UI/English card. A generated test's UTF-8 decoding fault was fixed without app changes and its failed receipt retained.53 exact live revisions,52 required stable reviews and36 exact image payloads pass. Raw ARCHIVE31/non-ARCHIVE0, hash-bound pending-publication gates pass. Actual prior-cohort rollback and exact restore pass. PR58 merged at e8bedfd7ed9931d37477e0fb6dbd21c9ce9d244b; allowlist asset only, no server configuration or shared template edit.
- **Status:** Approved OVS1 cohort delivered; Story443 stays open for wider era/consumer/language/device scope. No active jobs after evidence publication. No archive uploads or desktop control.
- **Who:** Bill directs; MemoryCoreChatGPT implements and verifies.
- **Evidence:** '''+evidencepin['repository']+'/tree/'+evidencepin['commit']+'/evidence/443/batch2/final\n'
shared[path]=old+entry.encode();work=pin('swccg-guild/work','shared-final',shared);print(json.dumps({'source_evidence':evidencepin['commit'],'shared_evidence':work['commit'],'files_readback':len(files)+len(shared)}))
