# Wiki image preservation — Story #382

Run on Bill's PC; the server continues serving its existing public originals. The ledger is SQLite, not an image mirror. Each payload is hashed in 128 KiB chunks; raw payloads are not stored by the normal runner. Refuse startup below 20 GiB PC free space. Source capacity checks remain necessary for wiki operation, but this job adds no server image staging and no server scheduler.

From the repository root (Python 3 standard library):

```
python -m tools.image_preservation inventory --data C:/Users/gythe/Documents/Codex/wiki-image-backup382
python -m tools.image_preservation histories --data C:/Users/gythe/Documents/Codex/wiki-image-backup382
python -m tools.image_preservation batch --data C:/Users/gythe/Documents/Codex/wiki-image-backup382 --limit 12
python -m unittest discover -s tests -p test_image_preservation.py -v
```

`inventory` checkpoints MediaWiki continuation after each page. `histories` checks public history, usage across namespaces and description-page provenance, 25 filenames at a time. File descriptions stay local; reports do not dump arbitrary source text into public evidence. Current and older version identities remain distinct. Non-image uploads are recorded but do not inflate image coverage.

`batch` uses an OS lock and serial Wayback requests, reuses captures before saving and leaves at least 30 seconds between saves. It checks the exact original URL, inventoried SHA-1, byte size, signature and SHA-256 of source versus archived `id_` payload. A capture URL alone never marks verification. External throttling stops the bounded batch and records Retry-After. Verified versions are never resubmitted on resume. Failed/unknown states stay visible. Current images changed since enumeration are rejected and require a new inventory/version reconciliation; historical public URLs can then preserve the earlier version.

This is an initial, **unfinished** implementation. Final delta reconciliation, complete history/usage scan, controlled retries across batches, exact File-page link delivery, recovery sampling and existing-upload/backup integration remain Story acceptance work. No 100% backup claim until all gates pass. Do not run overlapping capture batches or another archive-saving process against the same pilot URLs.

Initial actual state, launch commands and local sessions are in the #382 ticket handoff. Continue those jobs; do not duplicate a live inventory or save batch. Keep bulk metadata on the PC and publish compressed inventory/verification ledgers plus concise coverage evidence. Keep any later recovery sample under a 1 GiB cap with the same 20 GiB free-space reserve.
