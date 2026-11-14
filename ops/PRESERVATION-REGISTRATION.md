# Preservation registration inbox (Story 410)

This is metadata registration and a promotion interface for the existing server
owner. It does not submit captures, start a worker, upload stages, modify the
Story 382 SQLite ledger, install services or choose a new control directory.
Root supplies the reviewed existing server-local control path outside Git.

## Exact identity and independent backups

`tools/preservation_contracts.py` is the shared schema1 validator. A subject
binds a title, revision ID or public file-version timestamp/URL, UTF-8 or original
binary SHA-256, and byte count. Drafts bind their exact content hash. Receipts
identify the existing GitHub backup repository, immutable commit and relative
path, plus a successful independent restore/readback hash, size and UTC time.
The pure validator checks recorded structure; it does not replace the producer's
actual independent readback. Local staging and submitted URLs do not qualify.

A page's wikitext and its cited source normally have different hashes. Keep the
page's `backup_receipt` and the independent `source_backup_receipt` separate.
`source_backup_subject(source)` supplies the exact canonical source subject;
`validate_source_backup_receipt` validates it. One receipt may be reused only
when the subject and source have identical SHA-256 and byte count. Distinct
filenames, public history versions and source URLs still retain their mappings.

The pure identity helpers are `registration_object_id(subject, source)`,
`registration_job_id(source)` and `validate_registration_identity(record)`.
An exported `subject_id` identifies the publication/version. `object_id` binds
that subject to one exact source URL/hash. `job_id` is `payload:` plus the source
SHA-256, deduplicating payload work without dropping multiple citations from
one page or separate versions sharing bytes.

## Registration and updates

Clients use `tools/preservation_enqueue.py REQUEST.json --registry PATH`. It
sends metadata over the documented `gemp` connection to the fixed server
registration program; it has no archive submission endpoint. The server CLI is:

```
python3 ops/preservation_registry.py register --registry PATH < REQUEST.json
python3 ops/preservation_registry.py export --registry PATH
```

Each request has `schema_version: 1`, subject, source, readiness, owner,
continuation, approval_scope, backup_receipt and, where needed, a separate
source_backup_receipt. `source` contains url, sha256, bytes and checked_evidence
(a durable evidence path and its SHA-256). `readiness` contains ready, reason and
stage_bytes. A private stage locator may be retained privately but is omitted
from the public export. Do not put credentials in a registration request.

`generation` defaults to 0. Identical retries reuse their immutable request.
Changed observations for the same mapping require a strictly larger generation.
Earlier observations remain for audit, but only the latest generation appears
in exports or promotion. A duplicate old request is reported as superseded.
Metadata writes use a short server registration lock and fsynced atomic
publication. That lock does not claim or coordinate archive submission ownership.

The export includes object/job/subject/request IDs, exact registry-record path
and SHA-256, generation, source/version bindings, both effective backup receipts,
state/reason, owner, continuation and approval scope. Root can pin that export
and its hash in the existing Work evidence repository. A registration receipt
always says submitted:false. Missing backup, missing source proof or an unready
private stage remains explicit and never enters the URL queue.

## Existing owner integration

`promote_ready` must be invoked inside the existing server archive-owner lock.
The owner supplies these callbacks:

* `check_approval(request)`: verifies the exact pinned approval scope.
* `check_public(request)`: freshly verifies the exact public URL's complete
  payload SHA-256/size and public accessibility, including redirect/DNS policy.
* `enqueue(url, job_id)`: idempotently appends to the existing ordered URL queue
  and confirms durable registration with `{queued: true, url, job_id}`.

The enqueue callback performs tracked Git writes through the shared repository
transaction from PR 23, not outside it. Lock order is archive-owner lock, then
short Git writer lock; the backup job never takes the archive-owner lock.
Do not hold the Git writer lock during source checks or archive waits.

The owner provides a bounded limit and stage-byte budget. Promotion creates no
stage and cannot claim a nonexistent public snapshot is available. Early
registration of the remaining 45 source snapshots therefore stays unready until
their checked source and independent backup are available and the existing
staging process explicitly provides the public bytes within its budget.

An interruption after queue append can safely replay: the callback reuses the
existing URL and preserves queue order. A successful promotion records queued,
not submitted or verified. Queued records are not external preservation proof.
Worker 407 retains its separate accepted-SPN journal and provider control state.

The existing PR 19 image client still needs the reviewed delegation integration;
this module does not silently rewrite its active source or run its SQLite jobs.
Nightly exact-version reconciliation and receipt production are subsequent
Story 410 work, not claimed complete by the inbox alone.

## Focused tests

```
python -m unittest discover -s tests -p test_preservation_registration.py -v
```

The offline fixtures cover exact receipts, false recovery claims, filename and
history mappings, distinct page/source hashes, multiple citations, interruption,
idempotent replay, approval/public-byte/stage-budget gates and fixed-host enqueue.

