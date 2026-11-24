<?php
# Copy of the block appended to /opt/swccg-wiki/extra-settings.php on 2026-11-11
# (backup: extra-settings.php.bak-20261111-steam).
# Bill approved steam:// Workshop links (2026-11-11).
# Rollback: cp -a /opt/swccg-wiki/extra-settings.php.bak-20261111-steam /opt/swccg-wiki/extra-settings.php
#           && docker exec swccg_wiki apachectl graceful

# Bill approved 2026-11-11: allow steam:// Workshop links
$wgUrlProtocols[] = 'steam://';
