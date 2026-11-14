"""Rejected authentication must stop rather than create another submission lane."""
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import wayback_worker as W

URL='https://wiki.swccg.com/images/0/0e/Promo-Foil-L-itcouldbeworse.jpg'
CAP='https://web.archive.org/web/20261114000316/'+URL

class SubmissionFallback(unittest.TestCase):
    def test_large_queue_dedup_keeps_original_order_and_comments(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/W.QUEUE).parent.mkdir(parents=True)
            (root/W.QUEUE).write_text('# note\n'+URL+'\nhttps://example.org/b.png\n'+URL+'\n\n')
            urls,done=W.load(root)
            self.assertEqual([URL,'https://example.org/b.png'],urls);self.assertEqual({},done)
    def test_auth_401_never_falls_back(self):
        state={'authenticated':True}
        error=urllib.error.HTTPError('https://web.archive.org/save',401,'Unauthorized',{},None)
        with patch.object(W,'spn2_submit',side_effect=error) as spn,patch.object(W,'save_anon',return_value=CAP) as anon:
            with self.assertRaises(urllib.error.HTTPError):
                W.submit_capture(URL,None,state)
            self.assertTrue(state['authenticated'])
            spn.assert_called_once()
            anon.assert_not_called()
    def test_permission_denial_is_not_treated_as_bad_auth(self):
        error=urllib.error.HTTPError('https://web.archive.org/save',403,'Forbidden',{},None)
        with patch.object(W,'spn2_submit',side_effect=error),patch.object(W,'save_anon') as anon:
            with self.assertRaises(urllib.error.HTTPError):W.submit_capture(URL,None,{'authenticated':True})
            anon.assert_not_called()
    def test_throttle_keeps_existing_backoff_path(self):
        with patch.object(W,'spn2_submit',side_effect=W.Throttled('HTTP429')),patch.object(W,'save_anon') as anon:
            with self.assertRaises(W.Throttled):W.submit_capture(URL,None,{'authenticated':True})
            anon.assert_not_called()
    def test_authenticated_submission_unchanged(self):
        with patch.object(W,'spn2_submit',return_value={'job_id':'test-job'}),patch.object(W,'save_anon') as anon:
            self.assertEqual({'job_id':'test-job'},W.submit_capture(URL,None,{'authenticated':True}))
            anon.assert_not_called()
    def test_recapture_flag_unchanged(self):
        with patch.object(W,'spn2_submit',return_value={'job_id':'test-job'}) as spn:
            W.submit_capture(URL,{'recapture':True},{'authenticated':True})
            spn.assert_called_once_with(URL,force=True)
    def test_existing_anonymous_mode_unchanged(self):
        with patch.object(W,'spn2_submit') as spn,patch.object(W,'save_anon',return_value=CAP):
            self.assertEqual({'anonymous_capture':CAP},W.submit_capture(URL,None,{'authenticated':False}))
            spn.assert_not_called()

if __name__=='__main__':unittest.main()
