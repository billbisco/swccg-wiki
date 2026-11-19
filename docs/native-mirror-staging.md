# Byte-identical native mirrors

`checked_byte_identical_native_mirror` preserves a checked public forum attachment
as exact native bytes at `https://swccg.com/snapshots/native/<sha256>.txt` or `.doc`.
The source keeps its original forum URI in `primary_url`; the publication subject
retains its original version identity. Mirror-source mapping IDs are distinct and
must be explicitly mapped to the retained original-source registrations.

The native equivalence proof binds both URIs, identical SHA-256 values, exact byte
count, native kind and immutable checked-evidence path/hash. It has no fabricated
HTML or article-text hashes. Supported kinds are inertly checked GEMP deck XML and
OLE Word documents. Unknown kinds, unsafe paths, nonregular files, symlinks,
changed bytes and HTML/error payloads cannot be staged through this contract.

## Stage-only maintenance

After exact objects are registered, independently backed up and included in the
existing owner's approved cohort:

```sh
python3 ops/preservation_stage_native.py --objects-file approved-native-cohort.json
```

The file contains `{"object_ids": ["<exact object ID>"]}`. The command acquires the
existing `Control` owner lock and checks only those native objects. It restores
the immutable backup, validates the original bytes and format, refuses conflicting
staging, and checks the complete public HTTP response without following redirects.
The resulting receipt records status, content type, SHA-256 and byte count.

Private Git backups require an authorized genuine independent readback callback
through `stage_native_objects(..., readback=...)`. An operator may supply the
existing independently authenticated Git reader ephemerally; credentials must not
appear in source, command arguments, logs, receipts or persistent worker settings.
Local transfer alone is not an independent Git readback receipt.

Stage-only maintenance may run while the provider circuit is open. It cannot
enqueue URLs, submit captures, change provider state or modify pacing. Ordinary
paused worker preparation remains paused. The current public staging budget and
the native persistent-work reserve of 50 GiB still apply.

An explicitly approved one-shot native cohort can carry a frozen legacy inventory
baseline and an exact new-byte allowance, no larger than the unchanged 32 MiB
managed allowance. It must bind every requested object, SHA, byte count and URI;
extra objects and mismatched/oversized allowances fail before writes. This applies
only to stage-only maintenance, not normal worker preparation. Before/after file
metadata must prove that legacy staging was retained unchanged and only the exact
approved native paths were added. The configured global budget is not reset.

## Capture and verification

The existing owner alone queues and submits these approved targets under its
normal provider/canary/authentication controls and pacing. Native mirror replays
must match complete SHA-256 and byte count; XML text similarity is insufficient.
Retain the raw replay URI, exact original capture URI/timestamp and independent
verification evidence. Staged, ready, queued and submitted are not verified.

Withdrawn exact-payload tombstones take precedence over this path. No native or
photo payload is republished merely because a historical registration exists.

For an explicitly prioritized bounded cohort of at most six installed-approved,
ready native originals, use the same worker and owner lock:

```sh
python3 ops/wayback_worker.py /opt/swccg-ops/repos/swccg-wiki --minutes 12 --native-cohort-file approved-native-cohort.json
```

The file has the same `object_ids` list. This mode requires existing authenticated
owner credentials, never starts a second saver, and honors the saved provider
cooldown and authentication stop. It clamps submission pacing to at least 60
seconds and at most six attempts per run. An existing recovery probe outside the
cohort prevents the run before any provider request or probe mutation.

Only the selected URLs can be submitted, confirmed, checked from the backlog or
rechecked. Unrelated verification inbox entries remain unconsumed; mixed entries
retain their original bytes while eligible selected updates are applied. Staging
pruning is entirely disabled in this mode. The complete shared ledger remains
intact and unrelated queue entries retain their relative order. Default timer
behavior is unchanged when no native cohort is supplied.
