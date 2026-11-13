import json
from pathlib import Path

root=Path(__file__).parent
rows=json.loads((root/'drafts.json').read_bytes())
simple=[r for r in rows if r['layout']=='simple']
rich=[r for r in rows if r['layout']=='template-look']
samples=[]
for key in ['Hoth (Japanese)','A New Hope (Japanese)','Premiere Introductory Two-Player Game (Japanese)','Empire Strikes Back Introductory Two-Player Game (Japanese)']:
    samples.append(next(r['title'] for r in simple if r['set']==key))
samples.append(next(r['title'] for r in simple if r['title'] not in samples))
samples += ['2X-3KPR (Tooex) (Japanese)','BoShek (Japanese)','Alderaan (Japanese)',next(r['title'] for r in rich if r['set'].startswith('Reflections II:')),next(r['title'] for r in rich if not r['is_ja'])]
assert len(samples)==10 and len(set(samples))==10
(root/'sample-titles.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2),encoding='utf8')
final=samples+[next(r['title'] for r in rich if r['set'].startswith('Reflections III:')),'Tonnika Sisters (Japanese)']
(root/'final-sample-titles.json').write_text(json.dumps(final,ensure_ascii=False,indent=2),encoding='utf8')
task='''## User story
As a wiki reader, I want the preserved citation/style defects in #287's migration baseline resolved, so the rebuilt pages finish with functioning references and zero style flags.

## Requirements
- Resolve the remaining oversized promo's unpreserved BoardGameGeek citation and caption/style flags, without changing quoted card text or historical claims.
- Restore the 25 existing undefined `photo` citations to their existing printing-specific File pages while preserving native text and all old reference uses. Record these additive repairs in the migration report.
- Preserve every old reference/source URL; verify any newly added preservation replay. Recheck the fresh baseline and do not act on #287's obsolete 35-page count.

## Acceptance criteria
- [ ] AC1 Current baseline/backlog is saved and reconciles one remaining style-failing page plus 25 pre-existing undefined photo references.
- [ ] AC2 All baseline failures are repaired and final render has zero Cite errors; native text, card data and source links remain intact.
- [ ] AC3 Final style lint is zero on the complete #287 target set; archive verification, diffs and public reviewed output are linked.
- [ ] AC4 A PASS-REPORT and merged backup accompany completion; #287 links this Task's report before closing.

## Plan
Capture the fresh baseline, restore unambiguous File-backed photo definitions as part of the conservative converter, complete the structural rebuild, then repair the oversized promo's remaining style/archive flags immediately afterward. Check all final renders/lint and save evidence under this Task and #287. Wiki sandbox previews stand in for Test; production is wiki.swccg.com.

## Authorization / open questions
No open questions. #287 R8 records Bill's D7 authorization for the migration followed immediately by baseline lint repairs. Bill now explicitly directs ChatGPT to proceed with that migration-first plan. Scope is citation/style repair, not retranslation or gameplay edits.

MemoryCoreChatGPT
'''
(root/'followup-story.md').write_text(task,encoding='utf8')
(root/'followup-story.json').write_text(json.dumps(dict(title='Task: Resolve Japanese infobox migration citation/style backlog (#287)',body=task,type='Task',assignees=['MemoryCoreChatGPT2'])),encoding='utf8')
(root/'design-log.md').write_text('''# #287 — Shared card infobox migration

## 2026-11-13 — Migration first; preserve legacy data without interpretation

**Decision.** Bill approved the recommended sequence: shared infobox migration first, remaining Japanese-set content repairs afterward, with source/scan research allowed alongside. The shared skill records this order. ChatGPT takes the unstarted Ready story from its queued Alpha1 assignment under Bill's explicit direction.

**Why.** The refreshed 794-page inventory contains 43 simple layouts and 751 template-look layouts with many additional metadata labels. A printing's native text, editorial translation and source evidence are separate data. Existing fields need to survive structural rebuilding without silent correction or English substitution.

**Interface.** Implement #287's optional language/native/translation and edition fields. Add narrowly scoped conservation hooks for existing navigation, nonstandard leads, legacy type/set displays, row-label aliases, image notes, additional metadata/sections and the non-set oversized promo's original categories. All standard Template:Card defaults retain their old branches; English controls must render identically. These hooks preserve old values in the shared table rather than retaining a per-page hand-made infobox. The promo's Size/Year become ordinary optional metadata rows.

**Alternatives.** Reject a separate Japanese template, dropping irregular legacy fields, moving translations below References, or rewriting incomplete text during migration. Keep redundant legacy Versions data where it already exists; record it for later content reconciliation instead of choosing a new identity during conversion.

**Baseline defects.** The #361 repairs reduce the old 35-page style backlog to one oversized promo. Baseline render checks also reveal 25 pre-existing undefined `photo` references, all pointing at existing matching Premiere card images. Restore those definitions additively and track them under the required citation/style follow-up Task. Keep native prose unchanged.

**Verification.** Capture all 794 old rendered pages and 50 deterministic English controls before touching the template. Check 10 initial sandbox samples (5 per old layout), all-page content/link/file/reference/category conservation, 12 final product/layout examples, unchanged English HTML, guarded section-zero writes, supported scoped reviews and public output. Do not claim full linguistic or scan-edge verification from a structural migration.

**Who / status.** Bill authorized execution in chat; MemoryCoreChatGPT implements #287. Set-icon asset/lookup work stays on #286; content audits resume after the shared structure is verified.
''',encoding='utf8')
(root/'README.md').write_text('''# #287 — Japanese/shared card infobox migration in progress

Bill authorized migration first, then remaining Japanese-set content repairs. Shared guidance: ai-team-skills commit 426db52.

Current scope: 794 live manual infoboxes (793 Japanese plus the oversized English promo), captured after #361. No card article or production Template:Card has yet been changed for this migration.

Inputs: heads-before.json, before-renders.json.gz, targets.json, english-sample.json, baseline-summary.json, lint-backlog.csv. Converter: convert.py. Optional template extension: template.py / template-draft.wiki. Publication must use exact current revision/hash and timestamps; never replay old packets over a newer revision.

The draft preserves native sections and existing metadata/navigation. Old undefined photo references are restored from their existing printing-specific File pages and separately recorded. Further translation, statistics or identity repairs belong to the later content pass. The follow-up Task completes the original style backlog immediately after rebuilding.

Next: publish only Template:Card/sandbox, render the 10 initial samples and 50 English controls, fix conservation failures, then validate all 794 drafts before touching the production template or cards.
''',encoding='utf8')
print('Ten initial samples, twelve final fixtures, follow-up Task and design log prepared')
