#!/bin/python3

#inits
import os, sys
from pathlib import Path
import fileinput

#constants
wallpaper_location = os.path.expanduser("~/.cache/wal/wal")
discord_theme_css_path = os.path.expanduser("~/.config/BetterDiscord/themes/Translucence.theme.css")

# get wallaper
text_file = open(wallpaper_location,"r").read()
wallpaper_name = Path(text_file).name


# get discord link for wallpaper
text_file = open(discord_theme_css_path, "r")
text = text_file.read()
links = text.split("===")[1].split("\n")

wallpaper_link = ""
for link in links:
    link_file_name = link.split("/")[-1]
    
    if link_file_name == wallpaper_name:
        wallpaper_link = link
        



# set wallpaper


with open(discord_theme_css_path,'r',encoding='utf-8') as file:
    data = file.readlines()



for i,line in enumerate(data):
    if data[i].split("--app-bg:").__len__() > 1:
        data[i] = "	--app-bg: url("+wallpaper_link+");\n"
        


with open(discord_theme_css_path, 'w', encoding='utf-8') as file:
    file.writelines(data)
