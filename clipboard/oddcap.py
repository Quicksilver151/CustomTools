#!/bin/python3

import pyperclip as pc

content = pc.paste()

oddcap = ""

for i in range(content.__len__()):
	if i/2.0 == int(i/2):
		oddcap += content[i].upper()
	else:
		oddcap += content[i].lower()

pc.copy(oddcap)
