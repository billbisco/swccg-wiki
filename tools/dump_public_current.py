#!/usr/bin/env python3
"""Export exact public current wiki revisions with resumable bounded API batches.

Authoritative payloads use numeric page IDs. INDEX.tsv retains old canonical
paths as compatibility aliases; per-namespace JSONL records identify the exact
payload/revision/hash to restore. The membership inventory is observed over an
API scan window, not an atomic database snapshot. No credentials or Archive.org
requests are used. Checkpoints and partial payloads remain outside tracked pages.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
MAX_FILE = 95 * 1024 * 1024
RESERVE = 1024 * 1024 * 1024


class ExportError(RuntimeError):
    pass


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def request_api(params):
    query = {"format": "json", "formatversion": "2", "maxlag": "5", **params}
    request = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(query),
        headers={"User-Agent": "swccg-public-backup/1.0 (https://github.com/billbisco/swccg-wiki)"},
    )
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                result = json.load(response)
            if "error" not in result:
                return result
            if result["error"].get("code") not in {"maxlag", "readonly", "ratelimited"}:
                raise ExportError("MediaWiki rejected the public export query")
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504}:
                raise ExportError(f"Public wiki API HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError):
            pass
        if attempt < 5:
            time.sleep(min(30, 2 ** attempt))
    raise ExportError("Public wiki API retry budget exhausted; checkpoint retained")


def atomic(path: Path, data: bytes):
    if len(data) > MAX_FILE:
        raise ExportError("Generated file exceeds the regular-Git safety limit")
    path.parent.mkdir(parents=True, exist_ok=True)
    if shutil.disk_usage(path.parent).free < RESERVE + max(len(data), 4096) + 65536:
        raise ExportError("Local disk reserve reached; checkpoint retained")
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    os.replace(temporary, path)


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def namespaces(data):
    rows = data.get("query", {}).get("namespaces")
    if not isinstance(rows, (dict, list)):
        raise ExportError("Missing public namespace inventory")
    values = rows.values() if isinstance(rows, dict) else rows
    return sorted({int(row["id"]) for row in values if int(row["id"]) >= 0})


def decode_page(page):
    page_id = int(page.get("pageid", 0))
    namespace = int(page.get("ns", -1))
    if page_id <= 0 or namespace < 0 or not isinstance(page.get("title"), str):
        raise ExportError("Invalid public page identity")
    record = {"page_id": page_id, "namespace": namespace, "title": page["title"]}
    revisions = page.get("revisions", [])
    if not revisions:
        return {**record, "excluded": "no_public_revision_returned"}, None
    if len(revisions) != 1:
        raise ExportError("Expected one revision per public page")
    revision = revisions[0]
    slot = revision.get("slots", {}).get("main", {})
    if any(flag in revision or flag in slot for flag in ("texthidden", "sha1hidden", "suppressed")):
        return {**record, "excluded": "revision_content_not_public"}, None
    text = slot.get("content") if "content" in slot else revision.get("content")
    if not isinstance(text, str):
        raise ExportError("Missing visible revision content; refusing partial success")
    payload = text.encode("utf-8")
    sha1 = hashlib.sha1(payload).hexdigest()
    if revision.get("sha1", "").lower() != sha1 or revision.get("size") != len(payload):
        raise ExportError("MediaWiki content SHA1/size does not match exact UTF-8 payload")
    record.update({
        "revision_id": int(revision["revid"]), "parent_id": int(revision.get("parentid", 0)),
        "timestamp": revision["timestamp"], "mediawiki_sha1": sha1,
        "mediawiki_size": len(payload), "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "content_model": slot.get("contentmodel", revision.get("contentmodel", "unknown")),
        "payload_path": f"pages/public-current/payloads/{page_id}.wiki",
    })
    return record, payload


def closing_identity(page):
    record = {"page_id": int(page["pageid"]), "namespace": int(page["ns"]), "title": page["title"]}
    revisions = page.get("revisions", [])
    if not revisions:
        return {**record, "excluded": "no_public_revision_returned"}
    revision = revisions[0]
    slot = revision.get("slots", {}).get("main", {})
    if any(flag in revision or flag in slot for flag in ("texthidden", "sha1hidden", "suppressed")):
        return {**record, "excluded": "revision_content_not_public"}
    if len(revisions) != 1 or not revision.get("sha1") or not isinstance(revision.get("size"), int):
        raise ExportError("Missing public closing revision metadata")
    return {**record, "revision_id": int(revision["revid"]), "mediawiki_sha1": revision["sha1"].lower(),
            "mediawiki_size": revision["size"]}


class Exporter:
    def __init__(self, root, fetch=request_api, state_dir=None, batch_size=50):
        self.root = Path(root).resolve()
        self.fetch = fetch
        self.state_dir = Path(state_dir) if state_dir else self.root / ".git" / "wiki-public-export"
        self.state_path = self.state_dir / "state.json"
        self.batch_size = batch_size
        if not 1 <= batch_size <= 50:
            raise ExportError("Anonymous content batches must be between 1 and 50")
        self.state = None

    def save(self):
        atomic(self.state_path, json_bytes(self.state))

    def call(self, params):
        result = self.fetch(params)
        if "error" in result:
            raise ExportError("Public wiki API returned an error; checkpoint retained")
        return result

    def content_params(self):
        return {"action": "query", "prop": "revisions", "rvslots": "main",
                "rvprop": "ids|timestamp|sha1|size|content|contentmodel"}

    def store_batch(self, pages):
        records = []
        for page in pages:
            record, payload = decode_page(page)
            if payload is not None:
                atomic(self.state_dir / "payloads" / str(record["page_id"]), payload)
            records.append(record)
        self.store_records(records)

    def store_records(self, records):
        number = self.state["batches"]
        atomic(self.state_dir / "batches" / f"{number:08}.json", json_bytes(records))
        self.state["batches"] += 1

    def records(self):
        result = {}
        for number in range(self.state["batches"]):
            rows = json.loads((self.state_dir / "batches" / f"{number:08}.json").read_text(encoding="utf-8"))
            result.update({row["page_id"]: row for row in rows})
        return result

    def scan(self):
        ids = self.state["namespaces"]
        while self.state["namespace_position"] < len(ids):
            if shutil.disk_usage(self.root).free < RESERVE:
                raise ExportError("Local disk reserve reached; checkpoint retained")
            namespace = ids[self.state["namespace_position"]]
            params = {**self.content_params(), "generator": "allpages", "gapnamespace": namespace,
                      "gaplimit": self.batch_size, **self.state["continuation"]}
            response = self.call(params)
            if "pages" not in response.get("query", {}):
                # Empty namespaces legitimately omit query; only accept that on
                # their first/empty response, never a malformed continued batch.
                if self.state["continuation"]:
                    raise ExportError("Continued page batch omitted its query")
                pages = []
            else:
                pages = response["query"]["pages"]
            self.store_batch(pages)
            self.state["continuation"] = response.get("continue", {})
            if not self.state["continuation"]:
                self.state["namespace_position"] += 1
                print(f"Finished public namespace {namespace}", flush=True)
            self.save()
        self.state.update(phase="close", closing_position=0, closing_continuation={}, closing_batches=0)
        self.save()

    def close_inventory(self):
        current = namespaces(self.call({"action": "query", "meta": "siteinfo", "siprop": "namespaces"}))
        if current != self.state["namespaces"]:
            raise ExportError("Namespace set changed during export; start a fresh export")
        while self.state["closing_position"] < len(current):
            namespace = current[self.state["closing_position"]]
            response = self.call({"action": "query", "generator": "allpages", "gapnamespace": namespace,
                                  "gaplimit": 500, "prop": "revisions", "rvslots": "main",
                                  "rvprop": "ids|timestamp|sha1|size", **self.state["closing_continuation"]})
            rows = response.get("query", {}).get("pages", [])
            if not isinstance(rows, list) or (not rows and self.state["closing_continuation"]):
                raise ExportError("Missing closing public page inventory")
            clean = []
            for row in rows:
                if int(row.get("pageid", 0)) <= 0 or int(row.get("ns", -1)) != namespace:
                    raise ExportError("Invalid closing page inventory identity")
                clean.append(closing_identity(row))
            number = self.state["closing_batches"]
            atomic(self.state_dir / "closing" / f"{number:08}.json", json_bytes(clean))
            self.state["closing_batches"] += 1
            self.state["closing_continuation"] = response.get("continue", {})
            if not self.state["closing_continuation"]:
                self.state["closing_position"] += 1
            self.save()
        self.state.update(phase="reconcile", inventory_closed_at=utcnow())
        self.save()

    def closing_rows(self):
        result = {}
        for number in range(self.state["closing_batches"]):
            rows = json.loads((self.state_dir / "closing" / f"{number:08}.json").read_text(encoding="utf-8"))
            result.update({row["page_id"]: row for row in rows})
        return result

    def reconcile(self):
        known, closing = self.records(), self.closing_rows()
        new_exclusions = [identity for page_id, identity in closing.items() if page_id not in known and "excluded" in identity]
        if new_exclusions:
            self.store_records(new_exclusions)
            self.save()
            known.update({record["page_id"]: record for record in new_exclusions})
        keys = ("revision_id", "mediawiki_sha1", "mediawiki_size")
        missing = sorted(page_id for page_id, identity in closing.items() if "excluded" not in identity and (
            page_id not in known or "excluded" in known[page_id] or
            any(known[page_id].get(key) != identity.get(key) for key in keys)))
        for start in range(0, len(missing), self.batch_size):
            wanted = missing[start:start + self.batch_size]
            response = self.call({**self.content_params(), "pageids": "|".join(map(str, wanted))})
            pages = response.get("query", {}).get("pages")
            if not isinstance(pages, list):
                raise ExportError("Missing reconciliation page batch")
            if {page.get("pageid") for page in pages} != set(wanted):
                raise ExportError("Closing page inventory changed during reconciliation; checkpoint retained")
            self.store_batch(pages)
            self.save()
        self.state.update(phase="emit", capture_closed_at=utcnow())
        self.save()

    def aliases(self):
        path = self.root / "pages" / "INDEX.tsv"
        result = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                title, tab, relative = line.partition("\t")
                relative = relative.replace("\\", "/")
                if not tab or not relative.startswith("pages/") or ".." in Path(relative).parts:
                    raise ExportError("Unsafe existing canonical INDEX mapping")
                resolved = (self.root / relative).resolve()
                if not resolved.is_relative_to(self.root):
                    raise ExportError("Canonical alias leaves repository")
                portable = resolved.relative_to(self.root).as_posix().casefold()
                if not portable.startswith("pages/"):
                    raise ExportError("Canonical alias leaves pages directory")
                if portable == "pages/public-current" or portable.startswith("pages/public-current/"):
                    raise ExportError("Canonical INDEX alias enters reserved public-current storage")
                result[title] = relative
        return result

    def output_path(self, relative):
        path = self.root / relative
        if path.is_symlink() or not path.resolve().is_relative_to(self.root):
            raise ExportError("Generated output path leaves repository")
        if path.resolve().relative_to(self.root).as_posix().casefold() != Path(relative).as_posix().casefold():
            raise ExportError("Generated output path follows a redirected repository directory")
        return path

    def emit(self):
        records, closing, aliases = self.records(), self.closing_rows(), self.aliases()
        if not closing.keys() <= records.keys():
            raise ExportError("Closing inventory is not fully accounted for")
        by_path = {}
        numeric_alias_replacements = {}
        for identity in closing.values():
            numeric_alias = f"pages/by-id/{identity['page_id']}.wiki"
            path = aliases.get(identity["title"], numeric_alias)
            if path.startswith("pages/by-id/") and path != numeric_alias:
                numeric_alias_replacements[identity["title"]] = path
                path = numeric_alias
                aliases[identity["title"]] = path
            by_path.setdefault(path, []).append(identity["title"])
        collisions = {path: titles for path, titles in by_path.items() if len(titles) > 1}
        namespace_records = {namespace: [] for namespace in self.state["namespaces"]}
        index, excluded, total_bytes = [], [], 0
        for page_id in sorted(closing):
            identity = closing[page_id]
            record = {**records[page_id], **{key: identity[key] for key in ("page_id", "namespace", "title")}}
            reason = identity.get("excluded") or record.get("excluded")
            if reason:
                excluded.append({key: identity[key] for key in ("page_id", "namespace", "title")} | {"excluded": reason})
                continue
            payload = (self.state_dir / "payloads" / str(page_id)).read_bytes()
            if len(payload) != record["bytes"] or hashlib.sha256(payload).hexdigest() != record["sha256"]:
                raise ExportError("Checkpoint payload failed independent size/SHA256 readback")
            destination = self.output_path(record["payload_path"])
            atomic(destination, payload)
            canonical = aliases.get(record["title"], f"pages/by-id/{page_id}.wiki")
            canonical_output = self.output_path(canonical)
            record["canonical_path"] = canonical
            if canonical not in collisions and canonical != record["payload_path"]:
                atomic(canonical_output, payload)
            index.append((record["title"], canonical))
            namespace_records[record["namespace"]].append(record)
            total_bytes += len(payload)
        metadata = []
        for namespace, rows in namespace_records.items():
            path = f"pages/public-current/ns-{namespace}.jsonl"
            data = b"".join(json_bytes(row) for row in rows)
            atomic(self.output_path(path), data)
            metadata.append({"namespace": namespace, "pages": len(rows), "path": path,
                             "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        index_data = "".join(f"{title}\t{path}\n" for title, path in sorted(index, key=lambda row: row[0].casefold())).encode("utf-8")
        atomic(self.output_path("pages/INDEX.tsv"), index_data)
        manifest = {"schema_version": 1, "api": API, "revision_cutoff": self.state["capture_closed_at"],
                    "inventory_started_at": self.state["started_at"], "inventory_closed_at": self.state["inventory_closed_at"],
                    "membership_semantics": "anonymous closing namespace/revision inventory with changed revisions refreshed; per-page latest observed during scan/reconciliation through revision_cutoff watermark; not an atomic database snapshot",
                    "public_namespaces": self.state["namespaces"], "closing_inventory_pages": len(closing),
                    "captured_pages": len(index), "payload_bytes": total_bytes, "excluded_pages": excluded,
                    "canonical_alias_collisions": collisions, "numeric_alias_replacements": numeric_alias_replacements,
                    "namespace_metadata": metadata,
                    "index_sha256": hashlib.sha256(index_data).hexdigest(), "completed_at": utcnow()}
        atomic(self.output_path("pages/public-current/manifest.json"), json_bytes(manifest))
        self.state["phase"] = "complete"
        self.save()
        print(f"Completed exact public export: {len(index)} pages, {len(closing)} inventory IDs, {len(excluded)} explicitly excluded, {total_bytes} bytes", flush=True)
        return manifest

    def run(self):
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text(encoding="utf-8"))
            if self.state.get("schema_version") != 1 or self.state.get("api") != API or self.state.get("root") != str(self.root):
                raise ExportError("Incompatible export checkpoint")
        else:
            now = utcnow()
            public = namespaces(self.call({"action": "query", "meta": "siteinfo", "siprop": "namespaces"}))
            self.state = {"schema_version": 1, "api": API, "root": str(self.root), "started_at": now,
                          "namespaces": public, "namespace_position": 0,
                          "continuation": {}, "batches": 0, "phase": "scan"}
            self.save()
        if self.state["phase"] == "scan": self.scan()
        if self.state["phase"] == "close": self.close_inventory()
        if self.state["phase"] == "reconcile": self.reconcile()
        return self.emit()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--state-dir", type=Path)
    parser.add_argument("--batch-size", type=int, default=50)
    args = parser.parse_args()
    try:
        Exporter(args.root, state_dir=args.state_dir, batch_size=args.batch_size).run()
    except (ExportError, OSError, ValueError) as exc:
        print(f"Public export incomplete: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
