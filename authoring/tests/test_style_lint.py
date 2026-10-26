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


    def test_twitter_capture_covers_x_com_body_link(self):
        t = ('* [https://x.com/swccg/status/1327598657764356098 Tweet]\n'
             f'<ref>[https://twitter.com/swccg/status/1327598657764356098 Tweet]. Preserved copy: '
             f'[{WB}https://twitter.com/swccg/status/1327598657764356098 Internet Archive]</ref>')
        self.assertEqual(L.archive_flags(t), [])
        self.assertEqual(L.norm_url("https://www.x.com/a/status/1"), L.norm_url("http://twitter.com/a/status/1"))
        self.assertNotEqual(L.norm_url("https://box.com/a"), L.norm_url("https://twitter.com/a"))


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


class BannedWordsSkipDeckTitle(unittest.TestCase):
    """Chief, 2026-10-20: a deck page's bold name and decklist titles are names, not the editor's voice."""
    TITLE = "2007 Worlds Day 1 Adam Howland LS We'll Handle This"

    def test_2007_deck_fixture_bold_title_not_banned(self):
        text = fx("2007_Worlds_Day_1_Adam_Howland_LS_Well_Handle_This.r102390.wiki")
        self.assertTrue(text.startswith("'''" + self.TITLE + "'''"))
        for title in (self.TITLE, None):   # by title, and as a bare file
            flags, _ = L.lint(text, title)
            self.assertEqual([f for f in flags if f.startswith("BANNED")], [], title)

    def test_bold_title_skipped(self):
        for text, title in (("'''2007 Worlds Day 2 X LS We Have A Plan''' was the Light Side list.", "2007 Worlds Day 2 X LS We Have A Plan"),
                            ("'''We'll Handle This Deck''' was a Light Side list.", None),
                            ("Played it. The list was named '''Team X LS We Rule'''.", "Team X LS We Rule"),
                            ("* '''Deck title:''' We'll Handle This", None),
                            ("Sheet deck title '''We Came, We Saw''' on page 3.", None)):
            self.assertEqual([f for f in L.lint(text, title)[0] if f.startswith("BANNED")], [], text)

    def test_prose_we_still_flagged(self):
        page = "'''2007 Worlds Day 1 X LS We'll Handle This''' was the Light Side list.\n\nWe think it won."
        self.assertEqual(kinds(L.lint(page, "2007 Worlds Day 1 X LS We'll Handle This")[0]), ["BANNED"])
        self.assertEqual(kinds(L.lint(page)[0]), ["BANNED"])
        self.assertEqual(kinds(L.lint("'''We''' won the event.")[0]), ["BANNED"])   # one bold word is not a name
        self.assertEqual(kinds(L.lint("Intro.\n\n'''Character'''\n\nWe also played it.")[0]), ["BANNED"])
        self.assertEqual(kinds(L.lint("* '''Notes:''' we played it twice.")[0]), ["BANNED"])


class TranscriptSpeechSkipped(unittest.TestCase):
    """Chief, 2026-10-20: on transcript pages quoted speech is the speaker's, not the editor's voice."""
    TITLE = "2007 World Championship interviews (transcript)"
    SPEECH = "'''[00:10] Henry Dunn:''' We probably need more judges, and it is unclear who will help."

    def test_detected_by_title_or_category(self):
        self.assertTrue(L.is_transcript_page(self.TITLE, "x"))
        self.assertTrue(L.is_transcript_page("Some interview/Transcript", "x"))
        self.assertTrue(L.is_transcript_page("Some interview", "x\n[[Category:Transcripts]]"))
        self.assertTrue(L.is_transcript_page("Some interview", "x", ["Category:Transcripts"]))
        self.assertFalse(L.is_transcript_page("2007 World Championship", "x\n[[Category:Interviews]]"))

    def test_fixture_speech_not_flagged(self):
        text = fx("2007_World_Championship_interviews_transcript.r92965.wiki")
        flags, _ = L.lint(text, self.TITLE)
        speech = [f for f in flags if f.split()[0] in ("BANNED", "LONG") and "Dunn:" not in f]
        # only the editor's own lead and transcription note remain (fixture is the pre-cleanup revision)
        self.assertEqual(sorted(kinds(speech)), ["BANNED", "LONG"])
        self.assertTrue(any("marked [unclear]" in f for f in speech))
        self.assertTrue(any(f.startswith("LONG     31 words: The 2007 World Championship interviews") for f in speech))
        self.assertTrue(any("watch?v=LpWqJgmgh2Q" in f for f in flags))   # ARCHIVE still applies

    def test_speech_skipped_on_transcript_page(self):
        page = "Intro line.\n\n" + self.SPEECH + "\n'''Interviewer:''' We think this one probably ran long, " + "word " * 30 + "end.\n"
        self.assertEqual([f for f in L.lint(page, self.TITLE)[0] if f.split()[0] in ("BANNED", "LONG")], [])
        self.assertEqual([f for f in L.lint(page + "[[Category:Transcripts]]", "Some interview")[0]
                          if f.split()[0] in ("BANNED", "LONG")], [])

    def test_own_prose_still_flagged(self):
        page = "We probably filmed these.\n\n" + self.SPEECH + "\n"
        self.assertEqual(sorted(kinds(L.lint(page, self.TITLE)[0])), ["BANNED", "BANNED"])
        self.assertEqual(sorted(kinds(L.lint("''Words marked [unclear] were inaudible.''\n\n" + self.SPEECH, self.TITLE)[0])), ["BANNED"])

    def test_speech_still_flagged_on_ordinary_pages(self):
        self.assertIn("BANNED", kinds(L.lint(self.SPEECH, "Henry Dunn")[0]))
        self.assertEqual(sorted(kinds(L.lint("'''Note:''' we probably won.", self.TITLE)[0])), ["BANNED"] * 3)   # editorial label: note, we, probably

    def test_we_in_linked_card_name_accepted(self):
        for line in ("Shield 11 is listed as [[Ultimatum (Reflections III: A Collector's Bounty)|Ultimatum]].",
                     "Starting card [[We'll Handle This / Duel Of The Fates|We'll Handle This]].",
                     "Combo [[We Shall Double Our Efforts!]] was not in the deck."):
            self.assertEqual([f for f in L.lint(line)[0] if f.startswith("BANNED")], [], line)


class TalkPageComments(unittest.TestCase):
    """Chief, 2026-10-20: on Talk pages other accounts' signed comments are not linted for voice, and a
    Preserved copy anywhere on the page (incl. the forum thread's swccg.com snapshot) satisfies ARCHIVE."""
    CLAUDE = "[[User:Holocron Claude|Holocron Claude]] ([[User talk:Holocron Claude|talk]]) 18:05, 15 October 2026 (UTC)"
    BOT = "[[User:Comlink Cursor|Comlink Cursor]] ([[User talk:Comlink Cursor|talk]]) 00:21, 21 October 2026 (UTC)"
    FORUM = "[https://forum.starwarsccg.org/viewtopic.php?t=85240 thread]"
    SNAP = "[https://web.archive.org/web/20261012164154/https://swccg.com/snapshots/forum/t85240.html Internet Archive]"

    def voice(self, text, title):
        return [f for f in L.lint(text, title)[0] if f.split()[0] in ("BANNED", "LONG")]

    def test_talk_title_detection(self):
        for t in ("Talk:Geoff Bowman", "User talk:Comlink Cursor", "SWCCG Wiki talk:Style guide", "Template_talk:Card"):
            self.assertTrue(L.is_talk_page(t), t)
        for t in ("Geoff Bowman", "Small talk: a deck", None):
            self.assertFalse(L.is_talk_page(t), t)

    def test_other_users_comment_not_flagged(self):
        page = ("== Style pass ==\n=== Possibly faulty data ===\n"
                "* The starting card was inferred from the list.\n" + self.CLAUDE + "\n")
        self.assertEqual(self.voice(page, "Talk:Some deck"), [])

    def test_bot_comment_still_flagged(self):
        page = "== Build notes ==\n* The starting card was inferred from the list.\n" + self.BOT + "\n"
        self.assertEqual(kinds(self.voice(page, "Talk:Some deck")), ["BANNED"])
        draft = "== Build notes ==\n* The starting card was inferred from the list. ~~~~\n"
        self.assertEqual(kinds(self.voice(draft, "Talk:Some deck")), ["BANNED"])

    def test_indented_reply_is_its_own_comment(self):
        page = ("== Q ==\nIt was probably 1998. " + self.CLAUDE + "\n"
                ":Inferred from the box. " + self.BOT + "\n"
                ":Possibly. " + self.CLAUDE.replace("18:05", "19:00") + "\n")
        flags = self.voice(page, "Talk:Some set")
        self.assertEqual(len(flags), 1)
        self.assertIn("'inferred'", flags[0])

    def test_unsigned_text_still_flagged(self):
        page = "== Q ==\nThis was inferred.\n\n== R ==\nOk. " + self.CLAUDE + "\n"
        self.assertEqual(kinds(self.voice(page, "Talk:Some set")), ["BANNED"])

    def test_same_text_on_article_still_flagged(self):
        page = "* The starting card was inferred from the list.\n" + self.CLAUDE + "\n"
        self.assertEqual(kinds(self.voice(page, "Some deck")), ["BANNED"])

    def test_forum_link_with_snapshot_copy_elsewhere_passes_on_talk(self):
        page = "== TD ==\nHe was TD of Event #4 (" + self.FORUM + ").\n\n" + "* Preserved copy: " + self.SNAP + "\n"
        self.assertEqual(L.archive_flags(page, talk=True), [])
        self.assertEqual([f for f in L.lint(page, "Talk:Geoff Bowman")[0] if f.startswith("ARCHIVE")], [])
        # older flat snapshot name counts too
        flat = page.replace("snapshots/forum/t85240.html", "snapshots/forum-t85240.html")
        self.assertEqual(L.archive_flags(flat, talk=True), [])

    def test_article_ref_still_needs_its_own_copy(self):
        # Chief 2026-10-20 (later): articles accept the snapshot capture anywhere for body/list links
        # (ArticleSnapshotRoute), but a <ref> still needs its Preserved copy inside the same ref.
        page = "He was TD of Event #4.<ref>" + self.FORUM + "</ref>\n\n* Preserved copy: " + self.SNAP + "\n"
        flags = [f for f in L.lint(page, "Geoff Bowman")[0] if f.startswith("ARCHIVE")]
        self.assertEqual(len(flags), 1)
        self.assertIn("<ref> cites https://forum.starwarsccg.org/viewtopic.php?t=85240", flags[0])

    def test_other_thread_snapshot_does_not_count(self):
        page = "== TD ==\nSee " + self.FORUM + ".\n* " + self.SNAP.replace("t85240", "t85241") + "\n"
        self.assertEqual(len(L.archive_flags(page, talk=True)), 1)

    def test_live_talk_fixtures_pass(self):
        for name, title in (("Talk_2026_San_Diego_Super_Open.r116646.wiki", "Talk:2026 San Diego Super Open"),
                            ("Talk_Geoff_Bowman.r116647.wiki", "Talk:Geoff Bowman")):
            text = fx(name)
            self.assertEqual(L.lint(text, title)[0], [], name)
        # as an article, the restored comment's wording would still fail (the Geoff Bowman forum links now
        # pass on articles too, via their snapshot captures: ArticleSnapshotRoute)
        self.assertEqual(kinds(L.lint(fx("Talk_2026_San_Diego_Super_Open.r116646.wiki"), "Some article")[0]), ["BANNED"])
        self.assertEqual(L.lint(fx("Talk_Geoff_Bowman.r116647.wiki"), "Some article")[0], [])


class TalkPagePcSnapshots(unittest.TestCase):
    """Chief, 2026-10-20: on Talk pages a capture of swccg.com/snapshots/pc/<slug>.html covers the Players
    Committee post whose URL ends in /<slug>/ (archiving.md naming)."""
    PC = "[https://www.starwarsccg.org/2022-04-pc20-tournament/ PC20 Tournament]"
    SNAP = "[https://web.archive.org/web/20261021001000/https://swccg.com/snapshots/pc/2022-04-pc20-tournament.html Internet Archive]"

    def page(self, snap):
        return "== Sources ==\nThe event page is " + self.PC + ".\n\n:Preserved copy: " + snap + "\n"

    def test_pc_snapshot_matches_on_talk(self):
        self.assertEqual(L.archive_flags(self.page(self.SNAP), talk=True), [])
        self.assertEqual([f for f in L.lint(self.page(self.SNAP), "Talk:Timo Dusel")[0] if f.startswith("ARCHIVE")], [])
        nested = self.page(self.SNAP).replace("org/2022-04-pc20-tournament/", "org/community/2022-04-pc20-tournament/")
        self.assertEqual(L.archive_flags(nested, talk=True), [])   # slug is the last path segment

    def test_other_slug_does_not_match(self):
        other = self.SNAP.replace("2022-04-pc20-tournament.html", "2022-09-european-championship.html")
        flags = L.archive_flags(self.page(other), talk=True)
        self.assertEqual(len(flags), 1)
        self.assertIn("2022-04-pc20-tournament", flags[0])
        forum = self.SNAP.replace("pc/2022-04-pc20-tournament.html", "forum/t2022.html")
        self.assertEqual(len(L.archive_flags(self.page(forum), talk=True)), 1)
        res = self.page(self.SNAP).replace("www.starwarsccg.org/", "res.starwarsccg.org/")   # other host
        self.assertEqual(len(L.archive_flags(res, talk=True)), 1)

    def test_article_without_any_copy_still_fails(self):
        text = "The event page is " + self.PC + ".\n"
        self.assertEqual(len(L.archive_flags(text)), 1)
        self.assertEqual(len([f for f in L.lint(text, "Timo Dusel")[0] if f.startswith("ARCHIVE")]), 1)


class ArticleSnapshotRoute(unittest.TestCase):
    """Chief, 2026-10-20: on articles too, a Wayback capture of the swccg.com forum/pc snapshot satisfies
    ARCHIVE for the forum thread / PC post it preserves, wherever the link sits (body, See also,
    External links); refs keep the same-ref rule, where any Preserved copy inside the ref counts."""
    FORUM = "https://forum.starwarsccg.org/viewtopic.php?t=86618"
    FSNAP = "https://web.archive.org/web/20261021001248/https://swccg.com/snapshots/forum/t86618.html"
    PC = "https://www.starwarsccg.org/2026-04-san-diego-super-open-san-diego-california-apr-11-to-12-2026/"
    PSNAP = ("https://web.archive.org/web/20261021000913/https://swccg.com/snapshots/pc/"
             "2026-04-san-diego-super-open-san-diego-california-apr-11-to-12-2026.html")

    def arch(self, text, title="2026 San Diego Super Open"):
        return [f for f in L.lint(text, title)[0] if f.startswith("ARCHIVE")]

    def test_forum_match_in_body_and_see_also(self):
        page = ("Decks are in the [" + self.FORUM + " decklist thread].<ref>[" + self.FORUM + " t86618]. Preserved copy: ["
                + self.FSNAP + " Internet Archive]</ref>\n\n== See also ==\n* [" + self.FORUM + " GEMP decks]\n\n"
                "== References ==\n<references />\n")
        self.assertEqual(self.arch(page), [])
        flat = page.replace("snapshots/forum/t86618.html", "snapshots/forum-t86618.html")
        self.assertEqual(self.arch(flat), [])

    def test_pc_match_in_external_links(self):
        page = ("Results.<ref>[" + self.PC + " PC results]. Preserved copy: [" + self.PSNAP + " Internet Archive]</ref>\n\n"
                "== External links ==\n* [" + self.PC + " PC results page]\n")
        self.assertEqual(self.arch(page), [])

    def test_forum_non_match(self):
        other = self.FSNAP.replace("t86618", "t86617")
        page = "Decks: [" + self.FORUM + " thread].\n\n* Copy: [" + other + " Internet Archive]\n"
        flags = self.arch(page)
        self.assertEqual(len(flags), 1)
        self.assertIn("t=86618", flags[0])
        post = "Decks: [https://forum.starwarsccg.org/viewtopic.php?p=86618 post].\n\n* Copy: [" + self.FSNAP + " IA]\n"
        self.assertEqual(len(self.arch(post)), 1)   # p= is a post id, not the thread

    def test_pc_non_match(self):
        other = self.PSNAP.replace("2026-04-san-diego", "2025-01-las-vegas")
        page = "See [" + self.PC + " results].\n\n* Copy: [" + other + " Internet Archive]\n"
        self.assertEqual(len(self.arch(page)), 1)
        res = "See [https://res.starwarsccg.org/2026-04-san-diego-super-open-san-diego-california-apr-11-to-12-2026/ x].\n* [" + self.PSNAP + " IA]\n"
        self.assertEqual(len(self.arch(res)), 1)   # only www.starwarsccg.org posts map to pc/ snapshots

    HOME = "https://web.archive.org/web/20261020234753/https://swccg.com/snapshots/pc/home.html"

    def test_pc_bare_host_matches_home_snapshot(self):
        for host in ("https://www.starwarsccg.org/", "https://www.starwarsccg.org", "http://www.starwarsccg.org/",
                     "https://starwarsccg.org/", "http://starwarsccg.org"):
            page = "Run by the [" + host + " Players Committee].\n\n== External links ==\n* [" + host + " PC site]\n* [" + self.HOME + " IA]\n"
            self.assertEqual(self.arch(page), [], host)
            talk = "* Site: [" + host + " PC]. --Someone\n\n:Copy: [" + self.HOME + " IA]. --[[User:Comlink Cursor|Comlink Cursor]]\n"
            self.assertEqual(self.arch(talk, "Talk:Players Committee"), [], host)

    def test_pc_bare_host_non_match(self):
        host = "https://www.starwarsccg.org/"
        # a capture of some other pc/ snapshot does not cover the home page
        page = "See the [" + host + " PC site].\n\n* [" + self.PSNAP + " IA]\n"
        flags = self.arch(page)
        self.assertEqual(len(flags), 1)
        self.assertIn("starwarsccg.org", flags[0])
        # and the home capture does not cover a post with a real slug
        page = "See [" + self.PC + " results].\n\n* [" + self.HOME + " IA]\n"
        self.assertEqual(len(self.arch(page)), 1)
        # a non-root path on the host is a slug, not the home page
        page = "See [https://www.starwarsccg.org/tournaments/ tournaments].\n\n* [" + self.HOME + " IA]\n"
        self.assertEqual(len(self.arch(page)), 1)


class IndexPagesSkipLong(unittest.TestCase):
    """People, People/<letter> and [[Category:Indexes]] pages skip the sentence-length check."""

    NAMES = " · ".join(f"[[Player {i}]]" for i in range(80))
    PROSE = "Word " * 60 + "ends here."

    def long_flags(self, text, title, cats=None):
        return [f for f in L.lint(text, title, cats)[0] if f.startswith("LONG")]

    def test_people_fixture_passes(self):
        text = fx("People.r108468.wiki")
        self.assertEqual(self.long_flags(text, "People"), [])
        self.assertTrue(self.long_flags(text, "Someone"))  # same text under another title still flags

    def test_people_letter_titles(self):
        for t in ("People", "People/W", "People/A", "people/b"):
            self.assertTrue(L.is_index_page(t, ""), t)
        self.assertFalse(L.is_index_page("People/Westergard", ""))
        self.assertFalse(L.is_index_page("People of Tatooine", ""))

    def test_category_indexes_in_wikitext(self):
        text = self.NAMES + "\n\n[[Category:Indexes]]\n"
        self.assertEqual(self.long_flags(text, "Card index"), [])
        self.assertTrue(self.long_flags(self.NAMES, "Card index"))

    def test_category_indexes_from_live_categories(self):
        self.assertEqual(self.long_flags(self.PROSE, "Card index", {"Category:Indexes"}), [])
        self.assertTrue(self.long_flags(self.PROSE, "Card index", {"Category:Players"}))

    def test_other_checks_still_run_on_index_pages(self):
        text = "Contact x@example.com for the list.\n\n[[Category:Indexes]]\n"
        self.assertIn("EMAIL", kinds(L.lint(text, "People")[0]))


class ServiceAttachedRole(unittest.TestCase):
    """SERVICE ignores a role noun attached to a wikilink to another person (Chief, 2026-10-25)."""

    PERSON = "\n\n[[Category:People]]\n"

    def flags(self, lead, title="Richard Handley"):
        return L.service_flags(lead + self.PERSON, title)

    def test_role_before_link_with_quoted_short_form(self):
        lead = ("'''Richard Handley''' wrote for ''[[Star Wars Insider]]''. At [[DecipherCon 1999]] "
                "[[Evan Lorentz]] and Super Volunteer (\"Super Vol\") [[Kim Burns]] briefed him.")
        self.assertEqual(self.flags(lead), [])

    def test_link_then_appositive_role(self):
        lead = "'''Richard Handley''' met [[Kim Burns]], a DecipherCon volunteer, at [[DecipherCon 1999]]."
        self.assertEqual(self.flags(lead), [])

    def test_subject_as_volunteer_still_flags(self):
        lead = "'''Richard Handley''' was a volunteer at [[DecipherCon 1999]] alongside [[Kim Burns]]."
        self.assertEqual(kinds(self.flags(lead)), ["SERVICE"])

    def test_role_attached_to_self_link_still_flags(self):
        lead = "Super Volunteer [[Richard Handley]] worked the [[DecipherCon 1999]] hall."
        self.assertEqual(kinds(self.flags(lead)), ["SERVICE"])

    def test_role_attached_to_event_link_still_flags(self):
        lead = "'''Richard Handley''' was a volunteer [[DecipherCon 1999]] helper."
        self.assertEqual(kinds(self.flags(lead)), ["SERVICE"])

    def test_role_elsewhere_in_sentence_still_flags(self):
        lead = "'''Richard Handley''' met [[Kim Burns]] and later became a volunteer himself."
        self.assertEqual(kinds(self.flags(lead)), ["SERVICE"])
