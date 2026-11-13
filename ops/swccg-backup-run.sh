#!/bin/bash
# Nightly wiki backup wrapper (2026-11-01).
# The swccg-wiki-files job clone lives on the 100 GB volume and is RE-CLONED fresh (blobless, sparse,
# ~10 MB) before every run, then the old one is discarded. The long-lived clone at
# /opt/swccg-ops/repos/swccg-wiki-files grew 3.3-3.7 GB per night (a new promisor pack duplicating the
# blobs it had pushed was written on every fetch) and filled the root disk. The job only needs
# files/INDEX.tsv + USAGE.tsv and writes changed files, so it never needs old blobs.
set -uo pipefail
V=/mnt/HC_Volume_107153504
R=$V/swccg-ops/repos/swccg-wiki-files
mountpoint -q "$V" || { echo "ERROR: $V not mounted; refusing to run (would write to root disk)"; exit 1; }
NEW="$R.new"
rm -rf "$NEW"
SSHCMD="ssh -i /opt/swccg-ops/keys/swccg-wiki-files -o IdentitiesOnly=yes -o UserKnownHostsFile=/opt/swccg-ops/keys/known_hosts -o StrictHostKeyChecking=yes"
if git clone -q --filter=blob:none --sparse https://github.com/billbisco/swccg-wiki-files.git "$NEW" \
   && git -C "$NEW" sparse-checkout set --no-cone /files/INDEX.tsv /files/USAGE.tsv /files/DUPLICATES.tsv /README.md \
   && git -C "$NEW" remote set-url origin git@github.com:billbisco/swccg-wiki-files.git \
   && git -C "$NEW" config core.sshCommand "$SSHCMD" \
   && git -C "$NEW" config gc.auto 0 && git -C "$NEW" config maintenance.auto false; then
  rm -rf "$R" && mv "$NEW" "$R"
  echo "fresh files clone: $(du -sh "$R/.git" | cut -f1)"
else
  echo "WARN: fresh clone failed; using existing $R"; rm -rf "$NEW"
  [ -d "$R/.git" ] || exit 1
fi
/usr/bin/python3 /opt/swccg-ops/repos/swccg-wiki/ops/nightly_backup.py /opt/swccg-ops/repos/swccg-wiki "$R"
rc=$?
echo "files clone after run: $(du -sh "$R/.git" | cut -f1); root free: $(df -h --output=avail / | tail -1)"
exit $rc
