#!/usr/bin/env pipenv run python

from simple_ffmpeg import Ffmpeg

clip1 = 'files/1.mp4'
clip2 = 'files/2.mp4'
clip3 = 'files/3.mp4'
clipA = 'files/A.mp4'
clipB = 'files/B.mp4'
clipC = 'files/C.mp4'
test1 = 'files/test1.mp4'
test2 = 'files/test2.mp4'

video_list = []

def everything():
    movie = Ffmpeg('final.mp4')
    movie.append(clip1)
    movie.append(clipA)
    movie.append(clip2)
    movie.append(clipB)
    movie.append(clip3)
    movie.append(clipC)
    movie.write()

def select(filename):
    movie = Ffmpeg('final.mp4')

    file = open(filename)
    lines = file.readlines()
    for count in range(len(lines)+1):
        video_list.append('out' + str(count+1) + '.mp4')

    for i in range(len(lines)):
        movie.append(video_list[i])
        if lines[i].strip() != 'no':
            movie.append('files/' + lines[i].strip() + '.mp4')

    movie.append(video_list[len(video_list)-1])

    movie.write()

if __name__ == '__main__':
    # everything()
    select('ffmpeg-assembly-input.txt')
