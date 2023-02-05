#!/usr/bin/env bash

SOURCES_PATH='/sys/class/power_supply'

SOURCES=$(ls $SOURCES_PATH | grep BAT)
[[ -z "$SOURCES" ]] && exit 0

CAPACITIES=""
for BAT in "${SOURCES[@]}"; do
    CAP="$(cat "$SOURCES_PATH/$BAT/capacity")"
    STATSYMBOL="$([[ $(cat "$SOURCES_PATH/$BAT/status") == "Charging" ]] && echo '' || echo '↓')"
    STAT="$([[ $(cat "$SOURCES_PATH/$BAT/status") == "Charging" ]] && echo 'U 0xff00ffff' || echo 'U 0xffaa00ff')"
    LEVEL="$([[ $(cat "$SOURCES_PATH/$BAT/capacity") < 21 ]] && echo 'BG 0xffcf3f00' || echo 'BG 0xff1d222a' )"
    CAPACITIES="!Y $STAT $LEVEL Y! $STATSYMBOL $CAP% "
done

echo $CAPACITIES

