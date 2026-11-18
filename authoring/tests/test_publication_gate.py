"""Publication scope must not convert missing evidence into preservation success."""
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from publication_gate import publication_report, referenced_originals
import preservation_contracts as contracts
import style_lint


def sha(data):
    return hashlib.sha256(data).hexdigest()


def receipt(subject):
    return {'schema_version': 1, 'subject': copy.deepcopy(subject),
            'storage': {'kind': 'git', 'repository': 'https://github.com/billbisco/swccg-wiki',
                        'commit': 'a' * 40, 'path': 'evidence/exact.txt'},
            'verification': {'status': 'verified', 'independent': True,
                             'restored_sha256': subject['content_sha256'],
                             'restored_bytes': subject['bytes'], 'verified_at': '2026-11-14T12:00:00Z'}}


class PublicationGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.text = 'A sourced fact.<ref>[https://example.org/source Source]</ref>\n<references />'
        evidence = b'Checked complete primary source and exact cited claim.'
        (self.root / 'proof.txt').write_bytes(evidence)
        self.proof = {'path': 'proof.txt', 'sha256': sha(evidence)}
        subject = {'kind': 'source_snapshot', 'title': 'Source', 'content_sha256': sha(b'source'), 'bytes': 6}
        source = {'url': 'https://example.org/source', 'sha256': subject['content_sha256'],
                  'bytes': 6, 'checked_evidence': self.proof}
        oid = contracts.registration_object_id(subject, source)
        request = 'b' * 64
        self.row = {'subject': subject, 'subject_id': contracts.object_id(subject),
                    'object_id': oid, 'job_id': contracts.registration_job_id(source),
                    'request_id': request, 'record': f"requests/{subject['content_sha256']}/{oid}/{request}.json",
                    'record_sha256': 'd' * 64, 'generation': 0,
                    'source': source,
                    'backup_receipt': receipt(subject), 'state': 'awaiting_stage',
                    'owner': 'MemoryCoreChatGPT', 'reason': 'Provider outage',
                    'continuation': 'Central owner resumes after healthy canary', 'approval_scope': {'story': 409}}
        page_subject = {'kind': 'wiki_draft', 'title': 'Example', 'content_sha256': sha(self.text.encode()),
                        'bytes': len(self.text.encode())}
        self.page = {'title': 'Example', 'subject': page_subject, 'backup_receipt': receipt(page_subject),
                     'source_accuracy': {'status': 'checked', 'evidence': self.proof},
                     'sources': [{'url': 'https://example.org/source', 'object_id': oid, 'evidence': self.proof}],
                     'original_versions': [], 'rendered_originals': []}
        self.manifest = {'schema_version': 1, 'approval_scope': {'story': 409}, 'pages': [self.page]}

    def run_gate(self, flags=None, sources=None, revision_id=None):
        export = json.dumps({'schema_version': 1, 'submission_owner': 'server-wayback-owner',
                             'objects': getattr(self, 'rows', [self.row])}).encode()
        (self.root / 'registry.json').write_bytes(export)
        self.manifest['registry_export'] = {'path': 'registry.json', 'sha256': sha(export),
            'storage': {'kind': 'git', 'repository': 'https://github.com/swccg-guild/work',
                        'commit': 'c' * 40, 'path': 'evidence/registry.json'}}
        data = json.dumps(self.manifest).encode()
        path = self.root / 'manifest.json'
        path.write_bytes(data)
        return publication_report(self.text, 'Example', flags or ['ARCHIVE  missing capture'],
                                  sources or {'https://example.org/source'}, path, sha(data), revision_id)

    def test_private_work_backups_pass_without_claiming_capture_completion(self):
        for holder in (self.row, self.page):
            holder['backup_receipt']['storage']['repository'] = 'https://github.com/swccg-guild/work'
        result = self.run_gate()
        self.assertEqual([], result['errors'])
        self.assertTrue(result['publication_eligible'])
        self.assertFalse(result['preservation_complete'])
        self.assertEqual(['ARCHIVE  missing capture'], result['raw_flags'])

    def test_pending_is_eligible_but_never_complete_or_zero_flags(self):
        result = self.run_gate()
        self.assertEqual([], result['errors'])
        self.assertTrue(result['publication_eligible'])
        self.assertFalse(result['preservation_complete'])
        self.assertEqual(['ARCHIVE  missing capture'], result['raw_flags'])
        self.assertEqual('awaiting_stage', result['preservation_pending'][0]['state'])

    def mapped_proof(self):
        uri = 'https://github.com/swccg-guild/work/blob/' + 'a' * 40 + '/evidence/proof.txt'
        original = copy.deepcopy(self.proof)
        self.proof['path'] = uri
        self.manifest['evidence_files'] = [{'uri': uri, 'sha256': original['sha256'], 'path': original['path']}]
        return uri

    def test_immutable_uri_uses_checked_offline_file_without_registry_rewrite(self):
        self.mapped_proof()
        before = copy.deepcopy(self.row)
        with patch('urllib.request.urlopen', side_effect=AssertionError('offline only')):
            self.assertTrue(self.run_gate()['publication_eligible'])
        self.assertEqual(before, self.row)

    def test_uri_locator_requires_exact_identity_and_hash(self):
        uri = self.mapped_proof()
        entry = self.manifest['evidence_files'][0]
        for field, value in [('uri', uri + 'other'), ('sha256', '0' * 64), ('path', 'missing.txt')]:
            with self.subTest(field=field):
                before = entry[field]; entry[field] = value
                self.assertFalse(self.run_gate()['publication_eligible'])
                entry[field] = before
        self.manifest.pop('evidence_files')
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_uri_rejects_mutable_untrusted_and_ambiguous_locators(self):
        uri = self.mapped_proof()
        entry = self.manifest['evidence_files'][0]
        bad = [uri.replace('a' * 40, 'main'), uri.replace('github.com', 'evil.example'),
               uri.replace('swccg-guild/work', 'stranger/work'), uri.replace('github.com', 'user@github.com'),
               uri + '?', uri + '#fragment', uri.replace('/evidence/', '/../'),
               uri.replace('/evidence/', '/%2e%2e/'), uri.replace('/evidence/', '//'),
               uri.replace('/evidence/', '/./'), uri.replace('github.com', '[invalid'),
               uri.replace('https:', 'http:'), uri + ' ']
        for value in bad:
            with self.subTest(uri=value):
                entry['uri'] = value
                self.assertFalse(self.run_gate()['publication_eligible'])
        entry['uri'] = uri
        self.manifest['evidence_files'].append(copy.deepcopy(entry))
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_uri_rejects_bundle_escape_and_changed_bytes(self):
        self.mapped_proof()
        entry = self.manifest['evidence_files'][0]
        for path in ('../proof.txt', str(self.root / 'proof.txt'), 'C:proof.txt'):
            with self.subTest(path=path):
                entry['path'] = path
                self.assertFalse(self.run_gate()['publication_eligible'])
        entry['path'] = 'proof.txt'
        (self.root / 'proof.txt').write_bytes(b'tampered')
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_registered_uri_cannot_be_replaced_by_relative_alias(self):
        self.mapped_proof()
        self.page['sources'][0]['evidence'] = {'path': 'proof.txt', 'sha256': self.proof['sha256']}
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_uri_map_rejects_conflicting_payload_and_malformed_list(self):
        uri = self.mapped_proof()
        self.manifest['evidence_files'].append({'uri': uri + '2', 'sha256': '0' * 64, 'path': 'proof.txt'})
        self.assertFalse(self.run_gate()['publication_eligible'])
        self.manifest['evidence_files'] = {}
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_snapshot_equivalence_uses_exact_mapped_proof(self):
        self.mapped_proof()
        self.use_checked_snapshot()
        self.assertTrue(self.run_gate()['publication_eligible'])
        self.row['source']['provenance_equivalence']['evidence_path'] += 'other'
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_malformed_uri_reference_hash_fails_closed(self):
        self.mapped_proof()
        self.page['source_accuracy']['evidence'] = {'path': self.proof['path'], 'sha256': []}
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_non_archive_findings_block(self):
        self.assertFalse(self.run_gate(['EMAIL personal address'])['publication_eligible'])

    def test_new_unregistered_citation_blocks(self):
        self.assertFalse(self.run_gate(sources={'https://example.org/new'})['publication_eligible'])

    def test_invalid_page_or_object_backups_block(self):
        for location in ('page', 'object'):
            with self.subTest(location=location):
                holder = self.page if location == 'page' else self.row
                original = holder['backup_receipt']
                holder['backup_receipt'] = {'status': 'queued'}
                self.assertFalse(self.run_gate()['publication_eligible'])
                holder['backup_receipt'] = original

    def test_fake_verified_or_unowned_job_blocks(self):
        for key, value in [('state', 'verified'), ('owner', ''), ('continuation', ''), ('request_id', 'fake')]:
            with self.subTest(key=key):
                before = self.row[key]
                self.row[key] = value
                self.assertFalse(self.run_gate()['publication_eligible'])
                self.row[key] = before

    def test_changed_content_and_live_revision_mismatch_block(self):
        self.text += ' changed'
        self.assertFalse(self.run_gate()['publication_eligible'])
        self.text = self.text[:-8]
        self.assertFalse(self.run_gate(revision_id=123)['publication_eligible'])

    def test_exact_manifest_approval_is_required(self):
        self.run_gate()
        result = publication_report(self.text, 'Example', [], set(), self.root / 'manifest.json', '0' * 64)
        self.assertFalse(result['publication_eligible'])

    def test_missing_original_or_evidence_blocks(self):
        self.page['rendered_originals'] = ['File:Actual card.png']
        self.assertFalse(self.run_gate()['publication_eligible'])
        self.page['rendered_originals'] = []
        (self.root / 'proof.txt').write_text('tampered')
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_bad_manifest_fields_fail_closed(self):
        for key, value in [('source_accuracy', None), ('sources', None), ('original_versions', None),
                           ('rendered_originals', [None])]:
            with self.subTest(key=key):
                before = self.page[key]
                self.page[key] = value
                self.assertFalse(self.run_gate()['publication_eligible'])
                self.page[key] = before

    def test_literal_original_inventory(self):
        self.assertEqual({'File:A.png', 'File:B.png', 'File:C.png'}, referenced_originals(
            '[[File:A.png|thumb]]\n|image=B.png\n<gallery>\nFile:C.png|caption\n</gallery>'))

    def test_exact_original_version_can_pass_but_other_version_cannot(self):
        subject = {'kind': 'wiki_file_version', 'title': 'File:Actual card.png',
                   'content_sha256': sha(b'png'), 'bytes': 3,
                   'upload_timestamp': '2026-11-14T12:00:00Z',
                   'original_version_url': 'https://wiki.swccg.com/images/exact.png'}
        self.row['subject'] = subject
        self.row['source'].update(url=subject['original_version_url'], sha256=subject['content_sha256'], bytes=3)
        self.row['subject_id'] = contracts.object_id(subject)
        self.row['object_id'] = contracts.registration_object_id(subject, self.row['source'])
        self.row['job_id'] = contracts.registration_job_id(self.row['source'])
        self.row['record'] = f"requests/{subject['content_sha256']}/{self.row['object_id']}/{self.row['request_id']}.json"
        self.row['backup_receipt'] = receipt(subject)
        self.page['sources'][0]['object_id'] = self.row['object_id']
        self.page['sources'][0]['url'] = subject['original_version_url']
        self.page['rendered_originals'] = [subject['title']]
        self.page['original_versions'] = [{'subject': copy.deepcopy(subject),
            'object_id': self.row['object_id'], 'evidence': self.proof}]
        self.assertTrue(self.run_gate(sources={subject['original_version_url']})['publication_eligible'])
        self.page['original_versions'][0]['subject']['upload_timestamp'] = '2026-11-13T12:00:00Z'
        self.assertFalse(self.run_gate(sources={subject['original_version_url']})['publication_eligible'])

    def test_unhashable_json_values_fail_closed(self):
        for holder, key in [(self.page['sources'][0], 'object_id'), (self.row, 'state'),
                            (self.row['subject'], 'kind'), (self.page['subject'], 'kind')]:
            with self.subTest(key=key):
                before = holder[key]
                holder[key] = []
                self.assertFalse(self.run_gate()['publication_eligible'])
                holder[key] = before

    def test_missing_expanded_original_inventory_blocks(self):
        del self.page['rendered_originals']
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_unbacked_queue_status_and_unpinned_record_block(self):
        self.row['state'] = 'queued'
        self.assertFalse(self.run_gate()['publication_eligible'])
        self.row['queue_receipt'] = {'queued': True, 'url': self.row['source']['url'], 'job_id': self.row['job_id']}
        self.assertTrue(self.run_gate()['publication_eligible'])
        del self.row['record_sha256']
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_live_cli_title_cannot_override_actual_target(self):
        self.run_gate()
        manifest = self.root / 'manifest.json'
        args = ['style_lint.py', 'Actual page', '--title', 'Example', '--publication-manifest', str(manifest),
                '--approved-manifest-sha256', sha(manifest.read_bytes())]
        with patch.object(sys, 'argv', args), redirect_stdout(StringIO()), patch('sys.stderr', new=StringIO()):
            with self.assertRaises(SystemExit) as caught:
                style_lint.main()
        self.assertEqual(2, caught.exception.code)

    def test_default_cli_stays_strict(self):
        path = self.root / 'draft.wiki'
        path.write_bytes(self.text.encode('utf8'))
        with patch.object(sys, 'argv', ['style_lint.py', str(path)]), redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit) as caught:
                style_lint.main()
        self.assertEqual(1, caught.exception.code)

    def test_opt_in_cli_keeps_raw_warning(self):
        self.run_gate()
        path = self.root / 'draft.wiki'
        path.write_bytes(self.text.encode('utf8'))
        manifest = self.root / 'manifest.json'
        report = self.root / 'report.json'
        args = ['style_lint.py', str(path), '--title', 'Example', '--publication-manifest', str(manifest),
                '--approved-manifest-sha256', sha(manifest.read_bytes()), '--report-json', str(report)]
        with patch.object(sys, 'argv', args), patch.object(style_lint, 'fetch', return_value=[]), \
                patch.object(style_lint, 'fetch_categories', return_value=set()), redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit) as caught:
                style_lint.main()
        self.assertEqual(0, caught.exception.code)
        result = json.loads(report.read_text())
        self.assertTrue(result['raw_flags'])
        self.assertTrue(result['publication_eligible'])
        self.assertFalse(result['preservation_complete'])

    def test_crlf_draft_hash_is_not_silently_normalized(self):
        self.text = self.text.replace('\n', '\r\n')
        subject = self.page['subject']
        subject.update(content_sha256=sha(self.text.encode()), bytes=len(self.text.encode()))
        self.page['backup_receipt'] = receipt(subject)
        self.run_gate()
        path = self.root / 'draft.wiki'
        path.write_bytes(self.text.encode())
        manifest = self.root / 'manifest.json'
        args = ['style_lint.py', str(path), '--title', 'Example', '--publication-manifest', str(manifest),
                '--approved-manifest-sha256', sha(manifest.read_bytes())]
        with patch.object(sys, 'argv', args), patch.object(style_lint, 'fetch', return_value=[]), \
                patch.object(style_lint, 'fetch_categories', return_value=set()), redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit) as caught:
                style_lint.main()
        self.assertEqual(0, caught.exception.code)

    def test_page_subject_can_have_different_source_with_its_own_backup(self):
        self.row['subject'] = copy.deepcopy(self.page['subject'])
        self.row['subject_id'] = contracts.object_id(self.row['subject'])
        self.row['object_id'] = contracts.registration_object_id(self.row['subject'], self.row['source'])
        self.row['record'] = f"requests/{self.row['source']['sha256']}/{self.row['object_id']}/{self.row['request_id']}.json"
        self.row['backup_receipt'] = receipt(self.row['subject'])
        self.page['sources'][0]['object_id'] = self.row['object_id']
        self.assertFalse(self.run_gate()['publication_eligible'])
        self.row['source_backup_receipt'] = receipt(contracts.source_backup_subject(self.row['source']))
        self.assertTrue(self.run_gate()['publication_eligible'])

    def test_one_subject_retains_two_independent_source_jobs(self):
        other = copy.deepcopy(self.row)
        other['source'].update(url='https://example.org/second', sha256=sha(b'second'))
        other['object_id'] = contracts.registration_object_id(other['subject'], other['source'])
        other['job_id'] = contracts.registration_job_id(other['source'])
        other['record'] = f"requests/{other['source']['sha256']}/{other['object_id']}/{other['request_id']}.json"
        other['source_backup_receipt'] = receipt(contracts.source_backup_subject(other['source']))
        self.rows = [self.row, other]
        self.page['sources'].append({'url': other['source']['url'], 'object_id': other['object_id'], 'evidence': self.proof})
        result = self.run_gate(sources={'https://example.org/source', 'https://example.org/second'})
        self.assertTrue(result['publication_eligible'])
        self.assertEqual(2, len({item['job_id'] for item in result['preservation_pending']}))

    def use_checked_snapshot(self):
        source = self.row['source']
        primary = source['url']
        source.update(url='https://swccg.com/snapshots/pc/exact-source.html', primary_url=primary,
                      representation='checked_self_contained_snapshot')
        source['provenance_equivalence'] = {
            'primary_url': primary, 'snapshot_url': source['url'],
            'primary_html_sha256': sha(b'different primary rendered html'),
            'snapshot_html_sha256': source['sha256'],
            'primary_article_text_sha256': sha(b'exact article text'),
            'snapshot_article_text_sha256': sha(b'exact article text'),
            'evidence_path': self.proof['path'], 'evidence_sha256': self.proof['sha256']}
        self.row['object_id'] = contracts.registration_object_id(self.row['subject'], source)
        self.row['record'] = f"requests/{source['sha256']}/{self.row['object_id']}/{self.row['request_id']}.json"
        self.page['sources'][0]['object_id'] = self.row['object_id']

    def test_checked_primary_alias_preserves_actual_snapshot_payload_identity(self):
        self.use_checked_snapshot()
        result = self.run_gate()
        self.assertTrue(result['publication_eligible'], result['errors'])
        source = self.row['source']
        self.assertNotEqual(source['provenance_equivalence']['primary_html_sha256'], source['sha256'])
        self.assertFalse(result['preservation_complete'])

    def test_unproved_or_unrelated_primary_alias_blocks(self):
        self.use_checked_snapshot()
        proof = self.row['source']['provenance_equivalence']
        proof['snapshot_article_text_sha256'] = sha(b'different article text')
        self.assertFalse(self.run_gate()['publication_eligible'])
        proof['snapshot_article_text_sha256'] = proof['primary_article_text_sha256']
        self.page['sources'][0]['url'] = 'https://example.org/unrelated'
        self.assertFalse(self.run_gate()['publication_eligible'])

    def test_wrong_snapshot_payload_or_missing_equivalence_evidence_blocks(self):
        self.use_checked_snapshot()
        proof = self.row['source']['provenance_equivalence']
        proof['snapshot_html_sha256'] = proof['primary_html_sha256']
        self.assertFalse(self.run_gate()['publication_eligible'])
        proof['snapshot_html_sha256'] = self.row['source']['sha256']
        proof['evidence_path'] = 'missing-proof.json'
        self.assertFalse(self.run_gate()['publication_eligible'])


class PrivateWorkBackupContractTests(unittest.TestCase):
    repository = 'https://github.com/swccg-guild/work'

    def source_subject(self):
        return {'kind': 'source_snapshot', 'title': 'https://example.org/source',
                'content_sha256': sha(b'exact bytes'), 'bytes': len(b'exact bytes')}

    def work_receipt(self, subject):
        value = receipt(subject)
        value['storage']['repository'] = self.repository
        return value

    def test_exact_private_work_receipts_cover_all_subject_kinds(self):
        source = self.source_subject()
        subjects = [source,
                    {**source, 'kind': 'wiki_draft', 'title': 'Example'},
                    {**source, 'kind': 'wiki_revision', 'title': 'Example', 'revision_id': 42},
                    {**source, 'kind': 'wiki_file_version', 'title': 'File:Example.png',
                     'upload_timestamp': '2026-11-18T12:00:00Z',
                     'original_version_url': 'https://wiki.swccg.com/images/a/ab/Example.png'}]
        for subject in subjects:
            with self.subTest(kind=subject['kind']):
                self.assertEqual([], contracts.validate_backup_receipt(self.work_receipt(subject), subject))
        for repository in ('https://github.com/billbisco/swccg-wiki',
                           'https://github.com/billbisco/swccg-wiki-files'):
            with self.subTest(repository=repository):
                value = self.work_receipt(source)
                value['storage']['repository'] = repository
                self.assertEqual([], contracts.validate_backup_receipt(value, source))

    def test_private_work_does_not_relax_exact_identity_or_readback(self):
        subject = self.source_subject()
        cases = [
            ('subject', 'content_sha256', '0' * 64, 'exact object/version/hash'),
            ('storage', 'repository', 'https://github.com/stranger/work', 'independent backup repository'),
            ('storage', 'repository', self.repository + '-other', 'independent backup repository'),
            ('storage', 'repository', self.repository + '?ref=main', 'independent backup repository'),
            ('storage', 'commit', 'main', 'commit must be immutable'),
            ('storage', 'path', '../payload.txt', 'safe repository-relative path'),
            ('verification', 'status', 'queued', 'not verified'),
            ('verification', 'independent', False, 'not an independent backup'),
            ('verification', 'restored_sha256', '0' * 64, 'SHA-256 does not match'),
            ('verification', 'restored_bytes', subject['bytes'] + 1, 'byte count does not match'),
            ('verification', 'restored_bytes', True, 'byte count does not match'),
            ('verification', 'verified_at', '2026-11-18T12:00:00-04:00', 'UTC timestamp'),
        ]
        for section, field, value, expected in cases:
            with self.subTest(section=section, field=field, value=value):
                candidate = self.work_receipt(subject)
                candidate[section][field] = value
                self.assertTrue(any(expected in error for error in
                                    contracts.validate_backup_receipt(candidate, subject)))

    def test_private_work_container_retains_exact_member_and_artifact_checks(self):
        subject = self.source_subject()
        value = self.work_receipt(subject)
        value['storage'].update(container='tar.xz', member='raw/source.json',
                                artifact_sha256='b' * 64, artifact_bytes=128,
                                uncompressed_bytes=subject['bytes'] + 100)
        value['verification'].update(restored_container_sha256='b' * 64,
                                     restored_container_bytes=128)
        self.assertEqual([], contracts.validate_backup_receipt(value, subject))
        cases = [('storage', 'member', '../source.json', 'safe relative path'),
                 ('storage', 'artifact_sha256', '', 'compressed artifact SHA-256'),
                 ('storage', 'artifact_bytes', 0, 'compressed artifact byte count'),
                 ('storage', 'uncompressed_bytes', subject['bytes'] - 1, 'complete member-payload'),
                 ('verification', 'restored_container_sha256', 'c' * 64, 'container readback SHA-256'),
                 ('verification', 'restored_container_bytes', 129, 'container readback byte count')]
        for section, field, changed, expected in cases:
            with self.subTest(section=section, field=field):
                candidate = copy.deepcopy(value)
                candidate[section][field] = changed
                self.assertTrue(any(expected in error for error in
                                    contracts.validate_backup_receipt(candidate, subject)))


if __name__ == '__main__':
    unittest.main()
