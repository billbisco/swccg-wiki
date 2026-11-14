"""Durable, bounded public-version backup/reconciliation producer.

The inbox and spool are local durable work, never an independent Archive
submitter. Immutable Git payloads retain history; guarded latest-live projections
maintain the existing flat page/file mirrors consumed by other tools.
"""
from __future__ import annotations

import contextlib
import hashlib
import json
import os
import re
import shutil
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from backup_spool import Spool, BackupDeferred, DEFAULT_WORK, DISK_RESERVE
from backup_projection import Projection
from gitsync import commit_and_push, git, RepositoryBusy
from preservation_backups import revision_artifact, independent_receipt
from preservation_contracts import canonical_bytes, object_id, registration_object_id, validate_backup_receipt
from preservation_registry import atomic_json, iter_records, object_state, register, validate_request

API = "https://wiki.swccg.com/api.php"
SERVER_OWNER = "server-wayback-owner"


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@contextlib.contextmanager
def backup_owner(directory: Path):
    """Single spool/inbox owner; independent of the short shared Git lock."""
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "backup-owner.lock").open("a+b") as stream:
        if not stream.tell():
            stream.write(b"0")
            stream.flush()
        stream.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            raise BackupDeferred("another backup owner is running; pending work retained") from None
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)


class Inbox:
    def __init__(self, directory: Path):
        self.directory = directory
        for part in ("tasks", "completed", "issues"):
            (directory / part).mkdir(parents=True, exist_ok=True)

    def add(self, task: dict) -> str:
        key = hashlib.sha256(canonical_bytes(task)).hexdigest()
        atomic_json(self.directory / "tasks" / (key + ".json"), task, create_only=True)
        return key

    def pending(self, kind=None, *, due_only=False):
        # scandir is incremental; never load all historical version tasks.
        with os.scandir(self.directory / "tasks") as entries:
            for entry in entries:
                if entry.name.endswith(".json") and not (self.directory / "completed" / entry.name).exists():
                    if due_only:
                        issue = self.directory / "issues" / entry.name
                        if issue.exists() and json.loads(issue.read_text(encoding="utf-8")).get("retry_after", 0) > time.time():
                            continue
                    task = json.loads(Path(entry.path).read_text(encoding="utf-8"))
                    if kind is None or task["kind"] == kind:
                        yield entry.name[:-5], task

    def complete(self, key: str, evidence: dict) -> None:
        atomic_json(self.directory / "completed" / (key + ".json"), evidence)
        (self.directory / "issues" / (key + ".json")).unlink(missing_ok=True)

    def issue(self, key: str, reason: str) -> None:
        path = self.directory / "issues" / (key + ".json")
        previous = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        attempts = previous.get("attempts", 0) + 1
        atomic_json(self.directory / "issues" / (key + ".json"),
                    {"state": "needs_reconciliation", "reason": reason,
                     "attempts": attempts, "retry_after": time.time() + min(86400, 60 * 2 ** min(attempts, 11)),
                     "owner": "nightly-backup", "continuation": "retry the exact durable task in the next existing run"})

    def health_counts(self, *, scan_limit=50000, seconds=2):
        deadline = time.monotonic() + seconds
        pending, failed, oldest, scanned, partial = 0, 0, None, 0, False
        with os.scandir(self.directory / "tasks") as entries:
            for entry in entries:
                if scanned >= scan_limit or time.monotonic() >= deadline:
                    partial = True
                    break
                scanned += 1
                if not entry.name.endswith(".json") or (self.directory / "completed" / entry.name).exists():
                    continue
                pending += 1
                failed += (self.directory / "issues" / entry.name).exists()
                created = entry.stat().st_mtime
                oldest = created if oldest is None else min(oldest, created)
        return {"pending_task_count": pending, "failed_pending_task_count": failed,
                "oldest_pending_age_seconds_observed": None if oldest is None else max(0, int(time.time() - oldest)),
                "task_count_partial": partial, "task_metadata_scanned": scanned}


def discover_changes(api, inbox: Inbox, *, since: str | None = None, max_pages=10) -> dict:
    """Persist every task before advancing a bounded RC discovery cursor."""
    path = inbox.directory / "recentchanges.json"
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if not state.get("scan"):
        start = utcnow()
        prior = since or state.get("discovered_through") or (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        state["scan"] = {"start": start, "end": prior, "continue": {}}
    scan = state["scan"]
    for _ in range(max_pages):
        result = api({"action": "query", "list": "recentchanges", "rcstart": scan["start"],
                      "rcend": scan["end"], "rcdir": "older", "rcprop": "title|ids|loginfo|timestamp",
                      "rctype": "edit|new|log", "rclimit": "max", **scan["continue"]})
        for row in result.get("query", {}).get("recentchanges", []):
            if any(flag in row for flag in ("suppressed", "titlehidden")):
                continue
            if row.get("revid") and row.get("title"):
                inbox.add({"kind": "revision", "revision_id": row["revid"], "title": row["title"]})
            if row.get("logtype") == "upload" and row.get("title"):
                inbox.add({"kind": "file_history", "title": row["title"],
                           "upload_log_id": row.get("logid"), "observed_at": row.get("timestamp")})
            if row.get("logtype") == "move":
                title = (row.get("logparams") or {}).get("target_title")
                if title:
                    inbox.add({"kind": "page_history", "title": title})
        continuation = result.get("continue")
        if not continuation:
            state = {"discovered_through": scan["start"], "scan": None}
        else:
            scan["continue"] = continuation
        atomic_json(path, state)
        if not continuation:
            break
    return state


def reconcile_inventory(api, inbox: Inbox, *, pages=2) -> dict:
    """Cycle every public namespace, including Talk and File descriptions.

    Each discovered title drains its public revision/file history through
    separate bounded tasks. A completed scan starts a new generation, so a
    missed manual change is found even beyond RecentChanges retention.
    """
    path = inbox.directory / "inventory.json"
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if not state.get("namespaces"):
        data = api({"action": "query", "meta": "siteinfo", "siprop": "namespaces"})
        state = {"namespaces": sorted(int(row["id"]) for row in data["query"]["namespaces"].values()
                                      if int(row["id"]) >= 0), "index": 0, "continue": {}, "generation": 1}
    for _ in range(pages):
        namespace = state["namespaces"][state["index"]]
        data = api({"action": "query", "list": "allpages", "apnamespace": namespace,
                    "aplimit": 25, **state["continue"]})
        for row in data.get("query", {}).get("allpages", []):
            inbox.add({"kind": "page_history", "title": row["title"], "generation": state["generation"]})
            if namespace == 6:
                inbox.add({"kind": "file_history", "title": row["title"], "generation": state["generation"]})
        state["continue"] = data.get("continue", {})
        if not state["continue"]:
            state["index"] += 1
            if state["index"] == len(state["namespaces"]):
                state["index"] = 0
                state["generation"] += 1
        atomic_json(path, state)
    return state


class Producer:
    def __init__(self, api, pages_repo: Path, files_repo: Path, work=DEFAULT_WORK,
                 registry: Path | None = None, *, spool=None, commit=commit_and_push,
                 readback=independent_receipt, remote_head=None, max_run_bytes=256 * 1024 * 1024,
                 projection_factory=Projection):
        self.api, self.pages_repo, self.files_repo = api, pages_repo, files_repo
        self.inbox = Inbox(Path(work) / "inbox")
        self.source_inventory = Path(work) / "source-inventory"
        self.source_inventory.mkdir(parents=True, exist_ok=True)
        self.spool = spool or Spool(Path(work) / "spool")
        self.registry = registry
        self.commit, self.readback = commit, readback
        self.remote_head = remote_head or self._remote_head
        self.max_run_bytes, self.processed_bytes = max_run_bytes, 0
        self.deadline = None
        self.projections = {pages_repo: projection_factory(pages_repo, "page"),
                            files_repo: projection_factory(files_repo, "file")} if projection_factory else {}

    def check_deadline(self):
        if self.deadline is not None and time.monotonic() >= self.deadline:
            raise BackupDeferred("absolute producer deadline reached; task remains pending")

    @staticmethod
    def _remote_head(repository):
        value = git(repository, "ls-remote", "origin", "refs/heads/main", capture=True).stdout.split()[0]
        if not re.fullmatch(r"[0-9a-f]{40}", value):
            raise ValueError("remote immutable backup head is absent")
        return value

    def _save(self, artifact, repository: Path, projection=None):
        self.check_deadline()
        receipt = self.spool.receipt(artifact.subject)
        known_receipt = receipt is not None and not validate_backup_receipt(receipt, artifact.subject)
        if projection is None and known_receipt:
            return receipt
        if self.processed_bytes + artifact.subject["bytes"] > self.max_run_bytes:
            raise BackupDeferred("per-run backup byte budget reached; exact task retained")
        artifact = self.spool.save_artifact(artifact)
        if shutil.disk_usage(repository).free < artifact.subject["bytes"] * 2 + DISK_RESERVE:
            raise BackupDeferred("Git backup volume reserve reached; spool and task retained")
        # Binary source I/O has finished. Only verified disk copies happen
        # inside the shared Git reset/write/push transaction.
        def write():
            paths = artifact.write(repository)
            if projection:
                projector, observed = projection
                paths += projector.write(artifact, observed)
            return paths
        for attempt in range(3):
            try:
                self.commit(repository, [], "preserve exact public version: " + object_id(artifact.subject),
                            write)
                break
            except RepositoryBusy:
                if attempt == 2:
                    raise
                time.sleep(1)
        commit = self.remote_head(repository)
        repository_name = "https://github.com/billbisco/swccg-wiki" if repository == self.pages_repo else "https://github.com/billbisco/swccg-wiki-files"
        metadata = artifact.metadata_bytes()
        storage = {"kind": "git", "repository": repository_name, "commit": commit,
                   "path": artifact.payload_path, "metadata_path": artifact.metadata_path,
                   "metadata_bytes": len(metadata), "metadata_sha256": hashlib.sha256(metadata).hexdigest()}
        # Updating the compatible flat projection does not change the exact
        # immutable payload/version already independently restored. Retain its
        # stable receipt and registration observation rather than manufacturing
        # a fresh verified_at/commit on every reconciliation cycle.
        if not known_receipt:
            receipt = self.readback(artifact.subject, storage)
            self.spool.record_receipt(receipt)
            atomic_json(self.spool.directory / "backup-progress.json",
                        {"last_actual_verified_backup_at": receipt["verification"]["verified_at"],
                         "subject": artifact.subject, "storage": receipt["storage"]})
        self.processed_bytes += artifact.subject["bytes"]
        if projection and projection[0].deferred_reason:
            # The exact version backup succeeded independently. Its compatible
            # current projection has a separate visible retry, not a silent
            # completion or an inventory-cycle-length wait.
            task = {"kind": "page_history" if repository == self.pages_repo else "file_history",
                    "title": artifact.subject["title"], "projection_retry": time.time_ns()}
            key = self.inbox.add(task)
            self.inbox.issue(key, projection[0].deferred_reason)
        return receipt

    def _register_file(self, artifact, receipt):
        if self.registry is None:
            return None
        source = {"url": artifact.subject["original_version_url"],
                  "sha256": artifact.subject["content_sha256"], "bytes": artifact.subject["bytes"],
                  "checked_evidence": {"path": "https://raw.githubusercontent.com/" + receipt["storage"]["repository"].removeprefix("https://github.com/") + "/" + receipt["storage"]["commit"] + "/" + receipt["storage"]["metadata_path"],
                                       "sha256": receipt["storage"]["metadata_sha256"],
                                       "kind": "public-wiki-imageinfo-and-original-byte-hash",
                                       "wiki_sha1": artifact.provenance.get("sha1"),
                                       "upload_timestamp": artifact.subject["upload_timestamp"]}}
        request = {"schema_version": 1, "subject": artifact.subject, "source": source,
                   "backup_receipt": receipt, "source_backup_receipt": receipt,
                   "readiness": {"ready": True, "reason": "public exact original independently restored from Git",
                                 "stage_bytes": 0},
                   "owner": SERVER_OWNER, "continuation": "existing server owner validates public bytes and queues once within its budgets",
                   "approval_scope": {"ticket": 410, "purpose": "Bill-approved public Wiki version preservation"}}
        errors = validate_request(request)
        if errors:
            raise ValueError("; ".join(errors))
        try:
            result = register(self.registry, request)
            if result["state"] != "superseded":
                return result
        except ValueError:
            # A separately checked client can have registered this immutable
            # original first. That is not a failed backup or a reason to demote
            # its readiness, replace provenance, or reset its generation.
            pass
        key = registration_object_id(request["subject"], request["source"])
        for _ in range(3):
            existing = next(iter_records(self.registry, object_ids={key}), None)
            if existing is None:
                raise BackupDeferred("conflicting registration requires owned reconciliation")
            previous = existing["request"]
            if (previous["subject"] != request["subject"] or
                    any(previous["source"][name] != source[name] for name in ("url", "sha256", "bytes")) or
                    object_state(previous) not in {"ready", "awaiting_stage"}):
                raise BackupDeferred("existing exact-version registration needs backup/source repair; peer observation retained")
            result = register(self.registry, previous)
            if result["state"] != "superseded":
                return {**result, "reused_existing_observation": True}
        raise BackupDeferred("registration advanced repeatedly; retry without overwriting peer observations")

    def _mark_source_inventory(self, artifact, receipt):
        """Text backup is not proof that this revision's citations are preserved."""
        path = self.source_inventory / (object_id(artifact.subject) + ".json")
        atomic_json(path, {"schema_version": 1, "subject": artifact.subject,
                           "state": "source_inventory_required", "owner": "MemoryCoreChatGPT: Story 410 source-preservation reconciliation",
                           "story": "https://github.com/swccg-guild/work/issues/410",
                           "automatic_consumer_implemented": False,
                           "backup_storage": receipt["storage"],
                           "continuation": "inventory citations in this exact revision; check each exact source payload and independent backup, then register source mappings with the existing owner",
                           "capture_submitted": False}, create_only=True)

    def pending_source_inventory(self):
        count = 0
        scanned, partial, deadline = 0, False, time.monotonic() + 2
        with os.scandir(self.source_inventory) as entries:
            for entry in entries:
                if scanned >= 50000 or time.monotonic() >= deadline:
                    partial = True
                    break
                scanned += 1
                if entry.name.endswith(".json"):
                    row = json.loads(Path(entry.path).read_text(encoding="utf-8"))
                    count += row.get("state") == "source_inventory_required"
        return {"source_inventory_required": count, "source_inventory_count_partial": partial,
                "source_inventory_owner": "MemoryCoreChatGPT: Story 410 source-preservation reconciliation",
                "source_inventory_story": "https://github.com/swccg-guild/work/issues/410",
                "source_inventory_automatic_consumer_implemented": False}

    def due_tasks(self):
        """Favor short edit events without starving originals and history."""
        kinds = ("revision", "file_history", "file_usage", "page_history")
        pending = {kind: iter(self.inbox.pending(kind, due_only=True)) for kind in kinds}
        schedule = ("revision",) * 4 + ("file_history",) * 2 + ("file_usage", "page_history")
        while pending:
            for kind in schedule:
                if kind not in pending:
                    continue
                try:
                    yield next(pending[kind])
                except StopIteration:
                    del pending[kind]

    def task(self, key: str, task: dict) -> dict:
        kind = task["kind"]
        if kind in ("revision", "page_history"):
            projector = self.projections.get(self.pages_repo)
            observed = projector.observe(task["title"]) if projector else None
            query = {"action": "query", "prop": "revisions|info", "rvprop": "ids|timestamp|sha1|content|contentmodel",
                     "rvslots": "main", "rvlimit": 10}
            if kind == "revision":
                query.update(revids=str(task["revision_id"]))
                query.pop("rvlimit")
            else:
                query.update(titles=task["title"], **task.get("continue", {}))
            data = self.api(query)
            if data.get("query", {}).get("badrevids"):
                raise BackupDeferred("exact revision is no longer publicly available")
            receipts = []
            pages = data.get("query", {}).get("pages", [])
            for page in pages:
                if page.get("missing") or page.get("invalid"):
                    raise BackupDeferred("public title is missing; historical backups retained")
                for revision in page.get("revisions", []):
                    self.check_deadline()
                    artifact = revision_artifact(page, revision)
                    projection = (projector, observed) if observed and page["title"] == observed["title"] and page.get("lastrevid") == revision["revid"] else None
                    receipt = self._save(artifact, self.pages_repo, projection)
                    self._mark_source_inventory(artifact, receipt)
                    receipts.append({"subject": artifact.subject, "storage": receipt["storage"]})
                    self.spool.release(self.spool.save_artifact(artifact))
            if not receipts:
                raise BackupDeferred("no eligible public revision returned")
        elif kind == "file_history":
            projector = self.projections.get(self.files_repo)
            observed = projector.observe(task["title"]) if projector else None
            data = self.api({"action": "query", "titles": task["title"], "prop": "imageinfo",
                             "iiprop": "timestamp|url|size|mime|sha1|user", "iilimit": 5,
                             **task.get("continue", {})})
            receipts = []
            for page in data.get("query", {}).get("pages", []):
                if not page.get("imageinfo"):
                    raise BackupDeferred("public original/version metadata is unavailable")
                for index, info in enumerate(page["imageinfo"]):
                    self.check_deadline()
                    if type(info.get("size")) is int and self.processed_bytes + info["size"] > self.max_run_bytes:
                        raise BackupDeferred("per-run original byte budget reached before download")
                    projection = (projector, observed) if observed and page["title"] == observed["title"] and index == 0 and not task.get("continue", {}).get("iicontinue") else None
                    artifact = self.spool.file(page["title"], info, require_payload=projection is not None,
                                               deadline=self.deadline)
                    receipt = self._save(artifact, self.files_repo, projection)
                    registration = self._register_file(artifact, receipt)
                    receipts.append({"subject": artifact.subject, "storage": receipt["storage"],
                                     "registration": registration})
                    self.spool.release(artifact)
            if not task.get("continue"):
                self.inbox.add({**task, "kind": "file_usage"})
        elif kind == "file_usage":
            data = self.api({"action": "query", "titles": task["title"], "prop": "fileusage",
                             "fulimit": 50, **task.get("continue", {})})
            projector = self.projections.get(self.files_repo)
            for page in data.get("query", {}).get("pages", []):
                if page.get("missing"):
                    raise BackupDeferred("file usage title is no longer public")
                if projector:
                    self.commit(self.files_repo, [], "nightly backup: public file usage mappings",
                                lambda: projector.usage(page["title"], page.get("fileusage", [])))
            receipts = [{"kind": "file_usage", "remote_commit": self.remote_head(self.files_repo)}]
        else:
            raise ValueError("unknown backup task kind")
        if data.get("continue"):
            # Durable continuation before the current chunk is marked done.
            self.inbox.add({**task, "continue": data["continue"]})
        evidence = {"state": "independently_backed_up", "versions": receipts, "completed_at": utcnow()}
        self.inbox.complete(key, evidence)
        return evidence

    def run(self, *, since=None, task_limit=100, seconds=1800) -> dict:
        deadline = time.monotonic() + seconds
        self.deadline = deadline
        # Discovery completion is not backup completion; failures remain in
        # the durable inbox and cannot disappear behind a timestamp checkpoint.
        discovery_failures = []
        for name, discover in (("recentchanges", lambda: discover_changes(self.api, self.inbox, since=since)),
                               ("inventory", lambda: reconcile_inventory(self.api, self.inbox))):
            try:
                discover()
            except Exception as error:
                discovery_failures.append({"source": name, "reason": type(error).__name__})
                atomic_json(self.inbox.directory / (name + "-failure.json"),
                            {"state": "needs_reconciliation", "reason": type(error).__name__ + ": " + str(error),
                             "observed_at": utcnow(), "continuation": "retry discovery on next existing run; cursors were not advanced"})
        completed, failures = 0, []
        for key, task in self.due_tasks():
            if completed + len(failures) >= task_limit or time.monotonic() >= deadline:
                break
            try:
                self.task(key, task)
                completed += 1
            except Exception as error:
                self.inbox.issue(key, type(error).__name__ + ": " + str(error))
                failures.append({"task": key, "reason": type(error).__name__})
        counts = self.inbox.health_counts()
        progress = self.spool.directory / "backup-progress.json"
        last_verified = json.loads(progress.read_text(encoding="utf-8"))["last_actual_verified_backup_at"] if progress.exists() else None
        status = {"completed_tasks": completed, "failed_tasks": failures,
                  "discovery_failures": discovery_failures,
                  **self.pending_source_inventory(), **counts,
                  "last_actual_verified_backup_at": last_verified,
                  "pending": counts["pending_task_count"] > 0 or counts["task_count_partial"],
                  "archive_submitted": False, "observed_at": utcnow()}
        atomic_json(self.inbox.directory / "health.json", status)
        return status
