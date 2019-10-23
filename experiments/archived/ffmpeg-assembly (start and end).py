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

import yaml

video_list = []

def select(filename):
    end = False
    movie = Ffmpeg('final.mp4')

    stream = open(filename, 'r')
    text = yaml.safe_load(stream)

    count = 0
    num_cuts = len(text['scene-include-deleted'])

    if text['scene-times-deleted']['scene1'] == 'start':
        num_cuts = num_cuts-1
        count = 1
        if text['scene-include-deleted']['scene1'] == True:
            movie.append(text['scene-paths']['scene1'])

    if text['scene-times-deleted']['scene' + str(len(text['scene-times-deleted']))] == 'end':
        num_cuts = num_cuts - 1
        if text['scene-include-deleted']['scene' + str(len(text['scene-times-deleted']))] == True:
            end = True

    for i in range(num_cuts + 1):
        video_list.append(text['output-name'] + str(i+1) + '.mp4')

    video_list_count = 0

    for i in range(count, num_cuts+count):
        movie.append(video_list[video_list_count])
        video_list_count = video_list_count+1
        if text['scene-include-deleted']['scene' + str(i+1)] == True:
            movie.append(text['scene-paths-deleted']['scene' + str(i+1)])

    movie.append(video_list[len(video_list)-1])

    if end == True:
        movie.append(text['scene-paths']['scene' + str(len(text['scene-times']))])

    print('00:10:05' > '00:11:13')
    print(movie.give_inputs())
    movie.write()


if __name__ == '__main__':
    # everything()
    select('instructions.yaml')