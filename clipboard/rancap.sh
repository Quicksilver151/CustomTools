#!/usr/bin/env bash

# Read clipboard, preserving trailing newlines via sentinel
content="$(xclip -selection clipboard -o; printf x)"
content="${content%x}"

result=""
len=${#content}
for ((i = 0; i < len; i++)); do
    ch="${content:i:1}"
    if ((RANDOM % 2)); then
        result+="${ch^^}"
    else
        result+="${ch,,}"
    fi
done

printf '%s' "$result" | xclip -selection clipboard
