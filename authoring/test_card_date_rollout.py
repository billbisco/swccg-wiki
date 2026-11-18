import unittest
from card_date_rollout import apply_date_claim,sha256,UnsafeDateEdit

class DateRolloutTests(unittest.TestCase):
    def claim(self,text,**extra):return dict(field='released',old_value='',new_value='July 1996<ref>checked source</ref>',base_wikitext_sha256=sha256(text),card_uid='2_62',**extra)
    def test_add_preserves_other_fields_nested_values_and_surrounding_prose(self):
        text='Lead\n{{Card\n|title=Death Star: Trench\n|card_uid=2_62\n|text={{X|a=b}} [[One|Two]]\n|versions={{Card versions|a|b}}\n}}\nFoot'
        result=apply_date_claim(text,self.claim(text));self.assertEqual(text.replace('|versions=','|released=July 1996<ref>checked source</ref>\n|versions='),result)
    def test_change_empty_existing_field_preserves_whitespace(self):
        text='{{Card|card_uid=2_62|released= \n|versions=X}}';result=apply_date_claim(text,self.claim(text))
        self.assertIn('|released= July 1996<ref>checked source</ref>\n|versions=',result)
    def test_commented_and_nowiki_examples_are_not_edited(self):
        text='<!--{{Card|card_uid=9_1}}--><nowiki>{{Card|x=y}}</nowiki>{{Card|card_uid=2_62|versions=V}}'
        result=apply_date_claim(text,self.claim(text));self.assertTrue(result.startswith(text.split('{{Card|card_uid=2_62')[0]))
    def test_rejects_stale_base_even_when_target_date_is_empty(self):
        text='{{Card|card_uid=2_62|versions=V}}';claim=self.claim(text)
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text+'Peer change',claim)
    def test_rejects_date_overwrite_not_approved(self):
        text='{{Card|card_uid=2_62|released=1997|versions=V}}'
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text,self.claim(text))
    def test_rejects_duplicate_parameters(self):
        text='{{Card|card_uid=2_62|released=|released=|versions=V}}'
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text,self.claim(text))
    def test_rejects_other_printing(self):
        text='{{Card|card_uid=52_62|versions=V}}'
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text,self.claim(text))
    def test_rejects_unsourced_date(self):
        text='{{Card|card_uid=2_62|versions=V}}';claim=self.claim(text);claim['new_value']='1996'
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text,claim)
    def test_rejects_non_date_edit(self):
        text='{{Card|card_uid=2_62|versions=V}}';claim=self.claim(text);claim['field']='card_uid'
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text,claim)
    def test_rejects_multiple_actual_templates(self):
        text='{{Card|card_uid=2_62}}{{Card|card_uid=2_62}}'
        with self.assertRaises(UnsafeDateEdit):apply_date_claim(text,self.claim(text))
    def test_citation_links_with_piped_wiki_links_roundtrip(self):
        text='{{Card|card_uid=2_62|versions=V}}';claim=self.claim(text);claim['new_value']='1996<ref>[[Decipher|Publisher]] {{Cite|x=y}}</ref>'
        self.assertIn(claim['new_value'],apply_date_claim(text,claim))
    def test_approved_noop(self):
        text='{{Card|card_uid=2_62|released=1996<ref>X</ref>|versions=V}}';claim=self.claim(text);claim['old_value']=claim['new_value']='1996<ref>X</ref>'
        self.assertEqual(text,apply_date_claim(text,claim))

if __name__=='__main__':unittest.main()
