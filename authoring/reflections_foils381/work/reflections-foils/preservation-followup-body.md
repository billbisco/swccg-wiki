## Task
Complete deferred archive preservation from story381 without delaying the completed foil article publication Bill authorized on 14 November 2026.

Bill: “Please don't let Wayback block this. Queue the preservation requests for later and proceed with publishing the remaining 217 foil articles and finishing the ten incomplete ones.”

## Acceptance criteria
- [ ] Reconcile the 936 entries in evidence/381/preservation-queue.json with existing valid captures and exact checked source payloads. Retain all 228 outstanding Wiki original versions by filename/timestamp/SHA1/SHA256.
- [ ] Maintain the imported independently restored immutable backup/readback receipts and checked evidence in the517 existing central registrations. Preserve all object/job/request identities; increment generations for changed observations. Register the remaining 419 source/citation entries only after recovering exact payload/evidence; do not invent hashes.
- [ ] The existing server-wayback-owner alone stages/promotes/submits when its durable circuit permits. Verify raw exact-image replay bytes and source/snapshot text; add checked capture links with current Wiki revision guards.
- [ ] Record verified/remaining counts, merge exact live-source/evidence backups, retain uncaptured staging and skip already completed objects. Registration, queue acceptance and submission are not verification.

## Current state
Publication story381 is complete: all 217 drafts published and ten incomplete cards finished; 314 regular slots represented by 297 new and17 reused articles. No preservation result is being inferred from publication completion.

936 distinct queue entries remain for reconciliation, including228 exact Wiki image versions. The existing operations registry at `/root/.local/state/swccg-wayback/registry` has517 real registrations for known exact bytes, including all228 outstanding Wiki originals. Their generation1 observations include independently restored immutable backup receipts and checked evidence; all517 are ready for owner promotion, not submitted. Actual object/job/request IDs and server export are saved in evidence/381/central-registration-receipts.json and central-registry-server-export.json. The419 other source/citation entries retain URLs and routing in central-registration-remaining.json; recover payloads and reuse valid historical receipts before registering them.

The registry implementation is in `/opt/swccg-ops/repos/swccg-wiki/ops/preservation_registry.py`, not the application checkout `/opt/swccg-wiki`. No new worker/service, schedule, storage or configuration was created. This task stays Backlog for later preservation; publication is not waiting on it. Own Wiki identity Memory Core ChatGPT; board MemoryCoreChatGPT2, signed MemoryCoreChatGPT.

[Publication story381](https://github.com/swccg-guild/work/issues/381); [shared evidence](https://github.com/swccg-guild/work/tree/main/evidence/381); [source PR21](https://github.com/billbisco/swccg-wiki/pull/21). No approval question is outstanding.
