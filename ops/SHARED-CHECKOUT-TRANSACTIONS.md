# Shared checkout transactions (Stories 407 and 410)

The installed Wayback job uses `/opt/swccg-ops/repos/swccg-wiki`.
The installed backup wrapper also passes that checkout to `nightly_backup.py`.
The archive owner's run lock does not protect the backup job's Git writes.

`gitsync.commit_and_push` now holds a separate repository-write lock through
fetch/reset, the caller's write callback, staging, commit and push. It invokes
`redo` on the first attempt as well as every rejected-push retry. The callback
must reread any shared tracked state before merging its own changes. The
callback must not submit captures or wait for an external archive operation.

The lock lives in the Git common directory, so a hard reset does not remove it
and worktrees sharing Git data coordinate correctly. It is an OS lock released
when the process exits. The metadata inbox and accepted-SPN journal remain
outside Git and are not touched by reset or rejected-push recovery.

Callers must not write tracked files before calling `commit_and_push`. The
nightly backup's page and file callbacks follow this contract. The Story 407
worker integration removes its preceding `write_done(repo, done)` and retains
its merge-on-fresh-state `redo` callback. Deploy the coordinated worker and
helper revisions together; the helper alone does not make an old caller's
unlocked writes safe.

Lock contention raises `RepositoryBusy` after a bounded wait. A failed backup
does not advance its checkpoint. Story 410's reconciliation work also adds
same-window retry/progress handling; this prerequisite does not claim that
the existing daily timer provides an earlier retry by itself.

Offline verification:

```
python -m unittest discover -s ops/tests -p test_gitsync_coordination.py -v
```

The fixtures use temporary local Git repositories. They cover cross-process
contention, first-attempt callback locking, rejected-push replay preserving
another writer, survival of an accepted-job journal outside Git, the nightly
no-prewrite boundary and an unchanged backup checkpoint after failure.
