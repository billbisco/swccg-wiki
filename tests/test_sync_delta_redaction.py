"""Failed pushes must never leak the auth header or token."""
import contextlib
import io
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import sync_delta  # noqa: E402

FAKE = "ghp_" + "FAKEtoken1234567890abcdefXYZ"
FAKE_PAT = "github_pat_" + "11FAKE_abcdefghijklmnop"


class RedactionTest(unittest.TestCase):
    def test_redact_patterns(self):
        for raw in (
            f"http.extraheader=AUTHORIZATION: bearer {FAKE}",
            f"Authorization: token {FAKE}",
            f"https://x-access-token:{FAKE}@github.com/a/b.git",
            f"leaked {FAKE_PAT} here",
        ):
            out = sync_delta.redact(raw)
            self.assertNotIn(FAKE, out)
            self.assertNotIn(FAKE_PAT, out)
            self.assertIn("[REDACTED]", out)

    def test_failed_push_does_not_print_token(self):
        failing = subprocess.CompletedProcess(
            args=[], returncode=128, stdout="",
            stderr=f"fatal: auth failed for header bearer {FAKE}\n",
        )
        buf_out, buf_err = io.StringIO(), io.StringIO()
        with mock.patch.dict("os.environ", {"GH_TOKEN": FAKE}), \
             mock.patch.object(sync_delta.subprocess, "run", return_value=failing), \
             contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
            with self.assertRaises(sync_delta.GitError) as cm:
                sync_delta.push()
            import traceback
            tb = "".join(traceback.format_exception(cm.exception))
        blob = str(cm.exception) + tb + buf_out.getvalue() + buf_err.getvalue()
        self.assertNotIn(FAKE, blob)
        self.assertIn("[REDACTED]", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
