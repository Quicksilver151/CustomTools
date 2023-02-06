#!/bin/python3
from os import system
import re
import sys
import subprocess
output = str(subprocess.check_output(["xprop", "-root", "_NET_CURRENT_DESKTOP"]))
outputint =  int(re.findall(r'\b\d+\b', output)[0])

def main(args:list):
    if args.__len__() == 1:
        system("echo " +str(outputint + 1))
        return
    system("wmctrl -s "+str(int(args[1])+outputint))

if __name__ == "__main__":
    main(sys.argv)
