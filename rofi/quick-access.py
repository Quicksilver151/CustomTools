#!/bin/python3

from rofi import Rofi
from pathlib import Path
import os, sys
# import subprocess

# current_desktop = subprocess.getoutput("wmctrl -d | grep '*' | cut -d ' ' -f1")
# desktops_with_dolphin = subprocess.getoutput("wmctrl -l | grep Dolphin | awk '{print $2}' ORS=' '").split()


# mom can we get valid dirs?
def valid_dirs(dir: str) -> bool:
    return dir.split('.').__len__() < 2

# we have dirs at home
def get_dirs_from_home(path: str) -> list:
    filtered_options: list[Path] = [f for f in Path(f"~/{path}").expanduser().iterdir() if f.is_dir() or not f.name.startswith('.')]
    return filtered_options

def get_dirs(path: str) -> list:
    filtered_options: list[Path] = [f for f in Path(path).iterdir() if f.is_dir() or not f.name.startswith('.')]
    return filtered_options


def main(args: list):
    # get path to dir from args
    selected_path = "~/QuickAccess" if args.__len__() == 1 else args[1]

    # start rofi instance
    r = Rofi()

    # get sub dirs
    if "~" in selected_path:
        selectable_dirs: list[Path] = get_dirs_from_home(selected_path.lstrip("~/"))
    else:
        selectable_dirs: list[Path] = get_dirs(selected_path)
    

    rofi_display_names: list[str] = list(map(lambda f: f.name.lower(), selectable_dirs))

    # for i in range(len(selectable_dirs)):
        # options_lower.append(selectable_dirs[i].name.lower())

    # options = ['Downloads', 'Home', 'Videos', 'Saves', 'Documents', 'Anicli']
    index, key = r.select('', rofi_display_names)
    # print(index,key)

    # check if valid selection
    if -1 in [index, key]:
        return
    
    launch_command = f"nohup dolphin --new-window \"{selectable_dirs[index]}\" &"
    print(launch_command)
    # 0/0
    os.system(launch_command)



if __name__ == "__main__":
    main(sys.argv)


