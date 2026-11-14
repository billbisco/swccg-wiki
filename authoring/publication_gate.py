"""Opt-in publication eligibility; raw style lint and preservation status stay separate.

This consumes Story410's readback receipts and pinned server-registry export.
It never submits captures, reads credentials, or changes a queue/control file.
"""
from __future__ import annotations

import hashlib
import importlib
import json
import re
import sys
import urllib.parse
from pathlib import Path, PurePosixPath

PENDING_STATES = frozenset({
    'registered', 'awaiting_stage', 'ready', 'queued', 'submitted', 'retry',
    'auth_blocked', 'needs_attention',
})


def _hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _title(value: object) -> str:
    return ' '.join(value.replace('_', ' ').split()) if isinstance(value, str) else ''


def _url(value: str) -> str:
    return urllib.parse.urldefrag(value)[0]


def _safe_relative(value: object) -> bool:
    return (isinstance(value, str) and bool(value) and '\\' not in value
            and not PurePosixPath(value).is_absolute()
            and '..' not in PurePosixPath(value).parts
            and not re.match(r'^[A-Za-z]:', value))


def _read_file(root: Path, ref: object, errors: list[str], label: str) -> bytes | None:
    if not isinstance(ref, dict) or not _safe_relative(ref.get('path')):
        errors.append(label + ': safe bundle-relative evidence path required')
        return None
    path = (root / ref['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        errors.append(label + ': evidence escapes the bundle')
        return None
    try:
        data = path.read_bytes()
    except OSError:
        errors.append(label + ': evidence file unavailable')
        return None
    if _hash(data) != ref.get('sha256'):
        errors.append(label + ': evidence SHA-256 mismatch')
        return None
    return data


def _read_export(root: Path, ref: object, contracts, errors: list[str]) -> dict:
    data = _read_file(root, ref, errors, 'registry export')
    if data is None:
        return {}
    storage = ref.get('storage')
    repositories = contracts.BACKUP_REPOSITORIES | {'https://github.com/swccg-guild/work'}
    if (not isinstance(storage, dict) or storage.get('kind') != 'git'
            or not isinstance(storage.get('repository'), str) or storage['repository'] not in repositories
            or not re.fullmatch(r'[0-9a-f]{40}', str(storage.get('commit', '')))
            or not _safe_relative(storage.get('path'))):
        errors.append('registry export: immutable approved Git locator required')
    try:
        export = json.loads(data)
    except (ValueError, UnicodeError):
        errors.append('registry export: invalid JSON')
        return {}
    if (not isinstance(export, dict) or type(export.get('schema_version')) is not int or export['schema_version'] != 1
            or export.get('submission_owner') != 'server-wayback-owner'
            or not isinstance(export.get('objects'), list)):
        errors.append('registry export: unsupported central registry contract')
        return {}
    objects = {}
    for row in export['objects']:
        if not isinstance(row, dict) or not isinstance(row.get('subject'), dict):
            errors.append('registry export: malformed object')
            continue
        try:
            identity_errors = contracts.validate_registration_identity(row)
            oid = contracts.registration_object_id(row['subject'], row['source'])
        except (KeyError, ValueError, TypeError):
            errors.append('registry export: invalid exact subject')
            continue
        if identity_errors:
            errors.extend('registry export: ' + error for error in identity_errors)
            continue
        request = row.get('request_id', '')
        record = f"requests/{row['source']['sha256']}/{oid}/{request}.json"
        if (not isinstance(request,str)
                or not re.fullmatch(r'[0-9a-f]{64}', request) or row.get('record') != record
                or oid in objects):
            errors.append('registry export: inconsistent or duplicate object/job identity')
            continue
        objects[oid] = row
    return objects


def _backup_errors(contracts, receipt, subject):
    try:
        return contracts.validate_backup_receipt(receipt, subject)
    except (ValueError, TypeError):
        return ['malformed backup receipt or subject']


def _checked_object(binding, objects, root, contracts, errors):
    if (not isinstance(binding, dict) or not isinstance(binding.get('object_id'), str)
            or binding['object_id'] not in objects):
        errors.append('unregistered preservation object')
        return None
    row = objects[binding['object_id']]
    subject = row['subject']
    errors.extend('object backup: ' + e for e in _backup_errors(contracts, row.get('backup_receipt'), subject))
    source = row.get('source')
    if not isinstance(source, dict):
        errors.append('registered source record required')
        return row
    if type(source.get('bytes')) is not int or source['bytes'] < 0:
        errors.append('registered source needs an exact nonnegative byte count')
    if source.get('sha256') != subject['content_sha256'] or source.get('bytes') != subject['bytes']:
        try:
            source_errors = contracts.validate_source_backup_receipt(row.get('source_backup_receipt'), source)
        except (ValueError, TypeError):
            source_errors = ['malformed source backup receipt']
        errors.extend('source backup: ' + error for error in source_errors)
    if (any(not isinstance(row.get(k),str) or not row[k].strip() for k in ('owner','continuation','reason'))
            or not isinstance(row.get('approval_scope'),dict) or not row['approval_scope']):
        errors.append('object needs a durable owner, reason, continuation and approval scope')
    if not isinstance(row.get('state'), str) or row['state'] not in PENDING_STATES:
        # The registry export has no replay-proof field. A declared verified state
        # must use a future checked-receipt adapter, never a caller's bare boolean.
        errors.append('object state has no supported checked preservation receipt')
    evidence = binding.get('evidence')
    registered = source.get('checked_evidence')
    if not isinstance(evidence, dict) or not isinstance(registered,dict) or evidence.get('sha256') != registered.get('sha256'):
        errors.append('checked source evidence does not match the registered object')
    else:
        _read_file(root, evidence, errors, 'checked source')
    return row


def referenced_originals(text: str) -> set[str]:
    """Literal originals; publishers also provide expanded-template inventories."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    names = set(re.findall(r'\[\[\s*:?(?:File|Image)\s*:\s*([^\]|]+)', text, re.I))
    names.update(re.findall(r'^\|\s*(?:image|hires_image)\s*=\s*([^\n|{}]+)', text, re.M))
    for gallery in re.findall(r'<gallery\b[^>]*>(.*?)</gallery>', text, re.S | re.I):
        names.update(re.findall(r'^(?:File:|Image:)?([^|\n]+)', gallery, re.M))
    return {_title('File:' + name.strip()) for name in names if name.strip()}


def publication_report(text: str, title: str, flags: list[str], required_sources: set[str],
                       manifest_path: Path, approved_sha256: str, revision_id: int | None = None) -> dict:
    """Validate a pinned, explicitly approved scope without changing raw findings."""
    errors = [flag for flag in flags if not flag.startswith('ARCHIVE ')]
    report = {'publication_eligible': False, 'preservation_complete': False,
              'raw_flags': list(flags), 'errors': errors, 'preservation_pending': [],
              'manifest_sha256': None}
    try:
        data = manifest_path.read_bytes()
    except OSError:
        errors.append('publication manifest unavailable')
        return report
    report['manifest_sha256'] = _hash(data)
    if report['manifest_sha256'] != approved_sha256:
        errors.append('explicit approved manifest SHA-256 mismatch')
        return report
    try:
        manifest = json.loads(data)
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
        contracts = importlib.import_module('preservation_contracts')
    except (ValueError, UnicodeError, ImportError):
        errors.append('valid manifest and installed backup contract required')
        return report
    if any(not callable(getattr(contracts, name, None)) for name in (
            'validate_backup_receipt', 'validate_registration_identity',
            'registration_object_id', 'validate_source_backup_receipt')):
        errors.append('current Story 410 registration/backup contract required')
        return report
    if (not isinstance(manifest, dict) or type(manifest.get('schema_version')) is not int or manifest['schema_version'] != 1
            or not isinstance(manifest.get('approval_scope'),dict) or not manifest['approval_scope']
            or not isinstance(manifest.get('pages'), list)):
        errors.append('unsupported publication manifest contract')
        return report
    candidates = [p for p in manifest['pages'] if isinstance(p, dict) and _title(p.get('title','')) == _title(title)]
    if len(candidates) != 1:
        errors.append('exact page is absent or duplicated in approved scope')
        return report
    page = candidates[0]
    subject = page.get('subject')
    if (not isinstance(subject, dict) or not isinstance(subject.get('kind'),str)
            or subject['kind'] not in {'wiki_draft','wiki_revision'}
            or _title(subject.get('title','')) != _title(title)
            or subject.get('content_sha256') != _hash(text.encode('utf8'))
            or subject.get('bytes') != len(text.encode('utf8'))):
        errors.append('page subject does not bind exact title/content/bytes')
        return report
    if ((revision_id is None and subject['kind'] != 'wiki_draft')
            or (revision_id is not None and (subject['kind'] != 'wiki_revision' or subject.get('revision_id') != revision_id))):
        errors.append('subject does not bind the actual draft/live revision context')
    errors.extend('page backup: ' + e for e in _backup_errors(contracts, page.get('backup_receipt'), subject))
    accuracy = page.get('source_accuracy')
    if not isinstance(accuracy,dict):
        accuracy = {}
    if accuracy.get('status') != 'checked':
        errors.append('checked source accuracy is required')
    _read_file(manifest_path.parent, accuracy.get('evidence'), errors, 'source accuracy')
    objects = _read_export(manifest_path.parent, manifest.get('registry_export'), contracts, errors)
    mappings = page.get('sources')
    if not isinstance(mappings, list):
        errors.append('explicit source mappings required')
        mappings = []
    seen = set()
    for binding in mappings:
        if not isinstance(binding, dict) or not isinstance(binding.get('url'),str):
            errors.append('malformed source mapping')
            continue
        url = _url(binding['url'])
        if url in seen:
            errors.append('duplicate source mapping')
        seen.add(url)
        row = _checked_object(binding, objects, manifest_path.parent, contracts, errors)
        if row:
            report['preservation_pending'].append({'url':url,'object_id':row['object_id'],'job_id':row['job_id'],'state':row['state']})
    if {_url(u) for u in required_sources} - seen:
        errors.append('cited source is absent from the approved registered scope')
    versions = page.get('original_versions')
    if not isinstance(versions, list):
        errors.append('explicit original-version mappings required')
        versions = []
    covered = set()
    for binding in versions:
        row = _checked_object(binding, objects, manifest_path.parent, contracts, errors)
        if row:
            if row['subject']['kind'] != 'wiki_file_version' or binding.get('subject') != row['subject']:
                errors.append('original version does not bind exact public version identity')
            covered.add(_title(row['subject']['title']))
            report['preservation_pending'].append({'original':row['subject']['title'],'object_id':row['object_id'],'job_id':row['job_id'],'state':row['state']})
    rendered = page.get('rendered_originals')
    if not isinstance(rendered,list) or any(not isinstance(n,str) for n in rendered):
        errors.append('expanded original inventory must be a title list')
        rendered = []
    required = referenced_originals(text) | {_title(n) for n in rendered}
    if required - covered:
        errors.append('referenced original version is not registered/backed up')
    report['publication_eligible'] = not errors
    # This adapter admits pending objects only; it cannot assert global coverage.
    report['preservation_complete'] = not report['preservation_pending'] and not flags and not errors
    return report
