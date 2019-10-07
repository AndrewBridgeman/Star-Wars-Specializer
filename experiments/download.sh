#!/bin/sh

cd "$(dirname "$0")/files"

grab () {
    if [ $# = 2 ]; then
        dst=$1; shift
    else
        dst=$(basename "$1")
    fi

    url=$1

    curl "$url" --output "$dst"
}

master_url=https://github.com/AndrewBridgeman/Custom-Movie-Maker/blob/master

grab http://www.engr.colostate.edu/me/facil/dynamics/files/drop.avi

for i in 1 2 3 A B C; do
    grab "$i.mp4" "$master_url/Testing%20API's/$i.mp4?raw=true"
done
