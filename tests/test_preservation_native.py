import hashlib
import os
from pathlib import Path
import struct
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from preservation_contracts import validate_source_representation
from preservation_native import (MAX_NATIVE_BYTES, NATIVE_REPRESENTATION,
                                 is_native_capture_url, validate_native_mirror,
                                 validate_native_payload)


XML = b'<?xml version="1.0" encoding="utf-8"?><deck><card blueprintId="1_1" title="Example"/></deck>'


def source_for(data=XML, kind="gemp_deck_xml"):
    sha = hashlib.sha256(data).hexdigest()
    primary = "https://forum.starwarsccg.org/download/file.php?id=10233"
    mirror = "https://swccg.com/snapshots/native/" + sha + (".txt" if kind == "gemp_deck_xml" else ".doc")
    evidence = "https://github.com/swccg-guild/work/blob/" + "a" * 40 + "/evidence/native.json"
    return dict(url=mirror, primary_url=primary, sha256=sha, bytes=len(data),
                representation=NATIVE_REPRESENTATION,
                checked_evidence=dict(path=evidence, sha256="b" * 64),
                provenance_equivalence=dict(primary_url=primary, mirror_url=mirror,
                                            primary_sha256=sha, mirror_sha256=sha,
                                            bytes=len(data), native_kind=kind,
                                            evidence_path=evidence, evidence_sha256="b" * 64))


def ole_fixture():
    """Synthetic CFB directory fixture, not a historical document or Office export."""
    end, free = 0xFFFFFFFE, 0xFFFFFFFF
    header = bytearray(512)
    header[:8] = bytes.fromhex("d0cf11e0a1b11ae1")
    struct.pack_into("<HHHH", header, 26, 3, 0xFFFE, 9, 6)
    struct.pack_into("<II", header, 44, 1, 1)
    struct.pack_into("<III", header, 56, 4096, end, 0)
    struct.pack_into("<II", header, 68, end, 0)
    struct.pack_into("<109I", header, 76, 0, *([free] * 108))
    fat = [free] * 128
    fat[0], fat[1] = 0xFFFFFFFD, end
    for start in (2, 10):
        for sid in range(start, start + 7):
            fat[sid] = sid + 1
        fat[start + 7] = end
    directory = bytearray(512)
    for offset, name, kind, start, size in (
        (0, "Root Entry", 5, end, 0),
        (128, "WordDocument", 2, 2, 4096),
        (256, "1Table", 2, 10, 4096),
    ):
        encoded = (name + "\0").encode("utf-16le")
        directory[offset:offset + len(encoded)] = encoded
        struct.pack_into("<H", directory, offset + 64, len(encoded))
        directory[offset + 66] = kind
        struct.pack_into("<I", directory, offset + 116, start)
        struct.pack_into("<Q", directory, offset + 120, size)
    return bytes(header) + struct.pack("<128I", *fat) + bytes(directory) + bytes(8192)


class NativeMirrorContractTests(unittest.TestCase):
    def payload(self, data, source=None):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "payload.bin"
            path.write_bytes(data)
            return validate_native_payload(source or source_for(data), path)

    def test_xml_exact_native_and_contract_dispatch(self):
        source = source_for()
        self.assertEqual([], validate_source_representation(source))
        self.assertEqual("gemp_deck_xml", self.payload(XML, source))

    def test_outside_deck_cards_are_retained_native_xml(self):
        data = b'<deck><card blueprintId="1_1"/><cardOutsideDeck blueprintId="2_2"/></deck>'
        self.assertEqual("gemp_deck_xml", self.payload(data))

    def test_ole_directory_is_parsed_without_office(self):
        data = ole_fixture()
        self.assertEqual("ole_word_document", self.payload(data, source_for(data, "ole_word_document")))

    def test_native_capture_namespace_is_narrow(self):
        url = source_for()["url"]
        self.assertTrue(is_native_capture_url(url))
        for bad in (url + "?query=1", url + "#fragment", url.replace("https:", "http:"),
                    url.replace("swccg.com", "swccg.com.evil.invalid"),
                    url.replace("/native/", "/pc/"), url.replace(".txt", ".html"),
                    url.replace("/native/", "/native/../"), None):
            with self.subTest(bad=bad):
                self.assertFalse(is_native_capture_url(bad))

    def test_wrong_primary_or_mirror_identity_is_rejected(self):
        for field, value in (("primary_url", "https://forum.starwarsccg.org/viewtopic.php?t=1"),
                             ("primary_url", "https://forum.starwarsccg.org/download/file.php?id=10233&sid=bad"),
                             ("url", source_for()["url"].replace(".txt", ".doc")),
                             ("sha256", "c" * 64), ("bytes", True),
                             ("bytes", 0), ("bytes", MAX_NATIVE_BYTES + 1)):
            with self.subTest(field=field, value=value):
                source = source_for()
                source[field] = value
                self.assertTrue(validate_native_mirror(source))

    def test_proof_cannot_hide_different_bytes_size_or_kind(self):
        changes = {"primary_sha256": "c" * 64, "mirror_sha256": "c" * 64,
                   "bytes": len(XML) + 1, "native_kind": "html",
                   "primary_url": "https://example.invalid/different",
                   "mirror_url": source_for()["url"] + "?different=1",
                   "evidence_path": "https://github.com/swccg-guild/work/blob/main/evidence/native.json",
                   "evidence_sha256": "c" * 64}
        for field, value in changes.items():
            with self.subTest(field=field):
                source = source_for()
                source["provenance_equivalence"][field] = value
                self.assertTrue(validate_source_representation(source))

    def test_native_proof_needs_bound_checked_evidence(self):
        source = source_for()
        source["checked_evidence"]["path"] += ".other"
        self.assertTrue(validate_native_mirror(source))
        source = source_for()
        source["provenance_equivalence"]["primary_html_sha256"] = "d" * 64
        self.assertTrue(validate_native_mirror(source))

    def test_malformed_proof_values_fail_closed(self):
        for bad in (None, [], "not-proof"):
            source = source_for()
            source["provenance_equivalence"] = bad
            self.assertTrue(validate_source_representation(source))
        self.assertTrue(validate_native_mirror(None))
        for bad in ([], {}, True):
            source = source_for()
            source["provenance_equivalence"]["native_kind"] = bad
            self.assertTrue(validate_source_representation(source))

    def test_evidence_path_cannot_escape_immutable_commit(self):
        for suffix in ("/../other", "/%2e%2e/other", " with spaces"):
            source = source_for()
            source["provenance_equivalence"]["evidence_path"] += suffix
            source["checked_evidence"]["path"] += suffix
            self.assertTrue(validate_native_mirror(source))

    def test_full_byte_hash_and_length_not_text_similarity(self):
        for data in (XML + b" ", XML.replace(b"Example", b"ExampLe"), XML[:-1]):
            with self.subTest(data_sha=hashlib.sha256(data).hexdigest()):
                with self.assertRaises(ValueError):
                    self.payload(data, source_for())

    def test_html_dtd_entities_and_nested_tags_are_not_native_decks(self):
        for data in (b"<html><body>error</body></html>", b"<!DOCTYPE deck><deck/>",
                     b'<!DOCTYPE deck [<!ENTITY x "value">]><deck/>',
                     b'<deck><card blueprintId="1"><script/></card></deck>',
                     b'<deck><card title="missing ID"/></deck>', b'<deck/>',
                     b'<deck><card blueprintId="1"/>unexpected text</deck>',
                     b'<deck><card blueprintId="1"/></deck><extra/>',
                     '<deck/>'.encode('utf-16')):
            with self.subTest(data_sha=hashlib.sha256(data).hexdigest()):
                with self.assertRaises(ValueError):
                    self.payload(data)

    def test_overlarge_card_count_is_bounded(self):
        data = b'<deck>' + b'<card blueprintId="1"/>' * 10001 + b'</deck>'
        with self.assertRaises(ValueError):
            self.payload(data)

    def test_ole_header_alone_is_not_word(self):
        for data in (b"not OLE", bytes.fromhex("d0cf11e0a1b11ae1") + bytes(504),
                     ole_fixture()[:-1], ole_fixture().replace("WordDocument".encode("utf-16le"),
                                                           "NotAWordFile".encode("utf-16le"))):
            with self.subTest(length=len(data)):
                with self.assertRaises(ValueError):
                    self.payload(data, source_for(data, "ole_word_document"))

    def test_ole_directory_cycle_and_sector_escape_are_rejected(self):
        for next_sector in (1, 0xFFFF):
            data = bytearray(ole_fixture())
            struct.pack_into("<I", data, 512 + 4, next_sector)
            data = bytes(data)
            with self.subTest(next_sector=next_sector):
                with self.assertRaises(ValueError):
                    self.payload(data, source_for(data, "ole_word_document"))

    def test_symlink_is_not_a_native_payload(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "real").write_bytes(XML)
            try:
                (root / "link").symlink_to(root / "real")
            except OSError:
                self.skipTest("symlink privilege unavailable on this platform")
            with self.assertRaises(ValueError):
                validate_native_payload(source_for(), root / "link")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "POSIX FIFO fixture")
    def test_fifo_is_rejected_without_waiting_for_a_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pipe"
            os.mkfifo(path)
            with self.assertRaises(ValueError):
                validate_native_payload(source_for(), path)

    def test_original_representation_is_unchanged(self):
        self.assertEqual([], validate_source_representation(dict(url="https://example.invalid/original")))


if __name__ == "__main__":
    unittest.main()
