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

def select(filename):
    end = False
    movie = Ffmpeg('final.mp4')

    file = open(filename)
    lines = file.readlines()
    if lines[0].strip().rsplit()[0] == '(start)':
        if lines[0].strip().rsplit()[1] != 'no':
            movie.append('files/' + lines[0].strip().rsplit()[1] + '.mp4')
        lines.remove(lines[0])

    if lines[len(lines)-1].strip().rsplit()[0] == '(end)':
        if lines[len(lines)-1].strip().rsplit()[1] != 'no':
            end = True
            end_video = lines[len(lines)-1].strip().rsplit()[1]
        lines.remove(lines[len(lines)-1])

    for count in range(len(lines)+1):
        video_list.append('out' + str(count+1) + '.mp4')

    for i in range(len(lines)):
        movie.append(video_list[i])
        if lines[i].strip() != 'no':
            movie.append('files/' + lines[i].strip() + '.mp4')

    movie.append(video_list[len(video_list)-1])

    if end == True:
        movie.append('files/' + end_video + '.mp4')

    movie.write()

if __name__ == '__main__':
    # everything()
    select('ffmpeg-assembly-input.txt')
