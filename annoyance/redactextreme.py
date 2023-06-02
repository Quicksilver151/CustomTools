#!/bin/python3
import pyperclip as pc
content   : str   =  pc.paste()
raw_paragraph     : list  =  content.split("\n")
paragraphs : list  =  []

for paragraph in raw_paragraph:
    words = []
    for word in paragraph.split(" "):
        letters = []
        for letter in word:
            letters.append(letter)
        words.append(letters)
    paragraphs.append(words)

redacted : str = ""

for paragraph in paragraphs:
    for words in paragraph:
        for letter in words:
            redacted +="||"+letter+"||"
        redacted += "|| ||"
    redacted += "\n"

pc.copy(redacted)
