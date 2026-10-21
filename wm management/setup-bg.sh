#!/bin/bash

# go to workspace
wmctrl -s 9
#
# # first clear worskspace
# wmctrl -l | awk '$2 == 1 { print $1 }' | while read wid; do
#     xkill -id "$wid"
# done
#
# open all
nohup kitty --title tmux-bg -e nu -e "sleep 2sec;tmux-bg"&
sleep 0.5
xdotool key Control+Shift+minus
sleep 0.5
wmctrl -s 0

# nohup kitty --title btop -e nu -e btop&
# sleep 0.5
# # nohup kitty --title salatui -o font_size=16 -e nu -e "salat_mv -cant"&
# nohup kitty --title salatui -o font_size=16 -e nu -e "salatui"&
# sleep 0.5
# xdotool key Super+Shift+Left
# xdotool key Super+Control+Left
# xdotool key Super+Control+Left
# xdotool key Super+Control+Left
# xdotool key Super+Control+Left
# xdotool key Super+Control+Left
# xdotool key Super+Control+Left
# xdotool key Super+Control+Up
# xdotool key Super+Control+Up
# xdotool key Control+Shift+equal
# xdotool key Control+Shift+equal
# xdotool key Control+Shift+equal
#
