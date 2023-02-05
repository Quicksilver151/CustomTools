#!/bin/python3
import pyperclip as pc
content   : str   =  pc.paste()
lines     : list  =  content.split("\n")
paragraph : list  =  []

for line in lines:
    paragraph.append(line.split(" "))

redacted : str = ""
for line in paragraph:
    for word in line:
        redacted += "||"+word+" ||"
    redacted += "\n"
pc.copy(redacted)
