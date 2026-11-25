#!/bin/bash
# status: done/total and non-ok results for groups
cd /tmp/batches; tot=0; dn=0
for g in "$@"; do n=$(wc -l < $g/apply.tsv); d=$( [ -f $g/applied.jsonl ] && python3 -c "import json;print(len({json.loads(l)['title'] for l in open('$g/applied.jsonl') if json.loads(l)['result'].startswith(('edited','created','nochange'))}))" || echo 0); tot=$((tot+n)); dn=$((dn+d)); printf "%s %s/%s  " $g $d $n; done; echo; echo "TOTAL $dn/$tot"
cat $(for g in "$@"; do [ -f $g/applied.jsonl ] && echo $g/applied.jsonl; done) 2>/dev/null | grep -v '"result": "\(edited\|created\|nochange\)' | head -5
