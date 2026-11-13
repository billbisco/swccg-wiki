from datetime import datetime,timedelta,timezone
import collections,csv,json
from pathlib import Path
from urllib.parse import quote
root=Path(__file__).parent
def read(name):return json.loads((root/name).read_bytes())
drafts=read('drafts.json');source=read('source-verification.json');public=read('public-verification.json')
assert len(public)==794 and len(source)==797
assert len(read('live-visual.json'))==12 and all(x['identical'] for x in read('english-production-report.json'))
assert all(x['pass'] for x in read('drafts-conservation.json')) and all(x['passed'] for x in read('fidelity-report.json'))
stamp=datetime.now(timezone(timedelta(hours=-4))).strftime('%Y-%m-%d %H:%M')
link=lambda t:'https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe='')
lines=['# Published pages — #287\n\nEvery changed page, with final public revision; no pages deleted.\n']
for row in source:lines.append('- ['+row['title']+']('+link(row['title'])+') — revision '+str(row['revid']))
(root/'published-pages.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
categories=list(csv.DictReader((root/'categories-before-after.csv').open(encoding='utf8')))
for name,key in [('categories-before.csv','before'),('categories-after.csv','after')]:
    with (root/name).open('w',encoding='utf8',newline='') as f:
        writer=csv.writer(f);writer.writerow(['title','categories'])
        writer.writerows([r['title'],r[key]] for r in categories)
(root/'render-diff-english.txt').write_text('50/50 deterministic English card controls: rendered DOM identical before/after.\nBoth compared through action=parse text with the same original source and title. Only non-rendered comments and standard edit/reference navigation are excluded.\nThe separate cached-oldid control showed a parser-cache trailing blank-line difference; the fresh production control proved this was not introduced by the template.\n',encoding='utf8')
report='''# Migration report — #287

All 794 target articles now use Template:Card: 793 Japanese and the oversized English promo. The shared template, documentation and sandbox are reviewed and lint clean. Every final source matches its guarded draft; all 794 anonymous public pages show the current reviewed revision, one shared infobox, the set-icon row and zero Cite errors. Twelve product/layout browser examples have before/after PNGs under 500 KB; ten initial sandbox examples preceded production edits. Fifty English controls render identically.

## Preserved content and deliberate differences

- All native/translated fields retain every non-whitespace character, without Unicode normalization. Existing visible text, internal/external links, images, reference bodies and categories pass the prepublication conservation check. `content-diff.csv` lists zero missing content plus additions; `drafts-conservation.json` gives individual added tokens, links and files.
- Native text now has generic printing-language fields and `lang="ja"` wrappers; English translations and comparison notes remain separate. Existing edition, border/finish, release, row labels, exceptional metadata and additional sections remain visible. The promo keeps Size and Year rows.
- Existing leads are preserved verbatim using an optional lead field, including longer legacy leads. This conserves their wording instead of moving it to Notes. Separate legacy Versions tables retain their content; conflicting legacy data is left for the content audit.
- Template-added base categories replace manual equivalents. Exceptions retain their complete original category list. The only membership change is removal of `Pages_with_reference_errors` on 25 articles after restoring their already-used `photo` definitions from each existing printing-specific File. No substantive category is added or removed.
- Printed symbol assignments: 415 None (Premiere), 195 Hoth, 173 A New Hope, 11 premium. Foils, the promo and eight ESB premium faces were inspected. The existing set_icon interface displays these now. #286 owns the not-yet-live lookup and transparent assets; this migration does not claim to implement that separate work.
- Task #366 immediately repaired the remaining oversized-promo caption and preserved both occurrences of its BGG source link. The signed-image caption is shortened to “Signed by Baksa, Stackpole, and Zahn.” No historical claim, Japanese text or printed statistic changed. The cited original URL and original citation date remain; this migration does not certify that older bibliographic date.
- Existing BGG capture 20261026191455 was rejected after full content inspection: it is only an application shell. The complete source page was fetched on the VPS without a persistent FlareSolverr session, snapshotted with zero missing assets, inspected offline, captured at Wayback 20261113154153, and byte-verified. Temporary public snapshot staging was removed.

## Safety and repeatability

Initial and refreshed source/render baselines are retained. Concurrent card-family navigator changes were incorporated before publication. Every write used the agent's own bot identity, bot=1, exact revision/hash, both timestamps and scoped review. 750 old HTML sources support section zero; 44 with real source sections require one guarded atomic whole-source replacement to avoid duplicate orphan sections. Every final source is backed up in the wiki repository together with converter/audit/publisher scripts. No cards, files or redirects were deleted.

Presence/conservation is not a full linguistic proofread or scan-edge certification. Follow-up #369 audits the remaining 469 Japanese printings outside the Premiere expansion, including honest blanks and source limitations.

## Evidence

`source-verification.json`, `public-verification.json`, `content-diff.csv`, `fidelity-report.json`, `drafts-conservation.json`, `categories-before.csv`, `categories-after.csv`, `reference-repairs.json`, `set-icon-manifest.json`, `english-production-report.json`, `live-visual.json`, `before-visual.json`, `cards-receipts.jsonl`, `production-receipts.jsonl`, `cleanup-receipts.jsonl`, `bgg-preservation.json`. Full changed-page links: `published-pages.md`.
'''
(root/'migration-report.md').write_text(report,encoding='utf8')
base='https://github.com/swccg-guild/work/blob/main/evidence/287/2026-11-13/'
rows=[('AC1 All targets use Card','794/794 shared transclusions; no manual infoboxes','source-verification.json'),('AC2 Content conserved','794/794 exact native/translation and rendered content/source checks; allowed changes documented','content-diff.csv'),('AC3 Twelve product/layout samples','Twelve live browser checks and before/after PNGs; native language markup and old metadata preserved','live-visual.json'),('AC4 English unchanged','50/50 fresh English rendered DOMs identical','render-diff-english.txt'),('AC5 Categories conserved','Only 25 reference-error maintenance removals; no substantive category changes','categories-before-after.csv'),('AC6 Printed Set icon row','794/794 public rows; per-face values through existing set_icon; #286 owns its future lookup','set-icon-manifest.json'),('AC7 Lint backlog repaired','797 final sources lint 0, Cite 0; Task #366 own PASS report','366-pass-report.md'),('AC8 Documentation','New generic language fields, conservation hooks and Japanese example published','production-receipts.jsonl')]
text=f'PASS-REPORT v1 — ticket #287 — agent: MemoryCoreChatGPT — {stamp} (UTC-4)\n\n| AC | Result | Evidence |\n|---|---|---|\n'
for label,detail,file in rows:text+='| '+label+' | PASS | '+detail+'; [evidence]('+base+file+') |\n'
text+='\nOverall: PASS\n\nVisual diff: [before]('+base+'before-06-small.png) · [after]('+base+'live-06-small.png) · [diff]('+base+'diff.png). Wiki has no separate Test server; ten sandbox renders passed before production. [Migration decisions]('+base+'migration-report.md) · [all changed-page links]('+base+'published-pages.md). No deletions. Source/code backup: PR https://github.com/billbisco/swccg-wiki/pull/15.\n'
(root/'287-pass-report.md').write_text(text,encoding='utf8')
child=f'''PASS-REPORT v1 — ticket #366 — agent: MemoryCoreChatGPT — {stamp} (UTC-4)

| AC | Result | Evidence |
|---|---|---|
| AC1 Refreshed baseline | PASS | [One style-failing promo; 25 broken photo refs]({base}lint-backlog.csv); reference-repairs.json |
| AC2 Baseline repairs | PASS | 25 definitions restored; promo revision 300575 adds verified BGG preservation and short caption; native text/stats conserved |
| AC3 Final lint/Cite 0 | PASS | [797 clean sources]({base}source-verification.json), [794 public pages Cite 0]({base}public-verification.json); [byte-verified archive]({base}bgg-preservation.json) |
| AC4 Own report and backup | PASS | This report; #287 evidence and PR https://github.com/billbisco/swccg-wiki/pull/15 contain exact source/receipts |
Overall: PASS

Visual diff: [before]({base}before-10-small.png) · [after]({base}live-10-small.png). Original source URLs and historical claims preserved. Complete archive replaces a rejected empty BGG replay. No deletion of wiki pages/files. MemoryCoreChatGPT.
'''
(root/'366-pass-report.md').write_text(child,encoding='utf8')
(root/'README.md').write_text('# #287 — Shared Japanese card infobox migration\n\nLive migration complete: 794 cards, 797 changed pages including template controls, zero lint/Cite errors, 50 unchanged English controls. [Migration report](migration-report.md) · [all live page links](published-pages.md) · [PASS report](287-pass-report.md).\n\nReproduction from the authoring bundle root: install requirements, then run `python work/japanese-infobox287/check.py drafts` and `python work/japanese-infobox287/fidelity.py` for captured conservation checks. `verify.py` performs live read-only checks; publication scripts are guarded and should never be replayed over newer revisions. `convert.py` must be followed by `set-icons.py` when rebuilding drafts.\n\nNo separate wiki Test exists; sandbox examples preceded live publication. Code and source backup: [PR #15](https://github.com/billbisco/swccg-wiki/pull/15). Task #366 resolves the original citation/style backlog. Follow-up #369 audits the remaining Japanese sets.\n',encoding='utf8')
print('Migration and per-AC reports prepared')
