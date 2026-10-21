#!/bin/python3

FILE_MANAGER = "nohup dolphin --new-window"
TEXT_EDITOR  = "neovide"



from rofi import Rofi
from pathlib import Path
import os, sys


from pathlib import Path

def get_qa_meta(full_path: Path) -> list:
    quickaccess_file: Path = full_path / ".quickaccess"
    
    # Safety check if the file doesn't exist
    if not quickaccess_file.is_file():
        return []

    meta_list: list = []
    
    # Using 'with' properly closes the file after reading
    with open(quickaccess_file, 'r') as f:
        for line in f:
            # Skip empty lines or lines without the delimiter
            if "->" not in line:
                continue
                
            splits = line.split("->")
            
            # --- THE FIX FOR RELATIVE PATHS ---
            try:
                raw_path = Path(splits[0].strip()).expanduser()
                # If the path isn't absolute, make it relative to full_path
                if not raw_path.is_absolute():
                    resolved_path = (full_path / raw_path).resolve()
                else:
                    resolved_path = raw_path.resolve()
            except Exception:
                resolved_path = None
            # ----------------------------------

            try: 
                name: str = splits[1].strip()
            except IndexError: 
                name = "a"

            try: 
                top: bool = splits[2].strip().lower() == "true"
            except IndexError: 
                top = False

            meta = [resolved_path, name, top]
            meta_list.append(meta)
        
    return meta_list



def main(args: list):
    # get path to dir from args or default to ~/QuickAccess
    arg_path: str = "~/QuickAccess" if args.__len__() == 1 else args[1]
    
    # start rofi instance
    r = Rofi(rofi_args=['-i', '-sort', '-sorting-method', 'fzf'])

    # access path
    full_path: Path = Path(arg_path).expanduser()

    # rofi paths
    sub_dirs: list[Path] = [f for f in full_path.iterdir() if f.is_dir() or not f.name.startswith('.')]

    # filter non dirs:
    sub_dirs: list[Path] = list(filter(Path.is_dir, sub_dirs))

    # allows for special folder name syntax: "[SM] subject matter"
    def display(path: Path):
        if len(path.name.split("] ")) == 1:
            return path.name.lower()
        return path.name.split(" ")[0] + " " + path.name.split(" ", 1)[1].lower()
        
    # rofi display names
    rofi_display_names: list[str] = list(map(display, sub_dirs))

    # .quickaccess file parsing and adding
    qa_meta = get_qa_meta(full_path)
    for meta in qa_meta:
        if meta[2]:
            sub_dirs = [meta[0]] + sub_dirs
            rofi_display_names = [meta[1]] + rofi_display_names
        else:
            sub_dirs = sub_dirs + [meta[0]]
            rofi_display_names = rofi_display_names + [meta[1]]

    # show rofi popup
    index, key = r.select('', rofi_display_names)

    # check if valid selection
    if -1 in [index, key]:
        return
    
    selected_path: Path = sub_dirs[index]

    if selected_path.is_dir():
        launch_command = f"{FILE_MANAGER} \"{selected_path}\" &"
    else:
        # launch_command = f"cd '{selected_path.parent}'; {TEXT_EDITOR} \"{selected_path}\" &"
        launch_command = f"{TEXT_EDITOR} \"{selected_path}\" &"
    os.system(launch_command)



if __name__ == "__main__":
    main(sys.argv)
