import io,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
from image_preservation.ssh_source import request_item,receive
class SourceStreamTests(unittest.TestCase):
    def info(self,url='https://wiki.swccg.com/images/a/ab/Scan.png'):
        return {'id':'a'*64,'bytes':3,'url':url}
    def test_public_current_and_history(self):
        for url in ['https://wiki.swccg.com/images/a/ab/Scan.png','https://wiki.swccg.com/images/archive/0/01/20261114000000%21Scan.svg']:
            self.assertIn('relative_path',request_item(self.info(url)))
    def test_rejects_provider_private_thumbnail_and_path_escape(self):
        for url in ['https://archive.org/images/a/ab/Scan.png','https://web.archive.org/images/a/ab/Scan.png','https://wiki.swccg.com/images/deleted/a/ab/Scan.png','https://wiki.swccg.com/images/thumb/a/ab/Scan.png','https://wiki.swccg.com/images/a/ab/%2e%2e%2fsecret','https://wiki.swccg.com/images/a/ab/a%5cb']:
            with self.subTest(url=url),self.assertRaises(ValueError):request_item(self.info(url))
    def test_rejects_invalid_version_id_or_size(self):
        for key,value in [('id','x'*64),('bytes',-1)]:
            x=self.info();x[key]=value
            with self.assertRaises(ValueError):request_item(x)
    def test_stream_exact_bytes_and_no_overread(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'part';p=SimpleNamespace(stdout=io.BytesIO(b'{"id":"'+b'a'*64+b'","bytes":3}\nabcNEXT'))
            self.assertIsNone(receive(p,self.info(),path));self.assertEqual(path.read_bytes(),b'abc');self.assertEqual(p.stdout.read(),b'NEXT')
    def test_rejects_truncation_wrong_id_size_and_header(self):
        for blob in [b'',b'x'*4097,b'{"id":"wrong","bytes":3}\nabc',b'{"id":"'+b'a'*64+b'","bytes":4}\nabc',b'{"id":"'+b'a'*64+b'","bytes":3}\nab']:
            with tempfile.TemporaryDirectory() as d,self.assertRaises((RuntimeError,ValueError)):
                receive(SimpleNamespace(stdout=io.BytesIO(blob)),self.info(),Path(d)/'part')
    def test_source_error_does_not_create_payload(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'part';p=SimpleNamespace(stdout=io.BytesIO(b'{"id":"'+b'a'*64+b'","bytes":0,"error":"missing"}\n'))
            self.assertEqual(receive(p,self.info(),path),'missing');self.assertFalse(path.exists())
if __name__=='__main__':unittest.main()
