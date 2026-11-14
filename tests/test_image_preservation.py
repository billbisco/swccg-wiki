import hashlib,io,tempfile,unittest
from pathlib import Path
import sys
repo_tools=Path(__file__).resolve().parents[1]/'tools'
if repo_tools.is_dir():sys.path.insert(0,str(repo_tools))
from unittest.mock import patch
from image_preservation.network import image_signature,check_hashes,raw_capture,stream_hash
from image_preservation.store import connect,add_version
from image_preservation.runner import recover_interrupted
from email.message import Message
from types import SimpleNamespace

class Response(io.BytesIO):
    def __init__(self,body,mime):
        super().__init__(body);self.headers=Message();self.headers['Content-Type']=mime

class PreservationTests(unittest.TestCase):
    def setUp(self):
        # Unit tests exercise SQLite behavior independently of the host's temp filesystem.
        disk=patch('image_preservation.store.shutil.disk_usage',return_value=SimpleNamespace(free=100*1024**3))
        disk.start();self.addCleanup(disk.stop)
    def test_low_disk_stops_before_ledger_is_opened(self):
        with tempfile.TemporaryDirectory() as d:
            with patch('image_preservation.store.shutil.disk_usage',return_value=SimpleNamespace(free=1024)):
                with self.assertRaisesRegex(RuntimeError,'20 GiB'):connect(d)
            self.assertFalse((Path(d)/'inventory.sqlite').exists())
    def test_html_success_is_not_an_image(self):
        self.assertFalse(image_signature(b'<html>200 OK</html>','image/jpeg'))
    def test_svg_cannot_be_a_login_page(self):
        self.assertFalse(image_signature(b'<html><svg>icon</svg>login</html>','image/svg+xml'))
    def test_thumbnail_url_cannot_substitute_for_original(self):
        with self.assertRaises(ValueError):raw_capture('https://web.archive.org/web/20261114000316/https://wiki.swccg.com/images/thumb/a.jpg','https://wiki.swccg.com/images/a.jpg')
    def test_modified_binary_rejected(self):
        with self.assertRaises(ValueError):check_hashes({'sha1':'a'*40,'bytes':5},{'sha1':'a'*40,'sha256':'x','bytes':5},{'sha256':'y','bytes':5})
    def test_html_200_response_rejected_by_stream(self):
        with patch('image_preservation.network.open_url',return_value=Response(b'<html>OK</html>','text/html')):
            with self.assertRaises(ValueError):stream_hash('https://example.invalid/image','image/jpeg',15)
    def test_declared_image_with_html_payload_rejected(self):
        body=b'<html>login</html>'
        with patch('image_preservation.network.open_url',return_value=Response(body,'image/jpeg')):
            with self.assertRaises(ValueError):stream_hash('https://example.invalid/image','image/jpeg',len(body))
    def test_thumbnail_byte_size_rejected(self):
        with patch('image_preservation.network.open_url',return_value=Response(b'GIF89a' , 'image/gif')):
            with self.assertRaises(ValueError):stream_hash('https://example.invalid/image','image/gif',500)
    def test_oversized_response_stops_before_retaining_extra_bytes(self):
        with patch('image_preservation.network.open_url',return_value=Response(b'GIF89a'+b'x'*100,'image/gif')):
            with self.assertRaises(ValueError):stream_hash('https://example.invalid/image','image/gif',6)
    def test_matching_source_archive_and_inventory_pass(self):
        check_hashes({'sha1':'a'*40,'bytes':5},{'sha1':'a'*40,'sha256':'x','bytes':5},{'sha256':'x','bytes':5})
    def test_stale_version_rejected(self):
        with self.assertRaises(ValueError):check_hashes({'sha1':'a'*40,'bytes':5},{'sha1':'b'*40,'sha256':'x','bytes':5},{'sha256':'x','bytes':5})
    def test_queued_capture_does_not_become_verified_on_resume(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(d);x={'timestamp':'2026-11-13T00:00:00Z','sha1':'a'*40,'url':'https://wiki.swccg.com/images/a.jpg','size':5,'mime':'image/jpeg'}
            add_version(db,'File:a.jpg',x,True)
            db.execute("UPDATE versions SET status='checking',capture='https://example.invalid/capture'");db.commit()
            recover_interrupted(db)
            row=db.execute('SELECT * FROM versions').fetchone()
            self.assertEqual('retry',row['status']);self.assertIsNone(row['verified_at'])
            add_version(db,'File:a.jpg',x,True)
            self.assertEqual(1,db.execute('SELECT count(*) FROM versions').fetchone()[0]);db.close()
    def test_verified_row_not_rescheduled_on_restart(self):
        with tempfile.TemporaryDirectory() as d:
            db=connect(d);x={'timestamp':'2026-11-13T00:00:00Z','sha1':'a'*40,'url':'https://wiki.swccg.com/images/a.jpg','size':5,'mime':'image/jpeg'}
            add_version(db,'File:a.jpg',x,True);db.execute("UPDATE versions SET status='verified'");db.commit()
            recover_interrupted(db)
            self.assertEqual('verified',db.execute('SELECT status FROM versions').fetchone()[0]);db.close()

if __name__=='__main__':unittest.main()
