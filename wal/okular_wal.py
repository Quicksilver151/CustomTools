#!/bin/python3
 
#inits
import os, sys
from pathlib import Path
import fileinput

# config paths
colors_location = os.path.expanduser("~/.cache/wal/colors-putty.reg") #colors in numerical values
okular_config_path = os.path.expanduser("~/.config/okularpartrc")


# get color list
text_file = open(colors_location,"r")
text = text_file.read()
lines = text.split("\n")

# grabs 2 main colors
background_colors = lines[6].split(";")[0].split("\"=\"")[1].rstrip("\"  ").split(",")
foreground_colors = lines[3].split(";")[0].split("\"=\"")[1].rstrip("\"  ").split(",")

bg_color_line = "RecolorBackground="
fg_color_line = "RecolorForeground="
bgbg_color_line = "BackgroundColor="

bg_color = background_colors[0]
fg_color = foreground_colors[0]
bgbg_color = str(max(0,int(background_colors[0])-2))

bg_color_line += str(bg_color)
fg_color_line += str(fg_color)
bgbg_color_line += str(bgbg_color)

for i in range(2):
    i+=1
    bg_color = background_colors[i]
    fg_color = foreground_colors[i]
    bgbg_color = str(max(0,int(background_colors[i])-2))
    
    bg_color_line += (","+str(bg_color))
    fg_color_line += (","+str(fg_color))
    bgbg_color_line += (","+str(bgbg_color))
    

fg_color_line += "\n"
bg_color_line += "\n"
bgbg_color_line += "\n"
#print(bg_color_line)
#print(fg_color_line)

with open(okular_config_path,'r',encoding='utf-8') as file:
    data = file.readlines()



for i,line in enumerate(data):
    if data[i].split("RecolorBackground=").__len__() > 1: # for this prefix
        data[i] = bg_color_line
    
    if data[i].split("RecolorForeground=").__len__() > 1: # for this prefix
        data[i] = fg_color_line
        
    if data[i].split("BackgroundColor=").__len__() > 1: # for this prefix
        data[i] = bgbg_color_line
        break

#print(foreground_colors)
with open(okular_config_path, 'w', encoding='utf-8') as file:
    file.writelines(data)

