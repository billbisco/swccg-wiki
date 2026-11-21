import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import failed_capture_recovery as R
import wayback_worker as W
from wayback_control import Control, Paused

URL='https://example.com/a'
CAP='https://web.archive.org/web/20261020174512/'+URL


class Recovery(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name); self.clock=1800000000
        self.entry={'status':'failed','error':'no job_id: same snapshot had been made','tries':6,'last':'2026-11-01T00:00:00Z'}
        self.done={URL:dict(self.entry)}; self.changed={}
        self.data=R.initialize(self.root,self.done,self.clock)
        self.control=Control(self.root,'test',clock=lambda:self.clock); self.control.__enter__(); self.addCleanup(self.control.__exit__,None,None,None)
        self.control.initial_done={URL:dict(self.entry)}; self.control.done=self.done
        self.auth=patch.object(W,'AUTH','fixture'); self.auth.start(); self.addCleanup(self.auth.stop)
        self.guard=patch.object(W,'suppressed_url',return_value=False); self.guard.start(); self.addCleanup(self.guard.stop)

    def run_one(self, urls=()):
        R.reconcile_one(W,self.control,self.data,self.done,self.changed,urls,time.monotonic()+600)

    def test_freeze_classification_and_original(self):
        self.assertEqual('auth',R.category(dict(self.entry,error='HTTP Error 401: Unauthorized')))
        self.assertEqual('no_job',R.category(dict(self.entry,error='no job_id: already archived #401')))
        self.assertIsNone(R.category(dict(self.entry,error='connection refused')))
        self.done['new']=dict(self.entry)
        self.assertEqual(1,R.health(R.initialize(self.root,self.done,self.clock),self.done)['total'])
        self.assertEqual(self.entry,self.data['rows'][URL]['original'])

    def test_verified_first_and_durable_pace(self):
        with patch.object(R,'lookup',return_value=CAP) as look,patch.object(W,'verify',return_value=('verified',{'method':'sha256'})):
            self.run_one(); self.run_one(); self.assertEqual(1,look.call_count)
        self.assertEqual('verified',self.done[URL]['status'])
        self.assertEqual(1,R.health(self.data,self.done)['verified'])
        self.assertEqual(self.entry,R.load_cohort(self.root)['rows'][URL]['original'])

    def test_no_capture_only_requeues_active_requested_url(self):
        with patch.object(R,'lookup',return_value=None): self.run_one([URL])
        self.assertEqual('retry',self.done[URL]['status']); self.assertEqual(0,self.done[URL]['tries'])
        self.assertEqual(1,R.health(self.data,self.done)['in_progress'])

    def test_no_capture_not_in_queue_requires_review(self):
        with patch.object(R,'lookup',return_value=None): self.run_one()
        self.assertEqual(self.entry,self.done[URL]); self.assertEqual(1,R.health(self.data,self.done)['review'])

    def test_cooldown_and_received_candidate(self):
        self.control.state['mode']='half_open'
        with patch.object(R,'lookup',side_effect=AssertionError('no request')): self.run_one()
        self.assertEqual(0,self.data['next_at'])
        self.done[URL]['capture']=CAP
        self.assertEqual(URL,R.manual_candidates(W,self.root,self.done)[0]['url'])
        self.done[URL]['capture']=CAP.replace('/a','/b')
        self.assertEqual([],R.manual_candidates(W,self.root,self.done))

    def test_provider_pause_preserves_attempt_and_original(self):
        with patch.object(R,'lookup',side_effect=Paused('hold')):
            with self.assertRaises(Paused): self.run_one()
        self.assertEqual(self.entry,self.done[URL]); self.assertGreater(R.load_cohort(self.root)['next_at'],self.clock)

    def test_lookup_empty_vs_ambiguous(self):
        with patch.object(W,'_json',return_value={'archived_snapshots':{}}): self.assertIsNone(R.lookup(W,URL))
        with patch.object(W,'_json',return_value={}):
            with self.assertRaises(ValueError): R.lookup(W,URL)

    def test_registered_payload_must_match(self):
        self.done[URL]['registered_payload_sha256']='a'*64
        with patch.object(R,'lookup',return_value=CAP),patch.object(W,'verify',return_value=('verified',{'method':'sha256','sha256':'b'*64})):
            self.run_one()
        self.assertEqual('failed',self.done[URL]['status'])
