#!/bin/sh
time="$1"
shift 1
msg="$@"
termdown "$time" -T "$msg" --time-format "%H:%M:%S"; notify-all --urgency=critical -a "timer" "$msg"

