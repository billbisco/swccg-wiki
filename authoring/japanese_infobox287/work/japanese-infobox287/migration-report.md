# Migration report — #287

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
