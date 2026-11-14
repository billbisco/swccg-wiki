# Bounded public-version backups (Story 410)

## Existing service, compatible consumers

`nightly_backup.py PAGES_REPO FILES_REPO` remains the existing entry point. No
timer, unit, credential, Git deploy key, resource limit or storage configuration
change is required by this patch. The approved persistent mount must exist;
the default refuses to fall back to the root disk when it is unmounted.

Existing `pages/` files and `pages/INDEX.tsv` continue to represent current live
text. Existing `files/` originals, `files/INDEX.tsv` and `files/USAGE.tsv` remain
compatible. Page updates require the returned exact revision to equal the Wiki's
current `lastrevid`. Only the first current imageinfo entry can update the flat
file; historical originals are archived separately. The Git callback rechecks
the observed payload, title/index mapping and destination ownership, merges
unrelated index additions, and refuses to move a projection's revision/upload
marker backwards. A concurrent peer advance creates a separate durable retry;
it does not undo that peer's work or silently wait for a full inventory cycle.

## Why this replaces the former binary batch

The 14 November 2026 installed backup failed with a kernel-reported Python OOM
at 07:20:15 UTC: anonymous RSS 4,269,776 KiB. The old producer accumulated every
download in a Python `blobs` dictionary before its Git transaction. That code
pattern is removed. The kernel evidence establishes the killed process and
memory use; it did not include a Python allocation stack.

Public originals now stream in chunks of at most 128 KiB to
`/mnt/HC_Volume_107153504/work/swccg-preservation-backup/spool`. A version must
match both its MediaWiki SHA-1 and exact byte count before any Git copy. Per-file
budget is 64 MiB; active verified/inflight payload budget is 256 MiB; per-run
new backup budget is 256 MiB. Both spool and Git volumes retain a 2 GiB reserve.
The source fetch refuses redirects and unexpected transfer encodings. An
absolute deadline is checked around each `read1`/bounded read, and the default
network timeout is capped to the remaining time. Completed originals are
released only after exact independent Git readback. These limits are code
defaults, not promises that the entire historical corpus completes in one run.

## Durable discovery and independent completion

The local `inbox/` contains immutable hashed tasks, completed receipts, explicit
issues, a RecentChanges discovery cursor and an all-public-namespace inventory
cursor. Tasks are fsynced before a discovery cursor advances. Discovery means
the version is queued for backup; it never means that backup succeeded.

Exact edit revision IDs include Talk, File descriptions and other public
namespaces. Upload events queue public image history. Reconciliation cycles
all public page titles and drains their revision/image-history continuations,
so missed manual edits and changes beyond RecentChanges retention remain
discoverable. Suppressed/unavailable versions become explicit reconciliation
issues and are not exported. Failed items receive bounded backoff while other
independent items continue. Each run processes at most 100 tasks for 1,800
seconds by default; a history chunk contains at most ten revisions or five
image versions. API responses are capped at 16 MiB.

`--state` remains supported as a health-summary location. Schema 2 deliberately
does not update the old all-items-success `last` timestamp. Its one-time legacy
watermark is imported only as the first discovery lower bound. Pending tasks
survive a failed Git push, failed independent readback or later process restart.

## Restorable immutable versions and central registration

Every exact version gets a content-deduplicated
`preservation/objects/<prefix>/<sha256>.bin` and a separate
`preservation/versions/<subject-id>.json` mapping. Git writes happen only inside
the shared short reset/redo/stage/push transaction. Source network I/O and
independent GitHub readback happen outside that lock. The remote immutable
commit is read after push and both payload and version metadata are checked.
The returned schema-1 receipt binds exact subject, commit, paths and restored
SHA-256/bytes. Existing valid immutable receipts remain stable when only the
compatible current projection is refreshed.

Public file originals with verified independent receipts are registered in
`WAYBACK_CONTROL_DIR/registry`, defaulting to the existing account control
directory `/root/.local/state/swccg-wayback/registry` on the deployed server.
Registration retains every title/upload/original-URL mapping and checked
imageinfo evidence. It does not submit a capture or take a client-side archive
lock. Captures still belong exclusively to the existing server owner. Automatic
promotion/lifecycle consumption is a separate integration seam; this producer
does not claim that registration alone completes preservation.

## Validation and rollout boundaries

Offline tests cover current flat mirrors/index/usage compatibility, peer byte
and index moves, history ordering, filename collision, exact manual revisions,
all-namespace discovery, source hash/size failure, cache suppression/tampering,
redirect refusal, slow-stream deadline, crash partial recovery, durable retry,
repeat registration, independent restore and bounded original-memory growth.
An 8 MiB generated original fixture requires less than 2 MiB traced Python peak
allocation. Exact source/member/page independent restores have also been
exercised against the existing immutable backup repositories, separately from
the offline tests.

Deployment must use the reviewed exact head and run a small bounded backup
before declaring the former OOM resolved in production. Do not restart the
failed old binary-accumulating backup as part of source-only testing. Provider
authentication or Archive.org availability does not block these local backups
and registrations; it does block any honest claim that pending captures exist.

## Source citations and metadata memory are separate obligations

A backed-up page revision creates an exact-revision-owned
`source-inventory/<subject-id>.json` marker with state
`source_inventory_required`, an owner and continuation. Health reports its
pending count. Text backup alone neither registers every citation nor proves
any linked payload checked or captured; the source checker must resolve those
markers with exact source/backup/job evidence. No verified source hash is
invented from the revision text.

Measured on 14 November 2026: the deployed page INDEX was 4,533,086 bytes.
The files clone was absent outside the wrapper run; current GitHub file INDEX
and USAGE bodies were 3,625,037 and 3,560,493 bytes (39,644 and 55,630 rows).
Flat-table reads and writes now have explicit 16 MiB / 250,000-row caps. A
56,000-row controlled usage merge requires less than 64 MiB traced Python peak
allocation. That is distinct from the less-than-2-MiB binary streaming fixture;
neither measurement claims constant total process/Git RSS. A table exceeding
the cap becomes an explicit pending reconciliation issue, preserving its
existing bytes instead of attempting an unbounded split/sort.
