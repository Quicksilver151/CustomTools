#!/usr/bin/env bash

# Read clipboard, preserving trailing newlines via sentinel
content="$(xclip -selection clipboard -o; printf x)"
content="${content%x}"

redacted=""

# Split content by \n faithfully (keeps trailing/empty fields like Python split)
rest="$content"
while :; do
    if [[ "$rest" == *$'\n'* ]]; then
        para="${rest%%$'\n'*}"
        rest="${rest#*$'\n'}"
    else
        para="$rest"
        lastline=1
    fi

    # Split paragraph by single space faithfully (keeps empty fields)
    wrest="$para"
    lastword=""
    while :; do
        if [[ "$wrest" == *" "* ]]; then
            word="${wrest%% *}"
            wrest="${wrest#* }"
        else
            word="$wrest"
            lastword=1
        fi

        # Wrap every letter: ||letter||
        seg=""
        for ((j = 0; j < ${#word}; j++)); do
            seg+="||${word:j:1}||"
        done
        redacted+="${seg}|| ||"

        [[ -n "$lastword" ]] && break
    done

    redacted+=$'\n'

    [[ -n "$lastline" ]] && break
done

printf '%s' "$redacted" | xclip -selection clipboard
