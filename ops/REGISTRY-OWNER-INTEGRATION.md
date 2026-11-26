# Registry consumer seam (Story 410)

This module has no capture submitter or standalone runner. Integrate it into the
existing `wayback_worker.py` Control-owned run; keep that worker's provider
circuit, authentication behavior, accepted-job journal and service/timer.

## Exact approved cohort

The default is no approved objects, not every registration in the global inbox.
An operator-reviewed metadata file at `CONTROL/registry/approved-objects.json`
has schema version 1, owner `server-wayback-owner`, a nonempty `approval_scope`
with the immutable evidence/export reference, and `object_ids` containing the
exact approved registration object hashes. Maximum 5,000 mappings and 1 MiB.
Installing/revising this is an explicit review of owner data; it is not inferred
from a client's claim or a global registry export. Other clients' objects,
generations, queue order and completed ledger records remain untouched.

`load_allowed_objects(registry)` reads this file, returning an empty set if it
does not exist. Each eligible observation still requires valid independent
subject/source receipts and source-representation evidence. Metadata scans
retain one current observation per object rather than all historical bodies.
Readiness changes use a locked compare-and-swap against the exact registered
request; another client's newer generation cannot be overwritten by a stale
restore. Every prior observation remains immutable.

## Worker hook contract

After recovery reconciliation inside `_run`, when `ACTIVE_CONTROL` is the
actual active Control object:

```python
adapter = OwnerAdapter(worker_module, repo, control,
                       load_allowed_objects(control.directory / "registry"))
control.registry_adapter = adapter
prepared = adapter.prepare(deadline)
done.update(prepared["ledger_updates"])
changed.update(prepared["ledger_updates"])
control.checkpoint(done, control.initial_done)
urls = load(repo)[0]  # queue append may have reset/pushed the shared Git tree
```

Use the existing baseline/changed transaction and accepted-job journal; do not
replace in-memory `done` with a fresh ledger after applying the returned delta.
In the existing owner finalization, before clearing `ACTIVE_CONTROL`, call the
created adapter's `finish(deadline)`. A paused run that never created an adapter
does not need a new one. Preserve the worker's original outcome and durable
journal if this auxiliary reconciliation reports an error. No provider request
is permitted while the circuit is paused, half-open or authentication-blocked;
finish can record real accepted job IDs from existing receipts without network.

## Bounded staging, queue and version lifecycle

Prepare attempts are sized per run from the queue buffer (#1375): the worker
keeps about six hours of untried URLs in queue.txt (at least 100; allowance x
runs per hour x 6) and attempts up to `target - buffer` jobs, capped by
`WAYBACK_PROMOTE_MAX` (200) and `WAYBACK_PROMOTE_SECONDS` (150 s, never past
deadline - 60). A bare adapter still defaults to two. An exact-cohort cursor
keeps early failures from starving independent objects. All queue appends of
one prepare are written with a single commit and push; their `queued` receipts
are stored only after that push succeeds (a failed push stores none and rewinds
the cursor). Finish rotates its own bounded checks (`WAYBACK_FINISH_CHECKS`, 6).
Jobs whose URL already has a capture need an archive.org observation (replay,
CDX, id_ fetch); prepare and finish share one budget of
`WAYBACK_OWNER_OBSERVE_MAX` (10) observations per run, spaced by the worker's
`VERIFY_GAP_S`. Jobs beyond it are skipped without using the promotion cap, so
fresh never-captured jobs still fill it. A replay/CDX 429 or refusal records
the shared cooldown and ends archive.org calls for the run. Many filename/revision mappings share one exact SHA-256 payload
job; each mapping is retained, with actual capture-host provenance preserved.

Checked self-contained snapshots can be independently restored from their
existing Git backup/container into the approved persistent work volume, then
published at the exact approved snapshot target. The aggregate public-stage
budget is 32 MiB, including other existing stages; scan cap is 50,000 files.
There is a 2 GiB work-volume reserve. Existing different target bytes are never
overwritten. Already-public originals require an exact public hash/size check
and need no new public stage. Unrecognized private representations remain
pending, rather than inventing a capture target. Queue appends preserve order
and comments through the shared locked Git callback.

The default restore work path refuses a missing persistent mount before creating
directories or restoring bytes. Each owned private restored copy is removed on
success, restore/hash error, provider pause or expired staging deadline; a late
restore cannot accumulate outside the public-stage budget.

Registration/queued intent is not submission. Owner receipts report an actual
accepted job ID separately. Verified means strict indexed replay plus a whole
raw SHA-256/byte-count match to the registered payload; a text-similarity
verification from the legacy worker is insufficient. Immutable owner events
and hash-bound pointers live outside Git resets; export keeps actual capture
original URLs rather than rewriting a shared capture into another source URL.

A previously completed URL may refer to a different historical body. Only a
strict, indexed, raw mismatch after the current source passes its exact check
can request a new version epoch. The old full worker receipt and checked old
capture hashes are retained before returning a retry delta. Accepted pending
jobs are never reset. Terminal failures lacking usable version evidence become
owned repair records, not endless resets of the same payload.

A queued version epoch retains its old strict raw receipt before returning a
ledger delta. If the owner dies before the worker checkpoints that delta, the
next run revalidates the public bytes and replays the same intent. An accepted
job or already applied epoch never has its retry counter reset. The worker
retains the narrow payload/job/previous-capture/recapture fields across every
submission outcome. A completed epoch with wrong bytes becomes owned repair,
retaining its actual accepted job identity rather than claiming verification.
Provider pauses propagate immediately. Owner scans parse only approved object
directories, so unrelated malformed client data cannot block this cohort.

## Cleanup and remaining integration gate

The adapter does not delete stages. The existing pruner's citation safeguard
still applies. A production integration must connect verified registry receipts
to publication/citation reconciliation or approve an equally strict scoped
cleanup seam (exact approved mapping, independent source backup, strict raw
capture proof and unchanged staged bytes). Otherwise verified but uncited
stages can legitimately keep the aggregate budget full. Do not silently remove
that safeguard or claim the complete JIT workflow deployed before this gate and
the small worker hooks pass integration tests.

`protected_snapshot_urls()` returns only exact approved managed snapshot source
URLs, regardless of readiness. The worker must also protect legacy URL aliases
that resolve to those same stage files, and skip deletions if this metadata scan
fails. A registration's `owner` is its client's continuation owner; it does not
grant capture authority. Independently reviewed object identity plus the real
active Control lock govern promotion, including approved entries prepared by
other clients. Unknown global registrations remain excluded.

Source-only offline fixtures cover paused modes, absent active owner, unknown
global objects, stable ordered queue appends, shared mappings, exact JIT
restoration, stage quota, wrong source bytes, accepted job identity, strict
capture bytes, safe old-version retry, concurrent readiness CAS and receipt
pointer tampering. No live registry, stage, queue, configuration or capture API
is changed by those tests.

## Ticket auto-approval policy (Bill, 2026-11-25, #1359 Q1)

"Have the worker auto-approve every registered item that has a ticket number."
`ops/preservation_policy.py` runs inside the owner run before `prepare`. An
object is approved by policy when its latest observation is `ready` (valid
backup receipts, source proof and readiness), `approval_scope.ticket` is a work
ticket number (`123`, `"#123"` or a swccg-guild/work issue URL), and it is not
suppressed and not stamped with the 14 Nov 2026 hold. Held, not-ready and
`awaiting_stage` objects stay out; ready objects without a ticket are flagged in
`registry/policy-unapproved.json`.

Approvals are appended to `registry/policy-approvals.jsonl` (first record per
object wins; hourly registry scan). `approved-objects.json` is not rewritten and
keeps its operator role and 5,000-ID / 1 MiB guard. Each run the adapter gets the
explicit approvals plus a first-approved-first window of policy objects that are
still ready and not yet owner-verified, capped so the total stays within 5,000.
How many approved jobs are promoted per run is the adaptive buffer cap above
(#1375); the policy only widens the cohort. A policy error falls back to
the explicit approvals only. AIs register with a ticket; they do not hand-write
approvals.
