"""The migrated Wiki upload host retains exact original-file validation."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from preservation_contracts import subject_errors


class WikiUploadUrlTests(unittest.TestCase):
    def errors(self, url):
        return subject_errors({
            "kind": "wiki_file_version", "title": "File:ANH-D-hypo.gif",
            "content_sha256": "a" * 64, "bytes": 337153,
            "upload_timestamp": "2026-09-22T14:50:46Z",
            "original_version_url": url,
        })

    def test_current_api_original_and_retained_version(self):
        for path in ["a/a4/ANH-D-hypo.gif", "archive/a/a4/20260922145046!ANH-D-hypo.gif"]:
            with self.subTest(path=path):
                self.assertEqual([], self.errors("https://swccg.com/wiki/images/" + path))

    def test_legacy_original_remains_valid(self):
        self.assertEqual([], self.errors("https://wiki.swccg.com/images/a/a4/ANH-D-hypo.gif"))

    def test_rejects_thumbnails_other_hosts_and_nonoriginal_endpoints(self):
        for url in [
            "https://swccg.com/wiki/images/thumb/a/a4/ANH-D-hypo.gif/80px-ANH-D-hypo.gif",
            "https://wiki.swccg.com/images/thumb/a/a4/ANH-D-hypo.gif/80px-ANH-D-hypo.gif",
            "https://swccg.com/images/a/a4/ANH-D-hypo.gif",
            "https://wiki.swccg.com/wiki/images/a/a4/ANH-D-hypo.gif",
            "https://swccg.com/wiki/index.php?title=File:ANH-D-hypo.gif",
            "https://example.com/wiki/images/a/a4/ANH-D-hypo.gif",
            "https://swccg.com.example.com/wiki/images/a/a4/ANH-D-hypo.gif",
            "http://swccg.com/wiki/images/a/a4/ANH-D-hypo.gif",
            "https://user:secret@swccg.com/wiki/images/a/a4/ANH-D-hypo.gif",
            "https://swccg.com/wiki/images/a/a4/ANH-D-hypo.gif#page=1",
        ]:
            with self.subTest(url=url):
                self.assertTrue(self.errors(url))


if __name__ == "__main__":
    unittest.main()
