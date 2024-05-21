#!/bin/sh

contains() {
    case "$1" in
            (*"$2"*) true ;;
            (*) false ;;
    esac
}
pid=$(pidof "mpv")






mpv_workspaces=$(wmctrl -lp |grep " - mpv" | cut -d " " -f3)
mpv_process="$(wmctrl -lp |grep " - mpv" | cut -d ' ' --fields=3,4)"
current_workspace=$(wmctrl -d | grep '*' | cut -d ' ' -f1)

# echo $mpv_workspaces | while read line;
# do
#     if [ 0 -eq $current_workspace];
#     then
#         echo ok
#     fi;
#
# done;

IFS='
'
get_workspace_mpv_pid(){
    for item in $mpv_process
        do
        if contains "$item" "$current_workspace ";
        then
            echo "$item" | cut -d " " -f2;
        fi
    done
}

current_workspace_mpv_pid="$(get_workspace_mpv_pid)"
if [ "$current_workspace" -eq 2 ];
then
    if [ "$current_workspace_mpv_pid" ];
    then
        # wmctrl -x -R gl.mpv # GRAB FOCUS
        if [ $# -eq 0 ];
        then
            echo "{ \"command\": [\"loadfile\", \"$1\", \"append\"] }" | socat - "/tmp/mpv-socket"
            # echo playlist-next | socat - "/tmp/mpv-socket"
        else
            for video in "$@";
            do
                echo "{ \"command\": [\"loadfile\", \"$video\", \"append\"] }" | socat - "/tmp/mpv-socket"
                # echo '{ "command": ["playlist-next"] }' | socat - "/tmp/mpv-socket"
            done
        fi
    else
        /bin/mpv --input-ipc-server=/tmp/mpv-socket --player-operation-mode=pseudo-gui "$@"
        # mpv --input-ipc-server=/tmp/mpv-socket --player-operation-mode=pseudo-gui --vo=x11 "$@"
    fi
else
    /bin/mpv --player-operation-mode=pseudo-gui "$@"
    # mpv --player-operation-mode=pseudo-gui --vo=x11 "$@"
fi

