# Nightly public wiki backup

The `Sync from live wiki` workflow runs every night at 08:17 UTC (04:17
America/Caracas; GitHub may start the run later than the cron). It exports
current publicly readable page revisions from every nonnegative namespace,
including Talk, User and File descriptions. It uses the anonymous wiki API,
with no wiki credentials, and it commits only when the export differs. This
is the full page-text backstop (swccg-guild/work#1323). Incremental page and
image backups are a separate VPS job: `swccg-backup.timer` at 07:15 UTC
(03:15 America/Caracas) runs `ops/nightly_backup.py` and pushes to both
`billbisco/swccg-wiki` and `billbisco/swccg-wiki-files`. If the GitHub Action
fails, it opens or comments on a `Nightly wiki page backup failed` issue in
this repository (no AI). GitHub also emails the workflow's last modifier on
a failed scheduled run when Actions failure mail is enabled.

Uploaded image/PDF binaries and their retained public versions remain the job of
the existing VPS backup worker and `billbisco/swccg-wiki-files`. A File-description
page in this text export is not its uploaded original. Archive.org preservation
is separate and is not contacted by either export or its regression tests.

## Authoritative restore inventory

`pages/public-current/manifest.json` records the revision cutoff, the API inventory
observation window, namespace/count totals, exclusions, metadata-file hashes and
original payload byte count. This is not an atomic database transaction snapshot:
membership and selected revision metadata come from a closing public inventory;
new or changed revisions are fetched again before completion. The cutoff is the
final capture watermark, not a claim that every page was globally latest at one
instant. MediaWiki cannot combine historical rvstart cutoffs with multi-page
queries. Each row therefore identifies the latest public revision actually
observed during scan/closing/reconciliation. Hidden or unavailable public text
is explicitly excluded rather than invented; cached text hidden by the closing
pass is not published.

Each `pages/public-current/ns-N.jsonl` row records page ID, observed title and
namespace, exact revision/parent/timestamp, content model, MediaWiki SHA1 and size,
SHA256, byte count and `payload_path`. Restore from **`payload_path`**, under
`pages/public-current/payloads/`, at the same immutable Git commit as the manifest and metadata.
The bytes are UTF-8 API content without adding a newline, changing line endings,
or dropping empty pages. Reserved Git attributes disable newline/filter/ident
rewrites for this authoritative directory, including Windows checkouts. Verify metadata-file SHA256 first, then every payload's
SHA256, SHA1 and byte counts. The resulting text plus metadata identifies the
revision to import into a recovery wiki; do not import into production as a test.

`pages/INDEX.tsv` and old canonical `.wiki` paths are compatibility views, not the
authoritative restore inventory. Existing canonical paths are retained for
existing titles; new titles use numeric `pages/by-id/` compatibility paths, separate
from reserved authoritative payload storage. An ambiguous old filename alias is
reported and left alone, while both exact numeric payloads are preserved. If a
title was recreated with a different page ID, a numeric alias cannot overwrite
another ID's authoritative payload.

The push helper preserves competing Git writers. Canonical INDEX mappings into
reserved `pages/public-current/` storage are refused, so ordinary nightly/delta
writers cannot select an authoritative snapshot payload through INDEX. Authoritative numeric-payload
or namespace/manifest conflicts stop without a push and require a fresh full
export. Conflicting compatibility aliases keep upstream bytes; their paths are
recorded separately in the manifest. Compatibility INDEX unions update only its
digest/count, not the cutoff, revision IDs or authoritative payload hashes. Every
post-rebase push compares the entire reserved authoritative tree with the local
immutable dump snapshot, excluding only explicitly allowed compatibility fields
in its manifest. Even a conflict-free automatic Git merge of authoritative bytes
fails closed before pushing.

## Resuming an interrupted export

The exporter checkpoints each bounded API batch under
`.git/wiki-public-export/`; partial payloads are never added to tracked pages.
Rerun `python tools/dump_public_current.py` in that same isolated checkout to
resume its scan window, namespaces and continuation. A completed checkpoint re-emits
that same snapshot. Use a fresh isolated checkout (as hosted runs already do), or
a new `--state-dir`, for a new cutoff. Do not run two exporters against the same
checkout/checkpoint. A completed manifest is emitted only after every closing
inventory ID is accounted for and payloads are independently rehashed.

API errors, inconsistent SHA1/size, missing visible content, unsafe mappings or a
disk reserve below 1 GiB fail the job rather than producing a partial success.
The nightly schedule, job concurrency and 120-minute limit are set in
`.github/workflows/sync-from-live.yml`. The job is idempotent and pushes only
when the export changed.
