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

    video_link: str   =  pc.paste()
    

    os.system(f"mpv '{video_link}'")



if __name__ == "__main__":
    time.sleep(0.5)
    main()
