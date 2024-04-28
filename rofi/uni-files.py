#!/bin/python3

from rofi import Rofi
import os
import subprocess

current_desktop = subprocess.getoutput("wmctrl -d | grep '*' | cut -d ' ' -f1")
desktops_with_dolphin = subprocess.getoutput("wmctrl -l | grep Dolphin | awk '{print $2}' ORS=' '").split()

path = "~/Uni/Semester 1 Modules/"

def valid_dirs(dir: str) -> bool:
    return dir.split('.').__len__() < 2

def main():
    # start rofi instance:
    r = Rofi()

    # get directories
    raw_options: list[str] = os.listdir(os.path.expanduser(path))
    filtered_options = list(filter(valid_dirs, raw_options))
    
    options = []
    for option in filtered_options:
        # options.append(option.replace(" ","\\ "))
        options.append(option.replace(" "," "))

    options_lower: list = []

    for i in range(len(options)):
        options_lower.append(filtered_options[i].lower())

    # options = ['Downloads', 'Home', 'Videos', 'Saves', 'Documents', 'Anicli']
    index, key = r.select('', options_lower)
    # print(index,key)
    # open folder
    if -1 in [index, key]:
        return

    escape_path = path.replace(" ", "\\ ")
    full_path = os.path.expanduser(path)
    # full_path = os.path.expanduser(escape_path)
    
    os.system(f"nohup dolphin --new-window \"{full_path}{options[index]}\" &")
    # print(f"nohup dolphin --new-window {full_path}{options[index]} &")



if __name__ == "__main__":
    main()

