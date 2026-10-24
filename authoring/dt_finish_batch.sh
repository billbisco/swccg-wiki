#!/bin/bash
# After helpers finish: era format, card-page fixes, validate, build, package for the PC apply (Claude 2026-10-22).
#   bash dt_finish_batch.sh <batch> ID...      -> /mnt/user-data/outputs/<batch>-apply.tar (+ logs in /tmp/claude-0/<batch>.*)
set -e
B=$1; shift; IDS="$@"; L=/tmp/claude-0/$B
python3 dt_player_check.py $IDS
python3 era_format.py --apply $IDS > $L.era.log
python3 fix_card_pages.py --apply $IDS > $L.fix.log; grep "^MANUAL" $L.fix.log || true
python3 dt_validate.py $IDS > $L.val.log; grep -B1 "^   - " $L.val.log | grep -v "NO WIKI PAGE and not a\|^--" || true
python3 decktech_batch.py build $B $IDS > $L.build.log 2>&1 || { tail -5 $L.build.log; exit 1; }
tail -1 $L.build.log
python3 dt_drop_stale_rows.py y-$B.tsv - $IDS
python3 -c "import sys;b=[l.split(chr(9))[0] for l in open(sys.argv[1],encoding='utf-8') if chr(9) in l and any(c in l.split(chr(9))[0] for c in '#<>[]{}|')];b and sys.exit('page titles with characters MediaWiki forbids (set dest_title): %s' % b)" y-$B.tsv
python3 -c "import sys,collections;c=collections.defaultdict(set);[c[l.split(chr(9))[1].strip().lower()].add(l.split(chr(9))[1].strip()) for l in open(sys.argv[1],encoding='utf-8') if chr(9) in l];b=[v for v in c.values() if len(v)>1];b and sys.exit('case-colliding page files (Windows apply would merge them): %s' % b)" y-$B.tsv
D=/tmp/claude-0/${B}pkg; rm -rf $D; mkdir -p $D/pages
date -u -r $L.build.log +%Y-%m-%dT%H:%M:%SZ > $D/since.txt
cp y-$B.tsv wiki_api_apply.py $D/
while IFS=$'\t' read -r t f; do cp "$f" "$D/pages/"; done < y-$B.tsv
tar xf y-$B.tar -C $D gemp-import-$B 2>/dev/null || true
mkdir -p /mnt/user-data/outputs; (cd $D && tar cf /mnt/user-data/outputs/$B-apply.tar .)
ls -la /mnt/user-data/outputs/$B-apply.tar
