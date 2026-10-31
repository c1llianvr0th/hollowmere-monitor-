#!/bin/bash

HOST="hv-mon-04"

echo "[CHECK] Starting healthcheck..."

ping -c 1 "$HOST" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "[OK] Host reachable"
else
    echo "[ERROR] Host unreachable"
fi

echo "[CHECK] Checking monitoring service..."

systemctl is-active hollowmere-monitor

echo "[CHECK] Healthcheck completed."

# If the service reports active, do not assume
# someone is actually operating it.
