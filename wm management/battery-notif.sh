#!/bin/bash
while true
do
  battery_level=`acpi -b | grep -P -o '[0-9]+(?=%)'`
   if [ $battery_level -e 95 ]; then
      notify-send "Battery Full" "Level: ${battery_level}%"
      paplay /usr/share/sounds/freedesktop/stereo/message.oga
    elif [ $battery_level -le 10 ]; then
      notify-send --urgency=CRITICAL "Battery Low" "Level: ${battery_level}%"
      paplay /usr/share/sounds/freedesktop/stereo/message-new-instant.oga
      sleep 0.01
      paplay /usr/share/sounds/freedesktop/stereo/message-new-instant.oga
      sleep 0.01
      paplay /usr/share/sounds/freedesktop/stereo/message-new-instant.oga
  fi
 sleep 60
done 
