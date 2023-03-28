#!/bin/python3
 
#inits
import os, sys
from pathlib import Path
import fileinput

# config paths
colors_location = os.path.expanduser("~/.cache/wal/colors-putty.reg") #colors in numerical values
godot_config_path = os.path.expanduser("~/.config/godot/editor_settings-4.tres")
BG_OFFSET = 20

# get color list
text_file = open(colors_location,"r")
text = text_file.read()
lines = text.split("\n")

# grabs 2 main colors
background_colors = lines[5].split(";")[0].lstrip("\"Colour2=\"").rstrip("\"  ").split(",")
foreground_colors = lines[11].split(";")[0].lstrip("\"Colour8=\"").rstrip("\"  ").split(",")

bg_color_line = "interface/theme/base_color = Color("
fg_color_line = "interface/theme/accent_color = Color("
for i in range(3):
    bg_color = (int(background_colors[i])+BG_OFFSET)/256
    fg_color = (int(foreground_colors[i])+BG_OFFSET)/256
    
    bg_color_line += (str(bg_color)+", ")
    fg_color_line += (str(fg_color)+", ")

bg_color_line += "1)\n"
fg_color_line += "1)\n"    


#print(bg_color_line)
#print(fg_color_line)


with open(godot_config_path,'r',encoding='utf-8') as file:
    data = file.readlines()



for i,line in enumerate(data):
    if data[i].split("interface/theme/base_color").__len__() > 1: # for this prefix
        data[i] = bg_color_line
    
    if data[i].split("interface/theme/accent_color").__len__() > 1: # for this prefix
        data[i] = fg_color_line


with open(godot_config_path, 'w', encoding='utf-8') as file:
    file.writelines(data)

