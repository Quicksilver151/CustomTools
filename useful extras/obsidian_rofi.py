#!/bin/python3
from rofi import Rofi
import json
import platformdirs
import os


def main():
    r = Rofi()

    options: list[str] = get_vaults()
    
    l_options = []
    
    for option in options:
        l_options.append(option.lower())

    index, key = r.select("Vault: ", l_options)
    
    name = options[index]
    cmd = f"obsidian \"obsidian://open?vault={name}\""
    
    if -1 in [key, index]:
        return
    os.system(cmd)
    # print(index, name, cmd, key)



def get_vaults() -> list:
    obsidian_json_path = platformdirs.user_config_dir("obsidian") + "/obsidian.json"
    obsidian_json_file = open(obsidian_json_path,"r")
    json_data:dict = json.loads(obsidian_json_file.read())
    
    vault_list: list[str] = []

    for vault_id in json_data["vaults"].keys():
        is_open = json_data["vaults"][vault_id].__contains__("open")
        
        vault_name: str = json_data["vaults"][vault_id]["path"].split("/")[-1]
        if is_open:
            vault_list.reverse()
            vault_list.append(vault_name)
            vault_list.reverse()
        else:
            vault_list.append(vault_name)


    return vault_list




if __name__ == "__main__":
    main()
