#!/bin/python3
import pyperclip as pc
import os
import time

def main():

    file_url:  str = pc.paste()

    if "file://" not in file_url:
        os.system("notify-send --urgency=low defilecopy 'not a file in clipboard'")
        return;
    
    file_path: str = file_url.replace("file:///", "/")
    pc.copy(file_path)
    os.system("notify-send defilecopy 'changed to filepath'")



if __name__ == "__main__":
    time.sleep(0.5)
    main()
