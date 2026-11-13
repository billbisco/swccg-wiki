# #287 — Shared card infobox migration

## 2026-11-13 — Migration first; preserve legacy data without interpretation

**Decision.** Bill approved the recommended sequence: shared infobox migration first, remaining Japanese-set content repairs afterward, with source/scan research allowed alongside. The shared skill records this order. ChatGPT takes the unstarted Ready story from its queued Alpha1 assignment under Bill's explicit direction.

**Why.** The refreshed 794-page inventory contains 43 simple layouts and 751 template-look layouts with many additional metadata labels. A printing's native text, editorial translation and source evidence are separate data. Existing fields need to survive structural rebuilding without silent correction or English substitution.

**Interface.** Implement #287's optional language/native/translation and edition fields. Add narrowly scoped conservation hooks for existing navigation, nonstandard leads, legacy type/set displays, row-label aliases, image notes, additional metadata/sections and the non-set oversized promo's original categories. All standard Template:Card defaults retain their old branches; English controls must render identically. These hooks preserve old values in the shared table rather than retaining a per-page hand-made infobox. The promo's Size/Year become ordinary optional metadata rows.

**Alternatives.** Reject a separate Japanese template, dropping irregular legacy fields, moving translations below References, or rewriting incomplete text during migration. Keep redundant legacy Versions data where it already exists; record it for later content reconciliation instead of choosing a new identity during conversion.

**Baseline defects.** The #361 repairs reduce the old 35-page style backlog to one oversized promo. Baseline render checks also reveal 25 pre-existing undefined `photo` references, all pointing at existing matching Premiere card images. Restore those definitions additively and track them under the required citation/style follow-up Task. Keep native prose unchanged.

**Verification.** Capture all 794 old rendered pages and 50 deterministic English controls before touching the template. Check 10 initial sandbox samples (5 per old layout), all-page content/link/file/reference/category conservation, 12 final product/layout examples, unchanged English HTML, guarded section-zero writes, supported scoped reviews and public output. Do not claim full linguistic or scan-edge verification from a structural migration.

**Who / status.** Bill authorized execution in chat; MemoryCoreChatGPT implements #287. Set-icon asset/lookup work stays on #286; content audits resume after the shared structure is verified.
