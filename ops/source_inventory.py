"""Bounded exact-revision citation inventory; never an external-source fetcher.

Inventory is not source accuracy or external preservation. Literal candidates
and MediaWiki's rendered external links are recorded independently of checked
source receipts. Template-derived links need review because template rendering
is not pinned by the article revision alone. Existing markers/peer work are
updated only by compare-and-swap; immutable reports survive interruption.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import tempfile
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from preservation_backups import independent_receipt
from preservation_contracts import canonical_bytes, object_id, validate_backup_receipt
from preservation_registry import atomic_json, iter_records, object_state, public_url, registration_lock

MAX_REVISION_BYTES = 16 * 1024 * 1024
MAX_METADATA_BYTES = 1024 * 1024
MAX_CANDIDATES = 1000
MAX_REGISTRY_RECORDS = 10000
OWNER = "MemoryCoreChatGPT: Story 410 source-preservation reconciliation"
STORY = "https://github.com/swccg-guild/work/issues/410"
ARCHIVE_HOSTS = frozenset({"archive.org", "web.archive.org"})
LITERAL_URL = re.compile(r"(?:https?:)?//[^\s<>\[\]{}|\"']+", re.IGNORECASE)


def now():
    return datetime.now(timezone.utc).isoformat()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        # No cross-provider redirect can escape the hold or the read allowlist.
        raise ValueError("source inventory refuses redirects")


def safe_open(url: str, deadline: float):
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower()
    if host in ARCHIVE_HOSTS or host.endswith(".archive.org"):
        raise ValueError("Archive.org traffic is held")
    if (parts.scheme != "https" or host not in {"raw.githubusercontent.com", "wiki.swccg.com"}
            or parts.username or parts.password or parts.port not in {None, 443} or parts.fragment):
        raise ValueError("source inventory fetch is outside its Wiki/GitHub read allowlist")
    if host == "wiki.swccg.com" and parts.path != "/api.php":
        raise ValueError("source inventory may only read the Wiki API")
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise TimeoutError("source inventory deadline reached")
    request = urllib.request.Request(url, headers={"User-Agent": "swccg-source-inventory/1.0"})
    return urllib.request.build_opener(NoRedirect()).open(request, timeout=min(30, remaining))


def parse_revision(revision_id: int, deadline: float) -> dict:
    query = urllib.parse.urlencode({"action": "parse", "oldid": revision_id,
                                   "prop": "externallinks|templates", "format": "json", "formatversion": 2})
    with safe_open("https://wiki.swccg.com/api.php?" + query, deadline) as response:
        raw = response.read(MAX_REVISION_BYTES + 1)
    if len(raw) > MAX_REVISION_BYTES:
        raise ValueError("rendered link inventory exceeds response budget")
    data = json.loads(raw)
    if data.get("error") or data.get("warnings"):
        raise ValueError("Wiki parse did not produce an unambiguous inventory")
    parsed = data.get("parse", {})
    if parsed.get("revid") != revision_id or not isinstance(parsed.get("externallinks"), list):
        raise ValueError("Wiki parse does not bind the exact public revision")
    return parsed


def normalized_url(value: str) -> str | None:
    value = html.unescape(value)
    if value.startswith("//"):
        value = "https:" + value
    try:
        parts = urllib.parse.urlsplit(value)
        value = urllib.parse.urlunsplit((parts.scheme.lower(), parts.netloc, parts.path, parts.query, ""))
        return value if len(value) <= 8192 and public_url(value) else None
    except ValueError:
        return None


def candidates(text: str, parsed: dict) -> tuple[list[dict], list[str]]:
    links: dict[str, set[str]] = {}
    unresolved = []
    for origin, values in (("literal_wikitext", LITERAL_URL.findall(text)),
                           ("rendered_externallinks", parsed["externallinks"])):
        for value in values:
            if not isinstance(value, str):
                raise ValueError("rendered external-link candidate is malformed")
            url = normalized_url(value)
            if not url:
                # Never copy credential-bearing or non-public URLs into evidence.
                unresolved.append("rejected_url:" + hashlib.sha256(value.encode()).hexdigest())
                continue
            links.setdefault(url, set()).add(origin)
            if len(links) > MAX_CANDIDATES:
                raise ValueError("citation candidate count exceeds per-revision budget")
    if parsed.get("templates") or "{{" in text:
        unresolved.append("template_or_parser_expansion_needs_exact-source_review")
    if re.search(r"<(?:nowiki|pre|source|syntaxhighlight)\b", text, re.IGNORECASE):
        unresolved.append("literal_markup_needs_citation-context_review")
    return [{"url": url, "origins": sorted(origins)} for url, origins in sorted(links.items())], sorted(set(unresolved))


class SourceInventory:
    def __init__(self, directory: Path, registry: Path | None, *, parse=parse_revision,
                 readback=independent_receipt, registry_records=iter_records):
        self.directory, self.registry = Path(directory), registry
        self.parse, self.readback, self.registry_records = parse, readback, registry_records
        self.directory.mkdir(parents=True, exist_ok=True)

    def _existing_sources(self, subject, deadline):
        matches: dict[str, list[dict]] = {}
        if self.registry is None:
            return matches, True
        count, partial = 0, False
        for entry in self.registry_records(self.registry):
            count += 1
            if count > MAX_REGISTRY_RECORDS or time.monotonic() >= deadline:
                partial = True
                break
            request = entry["request"]
            if request["subject"] != subject:
                continue
            source = request["source"]
            url = normalized_url(source.get("primary_url", source["url"]))
            evidence = source.get("checked_evidence", {})
            state = object_state(request)
            if (url and state in {"ready", "awaiting_stage"} and evidence.get("path")
                    and re.fullmatch(r"[0-9a-f]{64}", evidence.get("sha256", ""))):
                matches.setdefault(url, []).append({"request_id": entry["request_id"],
                                                    "record": entry["path"], "state": state})
        return matches, partial

    def consume(self, path: Path, deadline: float) -> dict:
        with path.open("rb") as stream:
            raw = stream.read(MAX_METADATA_BYTES + 1)
        if len(raw) > MAX_METADATA_BYTES:
            raise ValueError("source marker exceeds metadata cap")
        marker = json.loads(raw)
        subject, storage = marker["subject"], marker["backup_storage"]
        if marker.get("schema_version") != 1 or subject.get("kind") != "wiki_revision" or path.stem != object_id(subject):
            raise ValueError("source marker does not bind an exact revision")
        if marker.get("state") != "source_inventory_required":
            return {"state": "peer_progress_preserved"}
        if subject["bytes"] > MAX_REVISION_BYTES:
            raise ValueError("revision exceeds source-inventory byte budget")
        with tempfile.TemporaryDirectory(prefix="source-inventory-", dir=self.directory) as temporary:
            restored = Path(temporary) / "revision.bin"
            proof = self.readback(subject, storage, restore_to=restored,
                                  fetch=lambda url: safe_open(url, deadline))
            if validate_backup_receipt(proof, subject):
                raise ValueError("revision readback did not verify")
            with restored.open("rb") as stream:
                payload = stream.read(MAX_REVISION_BYTES + 1)
            if len(payload) != subject["bytes"] or hashlib.sha256(payload).hexdigest() != subject["content_sha256"]:
                raise ValueError("restored revision bytes changed after verification")
        parsed = self.parse(subject["revision_id"], deadline)
        if parsed.get("revid") != subject["revision_id"]:
            raise ValueError("parser revision differs from backed-up revision")
        urls, unresolved = candidates(payload.decode("utf-8"), parsed)
        existing, partial = self._existing_sources(subject, deadline)
        for row in urls:
            host = (urllib.parse.urlsplit(row["url"]).hostname or "").lower()
            row.update(owner=OWNER, story=STORY, capture_submitted=False)
            row["existing_registrations"] = existing.get(row["url"], [])
            if host == "archive.org" or host.endswith(".archive.org"):
                row.update(state="provider_hold", continuation="Keep all Archive.org traffic paused until Bill explicitly resumes it.")
            elif row["existing_registrations"]:
                row.update(state="registered_source_backup", continuation="Retain existing exact-source proof and provider continuation; this inventory does not certify capture completion.")
            else:
                row.update(state="source_check_required", continuation="Check this cited source and exact payload; independently back it up and register it against this exact revision. Do not infer accuracy or a source hash from link text.")
        if partial:
            unresolved.append("registry_scan_partial_no_unmatched_source_assumed_absent")
        report = {"schema_version": 1, "subject": subject, "revision_readback": proof,
                  "observed_at": now(), "rendered_revision_id": parsed["revid"],
                  "sources": urls, "unresolved_constructs": sorted(set(unresolved)),
                  "source_accuracy_verified": False, "external_preservation_verified": False,
                  "archive_requests": 0, "owner": OWNER, "story": STORY}
        report_bytes = canonical_bytes(report) + b"\n"
        digest = hashlib.sha256(report_bytes).hexdigest()
        relative = "reports/" + path.stem + "/" + digest + ".json"
        with registration_lock(self.directory):
            if path.read_bytes() != raw:
                return {"state": "peer_progress_preserved"}
            atomic_json(self.directory / relative, report, create_only=True)
            updated = dict(marker, state="source_inventory_review_required" if unresolved else "source_inventory_recorded",
                           automatic_consumer_implemented=True, source_accuracy_verified=False,
                           source_inventory_report={"path": relative, "sha256": digest, "bytes": len(report_bytes)},
                           unresolved_source_count=sum(row["state"] != "registered_source_backup" for row in urls),
                           unresolved_construct_count=len(set(unresolved)),
                           source_inventory_continuation="Review the immutable source inventory report; resolve each owned source/check and template ambiguity. Inventory is not checked source accuracy or external preservation.")
            atomic_json(path, updated)
        return {"state": updated["state"], "sources": len(urls),
                "pending_sources": updated["unresolved_source_count"]}

    def run(self, *, limit=5, deadline=None):
        if type(limit) is not int or limit < 0:
            raise ValueError("source inventory task limit must be nonnegative")
        deadline = min(deadline or float("inf"), time.monotonic() + 60)
        completed, pending, failures, examined = 0, 0, [], 0
        with os.scandir(self.directory) as entries:
            for entry in entries:
                if completed + len(failures) >= limit or time.monotonic() >= deadline:
                    break
                examined += 1
                if examined > 50000:
                    break
                if not entry.name.endswith(".json") or not entry.is_file():
                    continue
                issue_path = self.directory / "consumer-issues" / entry.name
                previous = {}
                if issue_path.exists():
                    with issue_path.open("rb") as stream:
                        issue_raw = stream.read(MAX_METADATA_BYTES + 1)
                    if len(issue_raw) > MAX_METADATA_BYTES:
                        raise ValueError("consumer retry metadata exceeds cap")
                    previous = json.loads(issue_raw)
                    if previous.get("retry_after", 0) > time.time():
                        continue
                try:
                    row = self.consume(Path(entry.path), deadline)
                    if row["state"] != "peer_progress_preserved":
                        completed += 1
                        pending += row["pending_sources"]
                        issue_path.unlink(missing_ok=True)
                except Exception as error:
                    failures.append({"marker": entry.name, "reason": type(error).__name__})
                    attempts = previous.get("attempts", 0) + 1
                    atomic_json(issue_path, {"state": "source_inventory_retry", "attempts": attempts,
                                            "retry_after": time.time() + min(86400, 60 * 2 ** min(attempts, 11)),
                                            "reason": type(error).__name__, "owner": OWNER, "story": STORY,
                                            "continuation": "Retry the exact unchanged source marker after backoff; retain its backup and peer observations."})
        return {"source_inventory_processed_this_run": completed,
                "source_inventory_pending_sources_this_run": pending,
                "source_inventory_failures": failures,
                "source_inventory_automatic_consumer_implemented": True,
                "source_inventory_archive_requests": 0}
