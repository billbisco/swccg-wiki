#!/bin/bash
# run apply passes for groups in $GRPS until ~160s used (batches in /tmp/batches/<g>)
export WIKI_ENV_FILE=$HOME/mnt/gythe/.grok/claude-agent/wiki-bot-password.env
cd /tmp/sw/authoring; START=$(date +%s)
for g in ${GRPS:-none}; do
  case $g in
    wn1|wn2|we4|we5|we6|we7|xrows3) S="Events and players from old Players Committee forum topics that survive on forum.starwarsccg.org, swccg-guild/work#1339";;
    h1341a|h1341b|h1341d|h1341c|h1341c0|h1341c1|h1341c2|h1341c3) S="Versions navigator: fix redirect links, duplicates, missing members, stale split templates (Decipher sets), swccg-guild/work#1341";;
    pc1341) S="Versions navigator: merge families with the same picture (picture check), swccg-guild/work#1341";;
    rta|rta0|rta1|rta2) S="Preserved copies (checked Internet Archive captures) for forum.starwarsccg.org citations, swccg-guild/work#1339";;
    dc140|dc140b|dc0|dc1|dc2) S="SWCCG Players Committee and Retro Club Discord history (message permalinks; public sources first), swccg-guild/work#140";;
    n42*|nav1342) S="Versions navigator for Virtual Modern-origin families, Virtual Sets 0–9 (Theed Palace #1303 pattern), swccg-guild/work#1342";;
    n43*) S="Versions navigator for Virtual Modern-origin families, Virtual Sets 10–19 (Theed Palace #1303 pattern), swccg-guild/work#1343";;
    n44*) S="Versions navigator for Virtual Modern-origin families, Virtual Sets 20–27, Sets P, D, Premium and undated (Theed Palace #1303 pattern), swccg-guild/work#1344";;
    n45*) S="Versions navigator for Reflections Gold playtest and Remastered pairs (Theed Palace #1303 pattern), swccg-guild/work#1345";;
    n46*) S="Versions navigator for Virtual Legacy-origin families, Blocks 1–9 and Virtual Shields (Theed Palace #1303 pattern), swccg-guild/work#1346";;
    r48*) S="Versions navigator: families resolved from evidence (refused by the generator), swccg-guild/work#1348";;
    r47*) S="Versions navigator: Decipher ancillary products (2-player games, Jedi Pack, OTSD, anthologies), swccg-guild/work#1347";;
    e697*) S="Errata comparison table (Virtual Set 10 Modern; one column per published text state, changed words highlighted), swccg-guild/work#697";;
    r48h) S="Versions navigator: Captain Hera Syndulla family; stale inline lists on two single printings; Mysteries entry for the Border Breaker AI date, swccg-guild/work#1348";;
    r48l*) S="Versions navigator: Alter host cards (each Virtual host page joins its Decipher host navigator), swccg-guild/work#1348";;
    e[0-9]*) S="Errata comparison table (one column per published text state; changed words highlighted; dates from each page's sourced version history), swccg-guild/work#${g:1:3}";;
    *) S="Old Players Committee forum history (swccgpc.com), swccg-guild/work#601";;
  esac
  n=$(wc -l < /tmp/batches/$g/apply.tsv)
  d=$(python3 -c "import json;print(len({json.loads(l)['title'] for l in open('/tmp/batches/$g/applied.jsonl') if json.loads(l)['result'].startswith(('edited','created','nochange'))}))" 2>/dev/null || echo 0)
  echo "$g $d/$n"; [ "$d" -ge "$n" ] && continue
  left=$((${BUDGET:-160}-$(date +%s)+START)); [ $left -lt 15 ] && { echo PAUSE; exit; }
  timeout $left python3 apply_guarded.py /tmp/batches/$g "$S" >> /tmp/batches/$g.log 2>&1
  grep -v "^Talk:\|-> edited\|-> created\|nochange" /tmp/batches/$g.log | tail -3
done; echo ALLDONE
