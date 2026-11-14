import hashlib,io,sys,tempfile,unittest,urllib.request
from unittest.mock import Mock,patch
from email.message import Message
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
repo_tools=Path(__file__).resolve().parents[1]/'tools'
if repo_tools.is_dir():sys.path.insert(0,str(repo_tools))
from image_preservation.offline_backup import wiki_image_url,WikiOnlyRedirect,source_identity,hashes,backup_one,CAP

class OfflineBackupTests(unittest.TestCase):
    def test_archive_org_rejected_without_network(self):
        for url in ('https://archive.org/anything','https://web.archive.org/web/123/a','http://wiki.swccg.com/images/a'):
            with self.assertRaises(ValueError):wiki_image_url(url)
    def test_redirect_to_archive_org_rejected_before_follow(self):
        req=urllib.request.Request('https://wiki.swccg.com/images/a')
        with self.assertRaises(ValueError):WikiOnlyRedirect().redirect_request(req,None,302,'redirect',Message(),'https://web.archive.org/web/123/a')
    def test_non_image_wiki_path_rejected(self):
        with self.assertRaises(ValueError):wiki_image_url('https://wiki.swccg.com/wiki/File:a')
    def test_current_and_retained_original_paths_allowed(self):
        for path in ('a/b.jpg','archive/a/123%21b.jpg'):
            self.assertEqual('https://wiki.swccg.com/images/'+path,wiki_image_url('https://wiki.swccg.com/images/'+path))
    def test_metadata_mismatch_rejected(self):
        with self.assertRaises(ValueError):source_identity({'sha1':'a'*40,'bytes':10},{'sha1':'b'*40,'bytes':10})
    def test_independent_disk_read_detects_change(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'original';p.write_bytes(b'original');before=hashes(p)
            p.write_bytes(b'changed');self.assertNotEqual(before,hashes(p))
    def test_cache_cap_blocks_before_any_request(self):
        with tempfile.TemporaryDirectory() as d,patch('image_preservation.offline_backup.ensure_space'):
            db=Mock();db.execute.return_value.fetchone.return_value=None;opener=Mock()
            info={'id':'a'*64,'sha1':'b'*40,'bytes':1,'url':'https://wiki.swccg.com/images/a.jpg'}
            with self.assertRaisesRegex(RuntimeError,'25 GiB'):backup_one(db,info,Path(d),opener,{'used':CAP})
            opener.open.assert_not_called()
    def test_corrupt_reused_object_is_not_marked_backed_up(self):
        with tempfile.TemporaryDirectory() as d,patch('image_preservation.offline_backup.ensure_space'):
            root=Path(d);(root/'object').write_bytes(b'bad')
            db=Mock();db.execute.return_value.fetchone.return_value={'path':'object','sha256':hashlib.sha256(b'good').hexdigest()}
            opener=Mock();info={'sha1':hashlib.sha1(b'good').hexdigest(),'bytes':4}
            with self.assertRaises(ValueError):backup_one(db,info,root,opener,{'used':3})
            opener.open.assert_not_called()

if __name__=='__main__':unittest.main()
