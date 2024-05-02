#!/bin/python3

from rofi import Rofi
from pathlib import Path
import os, sys

def main(args: list):
    # get path to dir from args
    selected_path = "~/QuickAccess" if args.__len__() == 1 else args[1]

    # start rofi instance
    r = Rofi()

    # get valid sub dirs
    if "~" in selected_path:
        sub_dirs: list[Path] = [f for f in Path(selected_path).expanduser().iterdir() if f.is_dir() or not f.name.startswith('.')]
    else:
        sub_dirs: list[Path] = [f for f in Path(selected_path).iterdir() if f.is_dir() or not f.name.startswith('.')]
    

    rofi_display_names: list[str] = list(map(lambda f: f.name.lower(), sub_dirs))
    index, key = r.select('', rofi_display_names)

    # check if valid selection
    if -1 in [index, key]:
        return
    
    launch_command = f"nohup dolphin --new-window \"{sub_dirs[index]}\" &"
    os.system(launch_command)

if __name__ == "__main__":
    main(sys.argv)
