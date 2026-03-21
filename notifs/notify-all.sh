#!/bin/bash
MESSAGE="${@}"
URGENCY="default"
TITLE="notify-all"

# Set NTFY_SERVER in your ~/.bashrc or ~/.profile
# export NTFY_SERVER="http://100.x.x.x:2586"
# Defaults to localhost (works on the Pi itself)
NTFY_SERVER="${NTFY_SERVER:-http://pi@pi:2586}"
NTFY_TOPIC="${NTFY_TOPIC:-notifs}"

for arg in "$@"; do
    case $arg in
        --urgency=*)
            URGENCY="${arg#*=}"
            MESSAGE="${MESSAGE//$arg/}"
            ;;
        -a=*|-a*)
            TITLE="${arg#*-a}"
            TITLE="${TITLE#=}"
            TITLE="${TITLE## }"
            MESSAGE="${MESSAGE//$arg/}"
            ;;
    esac
done

MESSAGE="${MESSAGE## }"
MESSAGE="${MESSAGE%% }"

case $URGENCY in
    low)      PRIORITY="low" ;;
    critical) PRIORITY="high" ;;
    *)        PRIORITY="default" ;;
esac

curl -s \
    -H "Priority: $PRIORITY" \
    -H "Title: $TITLE" \
    -d "$MESSAGE" \
    "$NTFY_SERVER/$NTFY_TOPIC" > /dev/null
