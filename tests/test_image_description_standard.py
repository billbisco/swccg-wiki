import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "authoring"))

from image_description_standard import normalize


class SourcePreservingMigration(unittest.TestCase):
    def test_redirect_is_not_converted_into_a_description(self):
        before = "#REDIRECT [[File:Existing original.png]]"
        self.assertEqual(normalize(before)["text"], before)
        self.assertFalse(normalize(before)["changed"])

    def test_existing_source_rights_and_changes_survive(self):
        before = "== Summary ==\nA card scan.\n== Sources ==\n[https://example.org/book.pdf Book], page3.\n== Changes ==\nCropped from [[:File:Full.png]].\n== Rights ==\nOriginal credit: A.B.\n"
        result = normalize(before)
        self.assertIn("== Description ==", result["text"])
        self.assertIn("== Source and credit ==", result["text"])
        self.assertIn("== Changes ==\nCropped from [[:File:Full.png]].", result["text"])
        self.assertIn("== Rights ==\nOriginal credit: A.B.", result["text"])
        self.assertEqual(result["new_issues"], [])

    def test_source_line_split_keeps_the_original_label_and_url(self):
        result = normalize("A historic event photo.\n\nSource: https://example.org/post\n[[Category:Photographs]]")
        self.assertIn("== Description ==\n\nA historic event photo.", result["text"])
        self.assertIn("== Source and credit ==\n\nSource: https://example.org/post", result["text"])

    def test_source_line_within_summary_is_split(self):
        result = normalize("== Summary ==\nScreenshot of an event listing.\n\nSource: https://example.org/event\n")
        self.assertIn("== Source and credit ==\n\nSource:", result["text"])
        self.assertEqual(result["issues_after"], [])

    def test_bold_bulleted_source_within_summary_keeps_exact_source_line(self):
        line = "* '''Source:''' [https://example.org/event Event publication]."
        result = normalize("== Summary ==\nEvent logo.\n\n" + line)
        self.assertIn("== Source and credit ==\n\n" + line, result["text"])
        self.assertEqual(result["issues_after"], [])

    def test_source_and_credit_label_and_outside_colon_are_explicit_boundaries(self):
        for line in ["'''Source and credit:''' Shared by UserX.", "* '''Source''': https://example.org", "Source and credit: A named collection."]:
            with self.subTest(line=line):
                result = normalize("Existing subject.\n\n" + line)
                self.assertIn("== Source and credit ==\n\n" + line, result["text"])

    def test_empty_bold_source_field_does_not_become_a_subject(self):
        before = "* '''Source:'''\n[[Category:Logos]]"
        self.assertEqual(normalize(before)["text"], before)

    def test_poster_is_not_upgraded_to_photographer(self):
        result = normalize("Dinner group.\n\nPhoto provided by UserX on7May2020.")
        self.assertIn("Photo provided by UserX on7May2020.", result["text"])
        self.assertNotIn("photographer", result["text"])

    def test_embedded_source_sentence_stays_in_place_and_is_flagged(self):
        before = "A tournament photo. Photo provided by UserX from https://example.org/source."
        result = normalize(before)
        self.assertTrue(result["text"].endswith(before))
        self.assertIn("missing_source_and_credit_section", result["issues_after"])
        self.assertNotIn("== Source and credit ==", result["text"])

    def test_source_only_text_does_not_invent_subject(self):
        result = normalize("Source: https://example.org/source\n[[Category:Logos]]")
        self.assertTrue(result["text"].startswith("== Source and credit =="))
        self.assertNotIn("== Description ==", result["text"])

    def test_categories_and_empty_existing_fields_do_not_get_new_empty_headings(self):
        for before in ["[[Category:Scans]]", "== Summary ==\n[[Category:Scans]]", "== Source ==\n"]:
            result = normalize(before)
            self.assertEqual(result["text"], before)

    def test_template_information_not_mistaken_for_plain_subject(self):
        before = "{{Information|description=A portrait|source={{Cite|url=https://example.org}}}}\n[[Category:Photographs]]"
        result = normalize(before)
        self.assertFalse(result["changed"])
        self.assertIn("opaque_template_description", result["issues_after"])

    def test_code_comments_and_template_parameter_headings_not_rewritten(self):
        before = "<!--\n== Source ==\n--><!-- comment -->\n<nowiki>\n== Summary ==\n</nowiki>\n{{Template|text=\n== Sources ==\n}}\n== Summary ==\nAn actual subject.\n"
        result = normalize(before)
        self.assertIn("<nowiki>\n== Summary ==\n</nowiki>", result["text"])
        self.assertIn("{{Template|text=\n== Sources ==\n}}", result["text"])
        self.assertEqual(result["operations"], ["rename_heading:Summary->Description"])

    def test_competing_sections_are_not_merged_blindly(self):
        before = "== Source ==\nA.\n== Source and credit ==\nB.\n"
        result = normalize(before)
        self.assertEqual(result["text"], before)
        self.assertIn("legacy_section_heading", result["issues_after"])

    def test_recreation_and_preservation_labels_are_untouched(self):
        before = "== Summary ==\nRecreation of a missing white-border printing.\n== Source ==\nhttps://example.org/base.gif\n== Preservation ==\n[https://web.archive.org/web/20200101000000/https://example.org/base.gif Checked copy]."
        result = normalize(before)
        self.assertIn("Recreation of a missing white-border printing.", result["text"])
        self.assertIn("== Preservation ==\n[https://web.archive.org/web/20200101000000/https://example.org/base.gif Checked copy].", result["text"])

    def test_idempotent_on_both_standard_and_partial_migrations(self):
        for before in ["A subject with source in one sentence https://example.org.", "== Summary ==\nA.\n== Source ==\nB.", "Source: https://example.org"]:
            once = normalize(before)
            twice = normalize(once["text"])
            self.assertEqual(once["text"], twice["text"])
            self.assertFalse(twice["changed"])


if __name__ == "__main__":
    unittest.main()
