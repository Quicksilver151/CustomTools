#!/bin/bash
dunstctl set-paused true # pause notifs

i3lock -nc `cat ~/.cache/wal/colors`

dunstctl set-paused false # resume
