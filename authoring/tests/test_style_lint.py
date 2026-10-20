"""Tests for authoring/style_lint.py citation checks. Run: python3 -m unittest discover -s authoring/tests"""
import os
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import style_lint as L  # noqa: E402

FX = HERE / "fixtures"
WB = "https://web.archive.org/web/20261020174512/"


def fx(name):
    return (FX / name).read_text(encoding="utf-8")


def kinds(flags):
    return [f.split()[0] for f in flags]


class LivePageFixtures(unittest.TestCase):
    """Saved wikitext of real pages (revision ids in the file names)."""

    def test_virtual_block_4_flags_unarchived_sources(self):
        flags = L.archive_flags(fx("Virtual_Block_4.r113951.wiki"))
        self.assertEqual(len(flags), 3)
        self.assertTrue(any("boardgamegeek.com" in f for f in flags))
        self.assertTrue(any("star-wars.pl/News/10786" in f for f in flags))

    def test_virtual_block_7_flags_refs_and_external_links(self):
        flags = L.archive_flags(fx("Virtual_Block_7.r112843.wiki"))
        joined = "\n".join(flags)
        # <ref> without its own Preserved copy, although another ref archives the same PDF
        self.assertIn("<ref> cites https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf", joined)
        self.assertIn("forum.starwarsccg.org/viewtopic.php?t=36308", joined)
        # External links are no longer skipped
        self.assertIn("https://www.starwarsccg.org/resources/virtual-slips/", joined)
        self.assertIn("https://res.starwarsccg.org/cardlists/VBlock7Type.html", joined)

    def test_reflections_iv_before_and_after_archive_pass(self):
        before = L.archive_flags(fx("Reflections_IV_Virtual_Block_6.r112812.wiki"))
        self.assertEqual(len(before), 2)
        self.assertTrue(all("swccg-card-json" in f for f in before))
        self.assertEqual(L.archive_flags(fx("Reflections_IV_Virtual_Block_6.r113339.wiki")), [])

    def test_christian_mccarty_passes(self):
        text = fx("Christian_McCarty.r112964.wiki")
        flags, _ = L.lint(text, "Christian McCarty")
        self.assertEqual(flags, [])

    def test_christian_mccarty_earlier_revision_flags_table_links(self):
        flags = L.archive_flags(fx("Christian_McCarty.r112725.wiki"))
        self.assertEqual(sorted(f.split()[1] for f in flags), ["https://lotrtcgpc.net/", "https://wiki.lotrtcgpc.net/"])

    def test_cli_exit_codes(self):
        script = str(HERE.parent / "style_lint.py")
        bad = subprocess.run([sys.executable, script, str(FX / "Virtual_Block_4.r113951.wiki")], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("ARCHIVE", bad.stdout)
        good = subprocess.run([sys.executable, script, str(FX / "Christian_McCarty.r112964.wiki")], capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stdout)


class ArchiveCheck(unittest.TestCase):
    def test_ref_with_copy_passes(self):
        t = f'Fact.<ref>[https://example.com/a Title], site. Preserved copy: [{WB}https://example.com/a Internet Archive]</ref>'
        self.assertEqual(L.archive_flags(t), [])

    def test_ref_without_copy_fails_even_if_copy_elsewhere(self):
        t = (f'A.<ref>[https://example.com/a Title]</ref>\n'
             f'B.<ref>[https://example.com/a Title]. Preserved copy: [{WB}https://example.com/a Internet Archive]</ref>')
        self.assertEqual(kinds(L.archive_flags(t)), ["ARCHIVE"])

    def test_snapshot_route_copy_in_same_ref_passes(self):
        t = ('<ref>[https://forum.starwarsccg.org/viewtopic.php?t=1 Thread]. Preserved copy: '
             f'[{WB}https://swccg.com/snapshots/forum/t1.html Internet Archive]</ref>')
        self.assertEqual(L.archive_flags(t), [])

    def test_archive_org_details_counts(self):
        t = ('<ref>[https://www.youtube.com/watch?v=abc Video]. Preserved copy: '
             '[https://archive.org/details/youtube-abc Internet Archive]</ref>')
        self.assertEqual(L.archive_flags(t), [])

    def test_body_link_passes_with_copy_anywhere_on_page(self):
        t = (f'| Admin, [https://www.example.com/ Example]\n'
             f'<ref>[https://example.com Example]. Preserved copy: [{WB}https://example.com/ Internet Archive]</ref>')
        self.assertEqual(L.archive_flags(t), [])

    def test_body_link_without_copy_fails(self):
        self.assertEqual(kinds(L.archive_flags("See [https://example.org/x X].")), ["ARCHIVE"])

    def test_external_links_item_needs_copy(self):
        t = "== External links ==\n* [https://example.org/read Further reading]\n"
        self.assertEqual(kinds(L.archive_flags(t)), ["ARCHIVE"])
        t2 = f"== External links ==\n* [https://example.org/read Further reading]. Preserved copy: [{WB}https://example.org/read Internet Archive]\n"
        self.assertEqual(L.archive_flags(t2), [])

    def test_wayback_needs_14_digits(self):
        t = '<ref>[https://example.com/a T]. Copy: [https://web.archive.org/web/2026/https://example.com/a IA]</ref>'
        self.assertEqual(kinds(L.archive_flags(t)), ["ARCHIVE"])

    def test_skipped_hosts(self):
        t = ("[https://wiki.swccg.com/wiki/Main_Page Main]\n"
             "[https://swccg.com/images/a/ab/X.png X]\n"
             "[https://www.swccg.com/images/a/ab/Y.png Y]\n"
             f"[{WB}https://example.com/ IA]\n")
        self.assertEqual(L.archive_flags(t), [])

    def test_comments_and_trailing_punctuation(self):
        self.assertEqual(L.archive_flags("<!-- https://example.com/hidden -->"), [])
        t = f"See https://example.com/a. Copy: [{WB}https://example.com/a IA]"
        self.assertEqual(L.archive_flags(t), [])

    def test_named_ref_reuse_is_fine(self):
        t = (f'A.<ref name="x">[https://example.com/a T]. Preserved copy: [{WB}https://example.com/a IA]</ref> '
             f'B.<ref name="x" /> C.<ref name="a/b" />')
        self.assertEqual(L.archive_flags(t), [])


class EmailCheck(unittest.TestCase):
    def test_personal_email_flagged(self):
        self.assertEqual(kinds(L.email_flags("Contact: someone123@aol.com")), ["EMAIL"])

    def test_mailto_flagged(self):
        self.assertEqual(kinds(L.email_flags("[mailto:someone@hotmail.com Mail]")), ["EMAIL"])

    def test_allowed_addresses(self):
        self.assertEqual(L.email_flags("Write to rules@starwarsccg.org or support@decipher.com."), [])
        self.assertEqual(L.email_flags("Kept: old@isp.net <!-- email-ok: defunct club address -->"), [])

    def test_not_emails(self):
        self.assertEqual(L.email_flags("[[File:Logo@2x.png]] and https://medium.com/@user/post and [[A_B@c.wiki]]"), [])


class RefCheck(unittest.TestCase):
    def test_empty_and_placeholder_refs(self):
        self.assertEqual(kinds(L.ref_flags('A<ref name="oc">None</ref> B<ref></ref>')), ["REF", "REF"])

    def test_source_text_without_url_passes(self):
        self.assertEqual(L.ref_flags("A<ref>''Scrye'' 45, p. 12 (May 1999).</ref>"), [])
        self.assertEqual(L.ref_flags("A<ref>[[Decipher]] rulebook</ref>"), [])


class SourcesSection(unittest.TestCase):
    def test_person_page_sources_flagged(self):
        flags, _ = L.lint("'''X''' is a player.\n== Sources ==\n* Foo\n[[Category:People]]\n[[Category:Tournament Directors]]")
        self.assertIn("HEADING", kinds(flags))

    def test_deck_and_event_pages_allowed(self):
        for cat in ("Decklists", "Dark Side decks", "Tournaments", "Retro League", "Championships"):
            t = f"Deck.\n== Sources ==\n* [https://example.com/d PC decklist]. Preserved copy: [{WB}https://example.com/d IA]\n[[Category:{cat}]]"
            flags, _ = L.lint(t)
            self.assertNotIn("HEADING", kinds(flags), cat)

    def test_card_type_category_does_not_allow(self):
        flags, _ = L.lint("A card.\n== Sources ==\n* Foo\n[[Category:Epic Event]]")
        self.assertIn("HEADING", kinds(flags))

    def test_live_categories_count(self):
        flags, _ = L.lint("Deck.\n== Sources ==\n* Foo", cats={"Category:Decklists"})
        self.assertNotIn("HEADING", kinds(flags))


class ExternalLinksProse(unittest.TestCase):
    def test_external_links_annotation_is_linted(self):
        t = f"Body.\n== External links ==\n* [https://example.org/x X]. Preserved copy: [{WB}https://example.org/x IA] (reportedly the first)\n"
        flags, _ = L.lint(t)
        self.assertIn("BANNED", kinds(flags))

    def test_external_links_titles_are_not(self):
        t = f"Body.\n== External links ==\n* [https://example.org/x Research notes]. Preserved copy: [{WB}https://example.org/x IA]\n"
        flags, _ = L.lint(t)
        self.assertEqual(flags, [])


if __name__ == "__main__":
    unittest.main()


class MainPageArchiveExemption(unittest.TestCase):
    """Chief, 2026-10-20: Main Page body links are navigation, not citations."""

    def test_main_page_fixture_has_unarchived_links(self):
        flags = L.archive_flags(fx("Main_Page.r113732.wiki"))
        self.assertEqual(len(flags), 3)
        joined = "\n".join(flags)
        self.assertIn("https://play.swccg.com/", joined)
        self.assertIn("https://www.starwarsccg.org/vkit/", joined)
        self.assertIn("Star-Wars-CCG-Tournament-Guide-2.2.pdf", joined)

    def test_main_page_exempt_from_archive(self):
        text = fx("Main_Page.r113732.wiki")
        for title in ("Main Page", "Main_Page", "main page"):
            flags, _ = L.lint(text, title)
            self.assertFalse([f for f in flags if f.startswith("ARCHIVE")], title)

    def test_other_pages_not_exempt(self):
        text = "Play on [https://play.swccg.com/ GEMP].\n"
        self.assertEqual(kinds(L.lint(text, "Main Page")[0]), [])
        self.assertEqual(kinds(L.lint(text, "Main Page/Draft")[0]), ["ARCHIVE"])
        self.assertEqual(kinds(L.lint(text, "Virtual Block 7")[0]), ["ARCHIVE"])
        self.assertEqual(kinds(L.lint(text)[0]), ["ARCHIVE"])

    def test_main_page_other_checks_still_run(self):
        text = "Contact someone@example.com.\n\n== Sources ==\n* x\n"
        self.assertEqual(sorted(kinds(L.lint(text, "Main Page")[0])), ["EMAIL", "HEADING"])

    def test_cli_main_page_draft(self):
        script = str(HERE.parent / "style_lint.py")
        fixture = str(FX / "Main_Page.r113732.wiki")
        # no --title: not known to be the Main Page, so ARCHIVE applies
        bad = subprocess.run([sys.executable, script, fixture], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("ARCHIVE", bad.stdout)


class TemplateSourcesHeading(unittest.TestCase):
    """Chief, 2026-10-20: only a Sources heading in the page's own wikitext fails."""

    def test_card_template_heading_is_exempt(self):
        text = fx("Template_Card.r111232.wiki")
        self.assertIn("== Sources ==", text)
        flags, _ = L.lint(text, "Template:Card")
        self.assertFalse([f for f in flags if f.startswith("HEADING")])

    def test_card_page_using_template_passes(self):
        text = fx("Admiral_Motti_Battlestation_Coordinator_V.r114110.wiki")
        self.assertIn("|sources=", text)
        flags, _ = L.lint(text, "Admiral Motti, Battlestation Coordinator (V)")
        self.assertEqual(flags, [])

    def test_own_sources_heading_on_other_page_fails(self):
        # card pages may now keep Sources (Bill, 2026-10-20); a person page using a template may not
        text = "{{Infobox person\n|name=X\n}}\nX is a player.\n== Sources ==\n* x\n[[Category:Players]]\n"
        flags, _ = L.lint(text, "X")
        self.assertEqual(kinds(flags), ["HEADING"])

    def test_heading_outside_includeonly_on_template_fails(self):
        text = "<noinclude>\n== Sources ==\n</noinclude><includeonly>\n== Sources ==\n{{{sources}}}</includeonly>"
        self.assertEqual(kinds(L.lint(text, "Template:X")[0]), ["HEADING"])
        self.assertEqual(L.own_headings("<includeonly>\n== Sources ==\n</includeonly>\n== Notes ==\n"), ["Notes"])

    def test_unclosed_includeonly(self):
        self.assertEqual(L.own_headings("== Lead ==\n<includeonly>\n== Sources ==\n"), ["Lead"])


class BannedWordsSkipNames(unittest.TestCase):
    """Chief, 2026-10-20: card titles and link text are names, not the editor's voice."""

    def test_2009_reorganization_card_title_not_banned(self):
        text = fx("2009_Virtual_Block_Reorganization.r94305.wiki")
        self.assertIn("# We Have A Prisoner &amp; I Can't Shake Him!", text)
        flags, _ = L.lint(text, "2009 Virtual Block Reorganization")
        self.assertEqual([f for f in flags if f.startswith("BANNED")], [])

    def test_card_titles_plain_text(self):
        for line in ("* We Have A Prisoner", "Deploy We're Doomed (V) early.", "Old Allies / We Need Your Help is an Objective."):
            self.assertEqual([f for f in L.lint(line)[0] if f.startswith("BANNED")], [], line)

    def test_link_text_and_cardlink(self):
        for line in ("Played [[We Have A Plan|We Have A Plan]] first.", "Played [[Here We Go Again]] first.",
                     "Played {{CardLink|We're Doomed}} first.", "Read [https://example.org/x We probably won] (copy)."):
            self.assertEqual([f for f in L.lint(line)[0] if f.startswith("BANNED")], [], line)

    def test_editor_voice_still_flagged(self):
        self.assertEqual(kinds(L.lint("We think the card was probably reprinted.")[0]), ["BANNED", "BANNED"])
        self.assertEqual(kinds(L.lint("We Have A Prisoner was reprinted, we think.")[0]), ["BANNED"])


class SourcesOnCardAndSetPages(unittest.TestCase):
    """Bill, 2026-10-20: Sources lists are for pages that transcribe one source: card pages and
    set tables join deck and event pages."""
    SRC = f"\n== Sources ==\n* [https://example.com/c Card list]. Preserved copy: [{WB}https://example.com/c IA]\n"

    def test_card_template_page_allowed(self):
        text = fx("Admiral_Motti_Battlestation_Coordinator_V.r114110.wiki") + self.SRC
        flags, _ = L.lint(text, "Admiral Motti, Battlestation Coordinator (V)")
        self.assertEqual(flags, [])

    def test_cards_category_allowed(self):
        self.assertNotIn("HEADING", kinds(L.lint("A card." + self.SRC + "[[Category:Cards]]")[0]))
        self.assertNotIn("HEADING", kinds(L.lint("A card." + self.SRC, cats={"Category:Cards"})[0]))

    def test_set_table_pages_allowed(self):
        for cat in ("Sets", "Decipher sets", "Virtual Legacy sets", "Current Virtual sets"):
            self.assertNotIn("HEADING", kinds(L.lint("A set." + self.SRC + f"[[Category:{cat}]]")[0]), cat)
        self.assertNotIn("HEADING", kinds(L.lint("A set." + self.SRC, cats={"Category:Decipher sets"})[0]))

    def test_virtual_block_7_fixture_sources_allowed(self):
        text = fx("Virtual_Block_7.r112843.wiki")
        self.assertNotIn("HEADING", kinds(L.lint(text, "Virtual Block 7", cats={"Category:Sets"})[0]))

    def test_cardlink_and_sandbox_do_not_make_a_card_page(self):
        for t in ("Played {{CardLink|Motti}}.", "{{Card/sandbox\n|title=X\n}}", "<!-- {{Card|x}} -->"):
            self.assertIn("HEADING", kinds(L.lint(t + self.SRC)[0]), t)

    def test_other_pages_still_flagged(self):
        for cat in ("People", "Players", "Rules", "Epic Event", "Card types"):
            self.assertIn("HEADING", kinds(L.lint("Text." + self.SRC + f"[[Category:{cat}]]")[0]), cat)
