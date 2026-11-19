"""Tournament-stage facts retain the existing caption and publication rules."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import style_lint as L


class TournamentStageCaptions(unittest.TestCase):
    def flags(self, caption, gallery=True):
        text = (f"<gallery>\nFile:Group.jpg|{caption}\n</gallery>" if gallery else
                f"[[File:Group.jpg|thumb|{caption}]]")
        return [f for f in L.lint(text, "Photograph")[0] if f.startswith("CAPTION ")]

    def test_real_person_event_stage_in_gallery_and_thumbnail(self):
        caption = "[[Joe Olson]] (left), [[2021 World Championship]] Top 8"
        self.assertEqual(8, len(L.plain_caption(caption).split()))
        for gallery in (True, False):
            with self.subTest(gallery=gallery):
                self.assertEqual([], self.flags(caption, gallery))

    def test_stage_in_descriptive_event_label_or_event_article_title(self):
        for caption in (
            "[[Joe Olson]], [[2021 World Championship|2021 Worlds Top 8]]",
            "[[Joe Olson]], [[2021 World Championship|Top 8]]",
            "[[Joe Olson]], [[2021 World Championship Top 8]]",
            "[[Joe Olson]], [[2021 World Championship: Day 2]] Top 16.",
            "[[Joe Olson]], [[2021_World_Championship]]\tTOP 32",
        ):
            with self.subTest(caption=caption):
                self.assertEqual([], self.flags(caption))

    def test_generic_or_unlinked_stage_still_warns(self):
        for caption in (
            "[[Joe Olson]] at the top",
            "[[Joe Olson]], 2021 World Championship Top 8",
            "[[Joe Olson]], [[World Championship]] Top 8",
            "[[Joe Olson]], Top 8 at [[2021 World Championship]]",
            "[[Joe Olson]], [[2021 World Championship]] at the top",
        ):
            with self.subTest(caption=caption):
                self.assertTrue(any("('top')" in f for f in self.flags(caption)))

    def test_invalid_counts_and_nonarticle_or_malformed_links_still_warn(self):
        for caption in (
            "[[Joe Olson]], [[2021 World Championship]] Top 0",
            "[[Joe Olson]], [[2021 World Championship]] Top 08",
            "[[Joe Olson]], [[2021 World Championship]] Top 8th",
            "[[Joe Olson]], [[2021 World Championship]] Top 8.5",
            "[[Joe Olson]], [[File:2021 World Championship.jpg]] Top 8",
            "[[Joe Olson]], [[Category:2021 World Championship]] Top 8",
            "[[Joe Olson]], [[#2021 World Championship]] Top 8",
            "[[Joe Olson]], [[2021 World Championship| ]] Top 8",
            "[[Joe Olson]], [[[[2021 World Championship]] Top 8",
            "[[Joe Olson]], [[2021 World Championship]]] Top 8",
            "[[Joe Olson]], [[2021 <nowiki>World Championship]] Top 8",
            "[[Joe Olson]], [[2021 World Championship|<nowiki>Top 8]]",
            "[[Joe Olson]], <nowiki>[[2021 World Championship]] Top 8</nowiki>",
            "[[Joe Olson]], <!-- [[2021 World Championship]] Top 8 -->",
        ):
            with self.subTest(caption=caption):
                self.assertTrue(any("('top')" in f for f in self.flags(caption)))

    def test_stage_does_not_hide_other_spatial_or_description_words(self):
        flags = self.flags(
            "[[Joe Olson]], [[2021 Worlds]] Top 8 pictured on top right")
        for word in ("pictured", "top", "right"):
            self.assertTrue(any(f"('{word}')" in f for f in flags), flags)

    def test_stage_label_does_not_hide_another_top_in_the_caption(self):
        flags = self.flags("[[2021 Worlds|Top 8]], on top")
        self.assertTrue(any("('top')" in f for f in flags))

    def test_complete_visible_caption_keeps_twelve_word_limit(self):
        caption = ("[[Joe Olson]] (left), [[2021 World Championship]] Top 8 "
                   "with named fellow tournament finalists")
        self.assertEqual(13, len(L.plain_caption(caption).split()))
        flags = self.flags(caption)
        self.assertTrue(any("13 words (> 12)" in f for f in flags))
        self.assertFalse(any("('top')" in f or "('left')" in f for f in flags))


if __name__ == "__main__":
    unittest.main()
