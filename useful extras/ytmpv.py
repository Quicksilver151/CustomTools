#!/bin/python3
import pyperclip as pc
import os
import time
from pathlib import Path


new_mpv_socket_instance = "mpv --input-ipc-server=/tmp/ytmpv-socket --player-operation-mode=pseudo-gui"
append_mpv_socket_instance1 = r'echo "{ \"command\": [\"loadfile\", \"'
append_mpv_socket_instance2 = r'\", \"append\"] }" | socat - "/tmp/ytmpv-socket"'

def main():
    window_title = os.popen("xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_NAME").readline().split("=")[1].strip().strip('"')
    if not window_title.count("YouTube"):
        return

    os.system("xdotool key y y")

    time.sleep(0.25)

    video_link: str = pc.paste()
    
    socket_file = Path("/tmp/ytmpv-socket")
    if socket_file.exists():
        print("huh")
        os.system(f"{append_mpv_socket_instance1}{video_link}{append_mpv_socket_instance2}")
    else:
        os.system(f"{new_mpv_socket_instance} '{video_link}'")
        os.remove("/tmp/ytmpv-socket")




if __name__ == "__main__":
    time.sleep(0.5)
    main()
