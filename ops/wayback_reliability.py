"""Typed provider limits and bounded stale-job reconciliation for the sole owner."""
from __future__ import annotations

import json
from pathlib import Path
import time
from collections import Counter

from wayback_control import atomic_json, Paused
import failed_capture_recovery as recovery

LIMIT_CODES = {
    'error:user-session-limit': 'account_sessions',
    'error:too-many-daily-captures': 'url_daily_limit',
    'error:too-many-requests': 'target_host_limit',
    'error:too-many-redirects': 'target_redirects',
}
EVENTS = frozenset({'account_sessions','account_daily_limit','url_daily_limit','target_host_limit','target_redirects',
                    'unknown_limit','http_throttled','http_unavailable','http_auth','capacity_unknown','capacity_available'})
INTERVAL = 12 * 60


def classify(payload):
    """No provider strings or URL fragments cross this classification boundary."""
    code = payload.get('status_ext')
    if isinstance(code,str) and code.lower() in LIMIT_CODES: return LIMIT_CODES[code.lower()]
    msg = payload.get('message')
    msg = msg.lower() if isinstance(msg,str) else ''
    if 'limit of active save page now sessions' in msg or 'limit of concurrent active capture sessions' in msg:
        return 'account_sessions'
    if 'too many' in msg or 'limit' in msg or (isinstance(code,str) and ('limit' in code.lower() or 'too-many' in code.lower())):
        return 'unknown_limit'
    return None


def capacity(payload):
    if not isinstance(payload,dict): return None
    values={k:payload.get(k) for k in ('available','processing','daily_captures','daily_captures_limit','daily_status','daily_status_limit')}
    if any(type(values[k]) is not int or not 0<=values[k]<=10**9 for k in ('available','processing')): return None
    return {k:v for k,v in values.items() if type(v) is int and 0<=v<=10**9}


def load_stale(directory):
    path=Path(directory)/'stale-job-recovery.json'
    if not path.exists(): return None
    with path.open('rb') as f: raw=f.read(32*1024*1024+1)
    if len(raw)>32*1024*1024: raise ValueError('stale job manifest too large')
    data=json.loads(raw)
    if data.get('schema')!=1 or not isinstance(data.get('rows'),dict) or len(data['rows'])>20000: raise ValueError('invalid stale job manifest')
    return data


def save_stale(directory,data): atomic_json(Path(directory)/'stale-job-recovery.json',data)


def initialize_stale(w,directory,done,now):
    data=load_stale(directory)
    if data is None:
        data={'schema':1,'created_at':int(now),'next_at':0,'rows':{}}
    additional={u:{'original':e.copy(),'state':'waiting','next_at':0} for u,e in done.items() if u not in data['rows'] and e.get('status')=='pending' and w.stale(e)}
    if len(data['rows'])+len(additional)>20000: raise ValueError('stale job cohort too large')
    if additional or not (Path(directory)/'stale-job-recovery.json').exists():
        data['rows'].update(additional); save_stale(directory,data)
    return data


def stale_counts(data,done):
    if data is None:return None
    c=Counter()
    for u,row in data['rows'].items():
        c['total']+=1; e=done.get(u) or {}
        if e.get('status')=='verified': c['verified']+=1; c['manpc']+=(e.get('verify') or {}).get('lane')=='manpc'
        elif row['state']=='review' or e.get('status')=='failed': c['review']+=1
        elif e.get('status') in {'ok','unverified','retry'} or row['state']=='retried': c['in_progress']+=1
        else: c['waiting']+=1
    return {k:c[k] for k in ('total','verified','manpc','in_progress','review','waiting')}


def reconcile_stale(w,control,data,done,changed,urls,deadline):
    """One acknowledged job/status reconciliation per 12 minutes, never a save."""
    now=control.clock()
    if not data or control.state.get('mode')!='healthy' or not w.AUTH or now<data['next_at'] or time.monotonic()>deadline-180:return
    rows=[(u,r) for u,r in data['rows'].items() if r['state']=='waiting' and r['next_at']<=now and (done.get(u) or {}).get('status')=='pending']
    if not rows:return
    url,row=min(rows,key=lambda pair:(pair[1].get('attempts',0),not bool(done[pair[0]].get('capture')),pair[0]))
    data['next_at']=int(now)+INTERVAL; row['attempts']=row.get('attempts',0)+1; row['next_at']=int(now)+86400; save_stale(control.directory,data)
    current=done[url]; terminal=False; capture=current.get('capture')
    if not recovery.eligible(w,control.directory,url): row['state']='review'; save_stale(control.directory,data); return
    try:
        if capture and not recovery.matches_capture(w,url,capture): capture=None
        if not capture and current.get('job_id'):
            status=w.spn2_status(current['job_id']); phase=status.get('status')
            if phase=='pending': return # do not replace an acknowledged active job
            if phase=='success' and status.get('timestamp'):
                capture=f"https://web.archive.org/web/{status['timestamp']}/{status.get('original_url') or url}"
                if not recovery.matches_capture(w,url,capture): row['state']='review'; return
            elif phase=='error':
                terminal=True
                event=classify(status)
                if event in {'url_daily_limit','target_host_limit','target_redirects'}:
                    control.defer_source(url,event,status.get('_response_retry_after'))
                elif event in {'account_sessions','unknown_limit'}:
                    # Keep the acknowledged receipt; capacity/unknown holds
                    # are not evidence that this URL should be submitted again.
                    return
            else: return # uncertain status is never permission to resubmit
        if not capture: capture=recovery.lookup(w,url)
        if capture:
            entry=dict(current,capture=capture,status='unverified',last=w.iso(w.now()))
            try:
                status,proof=w.verify(url,capture)
                if status=='verified' and recovery.proof_matches(row['original'],proof):entry.update(status='verified',verify=proof)
                else: row['state']='review'
            except w.VerifyRetry as exc:
                if exc.side=='capture':w.mark_verify_deferred(entry,'stale capture replay unavailable')
                else:row['state']='review'
            done[url]=changed[url]=entry; control.checkpoint(done,control.initial_done)
        elif terminal and url in urls:
            entry=dict(current,status='retry',tries=0,last=w.iso(w.now())); entry.pop('job_id',None)
            done[url]=changed[url]=entry; control.checkpoint(done,control.initial_done); row['state']='retried'
        elif terminal or not current.get('job_id'):row['state']='review'
    except Paused:raise
    except (OSError,ValueError,TypeError,w.VerifyRetry):
        if row['attempts']>=3: row['state']='review'
    finally:save_stale(control.directory,data)


def canary_candidate(w,directory,done,health):
    """Only the explicitly accepted probe, and never while provider hold is active."""
    if health.get('mode')!='half_open' or not health.get('awaiting_canary_verification') or health.get('next_eligible_attempt_at'):return None
    state=json.loads((Path(directory)/'control.json').read_text(encoding='utf-8'))
    if state.get('mode')!='half_open' or state.get('next_attempt',0)>time.time():return None
    url=state.get('probe_url'); e=done.get(url) or {}; cap=e.get('capture')
    if not state.get('probe_accepted') or not cap or cap==state.get('probe_previous_capture') or not recovery.eligible(w,directory,url) or not recovery.matches_capture(w,url,cap):return None
    if e.get('status') not in {'ok','pending','unverified'}:return None
    return {'url':url,'capture':cap,'job_id':e.get('job_id') or '', 'status':e['status'],'defer':'canary'}
