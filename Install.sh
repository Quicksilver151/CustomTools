#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="$HOME/CustomPath"
mkdir -p "$TARGET_DIR"

# Remove extension
strip_ext() {
    filename=$(basename "$1")
    echo "${filename%%.*}"
}

find . -type f | while read -r src; do
    # Ignore anything inside dotfolders or dotfiles
    case "$src" in
        */.*) continue ;;
    esac

    # Allowed extensions only
    case "$src" in
        *.py|*.sh) ;;        # allowed
        *) continue ;;       # skip everything else
    esac

    base=$(basename "$src")

    # Skip installer & README
    case "$base" in
        Install.sh|README.md)
            continue
            ;;
    esac

    # Strip extension for the link target
    name_no_ext=$(strip_ext "$src")
    dest="$TARGET_DIR/$name_no_ext"

    # If symlink exists → skip
    if [[ -L "$dest" ]]; then
        continue
    fi

    # If a real file exists → error
    if [[ -e "$dest" ]]; then
        echo "ERROR: '$dest' exists and is NOT a symlink. Skipping." >&2
        continue
    fi

    # Ensure the source file is executable
    if [[ ! -x "$src" ]]; then
        chmod +x "$src"
    fi

    # Create the symlink
    ln -s "$(realpath "$src")" "$dest"
    echo "Linked: $dest → $src"
done
