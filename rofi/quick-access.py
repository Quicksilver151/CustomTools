#!/bin/python3

FILE_MANAGER = "nohup dolphin --new-window"
TEXT_EDITOR  = "neovide"



from rofi import Rofi
from pathlib import Path
import os, sys



def main(args: list):
    # get path to dir from args
    arg_path: str = "~/QuickAccess" if args.__len__() == 1 else args[1]
    
    # start rofi instance
    r = Rofi()

    full_path: Path = Path(arg_path).expanduser()
    sub_dirs: list[Path] = [f for f in full_path.iterdir() if f.is_dir() or not f.name.startswith('.')]
    
    
    # try for .quickaccess file
    quickaccess_file: Path = full_path / ".quickaccess"
    try: extra_paths: list[Path] = [Path(path.strip()).expanduser() for path in open(quickaccess_file, 'r').readlines()]
    except: extra_paths = []
    sub_dirs = sub_dirs + extra_paths

    # show rofi popup
    rofi_display_names: list[str] = list(map(lambda f: f.name.lower(), sub_dirs))
    index, key = r.select('', rofi_display_names)

    # check if valid selection
    if -1 in [index, key]:
        return
    
    selected_path: Path = sub_dirs[index]

    if selected_path.is_dir():
        launch_command = f"{FILE_MANAGER} \"{selected_path}\" &"
    else:
        print(os.path.dirname(selected_path), "ahahahah")

        launch_command = f"cd {selected_path.parent}; {TEXT_EDITOR} \"{selected_path}\" &"
    os.system(launch_command)



if __name__ == "__main__":
    main(sys.argv)
