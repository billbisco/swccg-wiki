# Complete-source chunk backups: proposed owner integration

Task [452](https://github.com/swccg-guild/work/issues/452) contributes a new
**explicit** `storage.kind = git_raw_chunks_v1` contract. Older validators
reject this kind. This contribution does not install the profile, change a
worker, upload a source, or make a registry record ready. The existing 410
owner controls shared-code deployment and subsequent approved recovery.

## Exact representation

Schema-1 receipts retain the original complete `subject`, including its
SHA-256, byte count, title and exact version/URL fields. A manifest JSON or a
chunk is never substituted as that subject. Registration/source IDs are
unchanged. The new profile allows exactly these storage keys:

| Field | Meaning |
|---|---|
| `kind` | Literal `git_raw_chunks_v1` |
| `repository` | `https://github.com/billbisco/swccg-wiki` or `https://github.com/billbisco/swccg-wiki-files` |
| `commit` | One immutable lowercase 40-hex Git commit |
| `path` | Repository-relative manifest path |
| `manifest_sha256`, `manifest_bytes` | Exact manifest identity, 1 byte through 4 MiB |
| `parts` | The complete ordered part descriptors, identical to the manifest |

The exact manifest keys are `schema_version` (integer 1), `profile` (literal
`git_raw_chunks_v1`), `subject` (the same original subject), and `parts`.
Each descriptor has exactly `index`, `offset`, `path`, `sha256`, and `bytes`.
Indices start at zero; offsets start at zero and are contiguous; part sizes
are positive integers at most 64 MiB; their sum equals the full subject size.
There are 1 through 16,384 parts. Paths must be safe, unique, different from
the manifest, and free of traversal, empty/dot segments, backslashes, control
characters, absolute roots and Windows drive syntax. Parts inherit the single
repository and commit; per-part repository/commit fields are rejected rather
than ignored. Unknown fields, duplicate JSON keys and nonfinite JSON numbers
are rejected. Symlink metadata, unsafe paths and Git LFS pointer bodies fail.

`stage()` reads an existing regular source with 128 KiB buffers. It writes a
new isolated directory containing `preservation/chunks/<full-sha256>/parts/`
and the exact manifest. Its result says `LOCAL_ONLY_NOT_BACKED_UP`: no commit,
timestamp, remote receipt, approval or ready flag is created. Failed staging
may leave incomplete local parts but never a successful manifest/result.
The default prefix is byte-preserved by this repository's attributes; another
approved repository/prefix must also store exact bytes, without LFS or text
conversion. Independent readback rejects any conversion.

## Independent producer and consumer

`preservation_backups.independent_receipt()` keeps its existing API and direct
Git/tar.xz behavior. For the explicit new kind, it delegates to the chunk
producer. At the pinned repository/commit, the producer:

1. Fetches immutable GitHub Contents metadata for the manifest path. It checks
   file type, exact path, size, Git blob SHA-1 and the corresponding Git/raw URLs.
   Requests use `application/vnd.github.object+json`, the [GitHub-supported
   Contents metadata media type](https://docs.github.com/en/rest/repos/contents)
   for files between 1 and 100 MB; raw payload requests remain unchanged.
2. Streams the manifest's raw bytes, independently computes Git's framed blob
   SHA-1 plus SHA-256/size, and checks the strict manifest and original subject.
3. Repeats both metadata and streamed raw readback for **every** ordered part.
   Each full part hash/size/Git identity must pass. No local staging payload is
   consulted as remote proof; neither a bare boolean nor a manifest-only
   response is sufficient.
4. Concatenates the recovered bytes into a separate full-source hash and
   optional temporary output. The exact full SHA-256 and byte count must pass
   before atomically replacing the requested restore destination. A failed
   restore preserves any prior destination and removes its partial temporary.

Only then is a receipt returned. Its verification has exactly the common
`status`, `independent`, `restored_sha256`, `restored_bytes`, `verified_at` fields,
plus `method = immutable-git-metadata-and-streamed-parts-v1`, `manifest_readback`
and `part_readbacks`. Each readback binds `path`, `sha256`, `bytes`,
`git_blob_sha1`, `repository` and `commit`; part readbacks additionally bind
`index` and `offset`. All are required in order. The pure shared validator
checks this recorded evidence; it does not itself perform a remote restore.
As with existing receipts, only the independent producer may claim real proof.
Tests inject in-memory transports, and their fixture receipts are not real
backup evidence.

Raw payload buffers are at most 128 KiB. Git JSON metadata is capped at 2 MiB,
manifest bytes at 4 MiB; no whole-source or whole-part buffer is accumulated.
GitHub redirects are refused by the existing transport. An HTTP/API failure,
missing part, hash mismatch or truncated/extended body yields no receipt.

## Budget boundary and manual commands

The existing worker's **64 MiB single-file, 256 MiB spool/per-run budgets** and
service configuration are unchanged. This profile does not wire automatic
large-source staging into a worker or claim a budget exception. The default
whole-source chunk readback/staging limit is 128 MiB, preserving the existing
readback cap. The new optional `chunk_max_total_bytes` argument applies only
to the chunk branch; direct Git/tar.xz callers retain their current bounds.
An explicitly authorized manual PC recovery may supply a larger exact byte
limit. Small parts do not evade the whole-source limit, which is checked
before any request. Any future worker integration must separately retain its
run accounting/deferral and owner approval; accepting a receipt is not worker
download authorization.

Code-only local invocation shape, not a production instruction or upload:

```text
python tools/preservation_chunks.py --subject exact-subject.json stage --source complete-source.pdf --out NEW-local-directory
```

After owner integration, approval, actual Git backup and review of privacy/disk
constraints, the independent manual producer can use:

```text
python tools/preservation_chunks.py --subject exact-subject.json --max-total-bytes EXPLICIT_AUTHORIZED_LIMIT verify --storage ACTUAL-immutable-storage.json --restore-to NEW-full-restore.pdf --receipt NEW-actual-receipt.json
```

No network/upload/capture action is performed by local staging. Neither command
changes a timer, registry, queue, credential, worker budget or provider hold.
Archive preservation writes remain paused; this contribution makes no Archive
requests or runtime-guard changes. Bulk local measurements
belong on Bill's PC, not VPS `/tmp`. Do not upload large source bodies, chunks,
private metadata or contact values as part of this code PR.

## Verification

Run the focused no-external-network fixtures:

```text
python -m unittest discover -s tests -p test_preservation_chunks.py -v
```

They cover metadata and every part, full atomic recovery, whole-source budgets,
wrong subject/hash/size/manifest, unknown fields/kinds, unsafe/duplicate/reordered
paths, gaps/overlaps, mixed commits/repositories, truncation/modification,
LFS/JSON-as-payload substitutions, local-only proof and bounded read calls.
Run existing authoring, operations and root regression suites too. Preserve
direct Git/tar.xz API tests and existing budget/deferral regressions. A real
large-file local stage/reconstruction remains explicitly **local** evidence;
it cannot replace the required future actual remote Git reconstruction.
