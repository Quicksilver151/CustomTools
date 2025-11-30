#!/bin/bash

PROGRAM="$1"
SERVICE="$2"
if pgrep -x "$SERVICE"
then
    notify-send "$PROGRAM Disabled"
    killall "$SERVICE"
else
    notify-send "$PROGRAM Enabled"
    "$PROGRAM"
fi
