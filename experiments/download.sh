#!/bin/sh

repo_slug=AndrewBridgeman/Custom-Movie-Maker
repo_url=https://raw.githubusercontent.com/$repo_slug
branch_url=$repo_url/media

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

grab http://www.engr.colostate.edu/me/facil/dynamics/files/drop.avi

for i in 1 2 3 A B C; do
    grab "$branch_url/$i.mp4"
done
