#!/usr/bin/env bash

second-monitor-setup
systemctl --user start kdeconnect
xinput set-prop "ASUP1411:00 093A:200B Touchpad" "libinput Middle Emulation Enabled" 0
dbus-update-activation-environment --systemd DISPLAY XAUTHORITY

systemctl --user import-environment XDG_CURRENT_DESKTOP DISPLAY XDG_SESSION_TYPE
dbus-update-activation-environment --systemd XDG_CURRENT_DESKTOP DISPLAY XDG_SESSION_TYPE
systemctl --user restart xdg-desktop-portal

# bash -c 'setsid -f nohup /nix/store/05qq2jsjrkl2plqb1paqrabs94dri12m-xdg-desktop-portal-1.20.4/libexec/xdg-desktop-portal -r >/dev/null 2>&1'
systemctl --user import-environment QT_QPA_PLATFORMTHEME
dbus-update-activation-environment --systemd QT_QPA_PLATFORMTHEME
pkill -f xdg-desktop-portal-kde
setsid -f start-portal >/dev/null 2>&1
setsid -f notify-listen >/dev/null 2>&1

nohup fcitx5 &
nohup lxqt-policykit-agent &
picom -bcf --corner-radius 4 --vsync --config ~/Documents/picom.conf
~/.config/polybar/docky/launch.sh
~/.config/conky/startup.sh
setup-dev
setup-late
