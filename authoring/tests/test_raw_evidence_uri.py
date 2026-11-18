"""Offline regression coverage for exact immutable evidence identities, not proof data."""
import hashlib,socket,tempfile,types,unittest
from pathlib import Path
from unittest.mock import patch
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import publication_gate as gate
ROOT=Path(__file__).resolve().parent
REPOS={'https://github.com/billbisco/swccg-wiki-files','https://github.com/swccg-guild/work'}
SHA='a'*40;RAW='https://raw.githubusercontent.com/billbisco/swccg-wiki-files/'+SHA+'/preservation/versions/fixture.json';BLOB='https://github.com/billbisco/swccg-wiki-files/blob/'+SHA+'/preservation/versions/fixture.json'
class ImmutableEvidenceTests(unittest.TestCase):
 def test_real_retained_raw_identities_accept_without_rewriting(self):
  urls=['https://raw.githubusercontent.com/billbisco/swccg-wiki-files/33ca16eba8c0049d7565da64eecc747a97c76f7f/preservation/versions/034cfad64e52541de9797df02e7734f5cec4fce45b4bdb57163f24c754d71a2f.json', 'https://raw.githubusercontent.com/billbisco/swccg-wiki-files/96ec6762b7249038d4edd3a295750b763cdfafe7/preservation/versions/54af6997d1431280ac2d362cae65e9c5bbf16b64b4d8a56beed661110fd7c025.json']
  for url in urls:
   with self.subTest(uri=url):self.assertTrue(gate._immutable_evidence_uri(url,REPOS))
 def test_both_canonical_official_forms_accept_full_commit(self):
  for uri in [RAW,BLOB,'https://raw.githubusercontent.com/swccg-guild/work/'+SHA+'/evidence/fixture.json','https://github.com/swccg-guild/work/blob/'+SHA+'/evidence/fixture.json']:
   with self.subTest(uri=uri):self.assertTrue(gate._immutable_evidence_uri(uri,REPOS))
 def test_mutable_references_rejected_in_both_forms(self):
  for revision in ['main','HEAD','v1','a'*7,'a'*39,'a'*41,'A'*40,'g'*40]:
   for uri in [RAW.replace(SHA,revision),BLOB.replace(SHA,revision)]:
    with self.subTest(uri=uri):self.assertFalse(gate._immutable_evidence_uri(uri,REPOS))
 def test_unapproved_repository_or_host_rejected(self):
  for uri in [RAW.replace('billbisco/swccg-wiki-files','outsider/repository'),RAW.replace('raw.githubusercontent.com','raw.githubusercontent.com.evil.example'),RAW.replace('raw.githubusercontent.com','user@raw.githubusercontent.com'),RAW.replace('raw.githubusercontent.com','raw.githubusercontent.com:443'),RAW.replace('https:','http:'),BLOB.replace('github.com','github.com.evil.example')]:
   with self.subTest(uri=uri):self.assertFalse(gate._immutable_evidence_uri(uri,REPOS))
 def test_unsafe_or_ambiguous_paths_rejected(self):
  for suffix in ['','/','../fixture.json','./fixture.json','x//fixture.json','%2e%2e/fixture.json','fixture.json?download=1','fixture.json#L1','x%2fy.json','x:y.json','x\\y.json','x y.json','x\ny.json','x\u00a0y.json']:
   for uri in ['https://raw.githubusercontent.com/billbisco/swccg-wiki-files/'+SHA+'/'+suffix,'https://github.com/billbisco/swccg-wiki-files/blob/'+SHA+'/'+suffix]:
    with self.subTest(uri=uri):self.assertFalse(gate._immutable_evidence_uri(uri,REPOS))
 def test_exact_raw_identity_round_trips_offline_without_normalization(self):
  # Deliberately synthetic bytes/fixture URI; never entered as publication evidence.
  with tempfile.TemporaryDirectory()as directory:
   root=Path(directory);payload=b'{"synthetic_regression_fixture":true}\n';(root/'fixture.json').write_bytes(payload);digest=hashlib.sha256(payload).hexdigest();errors=[];contracts=types.SimpleNamespace(BACKUP_REPOSITORIES=REPOS);entries=[dict(uri=RAW,sha256=digest,path='fixture.json')]
   with patch.object(socket,'socket',side_effect=AssertionError('External network blocked')):
    files=gate._evidence_files(root,entries,contracts,errors);self.assertEqual(errors,[]);self.assertEqual(gate._read_file(root,dict(path=RAW,sha256=digest),errors,'fixture',files),payload);self.assertEqual(errors,[])
    self.assertIsNone(gate._read_file(root,dict(path=BLOB,sha256=digest),errors,'different identity',files));self.assertTrue(errors)
 def test_wrong_payload_hash_fails_closed(self):
  with tempfile.TemporaryDirectory()as directory:
   root=Path(directory);(root/'fixture.json').write_bytes(b'fixture');errors=[];files=gate._evidence_files(root,[dict(uri=RAW,sha256='0'*64,path='fixture.json')],types.SimpleNamespace(BACKUP_REPOSITORIES=REPOS),errors);self.assertEqual(files,{});self.assertTrue(any('SHA-256 mismatch'in e for e in errors))
 def test_unsafe_local_locator_fails_closed(self):
  errors=[];files=gate._evidence_files(ROOT,[dict(uri=RAW,sha256='0'*64,path='../fixture.json')],types.SimpleNamespace(BACKUP_REPOSITORIES=REPOS),errors);self.assertEqual(files,{});self.assertTrue(errors)
if __name__=='__main__':unittest.main(verbosity=2)
