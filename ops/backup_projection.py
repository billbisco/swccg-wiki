"""Compatible latest-live flat mirrors, guarded against peer/history overwrite."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path

from gitsync import repository_write_lock
from preservation_backups import payload_hashes, payload_reader
from preservation_contracts import canonical_bytes

MAX_TABLE_BYTES = 16 * 1024 * 1024
MAX_TABLE_ROWS = 250000


def table_lines(path):
    if not path.exists():
        return []
    with path.open("rb") as stream:
        raw = stream.read(MAX_TABLE_BYTES + 1)
    if len(raw) > MAX_TABLE_BYTES:
        raise ValueError("flat metadata table exceeds its explicit 16 MiB input budget")
    lines = raw.decode("utf-8").splitlines()
    if len(lines) > MAX_TABLE_ROWS:
        raise ValueError("flat metadata table exceeds its explicit row budget")
    return lines


def table_bytes(lines):
    checked = []
    for line in lines:
        if len(checked) == MAX_TABLE_ROWS:
            raise ValueError("updated flat metadata table exceeds its explicit row budget")
        checked.append(line)
    raw = ("\n".join(checked) + "\n").encode()
    if len(raw) > MAX_TABLE_BYTES:
        raise ValueError("updated flat metadata table exceeds its explicit byte budget")
    return raw


def safe_name(title):
    name = title.replace(" ", "_").replace(":", "_").replace("/", "_")
    return "".join(character for character in name if character not in '?*"<>|')


def fingerprint(path):
    return payload_hashes(path)["sha256"] if path.is_file() else None


def write_payload(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".projection-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as output, payload_reader(payload) as source:
            shutil.copyfileobj(source, output, length=128 * 1024)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


class Projection:
    def __init__(self, repository: Path, kind: str, *, guard=repository_write_lock):
        self.repository, self.kind, self.guard = repository, kind, guard
        self.prefix = "pages" if kind == "page" else "files"
        self.deferred_reason = None

    def _relative(self, path):
        path = path.replace("\\", "/")
        return path if path.startswith(self.prefix + "/") else self.prefix + "/" + path

    def _index(self):
        path = self.repository / self.prefix / "INDEX.tsv"
        return [line.split("\t") for line in table_lines(path) if "\t" in line]

    def observe(self, title):
        """Capture a baseline before querying live text; no network under lock."""
        with self.guard(self.repository):
            key = title if self.kind == "page" else title.split(":", 1)[1]
            rows = self._index()
            matches = [row[1] for row in rows if row[0] == key]
            if matches:
                relative = self._relative(matches[0])
            else:
                relative = self.prefix + "/" + safe_name(key) + (".wiki" if self.kind == "page" else "")
                owners = {row[1].removeprefix(self.prefix + "/"): row[0] for row in rows}
                if (self.repository / relative).exists() or relative.removeprefix(self.prefix + "/") in owners:
                    # A sanitized-name collision must not overwrite another title.
                    relative += "." + hashlib.sha256(title.encode()).hexdigest()[:12]
            target = self.repository / relative
            if not target.resolve().is_relative_to(self.repository.resolve()) or ".." in Path(relative).parts:
                raise ValueError("flat index path escapes its backup repository")
            return {"title": title, "key": key, "relative": relative, "baseline": fingerprint(target),
                    "title_rows": [row for row in rows if row[0] == key],
                    "path_owners": [row[0] for row in rows if self._relative(row[1]) == relative]}

    def write(self, artifact, observed):
        """Call only in the existing Git callback and only for latest-live data."""
        self.deferred_reason = None
        target = self.repository / observed["relative"]
        rows = self._index()
        if ([row for row in rows if row[0] == observed["key"]] != observed["title_rows"] or
                [row[0] for row in rows if self._relative(row[1]) == observed["relative"]] != observed["path_owners"]):
            self.deferred_reason = "peer advanced the title index mapping or destination ownership during the Wiki query"
            return []
        if fingerprint(target) != observed["baseline"]:
            self.deferred_reason = "peer advanced the flat payload during the Wiki query"
            return []  # peer advanced during the public Wiki query; reconcile next run
        marker = self.repository / "preservation/projections" / (hashlib.sha256(observed["title"].encode()).hexdigest() + ".json")
        previous = json.loads(marker.read_text(encoding="utf-8")) if marker.exists() else {}
        subject = artifact.subject
        if previous.get("revision_id", 0) > subject.get("revision_id", 0):
            self.deferred_reason = "flat projection already records a newer revision"
            return []
        if previous.get("upload_timestamp", "") > subject.get("upload_timestamp", ""):
            self.deferred_reason = "flat projection already records a newer upload version"
            return []
        write_payload(target, artifact.payload)
        rows = [row for row in rows if row[0] != observed["key"]]
        if self.kind == "page":
            rows.append([observed["key"], observed["relative"]])
        else:
            rows.append([observed["key"], observed["relative"].removeprefix("files/"),
                         artifact.provenance.get("mime", ""), str(subject["bytes"])])
        index = self.repository / self.prefix / "INDEX.tsv"
        write_payload(index, table_bytes("\t".join(row) for row in sorted(rows)))
        write_payload(marker, canonical_bytes({**subject, "flat_path": observed["relative"]}) + b"\n")
        return [observed["relative"], self.prefix + "/INDEX.tsv", marker.relative_to(self.repository).as_posix()]

    def usage(self, title, rows):
        """Append public usage mappings as the compatible old dumper did."""
        path = self.repository / "files/USAGE.tsv"
        existing = set(table_lines(path))
        key = title.split(":", 1)[1]
        existing.update(key + "\t" + row["title"] for row in rows)
        write_payload(path, table_bytes(sorted(existing)))
        return ["files/USAGE.tsv"]
