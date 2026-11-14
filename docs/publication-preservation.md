# Publication with external preservation pending

Bill approved separating content delivery from external preservation under [Story 409](https://github.com/swccg-guild/work/issues/409). Source accuracy, independent restorable backup and durable preservation registration remain required. An Internet Archive outage alone does not hold an otherwise complete article. Accuracy applies to the claims actually asserted: an honestly incomplete article can publish supported known fields without waiting for every missing field. A preservation-specific ticket retains its stricter acceptance criteria until explicitly changed.

The editorial policy lives in `billbisco/ai-team-skills/shared/swccg-wiki/archiving.md`, under **Publication and preservation gates**. This document defines the opt-in reporting interface. It does not authorize capture submissions or replace native preview, exact-head conflict guards, source review, independent remote readback or public after-QA.

## Default and opt-in results

The existing command remains strict: any lint finding exits 1.

```sh
python authoring/style_lint.py draft.wiki --title "Exact Wiki title"
```

For an explicitly approved publication scope, pin the completed manifest bytes and invoke:

```sh
python authoring/style_lint.py draft.wiki --title "Exact Wiki title" \
  --publication-manifest evidence/publication.json \
  --approved-manifest-sha256 <approved-manifest-SHA256> \
  --report-json evidence/publication-report.json
```

The manifest hash must be approved by the authorized publisher as part of the reviewable packet; supplying a command-line string is not independent evidence of approval. Changing the draft, evidence, export, manifest or approval scope requires renewed review and a matching approved hash.

The command prints the actual raw findings and count, then a `PUBLICATION` JSON report. Exit 0 means `publication_eligible: true`; it does **not** mean zero lint or preserved. Every non-ARCHIVE finding still blocks. Unregistered sources, absent originals, unchecked source evidence, invalid backups, wrong draft/revision hashes and missing durable job ownership also block. The report retains `raw_flags`, `errors`, `preservation_pending` and `preservation_complete` separately. Never relabel a pending report as a strict-lint pass.

## Manifest schema 1

The top-level JSON object contains:

| Field | Required value |
| --- | --- |
| `schema_version` | Integer `1` |
| `approval_scope` | Nonempty object identifying the ticket and explicit approval evidence |
| `registry_export` | Bundle-relative `path`, exact `sha256`, and immutable Git `storage` locator |
| `pages` | Array containing exactly one matching title for each invocation |

The registry export locator is `{kind: "git", repository, commit, path}`. Use a full 40-character commit and safe repository-relative path in `billbisco/swccg-wiki`, `billbisco/swccg-wiki-files` or `swccg-guild/work`. All evidence paths are relative to the manifest directory, cannot escape it and must match their stated SHA-256. A structural validator cannot prove that a claimed Git object exists remotely; the producer/publisher must independently retrieve and check the immutable backup and export before approval.

Each page has:

| Field | Meaning |
| --- | --- |
| `title` | Exact canonical Wiki title; spaces and underscores normalize identically |
| `subject` | Story 410 exact subject: local files use `kind: "wiki_draft"`; live targets use `kind: "wiki_revision"` and the actual fetched revision ID |
| `backup_receipt` | Story 410 receipt bound to that exact subject, independently restored and checked |
| `source_accuracy` | `{status: "checked", evidence: {path, sha256}}`; evidence records source inspection and claim checks |
| `sources` | Explicit mappings `{url, object_id, evidence: {path, sha256}}` for every external cited source in scope |
| `rendered_originals` | Native expanded-page inventory of all public original File titles, including template-generated references |
| `original_versions` | Mappings `{object_id, subject, evidence: {path, sha256}}` for exact public original versions |

The gate also discovers literal File links, gallery entries and image fields. It cannot independently expand templates or discover client-side images: obtain `rendered_originals` from the native render and review it. Empty inventory is appropriate only when the rendered page has no originals. Register retained public history versions separately; do not publish private, deleted or suppressed versions.

Source URLs can differ from a registry payload URL when an inspected self-contained snapshot or equivalent primary representation preserves the claim. The source check must explicitly prove this relationship. A URL mapping or equal job identifier alone does not establish equivalence.

## Backup and registration contracts

Install Story 410's `tools/preservation_contracts.py` before using the opt-in interface. Its pure `validate_backup_receipt(receipt, subject)` validator is authoritative. The subject identifies kind, title, SHA-256 and bytes, plus the exact live revision ID or original upload timestamp/public original-version URL where applicable. The receipt identifies an approved independent Git repository, immutable commit/path, and a successful independent restore/readback with matching hash and bytes. A queued request, local file, unchecked push or wrong revision is rejected.

Use the real server `ops/preservation_registry.py` export, schema 1, with `submission_owner: "server-wayback-owner"`. Its objects retain the exact publication subject, source payload hash/bytes, checked-evidence hash, independent backup receipts, subject/object/job/request IDs and durable request-record path. Story 410's pure identity helpers distinguish each publication/source mapping while equal payloads can share a job. One page can have several distinct sources; the source hash need not equal the page hash. When they differ, `source_backup_receipt` must recover the canonical source subject defined by `source_backup_subject(source)`, in addition to the publication's own receipt. Equal hash and byte count allow recovery of the same exact payload through one receipt without dropping version/source mappings. The report validates these identities and requires an owner, reason, continuation and approval scope. Pin the export bytes in the publication evidence; do not manufacture a registry export from a client-side list.

Pending states admitted by this adapter are `registered`, `awaiting_stage`, `ready`, `queued`, `submitted`, `retry`, `auth_blocked` and `needs_attention`, provided all other evidence checks pass. These labels retain their actual meaning: registration is not submission and submission is not verification. `awaiting_backup` cannot pass the required receipt checks. Bare `verified` state is rejected because this export has no replay-verification contract; use the checked existing capture and ordinary strict workflow, or a separately implemented checked-receipt adapter. This adapter never invents a verified result.

All clients register with the central server inbox. The existing server owner alone promotes ready work to its URL queue and submits captures; a local lock on another computer cannot coordinate it. Bug 407's durable authentication stop, provider cooldown and canary recovery govern submissions. This reporter has no save client, credentials, queue writer or worker-control mutations.

## Publication and completion evidence

Before saving, record the approved manifest hash, immutable evidence/export and independently restored draft/source/original backups; inspect the exact diff and native preview. Publish with an exact current revision guard and preserve other editors' work. After saving, retrieve the actual revision, verify public text, images, references and navigation, and independently back up that exact live revision. A draft receipt cannot stand in for a live revision receipt.

Report content delivery and pending preservation as separate results. Each pending object keeps its central identifier, owner, reason and continuation on the Story/registry/handoff. Add a Preserved copy to article references or File preservation sections only after checking the actual capture. Preservation completion still requires all applicable replay/binary checks and per-version mappings; image audit 382 is not completed by an eligible publication report.
