import hashlib,io,json,sqlite3,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from image_preservation.store import connect,add_version,version_id
from image_preservation.ssh_backup import run
class FakeSource:
    def __init__(self,blob):self.stdout=io.BytesIO(blob)
    def wait(self,timeout=None):return 0
    def kill(self):pass
class SourceBackupTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.data=Path(self.temp.name);self.db=connect(self.data);self.items=[]
    def tearDown(self):self.db.close();self.temp.cleanup()
    def add(self,name,body):
        info={'timestamp':'2026-11-14T00:00:00Z','sha1':hashlib.sha1(body).hexdigest(),'size':len(body),'mime':'image/png','url':'https://wiki.swccg.com/images/a/ab/'+name}
        title='File:'+name;add_version(self.db,title,info,True);self.db.commit();identity=version_id(title,info)
        self.items.append((identity,body));return identity
    def stream(self,items=None):
        return FakeSource(b''.join((json.dumps({'id':key,'bytes':len(body)})+'\n').encode()+body for key,body in (items or self.items)))
    def test_checked_objects_and_all_version_mappings(self):
        self.add('A.png',b'abc');self.add('B.png',b'abc')
        with patch('image_preservation.ssh_backup.start',return_value=self.stream()):run(self.data)
        self.assertEqual(self.db.execute("SELECT count(*) FROM local_backups WHERE status='backed_up'").fetchone()[0],2)
        self.assertEqual(self.db.execute('SELECT count(*) FROM backup_objects').fetchone()[0],1)
        self.assertEqual(self.db.execute("SELECT count(*) FROM local_copy_sources WHERE kind='wiki_ssh'").fetchone()[0],2)
    def test_corrupt_payload_stays_unfinished(self):
        key=self.add('A.png',b'abc')
        with patch('image_preservation.ssh_backup.start',return_value=self.stream([(key,b'BAD')])):run(self.data)
        self.assertEqual(self.db.execute('SELECT status FROM local_backups').fetchone()[0],'needs_reconciliation')
        self.assertEqual(self.db.execute('SELECT count(*) FROM backup_objects').fetchone()[0],0)
    def test_truncated_stream_preserves_commit_and_resumes_missing_only(self):
        first=self.add('A.png',b'abc');second=self.add('B.png',b'def')
        blob=(json.dumps({'id':first,'bytes':3})+'\n').encode()+b'abc'+(json.dumps({'id':second,'bytes':3})+'\n').encode()+b'd'
        with patch('image_preservation.ssh_backup.start',return_value=FakeSource(blob)),self.assertRaises(RuntimeError):run(self.data)
        self.assertEqual(self.db.execute('SELECT version_id FROM local_backups').fetchone()[0],first)
        with patch('image_preservation.ssh_backup.start',return_value=self.stream([(second,b'def')])) as start:run(self.data)
        self.assertEqual([r['id'] for r in start.call_args.args[0]],[second])
        self.assertEqual(self.db.execute('SELECT count(*) FROM local_backups').fetchone()[0],2)
    def test_cap_stops_before_source_stream(self):
        self.add('A.png',b'abc')
        with patch('image_preservation.ssh_backup.CAP',2),patch('image_preservation.ssh_backup.start') as start,self.assertRaises(RuntimeError):run(self.data)
        start.assert_not_called()
if __name__=='__main__':unittest.main()
