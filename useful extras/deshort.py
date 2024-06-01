#!/bin/python3
import pyperclip as pc
import os
import time

def main():
    window_title = os.popen("xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_NAME").readline().split("=")[1].strip().strip('"')
    if not window_title.count("YouTube"):
        return

    os.system("xdotool key y y")

    time.sleep(0.25)

    shorts_link   : str   =  pc.paste()
    
    if not bool(shorts_link.count("shorts/")):
        return

    watch_link : str = shorts_link.replace("shorts/","watch?v=")

    pc.copy(watch_link)

    time.sleep(0.25)

    os.system("xdotool key ctrl+l ctrl+shift+v")

    time.sleep(0.25)
    
    os.system("xdotool key Return")


if __name__ == "__main__":
    time.sleep(0.5)
    main()
