#!/bin/bash

# Hollowmere nightly backup
# Runs as root through cron.

BACKUP_DIR="/backup"
SOURCE="/var/data"

DATE=$(date +%F)

mkdir -p "$BACKUP_DIR"

tar czf "$BACKUP_DIR/vault_$DATE.tgz" "$SOURCE"

echo "backup ok" >> /var/log/backup.log

# rack 13 asked to be included.
# i said no.
