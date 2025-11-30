#!/bin/bash

# go to workspace
wmctrl -s 1

# first clear worskspace
wmctrl -l | awk '$2 == 1 { print $1 }' | while read wid; do
    xkill -id "$wid"
done

# open all
nohup kitty --title battop -e nu -e battop&
sleep 0.5
nohup kitty --title btop -e nu -e btop&
sleep 0.5
nohup kitty --title salatui -o font_size=22 -e nu -e salatui&
sleep 0.5
xdotool key Super+Shift+Left
xdotool key Super+Control+Left
xdotool key Super+Control+Left
xdotool key Super+Control+Left
xdotool key Super+Control+Left
xdotool key Super+Control+Left
xdotool key Super+Control+Left
xdotool key Super+Control+Up
xdotool key Super+Control+Up
