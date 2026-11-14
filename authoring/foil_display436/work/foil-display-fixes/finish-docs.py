import json,hashlib,datetime
from pathlib import Path
from urllib.parse import quote
p=Path(__file__).parent
queue=[]
for title,h in json.loads((p/'published-heads.json').read_bytes()).items():
    r=h['revisions'][0];text=r['slots']['main']['content'];queue.append(dict(title=title,revid=r['revid'],url='https://wiki.swccg.com/index.php?title='+quote(title.replace(' ','_'),safe=':(),')+'&oldid='+str(r['revid']),exact_source_sha256=hashlib.sha256(text.encode()).hexdigest(),source_backup_container='published-heads.json',state='held; no Archive.org requests permitted',owner_followup='swccg-guild/work#412',original_image_version_changed=False))
(p/'preservation-queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf8')
(p/'design-log.md').write_text('''# Bug436 — design and verification record

Bill requested correcting Reflections orientations and holder framing, fixing giant inline table symbols, and filing a general transparent WebP printed-symbol story. Story435 is Backlog and linked to existing Story286; this delivery addresses the immediate display defects under436. No printed glyph pixels are invented or replaced.

All314 regular foil mappings audited. The215 holder photographs comprise214 uploads and the pre-existing Luke Skywalker File. Measured original-pixel rectangles were visually reviewed on nine contact sheets plus manual exceptions. Complete card borders/text are retained. Two perspective photos use conservative CSS polygons to remove external holder background. The helper clips and rotates the existing MediaWiki thumbnail; no historical source or uploaded File is modified. Every framed display links explicitly to its original File page.

Rebel Leadership needs clockwise rotation because the MediaWiki thumbnail loses EXIF orientation6. The four reported Light Side sites need clockwise rotation judged by artwork and the owning side's text. Rendezvous Point is already an upright portrait System and loses its erroneous left rotation. Executor, Flagship Executor and Yavin4 keep their correct left rotation. Source asymmetry is retained; no perspective resampling or invented pixels.

Template:Card photograph provides one reusable crop/rotation path to both280px article portraits and200px table images. Template:Card changes only its three primary-image branches when the new optional crop fields are present; all fallback/secondary-image paths remain intact. Exact round-trip checks conserve all non-image fields on216 articles, and every non-image table cell remains byte-identical.

Common.css's table.card-thumbs img rule forced every inline20px symbol to200px. The existing presentation hook now scopes an override to non-image table cells and permits source images inside crop frames to scale to their measured wrapper. The bot has ordinary edit/review rights but no interface CSS rights; no account/permission was changed. This is a normal application presentation-code deployment through the existing hook, with exact-file guard, PHP syntax check, rollback copy, graceful reload and documented cache-epoch refresh. Other settings/session configuration stay intact. Nginx's two-minute microcache is respected; all223 canonical URLs subsequently verified at their exact reviewed revisions with current CSS.

Verification:219 pre-publication native parser previews; twelve-card pilot including all five reported examples and three perspective/nonstandard images;31 native-browser cases across1280px/390px including the three set tables, Seeking An Audience and Shmi Skywalker, ordinary cards and both Japanese Alderaan controls. Mobile game-text column is reachable and its icons20px. All314 original File SHA1/timestamp/size/MIME values match previous evidence. Exact before/draft/published source and application hook independently restored from immutable GitHub data (766 payloads). Public Cite errors0; all314 exact foil table rows/images remain represented.

General red/card-field halos are still present in the old symbol assets; their print-faithful transparent WebP replacement is explicitly Story435, coordinated with286. Size correction does not assert asset cleanup completion.

Archive.org/web.archive.org hold remains absolute. No submissions, status/CDX/auth/canary/replay/verification requests made. Existing image-version preservation inventory unchanged;223 new Wiki revision observations queued offline for412. No service/timer started. GitHub source backups and direct Wiki checks proceed independently.
''',encoding='utf8')
(p/'PASS-REPORT.md').write_text('''PASS-REPORT v1 — bug436 — MemoryCoreChatGPT — 2026-11-14

| AC | Result | Evidence |
|---|---|---|
| AC1 Inventory/root causes | PASS |314 mappings from430; framing-proof.json216; framing-measurements.json215; EXIF analysis and design-log.md. Holder boundaries visually inspected, all eight previous rotations audited. |
| AC2 Orientations/framing/originals | PASS | Five named examples plus Rendezvous Point fixed;215 holders display only complete cards in articles/tables; explicit original links. Pilot screenshots/contact sheets reviewed. originals-unchanged.json verifies314 unchanged File versions. |
| AC3 Inline symbols and layout | PASS | Scoped application CSS restores requested dimensions; final-visual-checks.json checks every inline image across all three set tables at1280/390px. extra-visual-checks.json proves mobile game-text access and20px symbols. Non-image article/table fields conserved by build.py assertions. |
| AC4 Guarded delivery/review/public/backups | PASS pending final merge receipt |223 exact guarded, own-bot reviewed, canonical public revisions; Cite0.219 native parser previews;31 browser cases with original links and unbroken images; Japanese/unframed controls.766 independent exact before/draft/published/application payload restorations in exact-raw-subject-readback.json. Source PR41; final merge receipt follows. |

Broader transparent WebP/red-halo cleanup remains Story435 (Backlog), linked286; it is not claimed complete. Archive.org hold remains absolute; no requests made. Offline223-revision queue retains exact source hashes for deferred412 preservation. No original image bytes or articles deleted. Every changed live URL is listed in published-pages.md.
''',encoding='utf8')
print('Design log, per-AC report and223 held revision observations prepared')
