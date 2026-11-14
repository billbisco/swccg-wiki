import json,sys,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
tools=Path(__file__).resolve().parents[1]/'tools'
sys.path.insert(0,str(tools if tools.is_dir() else Path(__file__).resolve().parent))
from image_preservation.store import connect,add_version,version_id,upload_id

class UploadAliasTests(unittest.TestCase):
    def setUp(self):
        disk=patch('image_preservation.store.shutil.disk_usage',return_value=SimpleNamespace(free=100*1024**3));disk.start();self.addCleanup(disk.stop)
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.db=connect(self.temp.name);self.addCleanup(self.db.close)
        self.title='File:Original.gif'
        self.original={'url':'https://wiki.swccg.com/images/a/Original.gif','timestamp':'2026-09-25T03:41:04Z','sha1':'a'*40,'size':77010,'mime':'image/gif'}
        self.alias={**self.original,'url':'https://wiki.swccg.com/images/archive/a/20260925034104%21Original.gif'}
        self.db.execute('INSERT INTO files(title,current_url,sha1,timestamp,bytes) VALUES(?,?,?,?,?)',(self.title,self.original['url'],self.original['sha1'],self.original['timestamp'],self.original['size']))
    def test_same_upload_urls_share_identity_but_keep_alias_ids(self):
        self.assertEqual(upload_id(self.title,self.original),upload_id(self.title,self.alias))
        self.assertNotEqual(version_id(self.title,self.original),version_id(self.title,self.alias))
    def test_history_alias_cannot_become_second_current(self):
        add_version(self.db,self.title,self.original,True);add_version(self.db,self.title,self.alias,True)
        rows=self.db.execute('SELECT url,current FROM versions ORDER BY url').fetchall()
        self.assertEqual(2,len(rows));self.assertEqual(1,sum(x['current'] for x in rows))
        self.assertEqual(self.original['url'],next(x['url'] for x in rows if x['current']))
        self.assertEqual(1,self.db.execute('SELECT count(*) FROM upload_versions').fetchone()[0])
    def test_import_order_does_not_change_current_mapping(self):
        add_version(self.db,self.title,self.alias,True);add_version(self.db,self.title,self.original,True)
        row=self.db.execute('SELECT current_version_id FROM upload_versions').fetchone()
        self.assertEqual(version_id(self.title,self.original),row[0])
    def test_same_bytes_uploaded_later_are_separate_uploads(self):
        later={**self.original,'timestamp':'2026-10-01T00:00:00Z'}
        self.assertNotEqual(upload_id(self.title,self.original),upload_id(self.title,later))
    def test_reimport_preserves_verified_receipt(self):
        add_version(self.db,self.title,self.alias,False)
        self.db.execute("UPDATE versions SET status='verified',capture='retained-receipt',archive_sha256='payload-hash'")
        add_version(self.db,self.title,self.alias,True)
        row=self.db.execute('SELECT status,capture,archive_sha256,current FROM versions').fetchone()
        self.assertEqual(('verified','retained-receipt','payload-hash',0),tuple(row))
    def test_new_current_demotes_previous_upload_without_deleting_it(self):
        add_version(self.db,self.title,self.original,True)
        later={**self.original,'timestamp':'2026-10-01T00:00:00Z','sha1':'b'*40}
        self.db.execute('UPDATE files SET timestamp=?,sha1=? WHERE title=?',(later['timestamp'],later['sha1'],self.title))
        add_version(self.db,self.title,later,True)
        self.assertEqual(2,self.db.execute('SELECT count(*) FROM versions').fetchone()[0])
        self.assertEqual(1,self.db.execute('SELECT sum(current) FROM versions').fetchone()[0])
        self.assertEqual(2,self.db.execute('SELECT count(*) FROM upload_versions').fetchone()[0])

if __name__=='__main__':unittest.main()
