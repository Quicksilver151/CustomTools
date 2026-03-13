#!/bin/bash
for i in *."$1"; do
  out="${i%.$1}.$2"
  echo ffmpeg -i "$i" ${@:3} "$out"
  ffmpeg -i "$i" ${@:3} "$out"
done

