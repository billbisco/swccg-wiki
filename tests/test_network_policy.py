import io,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import Mock,patch
import sys
repo_tools=Path(__file__).resolve().parents[1]/'tools'
sys.path.insert(0,str(repo_tools if repo_tools.is_dir() else Path(__file__).resolve().parent))
from image_preservation import network,runner,follow_queue,restore
from image_preservation import __main__ as cli
class PCNetworkPolicyTests(unittest.TestCase):
 def test_provider_requests_fail_before_transport(self):
  for url in ['https://archive.org/wayback/available?url=x','https://web.archive.org/save/https://wiki.swccg.com/images/a.jpg','https://web.archive.org/cdx/search/cdx','https://web.archive.org/web/20261114000000id_/https://wiki.swccg.com/images/a.jpg']:
   with self.subTest(url=url),patch('image_preservation.network.urllib.request.build_opener') as transport,self.assertRaises(ValueError):network.open_url(url)
   transport.assert_not_called()
 def test_other_hosts_and_private_api_routes_rejected(self):
  for url in ['https://example.org/image','http://wiki.swccg.com/api.php','https://wiki.swccg.com.evil/api.php','https://user@wiki.swccg.com/api.php','https://wiki.swccg.com/wiki/Special:UserLogin']:
   with self.subTest(url=url),self.assertRaises(ValueError):network.client_url(url)
 def test_public_wiki_api_remains_usable(self):
  with patch('image_preservation.network.urllib.request.build_opener') as factory:
   factory.return_value.open.return_value=io.BytesIO(b'{"query":{"ok":true}}')
   self.assertEqual(network.api(action='query'),{'query':{'ok':True}})
   req=factory.return_value.open.call_args.args[0];self.assertTrue(req.full_url.startswith('https://wiki.swccg.com/api.php?'))
 def test_redirect_to_provider_fails_before_follow(self):
  request=network.urllib.request.Request('https://wiki.swccg.com/api.php')
  with self.assertRaises(ValueError):network.WikiClientRedirect().redirect_request(request,None,302,'redirect',{},'https://archive.org/')
 def test_retired_capture_helpers_cannot_mutate_or_request(self):
  db=Mock()
  calls=[lambda:runner.existing_capture('x'),lambda:runner.save_original('x'),lambda:runner.verify_one({},'x'),lambda:runner.batch(db,'unused')]
  with patch('image_preservation.network.open_url') as transport:
   for call in calls:
    with self.assertRaisesRegex(RuntimeError,'central server owner'):call()
   transport.assert_not_called();db.execute.assert_not_called()
 def test_retired_queue_verifier_cannot_start_ssh(self):
  with patch('subprocess.check_output') as ssh,self.assertRaises(RuntimeError):follow_queue.once(Mock())
  ssh.assert_not_called()
 def test_retired_restore_creates_no_directory(self):
  with patch('pathlib.Path.mkdir') as mkdir,self.assertRaises(RuntimeError):restore.sample(Mock(),'unused')
  mkdir.assert_not_called()
 def test_legacy_cli_fails_before_opening_ledger(self):
  for command in ['batch','run','restore']:
   with self.subTest(command=command),patch.object(sys,'argv',['image_preservation',command]),patch('sys.stderr',new=io.StringIO()),patch.object(cli,'connect') as connect,self.assertRaises(SystemExit) as error:cli.main()
   self.assertEqual(error.exception.code,2);connect.assert_not_called()
 def test_report_cli_still_closes_ledger(self):
  db=Mock()
  with patch.object(sys,'argv',['image_preservation','report']),patch.object(cli,'connect',return_value=db),patch.object(cli,'report',return_value={'ok':True}),patch('sys.stdout',new=io.StringIO()) as output:
   cli.main();self.assertIn('true',output.getvalue())
  db.close.assert_called_once()
if __name__=='__main__':unittest.main()
