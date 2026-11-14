# Existing worker registry hook (Stories 407 / 410)

The existing `wayback_worker.run` creates the adapter only after `Control.begin`
and recovery reconciliation. Prepare deltas enter the shared in-memory ledger
and changed transaction, then the durable checkpoint, before queue reload or
submission. Reload reads only URLs so a queue Git reset cannot discard those
deltas or recovered accepted jobs. Auth-blocked starts never create an adapter.

Finalization calls the existing adapter under the still-active Control lock,
even after prepare/provider pauses. A finish failure preserves the primary
pause/failure and checkpoints accepted receipts; `registry-repair.json` records
only exception type, phase and Story 410. A previously successful run becomes
failed if finish fails. Storage failures are reported by sanitized type while
preserving the original pause/failure.

Legacy pruning excludes every staged filesystem target returned by
`OwnerAdapter.protected_snapshot_urls()`, including URL aliases resolving to
that same file. It shares original ledger entries so unrelated legacy demotion
still persists. Metadata scan errors skip all deletion and record repair.
The existing citation and fresh verification checks still govern other targets;
no cleanup API or registry deletion authority is introduced. Empty approved
cohorts retain the existing legacy pruning behavior.

Dependency: integrate with the pinned Story 410 owner adapter providing
`protected_snapshot_urls()`. This worker commit deliberately does not modify
that adapter, the queue, done ledger, service, timers or credentials. Root owns
composite Windows/Linux verification, merge and deployment. These source-only
tests use temporary registries and mocked Git/provider boundaries; passing them
does not establish live provider recovery or complete preservation.

Offline focused verification:
`python -m unittest discover -s ops/tests -p test_wayback_owner_hook.py -v`
