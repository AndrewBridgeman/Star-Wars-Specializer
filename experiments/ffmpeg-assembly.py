#!/usr/bin/env pipenv run python

import ffmpeg

def main(filename):
    clip1 = ffmpeg.input('files/1.mp4')
    clip2 = ffmpeg.input('files/2.mp4')
    clip3 = ffmpeg.input('files/3.mp4')

    clipA = ffmpeg.input('files/A.mp4')
    clipB = ffmpeg.input('files/B.mp4')

    new_clip = clip1
    count = 0
    file = open(filename)
    line = file.read()

    while count < 2:
        if "A" in line and count == 0:
            new_clip = ffmpeg.concat(new_clip, clipA)
        if "B" in line and count == 1:
            new_clip = ffmpeg.concat(new_clip, clipB)
        if count == 0:
            new_clip = ffmpeg.concat(new_clip, clip2)
        if count == 1:
            new_clip = ffmpeg.concat(new_clip, clip3)
        count = count + 1


    new_clip = new_clip.output("asdf.mp4")
    ffmpeg.run(new_clip)

if __name__ == '__main__':
    main('ffmpeg-assembly-input.txt')
