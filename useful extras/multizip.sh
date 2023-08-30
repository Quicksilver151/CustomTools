#!/bin/sh
for i in */; do zip -r "${i%/}.$1" "$i"; done
