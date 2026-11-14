# Wiki image preservation — Story382

## Provider hold and ownership

Bill's14November2026 hold pauses every Archive.org request, including saves, CDX/availability/status/authentication checks, canaries and replay downloads, until his explicit resumption following the provider response. Shared policy: billbisco/ai-team-skills AGENTS.md, Active Archive.org hold. The existing server Wayback service/timer remain stopped; the timer is disabled and its durable authentication guard retained.

PC capture, queue-verification and Archive.org recovery commands are **retired**. Their entry points fail before ledger/network work; the PC network helper permits only the public Wiki API/images and validates redirects before following them. This central-owner boundary continues after the temporary hold. Only the existing server owner may submit or fetch provider payloads when Bill authorizes resumption. Existing verified receipts and immutable historical source commits remain evidence; they do not authorize another client or a recovery canary.

## PC inventory and exact original backups

Run these commands from a source checkout with a separate PC data directory. Inspect the current Story382 handoff, PID, log, heartbeat and OS lock before starting a job. Reuse its active process and ledger.

```text
python -m tools.image_preservation inventory --data C:/Users/gythe/Documents/Codex/wiki-image-backup382
python -m tools.image_preservation histories --data C:/Users/gythe/Documents/Codex/wiki-image-backup382
python -m tools.image_preservation report --data C:/Users/gythe/Documents/Codex/wiki-image-backup382
python -m tools.image_preservation.offline_backup --data C:/Users/gythe/Documents/Codex/wiki-image-backup382 --limit 50
```

The HTTP source copier accepts exact HTTPS Wiki image originals, checks inventoried SHA1/size, records SHA256 and independently rereads the stored object. It can reuse independently audited existing PC files with `--reuse-index` and an explicit approved `--reuse-root`. Equal payloads share content-addressed storage; each filename/public upload timestamp/original URL retains its mapping and stable upload identity. URL aliases remain available with their receipts.

For the existing GEMP Wiki server, `python -m tools.image_preservation.ssh_backup --data <PC-data-directory> --limit 50` streams inventoried public original paths directly from the existing public image mount through SSH. Batches are bounded to500 originals/128MiB, with a single larger inventoried original handled alone. The remote reader runs at nice10, resolves paths under that public mount and stages no payloads. The client checks framing, exact inventory bytes/SHA1, SHA256 and independent disk readback. Deleted/private/thumbnail paths are excluded. Its missing-only batch selection includes newly reconciled inventory rows; one OS lock prevents overlapping source copiers.

The object cache has a25GiB cap and a20GiB PC free-space reserve, checked during large reads. Stream128KiB chunks. Metadata is in SQLite; the heartbeat is supplementary. Windows readers may briefly delay atomic heartbeat replacement; committed SQLite rows remain authoritative. A failed/mismatched original stays visibly unfinished and requires reconciliation. Preserve the observed source bytes separately when appropriate; recover an expected version only from an exact matching checked payload, with source URL discrepancies retained.

`inventory` checkpoints paginated current originals. `histories` records public retained history, usage across namespaces and current File-description provenance. Dimensions, upload metadata, description revision/text, original URLs, local hashes and independent receipts can be exported per version. Non-image uploads remain separately counted. Use a consistent bounded SQLite snapshot for evidence exports so the copier's writer is not held indefinitely. The current offline evidence scripts also audit baseline-ID conservation and a fresh Wiki-only delta.

## Independent backup and central registration

Use the existing approved image-backup repository for immutable off-site copies. A successful push is incomplete until a separate network restore/readback matches every original SHA256 and byte count, exact manifest and filename/version mapping. Windows text conversion/filters must be disabled for raw-byte restore. Keep compressed inventory, exact source/backup manifests and checked receipts in shared Story evidence; raw images belong in the image repository or PC object cache.

Register exact checked subjects/receipts through the existing deployed `ops/preservation_registry.py` inbox; preserve prior owners/observations and durable object/job/request IDs. During the hold, new requests retain readiness.ready=false and an explicit continuation. Registration and export are metadata operations and do not promote a queue or submit a capture. The central server owner controls all future staging/submission/replay verification.

Story382 remains unfinished until all applicable acceptance criteria pass: final delta, every in-scope full-resolution Archive.org payload verified, exact File-page links, Archive.org-only restore sample and incremental completion integration. PC/GitHub backups, pending metadata and previously checked captures are reported separately. Never claim full preservation from a queued request or a partial local pass.
