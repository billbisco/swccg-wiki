# Resume story381

Read the current shared AI-team checkout and story381 before editing. Bill authorized completing the regular foil articles; no policy/permission question is open. Use Memory Core ChatGPT on the wiki and the assigned MemoryCoreChatGPT2 board reviewer, signed MemoryCoreChatGPT. Do not use Admin, disclose credentials or ask Bill the same settled questions.

## State

314 regular slots:114 Reflections,100 Reflections II,100 Reflections III. Initial16 existing. Of298 initial gaps:70 fully verified new,10 additional live/preservation-incomplete,217 unsaved new drafts,one discovered existing printing reused. All298 physical faces independently read and original hashes checked. All217 drafts pass new-article style/field/infobox-preview checks. All12 Reflections III AI artworks manually matched against regular/AI references. No article deletion is needed.

Story: https://github.com/swccg-guild/work/issues/381

Source backup checkpoint: https://github.com/billbisco/swccg-wiki/pull/18 (branch codex/reflections-foil-articles-381). Read actual merge state; open a successor PR if this checkpoint is merged rather than pushing invisibly to an old merged branch.

Evidence: https://github.com/swccg-guild/work/tree/main/evidence/381

Authoring code is under authoring/reflections_foils381/work/reflections-foils in swccg-wiki. Restore it under work/reflections-foils relative to a checkout containing work/wiki-tools and work/japanese-infobox287/vendor; requirements are listed beside the authoring bundle. Installed shared authoring equivalents may be used. This PC scratch is C:\Users\gythe\Documents\Codex\2026-11-06\legacy-integration-release\work\reflections-foils.

Exact original photographs are in billbisco/swccg-wiki-files: sources/381/photos for discovery assets, files/ for uploaded wiki originals. Match each readings.json source_photo and SHA256, not a similar-looking image. The first published originals can be recovered from the recorded source URLs or uploaded filenames if needed. Original-image preservation is independent of source-page/gallery preservation.

## Blocker and next action

Anonymous Save Page Now GETs returned520 on both VPS and PC. Public POST explicitly returned429 automated-traffic throttling; submissions stopped. Documented authenticated VPS route returned401. One ordinary retry after an extended cooldown still520. Do not hammer, rotate routes to bypass throttling, change lint, or invent replays. Credentials remain in remote memory only. Existing verified receipts can be reused; failures/queued URLs cannot count as captures.

First next step after service recovery or maintenance of its existing credential: run the ordinary batch8 primary-preservation step once, then verify the returned payload. Its staging remains at /opt/swccg-res/snapshots/psa/reflections381-batch8-primary-sources.html. Also retain reflections381-batch8-wiki-originals.html. Both URLs and exact pending image versions are in ops/wayback/queue.txt; do not delete uncaptured staging.

Run from the authoring workspace root:

```
python work/reflections-foils/preserve-primary-batch.py batch8
python work/reflections-foils/repair-batch-citations.py batch8
python work/reflections-foils/preview.py batch8-family-final --sandbox
```

Before publishing any family packet, re-fetch current family heads and rebuild/repair its navigation from those current sources. Old before_revid/hash guards are intentionally stale after later edits. Keep the verified primary/citation evidence. Do not rerun upload-batch.py for batch8: its original images are already uploaded, reviewed and unchanged. Publish the refreshed family-final packet, then:

```
python work/reflections-foils/archive-batch-images.py batch8
python work/reflections-foils/build-preservation-links.py batch8
```

Publish the generated Preservation packet (check its filename), run full verify-batch.py batch8 and visual checks. The image archiver uses a20-second save cadence; never run concurrent Wayback jobs. A gallery capture is only an optimization, not the individual binary proof. Existing batch8-partial-public-verification.json proves only its31 published pages, not family/preservation completion.

Also capture the existing Don't Get Cocky image version in batch12-existing-image-captures.jsonl, compare raw replay bytes and add the File Preservation link. The reused article metadata/checklist/Talk edits304301–304303 passed supported review, exact/public/style/Cite and desktop/mobile checks. Its four reciprocal family links were already present. Do not create a duplicate or upload another copy. The image is backed up under its existing filename.

## Remaining publication pipeline

217 drafts: batches9–11 Reflections I33;12–21 Reflections II94;22–31 Reflections III90. batch12 contains nine NEW cards; its separate existing-reading ledger is Don't Get Cocky. batch17 has seven, batch21 eight, batch27 four, batch31 six. Do not assume ten rows.

For each stage, inspect code/outputs before advancing:

1. preserve-batch.py STAGE: verify self-contained exact source-photograph snapshot.
2. upload-batch.py STAGE: regenerate complete payload and upload unchanged originals with guarded own-bot review. Current prepare-draft-files.py packets deliberately have draft_only:true and no upload bytes/description/archive claim.
3. fetch-families.py STAGE, build-batch.py STAGE; retain existing shared Card versions navigators. If one is present, prepare its shared navigator update, as done for Vader, rather than copying inline navigation everywhere.
4. scan-batch-citations.py STAGE, archive-batch-citations.py STAGE; exact-primary fallback only where needed. remaining-citation-readiness.json inventories211 unique URLs:27 reusable verified receipts,184 unresolved. Never queue live forum.starwarsccg.org or www.starwarsccg.org URLs; use the documented snapshot route. Existing capture receipts are not permission to claim a new capture unverified.
5. repair-batch-citations.py STAGE; zero style flags, preview and conservation checks, then guarded own-bot publish. New article packet, complete File payload, family-final, set and signed Talk packets are separate.
6. build-batch-set-talk.py STAGE supports the current Possible foils heading on all three sets; inspect exact row title/root/AI/twin matches. Publish direct checklist and Talk packets from fresh heads.
7. archive-batch-images.py STAGE; byte-check each exact public image version; build/publish Preservation links. verify-batch.py STAGE, shared-family verifier if needed, representative desktop/mobile capture and inspect the images. Never use a stable_revid pointer alone as proof a review action succeeded: publisher uses supported action=review.
8. update-inventory-progress.py, check-publication-identities.py, refresh current backup heads and reports. Back up live edits in a merged PR, originals in files repo, evidence on the story. Close only with all ACs passing.

## Important details

- Maintain initial-manifest.json and initial-inventory.csv as immutable census evidence; manifest.json is current delivery status.
- Product-qualified foil names distinguish real physical printings. Unpublished normalization ledger covers Light Death Star/Kiffex and printed Artoo-Detoo. Death Star Light root is Death Star (Special Edition), Dark root Death Star; Light Kiffex root Kiffex (Jabba's Palace). Ric Olié source ledger must be read explicitly as UTF8.
- No unverified gemp_id/card_uid. Publication IDs are separate from playable mappings. 299 distinct English IDs were checked including the original Luke pilot.
- Mirax foil deploy7 is intentional physical evidence, not an asserted official erratum. Redemption reads “have been modified” (second full photo confirms). Slave I prints Hyperdrive4. Do not normalize named creature stats or Brainiac symbols into guessed numeric values. Original premium icons differ from Special Edition; Coruscant/Reflections II/Theed Palace use verified text labels where no icon asset exists.
- Conquest and Red5 families received independent later navigation additions; the current backup retains them. Their foil printed text/stats are unchanged. Do not replay old whole-family baselines over them.
- Git partial repositories: never git status/check out massive trees. store.py uses a scoped index, latest main and path-conservation assertions. For a new source checkpoint, use a new PR/branch after PR18 is merged.
- Bulky VPS work belongs under /mnt/HC_Volume_107153504/work/memorycorechatgpt-reflections381-20261113, never RAM-backed /tmp. Any own browser/Flare session closes in finally; no detached worker is arranged to finish publication.
