import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "authoring"))

from style_lint import service_flags


class ServiceTableNamespaceScope(unittest.TestCase):
    def test_file_portrait_roles_do_not_require_service_tables(self):
        captions = [
            "Kevin Reitzel in1999, while he worked for Decipher.\n[[Category:Players]]",
            "Kendrick Summers, Decipher's Gold Leader.\n[[Category:Players]]",
            "Paul Todd Feldman (Red16), Decipher's featured Squadron Member.\n[[Category:Players]]",
        ]
        for text in captions:
            with self.subTest(text=text):
                self.assertEqual(service_flags(text, "File:Person portrait.jpg"), [])

    def test_image_namespace_alias_also_remains_an_image_caption(self):
        self.assertEqual(service_flags("He worked for Decipher.\n[[Category:People]]", "Image:Portrait.png"), [])

    def test_person_article_still_requires_matching_service_table(self):
        text = "'''Example Person''' worked for Decipher.\n[[Category:Players]]"
        flags = service_flags(text, "Example Person")
        self.assertTrue(any("SERVICE" in flag and "Decipher" in flag for flag in flags))

    def test_person_article_with_a_matching_service_table_passes(self):
        text = "'''Example Person''' worked for Decipher.\n== Service ==\n{| class=\"wikitable\"\n! Dates !! Service\n|-\n|1999 ||Decipher employee\n|}\n[[Category:Players]]"
        self.assertEqual(service_flags(text, "Example Person"), [])


if __name__ == "__main__":
    unittest.main()
