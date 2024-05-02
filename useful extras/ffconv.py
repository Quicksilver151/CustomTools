#!/usr/bin/python3

import glob
import os



# path = input("Path")
if __name__ == "__main__":
    
    path = os.getcwd()+"/"
    ext_from = input("Extension from: ")
    ext_to = input("Extension to  : ")
    args = ""
    args = input("args:\n")


    if args:
        args += " "

    pattern_path = path+"*."+ext_from

    total = ""

    # if extension same....
    name_add = ""
    if ext_from == ext_to:
        name_add = "ffconv/"
        os.system("mkdir ffconv")
        


    for file_from in glob.glob(pattern_path):
        file_from = base = os.path.basename(file_from)
        file_to = os.path.splitext(file_from)[0]+"."+ext_to
        
        total += (f"ffmpeg -i \"{file_from}\" {args}\"{name_add}{file_to}\" && ")

    size = len(total)
    total = total[:size - 4]
    # print(total)
    # pyperclip.copy(total)

    os.system(total)

