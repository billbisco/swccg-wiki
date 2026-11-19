"""Pure contracts and inert payload checks for exact native attachment mirrors.

This module performs no network requests, staging, document execution or writes.
An equivalent-looking export never substitutes for matching complete bytes.
"""
from __future__ import annotations

import hashlib
import io
import os
from pathlib import Path
import re
import stat
import struct
import urllib.parse
import xml.etree.ElementTree as ET

NATIVE_REPRESENTATION = "checked_byte_identical_native_mirror"
MAX_NATIVE_BYTES = 64 * 1024 * 1024
_EXTENSIONS = {"gemp_deck_xml": "txt", "ole_word_document": "doc"}
_MIRROR = re.compile(r"https://swccg\.com/snapshots/native/([0-9a-f]{64})\.(txt|doc)")
_PRIMARY = re.compile(r"https://forum\.starwarsccg\.org/download/file\.php\?id=[1-9][0-9]*")
_EVIDENCE = re.compile(
    r"https://github\.com/(?:swccg-guild/work|billbisco/swccg-wiki(?:-files)?)/"
    r"blob/[0-9a-f]{40}/[^?#\s]+"
)
_SHA = re.compile(r"[0-9a-f]{64}")


def is_native_capture_url(url: object) -> bool:
    """Recognize only the approved native namespace, never an HTML/text fallback."""
    return isinstance(url, str) and _MIRROR.fullmatch(url) is not None


def validate_native_mirror(source: object) -> list[str]:
    """Validate recorded exact equivalence, not the existence of remote evidence."""
    if not isinstance(source, dict):
        return ["native source must be an object"]
    errors = []
    if source.get("representation") != NATIVE_REPRESENTATION:
        errors.append("native representation is unsupported")
    primary, mirror = source.get("primary_url"), source.get("url")
    if not isinstance(primary, str) or not _PRIMARY.fullmatch(primary):
        errors.append("native primary must be the canonical HTTPS forum attachment URI")
    match = _MIRROR.fullmatch(mirror) if isinstance(mirror, str) else None
    if not match:
        errors.append("native mirror must be an exact approved SHA-named txt/doc URL")
    digest, size = source.get("sha256"), source.get("bytes")
    if not isinstance(digest, str) or not _SHA.fullmatch(digest):
        errors.append("native source needs a lowercase SHA-256")
    if type(size) is not int or not 0 < size <= MAX_NATIVE_BYTES:
        errors.append("native source needs positive bytes within the 64 MiB limit")
    proof = source.get("provenance_equivalence")
    if not isinstance(proof, dict):
        return errors + ["native byte-equivalence proof is required"]
    if proof.get("primary_url") != primary or proof.get("mirror_url") != mirror:
        errors.append("native proof URLs do not bind the exact primary/mirror pair")
    for field in ("primary_sha256", "mirror_sha256", "evidence_sha256"):
        value = proof.get(field)
        if not isinstance(value, str) or not _SHA.fullmatch(value):
            errors.append("native proof needs " + field)
    if proof.get("primary_sha256") != digest or proof.get("mirror_sha256") != digest:
        errors.append("native primary, mirror and source SHA-256 must all match")
    if match and match[1] != digest:
        errors.append("native mirror filename SHA-256 differs from its payload")
    if type(proof.get("bytes")) is not int or proof.get("bytes") != size:
        errors.append("native proof must bind the exact byte count")
    kind = proof.get("native_kind")
    if not isinstance(kind, str) or kind not in _EXTENSIONS:
        errors.append("native proof kind is unsupported")
    elif match and match[2] != _EXTENSIONS[kind]:
        errors.append("native mirror extension does not match the proved native kind")
    evidence = proof.get("evidence_path")
    if (not isinstance(evidence, str) or not _EVIDENCE.fullmatch(evidence)
            or any(part in {".", ".."} for part in urllib.parse.unquote(evidence).split("/"))):
        errors.append("native proof needs an immutable approved Git evidence URL")
    checked = source.get("checked_evidence")
    if not isinstance(checked, dict) or (
        checked.get("path") != evidence or checked.get("sha256") != proof.get("evidence_sha256")
    ):
        errors.append("native equivalence evidence must bind the checked evidence path/hash")
    if any(not isinstance(key, str) for key in proof):
        errors.append("native proof field names must be strings")
    if any(isinstance(key, str) and ("html" in key.lower() or "article_text" in key.lower()) for key in proof):
        errors.append("native equivalence cannot use fabricated HTML/article-text proof fields")
    return errors


def _check_deck_xml(data: bytes) -> None:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeError as error:
        raise ValueError("native deck must be UTF-8 XML") from error
    if "\0" in text or re.search(r"<!\s*(DOCTYPE|ENTITY)\b", text, re.I):
        raise ValueError("native deck cannot contain NUL, DTD or entity declarations")
    depth = cards = 0
    try:
        for event, element in ET.iterparse(io.StringIO(text), events=("start", "end")):
            if event == "start":
                depth += 1
                if depth == 1 and element.tag != "deck":
                    raise ValueError("native deck XML root must be deck")
                if depth == 2:
                    cards += 1
                    if element.tag not in {"card", "cardOutsideDeck"} or not element.get("blueprintId", "").strip():
                        raise ValueError("native deck must contain card/cardOutsideDeck elements with blueprintId")
                    if cards > 10000:
                        raise ValueError("native deck exceeds the bounded card-element count")
                if depth > 2:
                    raise ValueError("native deck contains unexpected nested elements")
            else:
                if (element.text or "").strip() or (element.tail or "").strip():
                    raise ValueError("native deck contains unexpected text content")
                element.clear()
                depth -= 1
    except ET.ParseError as error:
        raise ValueError("native deck XML is malformed") from error
    if not cards or depth:
        raise ValueError("native deck must contain at least one complete card element")


def _check_ole_word(data: bytes) -> None:
    """Read the bounded CFB directory; never load Office or execute streams/macros."""
    end, free, fat_marker = 0xFFFFFFFE, 0xFFFFFFFF, 0xFFFFFFFD
    if len(data) < 512 or data[:8] != bytes.fromhex("d0cf11e0a1b11ae1"):
        raise ValueError("native Word document lacks the OLE compound signature")
    major, byte_order, shift, mini_shift = struct.unpack_from("<HHHH", data, 26)
    if byte_order != 0xFFFE or (major, shift) not in {(3, 9), (4, 12)} or mini_shift != 6:
        raise ValueError("native Word document has an unsupported OLE header")
    sector_size = 1 << shift
    if len(data) % sector_size:
        raise ValueError("native Word document has truncated OLE sectors")
    sectors = len(data) // sector_size - 1
    fat_count, first_dir = struct.unpack_from("<II", data, 44)
    first_difat, difat_count = struct.unpack_from("<II", data, 68)
    if not 0 < fat_count <= sectors or difat_count > sectors:
        raise ValueError("native Word document has invalid OLE allocation counts")

    def sector(sid: int) -> bytes:
        if not 0 <= sid < sectors:
            raise ValueError("OLE sector points outside the complete file")
        return data[(sid + 1) * sector_size:(sid + 2) * sector_size]

    fat_ids = [v for v in struct.unpack_from("<109I", data, 76) if v != free]
    difat_ids = set()
    sid = first_difat
    for _ in range(difat_count):
        if sid in difat_ids:
            raise ValueError("OLE DIFAT chain contains a cycle")
        difat_ids.add(sid)
        values = struct.unpack("<" + "I" * (sector_size // 4), sector(sid))
        fat_ids.extend(v for v in values[:-1] if v != free)
        sid = values[-1]
    if (not difat_count and first_difat not in {end, free}) or (difat_count and sid != end) or len(fat_ids) != fat_count or len(set(fat_ids)) != fat_count:
        raise ValueError("OLE FAT/DIFAT declaration is inconsistent")
    fat = []
    for sid in fat_ids:
        fat.extend(struct.unpack("<" + "I" * (sector_size // 4), sector(sid)))
    if any(sid >= len(fat) or fat[sid] != fat_marker for sid in fat_ids):
        raise ValueError("OLE FAT sectors are not marked consistently")
    directory, seen = bytearray(), set()
    sid = first_dir
    while sid != end:
        if sid in seen or sid in fat_ids or sid in difat_ids or len(seen) >= sectors:
            raise ValueError("OLE directory chain is cyclic or overlaps allocation sectors")
        seen.add(sid)
        directory.extend(sector(sid))
        if sid >= len(fat):
            raise ValueError("OLE directory FAT entry is missing")
        sid = fat[sid]
    names, roots = {}, 0
    for offset in range(0, len(directory), 128):
        entry = directory[offset:offset + 128]
        kind = entry[66]
        if not kind:
            continue
        length = struct.unpack_from("<H", entry, 64)[0]
        if kind not in {1, 2, 5} or not 2 <= length <= 64 or length % 2 or entry[length - 2:length] != b"\0\0":
            raise ValueError("OLE directory has an invalid name/type")
        try:
            name = bytes(entry[:length - 2]).decode("utf-16le")
        except UnicodeError as error:
            raise ValueError("OLE directory name is malformed") from error
        if "\0" in name:
            raise ValueError("OLE directory name contains an embedded NUL")
        if kind == 5:
            roots += 1
        if kind == 2:
            size = struct.unpack_from("<Q", entry, 120)[0]
            if major == 3:
                size &= 0xFFFFFFFF
            if name in names or size > len(data):
                raise ValueError("OLE stream directory is duplicate or exceeds the file")
            names[name] = size
    if roots != 1 or not names.get("WordDocument") or not (names.get("0Table") or names.get("1Table")):
        raise ValueError("OLE directory does not identify a Word document and table stream")


def validate_native_payload(source: dict, path: str | Path) -> str:
    """Raise ValueError on metadata/bytes/type mismatch; return the verified kind."""
    errors = validate_native_mirror(source)
    if errors:
        raise ValueError("; ".join(errors))
    path = Path(path)
    if path.is_symlink():
        raise ValueError("native payload path cannot be a symlink")
    flags = (os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
             | getattr(os, "O_NONBLOCK", 0))
    try:
        if not stat.S_ISREG(path.lstat().st_mode):
            raise ValueError("native payload path must identify a regular file")
        with os.fdopen(os.open(path, flags), "rb") as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode) or info.st_size != source["bytes"]:
                raise ValueError("native payload size/type differs from the complete source")
            data = stream.read(MAX_NATIVE_BYTES + 1)
    except OSError as error:
        raise ValueError("native payload is not a readable regular file") from error
    if len(data) != source["bytes"] or hashlib.sha256(data).hexdigest() != source["sha256"]:
        raise ValueError("native payload full SHA-256/byte count differs from the source")
    kind = source["provenance_equivalence"]["native_kind"]
    if kind == "gemp_deck_xml":
        _check_deck_xml(data)
    else:
        _check_ole_word(data)
    return kind
