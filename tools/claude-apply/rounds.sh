#!/bin/bash
# rounds.sh <groupsfile> <nrounds> : run up to 10 unfinished groups per round
cd /tmp/batches; ALL=$(cat $1)
for r in $(seq 1 $2); do
 TODO=$(for g in $ALL; do n=$(wc -l < $g/apply.tsv); d=$([ -f $g/applied.jsonl ] && python3 -c "import json;print(len({json.loads(l)['title'] for l in open('$g/applied.jsonl') if json.loads(l)['result'].startswith(('edited','created','nochange'))}))" || echo 0); [ $d -lt $n ] && echo $g; done | head -10 | tr '\n' ' ')
 [ -z "$TODO" ] && break
 ~/w/tools/par.sh $TODO >/dev/null
done
~/w/tools/st.sh $ALL | tail -6
