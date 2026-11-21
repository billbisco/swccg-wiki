import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import wayback_worker as W
import wayback_reliability as R
from wayback_control import Control,Paused

URL='https://example.com/a'; CAP='https://web.archive.org/web/20261020174512/'+URL


class ReliabilityTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.root=Path(self.t.name)
        self.time=1800000000; self.c=Control(self.root,'fixture',clock=lambda:self.time);self.c.__enter__();self.addCleanup(self.c.__exit__,None,None,None)
        self.p=patch.object(W,'AUTH','fixture');self.p.start();self.addCleanup(self.p.stop)

    def test_exact_scope_and_unknown_limit(self):
        for code,event in R.LIMIT_CODES.items():
            self.assertEqual(event,R.classify({'status_ext':code,'message':'ambiguous limit'}))
        self.assertEqual('unknown_limit',R.classify({'message':'unknown limit'}))
        self.assertIsNone(R.classify({'message':'ordinary source failure'}))
        with patch.object(W,'_json',return_value={'status_ext':'error:too-many-daily-captures','_response_retry_after':'90000'}):
            with self.assertRaises(W.ScopedLimit) as x:W.spn2_submit(URL)
            self.assertEqual('90000',x.exception.retry_after)

    def test_scope_preserves_global_counter_and_other_hosts(self):
        self.c.state['failure_count']=6;self.c.defer_source(URL,'target_host_limit','3600')
        self.assertFalse(self.c.source_allowed('https://example.com/b'))
        self.assertTrue(self.c.source_allowed('https://other.example/b'))
        self.assertEqual(6,self.c.state['failure_count']);self.assertEqual('healthy',self.c.state['mode'])
        self.time+=3600;self.assertTrue(self.c.source_allowed(URL))

    def test_capacity_zero_no_exponential_and_retry_after(self):
        self.c.state['failure_count']=6
        with patch.object(W,'spn2_user_status',return_value={'available':0,'processing':3}):
            with self.assertRaises(Paused):W.ensure_capacity(self.c)
        self.assertEqual(6,self.c.state['failure_count']);self.assertEqual('account_sessions',self.c.state['provider_event'])
        self.assertEqual(self.time+900,self.c.state['next_attempt'])
        self.assertIsNone(R.capacity({'available':True,'processing':0}))

    def test_capacity_cached_and_consumed(self):
        with patch.object(W,'spn2_user_status',return_value={'available':2,'processing':1}) as call:
            W.ensure_capacity(self.c);W.consume_capacity(self.c);W.ensure_capacity(self.c);self.assertEqual(1,call.call_count)
            W.consume_capacity(self.c)
            with self.assertRaises(Paused):W.ensure_capacity(self.c)

    def test_stale_pending_is_polled_not_resubmitted(self):
        e={'status':'pending','job_id':'old','last':'2026-01-01T00:00:00Z','tries':1};d={URL:e};self.c.done=d;self.c.initial_done={URL:dict(e)}
        m=R.initialize_stale(W,self.root,d,self.time)
        with patch.object(W,'spn2_status',return_value={'status':'pending'}) as status,patch.object(W.recovery,'lookup',side_effect=AssertionError('active job')):
            R.reconcile_stale(W,self.c,m,d,{},[URL],time.monotonic()+600)
            R.reconcile_stale(W,self.c,m,d,{},[URL],time.monotonic()+600)
        self.assertEqual(1,status.call_count);self.assertEqual('pending',d[URL]['status']);self.assertEqual(e,R.load_stale(self.root)['rows'][URL]['original'])

    def test_stale_success_adopts_exact_capture_and_keeps_original_job(self):
        e={'status':'pending','job_id':'old','last':'2026-01-01T00:00:00Z','tries':1};d={URL:e};self.c.done=d;self.c.initial_done={URL:dict(e)}
        m=R.initialize_stale(W,self.root,d,self.time)
        with patch.object(W,'spn2_status',return_value={'status':'success','timestamp':'20261020174512','original_url':URL}),patch.object(W,'verify',return_value=('verified',{'method':'sha256'})):
            R.reconcile_stale(W,self.c,m,d,{},[],time.monotonic()+600)
        self.assertEqual('verified',d[URL]['status']);self.assertEqual('old',d[URL]['job_id']);self.assertEqual(1,R.stale_counts(m,d)['verified'])

    def test_canary_requires_new_accepted_capture_and_no_hold(self):
        self.c.state['mode']='half_open';self.c.done={URL:{'capture':CAP,'status':'retry'}};self.c.submitting(URL)
        self.assertIsNone(self.c.accepted_probe());self.c.accepted_submission()
        health={'mode':'half_open','awaiting_canary_verification':True,'next_eligible_attempt_at':None}
        self.c.done[URL]['status']='ok'
        self.assertIsNone(R.canary_candidate(W,self.root,self.c.done,health))
        self.c.done[URL]['capture']=CAP.replace('20261020174512','20261021174512')
        self.assertEqual(URL,R.canary_candidate(W,self.root,self.c.done,health)['url'])
        health['next_eligible_attempt_at']='hold';self.assertIsNone(R.canary_candidate(W,self.root,self.c.done,health))
