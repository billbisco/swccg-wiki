#!/bin/bash
# Install / repair the swccg-ops jobs on the wiki VPS. Idempotent. Run as root.
# Needs: the Hetzner volume mounted at /mnt/HC_Volume_107153504, and
# deploy keys in /opt/swccg-ops/keys/{swccg-wiki,swccg-wiki-files} added (write access)
# to the matching GitHub repos, and keys/known_hosts with github.com's ED25519 key.
set -euo pipefail
OPS=/opt/swccg-ops
K=$OPS/keys
R=$OPS/repos
mkdir -p "$R" /var/lib/swccg-ops

ssh_for() { echo "ssh -i $K/$1 -o IdentitiesOnly=yes -o UserKnownHostsFile=$K/known_hosts -o StrictHostKeyChecking=yes"; }

# swccg-wiki: full clone (~60 MB)
if [ ! -d "$R/swccg-wiki/.git" ]; then
  git clone -q https://github.com/billbisco/swccg-wiki.git "$R/swccg-wiki"
fi
git -C "$R/swccg-wiki" remote set-url origin git@github.com:billbisco/swccg-wiki.git
git -C "$R/swccg-wiki" config core.sshCommand "$(ssh_for swccg-wiki)"

# swccg-wiki-files: ~4 GB on GitHub. The nightly backup does NOT keep a long-lived clone of it:
# ops/swccg-backup-run.sh (installed to /usr/local/sbin) makes a fresh blobless sparse clone on the
# 100 GB volume before every run and discards the previous one. A long-lived clone on the root disk
# grew 3-4 GB per night (duplicate promisor packs of the blobs it had pushed) and filled the disk on
# 2026-11-01. Never put this clone back on /.
VOL=/mnt/HC_Volume_107153504
mountpoint -q "$VOL" || { echo "ERROR: $VOL is not mounted"; exit 1; }
mkdir -p "$VOL/swccg-ops/repos"
install -m 755 "$R/swccg-wiki/ops/swccg-backup-run.sh" /usr/local/sbin/swccg-backup-run.sh
if [ -d "$R/swccg-wiki-files/.git" ]; then
  echo "NOTE: old root-disk clone $R/swccg-wiki-files is no longer used; remove it after checking it holds no local work."
fi

cat > /etc/systemd/system/swccg-wayback.service <<EOF
[Unit]
Description=swccg Wayback Machine save queue (ops/wayback_worker.py)
After=network-online.target
[Service]
Type=oneshot
Nice=10
IOSchedulingClass=idle
TimeoutStartSec=15min
ExecStart=/usr/bin/python3 $R/swccg-wiki/ops/wayback_worker.py $R/swccg-wiki --minutes 10
EOF
cat > /etc/systemd/system/swccg-wayback.timer <<EOF
[Unit]
Description=Run the swccg Wayback queue every 15 minutes
[Timer]
OnBootSec=5min
OnUnitInactiveSec=15min
[Install]
WantedBy=timers.target
EOF
cat > /etc/systemd/system/swccg-backup.service <<EOF
[Unit]
Description=swccg nightly wiki backup to GitHub (ops/nightly_backup.py)
After=network-online.target
[Service]
Type=oneshot
Nice=10
IOSchedulingClass=idle
TimeoutStartSec=3h
ExecStart=/usr/bin/python3 $R/swccg-wiki/ops/nightly_backup.py $R/swccg-wiki $R/swccg-wiki-files
EOF
# The drop-in replaces the ExecStart above: run through the wrapper, files clone on the volume.
mkdir -p /etc/systemd/system/swccg-backup.service.d
cat > /etc/systemd/system/swccg-backup.service.d/10-volume-wrapper.conf <<EOF
# run via wrapper; files clone on the volume, fresh each run
[Unit]
RequiresMountsFor=$VOL
[Service]
ExecStart=
ExecStart=/usr/local/sbin/swccg-backup-run.sh
EOF
cat > /etc/systemd/system/swccg-backup.timer <<EOF
[Unit]
Description=swccg nightly wiki backup (07:15 UTC = 03:15 Caracas)
[Timer]
OnCalendar=*-*-* 07:15:00 UTC
Persistent=true
[Install]
WantedBy=timers.target
EOF
systemctl daemon-reload
systemctl enable --now swccg-wayback.timer swccg-backup.timer
systemctl list-timers --no-pager 'swccg-*'
