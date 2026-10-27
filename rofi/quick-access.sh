#!/usr/bin/env bash

FILE_MANAGER="nohup dolphin --new-window"
TEXT_EDITOR="neovide"

ARG_PATH="${1:-$HOME/QuickAccess}"
FULL_PATH="${ARG_PATH/#\~/$HOME}"

[ ! -d "$FULL_PATH" ] && exit 1

# Arrays to hold paths and display names
paths=()
displays=()

# First, parse .quickaccess file for top entries and others
if [ -f "$FULL_PATH/.quickaccess" ]; then
    # Read top entries first
    while IFS= read -r line || [ -n "$line" ]; do
        # Skip empty lines or lines without delimiter
        [[ "$line" =~ ^[[:space:]]*$ ]] && continue
        [[ "$line" != *"->"* ]] && continue
        
        # Split on exact "->" string
        part1="${line%%->*}"
        part2="${line#*->}"
        if [[ "$part2" == *"->"* ]]; then
            part3="${part2#*->}"
            part2_name="${part2%%->*}"
        else
            part3="false"
            part2_name="$part2"
        fi
        
        raw_path="$(echo "$part1" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
        name_str="$(echo "$part2_name" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
        top_str="$(echo "$part3" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
        
        # Expand ~
        raw_path="${raw_path/#\~/$HOME}"
        
        # Resolve path
        if [[ "$raw_path" = /* ]]; then
            resolved_path=$(realpath "$raw_path" 2>/dev/null || echo "$raw_path")
        else
            resolved_path=$(realpath "$FULL_PATH/$raw_path" 2>/dev/null || echo "$FULL_PATH/$raw_path")
        fi
        
        [ -z "$name_str" ] && name_str="a"
        top_str_lower=$(echo "$top_str" | tr '[:upper:]' '[:lower:]')
        
        if [ "$top_str_lower" = "true" ]; then
            paths=("$resolved_path" "${paths[@]}")
            displays=("$name_str" "${displays[@]}")
        else
            paths+=("$resolved_path")
            displays+=("$name_str")
        fi
    done < "$FULL_PATH/.quickaccess"
fi

# Then add subdirectories (skip hidden files/dirs that start with .)
while IFS= read -r -d '' dir; do
    [ -z "$dir" ] && continue
    # Only keep entries that are directories (follows symlinks, so folder
    # symlinks are included; symlinks to files are skipped)
    [ -d "$dir" ] || continue
    basename_dir=$(basename "$dir")
    # Skip hidden
    [[ "$basename_dir" == .* ]] && continue
    # Resolve symlinks so we open the original folder path
    dir=$(realpath "$dir" 2>/dev/null || echo "$dir")
    
    # Format display name: handle "[SM] subject matter" syntax
    if [[ "$basename_dir" == *"] "* ]]; then
        # Split on "] " - take "[SM]" + " " + rest lowercased
        prefix=$(echo "$basename_dir" | cut -d']' -f1)"]"
        rest=$(echo "$basename_dir" | cut -d']' -f2- | sed 's/^[[:space:]]*//' | tr '[:upper:]' '[:lower:]')
        disp="$prefix $rest"
    else
        disp=$(echo "$basename_dir" | tr '[:upper:]' '[:lower:]')
    fi
    
    paths+=("$dir")
    displays+=("$disp")
done < <(find "$FULL_PATH" -maxdepth 1 -mindepth 1 \( -type d -o -type l \) -print0 2>/dev/null | sort -z)

choice=$(printf '%s\n' "${displays[@]}" | rofi -dmenu -p "" -i -sort -sorting-method fzf)

[ -z "$choice" ] && exit 0

# Find selected index
idx=-1
for i in "${!displays[@]}"; do
    if [ "${displays[$i]}" = "$choice" ]; then
        idx=$i
        break
    fi
done

[ "$idx" -lt 0 ] && exit 0

selected_path="${paths[$idx]}"

if [ -d "$selected_path" ]; then
    eval "$FILE_MANAGER \"${selected_path}\"" >/dev/null 2>&1 &
else
    nohup "$TEXT_EDITOR" "$selected_path" >/dev/null 2>&1 &
fi
