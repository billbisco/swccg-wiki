import json,re
from pathlib import Path
root=Path(__file__).parent
live=(root/'story-live.md').read_text(encoding='utf-8-sig');progress=json.loads((root/'completion-progress.json').read_bytes());created=progress['counts']['created'];remaining=progress['remaining_to_complete']
delivery=f'''## Current delivery

The dated inventory reconciles 314 regular pack foils: 114 Reflections I, 100 Reflections II and 100 Reflections III. Sixteen articles existed initially; {created} of the 298 missing English articles have now been completed and verified, leaving {remaining}. All remaining source photographs have been retrieved and backed up; discovery photographs and OCR are not approved transcriptions until each physical face has been read.

Completed batches have independently transcribed text/stats/symbols, unchanged original photographs, version-specific wiki-original binary captures and File-page replay links, reviewed sources, direct checklist targets, reciprocal family navigation, source conservation and anonymous public/desktop/mobile checks. The existing shared Darth Vader navigator now includes the foil, and all eleven existing member pages were checked for propagation. Source differences and symbolic values are retained; no unverified playable mappings are asserted.

Next: continue complete physical-reading/publication batches. The sixth batch's ten starship faces have been read and its source-photo preservation is underway. Rarity and release facts use explicitly credited collecting references; printed data comes from physical card faces. No article deletion is required by the completed work. The source PR and whole story remain In Progress.

[Inventory, field evidence, verification and all changed-page links](https://github.com/swccg-guild/work/tree/main/evidence/381). [Source PR18](https://github.com/billbisco/swccg-wiki/pull/18). [Detailed batch report](https://github.com/swccg-guild/work/blob/main/evidence/381/current-batch-report.md).
'''
assert live.count('## Current delivery')==1
new=re.sub(r'## Current delivery\n.*',delivery,live,flags=re.S)
(root/'story-current.md').write_text(new,encoding='utf8')
readme=(root/'README.md').read_text(encoding='utf8');match=re.search(r'First verified batch:|\d+ new articles completed',readme);assert match;start=match.start()
readme=readme[:start]+f'{created} new articles completed and verified so far; {remaining} initially missing articles remain. See current-batch-report.md, completion-progress.json and published-pages.md. The story remains In Progress. Do not replay old guarded packets against newer sources. Source-photo originals for all remaining cards are backed up; OCR remains an unapproved reading aid. Shared file-payload JSON omits base64 image data; restore originals from the image repository and use upload-batch.py STAGE --prepare to regenerate it.\n'
(root/'README.md').write_text(readme,encoding='utf8');print(created,'verified new articles;',remaining,'remain')
