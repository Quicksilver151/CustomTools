#!/usr/bin/env bash

OBSIDIAN_JSON="${XDG_CONFIG_HOME:-$HOME/.config}/obsidian/obsidian.json"

[ ! -f "$OBSIDIAN_JSON" ] && exit 1

# Get vaults with open/closed status - open vaults first (matching original behavior)
open_names=()
closed_names=()
open_display=()
closed_display=()

while IFS=$'\t' read -r name status; do
    [ -z "$name" ] && continue
    disp=$(echo "$name" | tr '[:upper:]' '[:lower:]')
    if [ "$status" = "open" ]; then
        open_names+=("$name")
        open_display+=("$disp")
    else
        closed_names+=("$name")
        closed_display+=("$disp")
    fi
done < <(jq -r '.vaults[] | "\(.path | split("/") | last)\t\(if has("open") then "open" else "closed" end)"' "$OBSIDIAN_JSON")

# Combine: open first, then closed
all_names=("${open_names[@]}" "${closed_names[@]}")
all_display=("${open_display[@]}" "${closed_display[@]}")

[ ${#all_display[@]} -eq 0 ] && exit 1

choice=$(printf '%s\n' "${all_display[@]}" | rofi -dmenu -p "Vault: " -i)

[ -z "$choice" ] && exit 0

# Find selected index
idx=-1
for i in "${!all_display[@]}"; do
    if [ "${all_display[$i]}" = "$choice" ]; then
        idx=$i
        break
    fi
done

[ "$idx" -lt 0 ] && exit 0

vault="${all_names[$idx]}"

# URL encode vault name
encoded_vault=$(printf '%s' "$vault" | jq -sRr @uri)

# Try to open with obsidian
if command -v obsidian-app >/dev/null 2>&1; then
    nohup obsidian-app "obsidian://open?vault=${encoded_vault}" >/dev/null 2>&1 &
elif command -v obsidian >/dev/null 2>&1; then
    nohup obsidian "obsidian://open?vault=${encoded_vault}" >/dev/null 2>&1 &
else
    xdg-open "obsidian://open?vault=${encoded_vault}" >/dev/null 2>&1 &
fi
