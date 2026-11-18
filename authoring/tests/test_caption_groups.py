"""Sourced ordered-group captions retain identification without relaxing lint."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import style_lint as L


class OrderedGroupCaptions(unittest.TestCase):
    TOP_EIGHT = (
        "Top 8, from left: [[Bryan Mischke|Mischke]], [[Jonny Chu|Chu]], "
        "[[Brian Fred|Fred]], [[Casey Anis|Anis]], [[Ryan Jellison|Jellison]], "
        "[[Anthony Howard|Howard]], [[Hayes Hunter|Hunter]], [[Joe Olson|Olson]]"
    )

    def flags(self, caption, gallery=True):
        text = (f"<gallery>\nFile:Group.jpg|{caption}\n</gallery>" if gallery else
                f"[[File:Group.jpg|thumb|{caption}]]")
        return [f for f in L.lint(text, "Photograph")[0] if f.startswith("CAPTION ")]

    def test_actual_twelve_word_top_eight_in_gallery_and_thumbnail(self):
        self.assertEqual(12, len(L.plain_caption(self.TOP_EIGHT).split()))
        for gallery in (True, False):
            with self.subTest(gallery=gallery):
                self.assertEqual([], self.flags(self.TOP_EIGHT, gallery))

    def test_right_order_and_terminal_period(self):
        self.assertEqual([], self.flags(
            "Top 2, from right: [[Casey Anis|Anis]], [[Hayes Hunter|Hunter]]."))

    def test_case_and_harmless_whitespace(self):
        self.assertEqual([], self.flags(
            "\tTOP 2, FROM LEFT: [[Jonas Hagen Nørregaard|Jonas]],\t[[Eric Hunter|Eric]]. "))

    def test_commas_inside_links_are_not_list_separators(self):
        self.assertEqual([], self.flags(
            "Top 2, from left: [[Example, Junior|Junior]], [[Example, Senior|Senior]]"))

    def test_complete_caption_still_has_twelve_word_limit(self):
        caption = self.TOP_EIGHT.replace("|Mischke]]", "|Bryan Mischke]]")
        flags = self.flags(caption)
        self.assertTrue(any("13 words (> 12)" in f for f in flags))
        self.assertFalse(any("('top')" in f or "('left')" in f for f in flags))

    def test_malformed_or_non_subject_lists_keep_intro_warnings(self):
        for tail in (
            "Anis, Hunter", "[[Anis]], Hunter", "[[Anis]] and [[Hunter]]",
            "[[Anis]],, [[Hunter]]", "[[Anis]], [[Hunter]],",
            "[[Anis]], [[Hunter]], [[Olson]]", "[[Anis]]",
            "[[:File:Group.jpg|Anis]], [[Hunter]]",
            "[[Category:People|Anis]], [[Hunter]]", "[[#Anis]], [[Hunter]]",
            "[[ ]], [[Hunter]]", "[[Anis| ]], [[Hunter]]",
            "[[Anis|]], [[Hunter]]", "[[[[Anis]]]], [[Hunter]]",
            "[[Anis]], [[Hunter]", "[[Anis]], <nowiki>[[Hunter]]</nowiki>",
            "[[Anis]]<!--hidden-->, [[Hunter]]", "[[Anis]], [[Hunter]]<br>",
        ):
            with self.subTest(tail=tail):
                flags = self.flags("Top 2, from left: " + tail)
                self.assertTrue(any("('top')" in f for f in flags), flags)
                self.assertTrue(any("('left')" in f for f in flags), flags)

    def test_unrecognized_introductions_are_not_masked(self):
        for intro in ("Top 1, from left:", "Top 02, from left:",
                      "Top -2, from left:", "Top two, from left:",
                      "Top 2 from left:", "Top 2, left to right:",
                      "Photograph Top 2, from left:", "Top 2, from the left:"):
            with self.subTest(intro=intro):
                flags = self.flags(intro + " [[Anis]], [[Hunter]]")
                self.assertTrue(any("('top')" in f for f in flags), flags)

    def test_extra_description_and_unlinked_side_still_warn(self):
        caption = self.TOP_EIGHT + ", pictured in the background on right"
        flags = self.flags(caption)
        for word in ("pictured", "background", "right", "left", "top"):
            self.assertTrue(any(f"('{word}')" in f for f in flags), (word, flags))

    def test_only_intro_tokens_are_masked(self):
        flags = self.flags("Top 2, from left: [[Anis|pictured]], [[Hunter]]")
        self.assertTrue(any("('pictured')" in f for f in flags))
        self.assertFalse(any("('top')" in f or "('left')" in f for f in flags))

    def test_oversized_count_does_not_parse_unbounded_integer(self):
        flags = self.flags("Top " + "9" * 5000 + ", from left: [[Anis]], [[Hunter]]")
        self.assertTrue(any("('top')" in f for f in flags))
        self.assertTrue(any("('left')" in f for f in flags))


if __name__ == "__main__":
    unittest.main()
