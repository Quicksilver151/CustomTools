#!/bin/env bash

OFFLINE_NOTIFIED=false

while true; do
    if pi-ing; then
        OFFLINE_NOTIFIED=false
    else
        if [ "$OFFLINE_NOTIFIED" = false ]; then
            notify-send "Pi is offline" --urgency=critical
            OFFLINE_NOTIFIED=true
        fi
    fi
    sleep 900  # 15 minutes
done
