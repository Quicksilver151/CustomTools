#!/bin/bash
for i in *.$1;
do
  echo ffmpeg -i "$i" ${@:3} "$(basename $i .$1).$2";
  ffmpeg -i "$i" ${@:3} "$(basename $i .$1).$2";
done

