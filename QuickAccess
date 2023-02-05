#!/bin/python3

from rofi import Rofi
import os
import subprocess

current_desktop = subprocess.getoutput("wmctrl -d | grep '*' | cut -d ' ' -f1")
desktops_with_dolphin = subprocess.getoutput("wmctrl -l | grep Dolphin | awk '{print $2}' ORS=' '").split()


def main():
    # start rofi instance:
    r = Rofi()

    # get directories
    raw_options: list[str] = os.listdir(os.path.expanduser("~/QuickAccess"))
    options = []
    
    for option in raw_options:
        options.append(option.replace(" ","\ "))

    print(options)
    options_lower: list = []

    for i in range(len(options)):
        options_lower.append(raw_options[i].lower())

    # options = ['Downloads', 'Home', 'Videos', 'Saves', 'Documents', 'Anicli']
    index, key = r.select('', options_lower)
    print(index,key)
    # open folder
    if key == -1:
        return
    
    os.system("nohup dolphin --new-window ~/QuickAccess/"+str(options[index])+" &")


if __name__ == "__main__":
    main()

