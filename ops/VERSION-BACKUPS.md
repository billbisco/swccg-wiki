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

Health includes pending and failed-pending task counts, oldest observed pending
age, the last actual independent backup verification timestamp, and separate
citation-inventory counts. Metadata scans are bounded to 50,000 entries/two
seconds each; partial counts are explicitly marked as lower bounds. Discovery,
usage-only work, cached receipt reuse and process success do not manufacture
verified-backup progress or claim the historical backlog completed.

## Fair progress and remaining citation work (14 November 2026)

Each bounded processing pass interleaves four exact revisions, two original-history tasks, one usage task and one page-history task. Empty kinds are skipped incrementally. A large edit backlog cannot consume every slot before an original or projection-history retry receives work; the existing task, time and byte budgets still apply, and failures retain their own backoff.

Source-inventory markers and health explicitly name the Story410 implementation owner and link the shared ticket. The nightly entry point now installs a bounded consumer: at most five exact-revision markers and sixty seconds within the existing absolute producer deadline. It independently restores/hash-checks the pinned GitHub revision, asks the Wiki API to parse that exact revision's external links, and combines those with conservative literal URL candidates. It never fetches a cited external source, submits a capture or changes a registry record. Its network reader allows only HTTPS GitHub raw reads and the Wiki API; all redirects are refused, and Archive.org hosts are denied before opening a connection.

Each candidate is retained in an immutable, hash-addressed inventory report with an owner and continuation. A matching existing registration is reused only for the exact article subject/source URL and a structurally valid independent subject/source backup and checked-proof locator. Unmatched URLs remain `source_check_required`; Archive.org URLs remain `provider_hold`. A partial registry scan, unsafe/malformed link or template/parser expansion remains explicit review work. Templates can change independently of the article revision: rendered external links are an observed candidate inventory, not a claim to have reconstructed historic template rendering or checked each source's meaning.

The original marker is compare-and-swap advanced only after its immutable report exists. Peer progress, owner and original continuation are preserved. `source_inventory_recorded` means candidate enumeration was recorded, **not** source accuracy or external preservation; unresolved constructs use `source_inventory_review_required`. Health separately reports unprocessed markers, review markers, recorded inventories and unresolved source obligations, with the existing partial-scan signal. No page/source hash, independent receipt or capture is fabricated from link text. Interrupted work retains its original marker, and the consumer never starts or probes the held Archive.org worker.

`source_inventory_failures` lists actual errors encountered in this invocation and makes the nightly process exit nonzero. `source_inventory_failed_pending` separately counts durable retry issues attached to still-unprocessed markers, including during backoff; a later process exit zero is not proof that those older errors disappeared. These bounded counts use `source_inventory_count_partial` as the explicit lower-bound flag. Ordinary held sources and review obligations are pending work, not runtime failures; a peer's advanced marker is not relabeled failed by an obsolete retry file.

## Missing public titles and ongoing non-image coverage

A public move without a redirect can leave an old `page_history` task whose title no longer exists. After an unambiguous public API missing-title response, the producer keeps a `public_title_unavailable` disposition with its observation time and no versions or independent-backup claim. It retains historical Git/spool payloads. An observed public move target is checkpointed as a separate history task before the old task completes; later namespace generations and RecentChanges discover recreated titles. Exact revision IDs, invalid/mismatched titles and ambiguous API results are not silently retired. Health counts these dispositions separately as `unavailable_public_title_tasks`; task completion is not a claim that an absent page was backed up.

The namespace inventory enumerates every nonnegative public namespace, including Talk, File descriptions, MediaWiki, Template, Category and custom Card namespaces. File-history discovery and backup/registration have **no image-only MIME filter**: PDFs, text decklists and other public non-image uploads follow the same exact-version hash/receipt path as images. The existing 64 MiB single-file safety cap and 256 MiB per-run payload budget remain; future oversized originals are explicit resumable deferrals, not silently omitted or falsely complete. All public file history uses continuation. Suppressed/private/deleted payloads remain excluded from new public recovery requests.

The actual14November deployed producer completed100tasks in11m53s with no new task/discovery failure. A separate two-task smoke restored exact page/image bytes and checked compatible flat mirrors. The run left5739durable tasks and one earlier peer-projection retry; these are backlog, not a daily arrival measurement or proof of unprotected articles.

Bill approved hourly backups after root recommended temporary catch-up. The existing timer retains daily07:15UTC and adds hourly calendar events through17November2026UTC, then automatically returns to daily scheduling. Limits, service, deploy keys, mounted work volume and archive authentication circuit stay unchanged. The source timer is recorded in ops/systemd/swccg-backup.timer; its actual installation and monitored invocation are recorded on Story410. No application Git update implicitly installs or changes systemd configuration.

## Multiple publishers of the same original

Newly discovered revision and upload/replacement events have durable priority indexes written before discovery advances its cursor. Revision IDs and upload event timestamps/log IDs determine newest-first priority; filesystem creation order does not. Each ten-turn cycle reserves four recent revision turns, two recent upload turns, one older revision turn, one older file-history turn, one usage turn and one page-history turn; empty lanes are skipped. The priority selection retains at most 100 due tasks per event lane; existing unindexed tasks continue through ordinary lanes without a source refetch or migration. Completion removes its own pointer, while durable backoff excludes delayed tasks from the priority window. Existing task/time/byte limits and the single-owner lock remain. Queued events are not verified backups: sustained arrivals can exceed bounded capacity, and errors or long original histories can defer payloads to later runs.

An exact original can already be registered by another AI with a different checked-proof locator, backup receipt or continuation owner. Reconciliation reuses a current ready/awaiting-stage observation only when the full subject and source URL/hash/byte count match and its independent backup/source contract is valid. It does not demote that observation or rewrite its provenance. An incomplete existing backup remains an owned repair; a successful new file backup cannot turn it into a fabricated ready source. Staging also checks the actual post-CAS state, so public bytes without required checked evidence never authorize queue promotion.
