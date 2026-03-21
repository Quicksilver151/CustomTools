#!/bin/bash
# notify-listen

# Set NTFY_SERVER in your ~/.bashrc or ~/.profile
# export NTFY_SERVER="http://100.x.x.x:2586"
# Defaults to localhost (works on the Pi itself)
NTFY_SERVER="${NTFY_SERVER:-http://pi@pi:2586}"
NTFY_TOPIC="${NTFY_TOPIC:-notifs}"

ntfy subscribe "$NTFY_SERVER/$NTFY_TOPIC" | while read -r message; do
    BODY=$(echo "$message" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('message',''))" 2>/dev/null || echo "$message")
    PRIORITY=$(echo "$message" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('priority',3))" 2>/dev/null || echo "3")

    case $PRIORITY in
        1|2) URGENCY="low" ;;
        4|5) URGENCY="critical" ;;
        *)   URGENCY="normal" ;;
    esac

    notify-send -a "notify-all" -u "$URGENCY" "$BODY"
done
