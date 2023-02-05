#!/bin/python3

import pyperclip as pc
from random import randint

content = pc.paste()

rancap = ""
for char in content:
    if randint(0,1):
        rancap += char.upper()
    else:
        rancap += char.lower()

pc.copy(rancap)
