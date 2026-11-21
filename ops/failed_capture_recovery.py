"""Owner-locked reconciliation of historical terminal failures (#1247).

The immutable originals live only in the owner's existing private state directory.
No new submission client: only already queued URLs can be reset to ordinary retry.
"""
from __future__ import annotations

from collections import Counter
import json
import re
import time
from pathlib import Path
from urllib.parse import urlsplit, quote
from urllib.request import Request

from wayback_control import atomic_json

INTERVAL = 12 * 60
MAX_ROWS = 20000
TRANSIENT = ("stalled spn2", "connection refused", "errno 111", "timed out", "429", "503", "502")
CATEGORIES = ('no_job', 'auth', 'other')


def category(entry):
    if entry.get('status') != 'failed': return None
    error = str(entry.get('error') or '').lower()
    if any(s in error for s in TRANSIENT): return None
    if re.search(r'http (?:error )?401\b', error): return 'auth'
    if 'no job_id' in error: return 'no_job'
    return 'other'


def load_cohort(directory):
    path = Path(directory) / 'failed-recovery.json'
    if not path.exists(): return None
    with path.open('rb') as stream:
        raw = stream.read(32 * 1024 * 1024 + 1)
    if len(raw) > 32 * 1024 * 1024: raise ValueError('recovery state exceeds budget')
    data = json.loads(raw)
    if data.get('schema') != 1 or not isinstance(data.get('rows'), dict) or len(data['rows']) > MAX_ROWS:
        raise ValueError('invalid recovery state')
    return data


def save(directory, data):
    atomic_json(Path(directory) / 'failed-recovery.json', data)


def initialize(directory, done, now):
    data = load_cohort(directory)
    if data is None:
        rows = {url: {'category': category(e), 'original': e.copy(), 'state': 'waiting'}
                for url, e in done.items() if category(e)}
        if len(rows) > MAX_ROWS: raise ValueError('recovery cohort exceeds budget')
        data = {'schema': 1, 'created_at': int(now), 'next_at': 0, 'rows': rows}
        save(directory, data)
    return data


def health(data, done):
    if data is None: return None
    counts = Counter()
    for url, row in data['rows'].items():
        counts['total'] += 1; counts[row['category']] += 1
        entry = done.get(url) or {}
        if entry.get('status') == 'verified':
            counts['verified'] += 1
            counts['verified_manpc'] += (entry.get('verify') or {}).get('lane') == 'manpc'
        elif entry.get('status') in {'retry', 'pending', 'ok', 'unverified'}:
            counts['in_progress'] += 1
        elif row.get('state') in {'review', 'retried'}:
            counts['review'] += 1
        else:
            counts['waiting'] += 1
    return {name: counts[name] for name in ('total', *CATEGORIES, 'verified', 'verified_manpc', 'in_progress', 'review', 'waiting')}


def matches_capture(w, url, capture):
    try:
        if urlsplit(capture).hostname != 'web.archive.org': return False
        _, original = w.capture_parts(capture)
        return w.same_original(url, original)
    except (ValueError, TypeError):
        return False


def lookup(w, url):
    """Distinguish a definitive empty availability response from transport failure."""
    q='https://archive.org/wayback/available?url='+quote(url,safe='')
    payload=w._json(Request(q,headers={'User-Agent':w.UA,'Accept':'application/json'}))
    if not isinstance(payload,dict) or not isinstance(payload.get('archived_snapshots'),dict):
        raise ValueError('bad availability response')
    snapshots=payload['archived_snapshots']
    if not snapshots: return None
    closest=snapshots.get('closest')
    if not isinstance(closest,dict) or closest.get('available') is not True:
        raise ValueError('ambiguous availability result')
    capture=closest.get('url','').replace('http://web.archive.org/','https://web.archive.org/',1)
    if not matches_capture(w,url,capture): raise ValueError('different original')
    return capture


def eligible(w, directory, url):
    return not w.banned(url) and not w.suppressed_url(Path(directory)/'registry',url)


def proof_matches(entry, proof):
    expected=entry.get('registered_payload_sha256')
    return not expected or (proof.get('method')=='sha256' and proof.get('sha256')==expected)


def manual_candidates(w, directory, done):
    data=load_cohort(directory)
    if not data: return []
    rows=[]
    for url, old in data['rows'].items():
        entry=done.get(url) or {}; capture=entry.get('capture')
        if entry.get('status') not in {'failed','pending','ok','unverified'} or not capture: continue
        if old.get('state')=='review' or not eligible(w,directory,url) or not matches_capture(w,url,capture): continue
        rows.append({'url':url,'status':entry['status'],'capture':capture,'job_id':entry.get('job_id') or '', 'defer':'recovery'})
    return rows


def reconcile_one(w, control, data, done, changed, urls, deadline):
    """One reconciliation probe per 12 min; no submission outside the existing loop."""
    now=control.clock()
    if (not data or control.state['mode']!='healthy' or not w.AUTH or now<data['next_at'] or time.monotonic()>deadline-180): return
    candidates=[(u,r) for u,r in data['rows'].items() if r.get('state')=='waiting' and (done.get(u) or {}).get('status')=='failed']
    if not candidates: return
    # Prefer already-archived responses, then authentication failures. Round-robin
    # after an inconclusive attempt, rather than letting one dead source monopolize.
    url,row=min(candidates,key=lambda item:(item[1].get('attempts',0),CATEGORIES.index(item[1]['category']),not bool(done[item[0]].get('capture')),item[0]))
    data['next_at']=int(now)+INTERVAL
    row['attempts']=row.get('attempts',0)+1
    save(control.directory,data) # durable throttle before any HTTP
    if not eligible(w,control.directory,url):
        row['state']='review'; row['reason']='withdrawn_or_excluded'; save(control.directory,data); return
    current=done[url]
    prior=current.get('capture')
    capture=prior if prior and matches_capture(w,url,prior) and row['attempts']==1 else None
    try:
        if not capture: capture=lookup(w,url)
        if capture:
            status,proof=w.verify(url,capture)
            if status=='verified' and proof_matches(current,proof):
                update=dict(current,capture=capture,status='verified',verify=proof,last=w.iso(w.now()))
                done[url]=changed[url]=update
                control.checkpoint(done,control.initial_done)
            elif row['attempts']>=2:
                row['state']='review'; row['reason']='capture_not_matching'
            # A distinct capture is never silently substituted on a receipt,
            # and a mismatching historical capture is not grounds for a new save.
        elif url in urls and row['category'] in {'auth','no_job'}:
            # Existing owner still decides when/if a submission is allowed.
            update=dict(current,status='retry',tries=0,last=w.iso(w.now()))
            update.pop('job_id',None)
            done[url]=changed[url]=update
            control.checkpoint(done,control.initial_done)
            row['state']='retried'; row['reason']='no_capture_active_queue'
        else:
            row['state']='review'; row['reason']='no_capture_or_outside_active_queue'
    except w.VerifyRetry as exc:
        if exc.side=='capture' and capture and not prior:
            # A lookup-derived capture is only a candidate. The second lane
            # must still prove the contents; do not call it verified or ok.
            update=dict(current,capture=capture,status='unverified',last=w.iso(w.now()))
            w.mark_verify_deferred(update,'recovery replay unavailable')
            done[url]=changed[url]=update
            control.checkpoint(done,control.initial_done)
        elif exc.side!='capture' and row['attempts']>=2:
            row['state']='review'; row['reason']='source_unavailable'
    except (OSError,ValueError,TypeError):
        if row['attempts']>=3:
            row['state']='review'; row['reason']='lookup_inconclusive'
    finally:
        save(control.directory,data)
