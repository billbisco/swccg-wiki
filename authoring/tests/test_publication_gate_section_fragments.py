"""Section links must bind the real file while preserving literal-block handling."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from publication_gate import referenced_originals


class FileSectionFragments(unittest.TestCase):
    def test_section_targets_bind_the_canonical_original(self):
        cases = [
            ('[[:File:Card.png#filehistory|file history]]', {'File:Card.png'}),
            ('[[File:Card.png#Summary|thumb|Caption]]', {'File:Card.png'}),
            ('[[Image:Card.png#Summary]]', {'File:Card.png'}),
            ('[[File:Card.png]][[:File:Card.png#filehistory]]', {'File:Card.png'}),
            ('|image=Card.png#Summary\n|hires_image=Card-hires.webp#filehistory\n',
             {'File:Card.png', 'File:Card-hires.webp'}),
            ('<gallery>\nFile:Card.png#Summary|caption\n</gallery>', {'File:Card.png'}),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(referenced_originals(text), expected)

    def test_fragment_only_targets_do_not_create_phantom_originals(self):
        self.assertEqual(referenced_originals('[[:File:#filehistory]]\n|image=#Summary\n'), set())

    def test_percent_encoding_and_paths_are_not_rewritten(self):
        self.assertEqual(referenced_originals('[[File:A%23B.png#History]]'), {'File:A%23B.png'})
        self.assertEqual(referenced_originals('[[File:subdir/Card.png#History]]'), {'File:subdir/Card.png'})

    def test_peer_literal_and_comment_behavior_is_preserved(self):
        cases = [
            ('<nowiki>[[File:hidden.png#History]]</nowiki>[[File:visible.png#History]]',
             {'File:visible.png'}),
            ('<pre>[[File:hidden.png#History]]</pre>[[File:visible.png]]',
             {'File:visible.png'}),
            ('<!-- <nowiki> -->[[File:visible.png]]<!-- </nowiki> -->',
             {'File:visible.png'}),
            ('<code>[[File:visible.png#History]]</code>', {'File:visible.png'}),
            ('<!-- [[File:hidden.png#History]] -->[[File:visible.png]]',
             {'File:visible.png'}),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(referenced_originals(text), expected)


if __name__ == '__main__':
    unittest.main()
