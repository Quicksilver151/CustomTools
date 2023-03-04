# How to install

- Install all the dependencies mentioned under **requirements** in [README.md](../README.md)





## Discord:

- Download and install Betterdiscord

- Upload your wallpapers to some throwaway discord server for storage

- Locate your themes folder (probably in `~/.config/BetterDiscord/themes/`)

- Make sure you have `    --app-bg: url(.....` present in your theme file (that is the part this script will modify)

- Open the `set_discord_bg_link_wal.py` file and set your css file location

- Create a commented region in your theme.css and place the image links within two (===) bars

```css
/**
links should go within the (===)
===
https://cdn.discordapp.com/attachments/[server_id]/[channel_id]/[picture1 name].png
https://cdn.discordapp.com/attachments/[server_id]/[channel_id]/[picture2 name].png
etc...
===
**/
```

- Run pywal and set it to a background that you've provided a link for in your theme

- Run `set_discord_bg_link_wal.py` with python3

- Discord will update the background automatically
