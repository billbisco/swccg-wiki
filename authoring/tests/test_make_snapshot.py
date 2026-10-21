"""Tests for authoring/make_snapshot.py FlareSolverr session handling (FlareSolverr and HTTP are mocked).
Run: python3 -m unittest discover -s authoring/tests"""
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import make_snapshot as M  # noqa: E402

FS = 'http://localhost:8191/v1'
PAGE = ('<html><head><link rel="stylesheet" href="/style.css"></head>'
        '<body><p>hello</p></body></html>')


class Resp:
    def __init__(self, ok=False, content=b'', headers=None, js=None):
        self.ok, self.content, self.headers, self._js = ok, content, headers or {}, js

    def json(self):
        return self._js


def fake_post(calls):
    def post(url, json=None, timeout=None):
        calls.append(json)
        if json['cmd'] == 'request.get':
            return Resp(js={'solution': {'response': '<html><body><pre>p{color:red}</pre></body></html>'}})
        return Resp(js={'status': 'ok'})
    return post


def blocked_get(self, url, timeout=None):  # Cloudflare blocks every plain HTTP fetch
    return Resp(ok=False, headers={'cf-mitigated': 'challenge'})


@mock.patch.object(M.requests.Session, 'get', blocked_get)
class SessionTests(unittest.TestCase):
    def run_main(self, *extra, fail=False):
        calls = []
        with tempfile.TemporaryDirectory() as d:
            src, out = os.path.join(d, 'p.html'), os.path.join(d, 'o.html')
            Path(src).write_text(PAGE, encoding='utf-8')
            args = [src, '--url', 'https://forum.example.org/viewtopic.php?t=1', '-o', out, '--flaresolverr', FS, *extra]
            with mock.patch.object(M.requests, 'post', fake_post(calls)), \
                 mock.patch('sys.stderr', new_callable=lambda: open(os.devnull, 'w')):
                if fail:
                    with mock.patch.object(M, 'inline_css', side_effect=RuntimeError('boom')):
                        with self.assertRaises(RuntimeError):
                            M.main(args)
                else:
                    M.main(args)
                    self.assertIn('p{color:red}', Path(out).read_text(encoding='utf-8'))
        return calls

    def test_default_session_is_unique_per_run_and_destroyed(self):
        calls = self.run_main()
        gets = [c for c in calls if c['cmd'] == 'request.get']
        self.assertEqual(len(gets), 1)
        name = gets[0]['session']
        self.assertRegex(name, r'^snap-%d-\d{8}T\d{12}$' % os.getpid())
        self.assertNotEqual(name, 'snap')
        self.assertEqual(calls[-1], {'cmd': 'sessions.destroy', 'session': name})
        self.assertNotEqual(name, M.default_fs_session())

    def test_destroy_runs_on_error(self):
        calls = self.run_main(fail=True)
        name = calls[0]['session']
        self.assertEqual(calls[-1], {'cmd': 'sessions.destroy', 'session': name})

    def test_named_session_flag(self):
        calls = self.run_main('--fs-session', 'mine')
        self.assertEqual([c['session'] for c in calls], ['mine', 'mine'])
        self.assertEqual(calls[-1]['cmd'], 'sessions.destroy')

    def test_keep_session_flag(self):
        calls = self.run_main('--fs-session', 'mine', '--keep-fs-session')
        self.assertEqual([c['cmd'] for c in calls], ['request.get'])

    def test_backward_compatible_fetcher_and_no_destroy_when_unused(self):
        calls = []
        with mock.patch.object(M.requests, 'post', fake_post(calls)):
            f = M.Fetcher('auto', 'UA', None, FS)  # old positional signature
            self.assertTrue(f.fs_session.startswith('snap-'))
            f.close()  # FlareSolverr never used -> nothing to destroy
            self.assertEqual(calls, [])
            with M.Fetcher('auto', 'UA', None, FS) as g:
                self.assertIsNotNone(g.get('https://forum.example.org/a.css'))
            self.assertEqual(calls[-1], {'cmd': 'sessions.destroy', 'session': g.fs_session})
            M.Fetcher('auto', 'UA', None).close()  # no FlareSolverr at all


if __name__ == '__main__':
    unittest.main()
