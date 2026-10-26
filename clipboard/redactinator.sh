#!/usr/bin/env bash

# Read clipboard, preserving trailing newlines via sentinel
content="$(xclip -selection clipboard -o; printf x)"
content="${content%x}"

redacted=""

# Split content by \n faithfully (keeps trailing/empty fields like Python split)
rest="$content"
while :; do
    if [[ "$rest" == *$'\n'* ]]; then
        line="${rest%%$'\n'*}"
        rest="${rest#*$'\n'}"
    else
        line="$rest"
        lastline=1
    fi

    # Split line by single space faithfully (keeps empty fields)
    wrest="$line"
    lastword=""
    while :; do
        if [[ "$wrest" == *" "* ]]; then
            word="${wrest%% *}"
            wrest="${wrest#* }"
        else
            word="$wrest"
            lastword=1
        fi

        redacted+="||${word} ||"

        [[ -n "$lastword" ]] && break
    done

    redacted+=$'\n'

    [[ -n "$lastline" ]] && break
done

printf '%s' "$redacted" | xclip -selection clipboard
