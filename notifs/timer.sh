#!/bin/sh
time="$1"
shift 1
msg="$@"
termdown "$time" -T "$msg" --time-format "%H:%M:%S" --no-figlet-y-offset 0; notify-all --urgency=critical -a "timer" "$msg"

