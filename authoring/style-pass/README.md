# Style pass (2026-10-15)

Re-applies SWCCG Wiki:Style guide to articles created before the guide existed.

1. Snapshot: every ns0 page created by Admin / Datacard Grok / Holocron Claude, minus decklists and card pages; lint with `style_lint.py` (per-page timeout; huge transcriptions hang the regex).
2. Drafts: helper agents follow `AGENT_BRIEF.md`, one batch of ~28 pages each, writing `out/<file>.wiki|.talk|.sum`.
3. `mkman.py man.json <batches>` builds a manifest (rejects dangling named refs).
4. Apply from Bill's PC: `style_apply.py man.json` (bot password env; 100 s per call; skips any page whose latest revision is newer than the snapshot; appends the Talk note).
5. Pages skipped because another editor changed them are redone against the current text (three-way merge) and applied the same way.

Deferred (Bill 2026-10-15, "articles only for now"): scripted pass on ~1,000 player/person pages — Sources list → refs on Tournament Results rows, "—" place cells → blank.
