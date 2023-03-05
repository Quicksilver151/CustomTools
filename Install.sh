#!/bin/env sh

QAPath=~/QuickAccess
CustomPath=~/CustomPath


mkdir $QAPath
mkdir $CustomPath

ln -sr ./annoyance/oddcap.py $CustomPath/oddcap
ln -sr ./annoyance/rancap.py $CustomPath/rancap
ln -sr ./annoyance/redactinator.py $CustomPath/redactinator
ln -sr ./fun/randsamplinggrid.py $CustomPath/randsamplinggrid
ln -sr ./useful\ extras/ffconv.py $CustomPath/ffconv
ln -sr ./wal/polywal.sh $CustomPath/polywal
ln -sr ./wal/set_discord_bg_link_wal.py $CustomPath/set_discord_bg_link_wal
ln -sr ./wal/set_firefox_tabliss_wal.sh $CustomPath/set_firefox_tabliss_wal


