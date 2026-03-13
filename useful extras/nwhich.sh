#!/bin/bash

wpath=$(which $@)

if [ -z $wpath ];
then
  echo "'$@' command not found";
  exit 0
fi

get_type() {
  file -i "$1"| cut -d ';' -f 1| cut -d ":" -f 2 | cut -d "/" -f 1
  
}

get_linked_file() {

  ftype=$(get_type $1)

  if [ "$ftype" = " inode" ];
  then
    get_linked_file "$(realpath "$1")"
  else
    echo "$1"
  fi
}


fpath=$(get_linked_file "$wpath")
ftype=$(get_type "$fpath")

if [ $ftype = "text" ];
then
  nvim "$fpath"
else
  echo "$fpath" is not a text file
fi

