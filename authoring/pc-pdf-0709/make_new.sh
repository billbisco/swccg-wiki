#!/bin/bash
cd "$(dirname "$0")"
rm -rf final-new; python3 build.py events-new.json names-build.tsv final-new > build-new.log 2>&1; tail -1 build-new.log
cp events-new.json events-all.json
python3 hubs.py events-new.json final-new
date -u +%Y-%m-%dT%H:%M:%SZ > final-new/since.txt
