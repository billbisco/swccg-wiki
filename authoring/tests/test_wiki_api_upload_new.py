"""Missing-only uploads preserve literal descriptions and support deferred review."""
from email import policy
from email.parser import BytesParser
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wiki_api_apply import Wiki


class UploadNewTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "native.jpg"
        self.native = b"\xff\xd8native-photo-bytes\xff\xd9"
        self.path.write_bytes(self.native)
        self.wiki = Wiki.__new__(Wiki)  # No sign-in or network in these unit tests.
        self.wiki.csrf = "test-csrf"
        self.wiki.get = Mock(return_value={"query": {"pages": [{"missing": True}]}})
        self.wiki._open = Mock(return_value={"upload": {"result": "Success"}})
        self.wiki.post = Mock(return_value={"purge": [{"purged": True}]})
        self.wiki.review = Mock(return_value=" (reviewed)")
        self.filename = "Example event photograph.jpg"
        self.text = ("== Description ==\n\nAn attendee at the event.\n\n"
                     "== Source and credit ==\n\nShared by Áda — 22 September 2024.\n")

    def upload(self, **options):
        return self.wiki.upload_new(self.path, self.filename, self.text,
                                    "Publish approved event photograph", **options)

    def parts(self):
        request = self.wiki._open.call_args.args[0]
        header = request.get_header("Content-type")
        message = BytesParser(policy=policy.default).parsebytes(
            ("Content-Type: " + header + "\r\nMIME-Version: 1.0\r\n\r\n").encode()
            + request.data)
        return {part.get_param("name", header="content-disposition"):
                part.get_payload(decode=True) for part in message.iter_parts()}

    def test_deferred_review_preserves_literal_unicode_text_and_native_bytes(self):
        self.assertEqual(self.upload(review=False), "Success")
        fields = self.parts()
        self.assertEqual(fields["text"], self.text.encode("utf-8"))
        self.assertEqual(fields["file"], self.native)
        self.assertEqual(fields["filename"].decode(), self.filename)
        self.assertNotIn(b"== Summary ==", fields["text"])
        self.assertNotIn("ignorewarnings", fields)
        self.wiki.review.assert_not_called()
        self.wiki.post.assert_called_once_with(
            action="purge", titles="File:" + self.filename, forcelinkupdate="1")

    def test_existing_four_argument_call_keeps_default_review(self):
        self.assertEqual(self.upload(), "Success (reviewed)")
        self.wiki.review.assert_called_once_with("File:" + self.filename)
        self.assertEqual(self.parts()["text"], self.text.encode("utf-8"))

    def test_explicit_review_true_keeps_review(self):
        self.assertEqual(self.upload(review=True), "Success (reviewed)")
        self.wiki.review.assert_called_once_with("File:" + self.filename)

    def test_existing_file_is_refused_without_upload_or_review(self):
        self.wiki.get.return_value = {"query": {"pages": [{"pageid": 1}]}}
        self.assertEqual(self.upload(review=False), "ERROR exists: refusing to overwrite")
        self.wiki._open.assert_not_called()
        self.wiki.post.assert_not_called()
        self.wiki.review.assert_not_called()

    def test_upload_warning_is_not_ignored_or_reviewed(self):
        self.wiki._open.return_value = {
            "upload": {"result": "Warning", "warnings": {"exists": self.filename}}}
        self.assertTrue(self.upload(review=False).startswith("ERROR Warning:"))
        self.assertNotIn("ignorewarnings", self.parts())
        self.wiki.post.assert_not_called()
        self.wiki.review.assert_not_called()

    def test_api_error_does_not_purge_or_review(self):
        self.wiki._open.return_value = {"error": {"code": "permissiondenied", "info": "Denied"}}
        self.assertEqual(self.upload(), "ERROR permissiondenied: Denied")
        self.wiki.post.assert_not_called()
        self.wiki.review.assert_not_called()


if __name__ == "__main__":
    unittest.main()
