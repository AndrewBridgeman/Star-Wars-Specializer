#!/usr/bin/env pipenv run python

from simple_ffmpeg import Ffmpeg

import yaml

video_list = []

def select(filename):
    movie = Ffmpeg('final.mp4')

    stream = open(filename, 'r')
    text = yaml.safe_load(stream)

    for i in range(len(text['scene-paths-deleted'])+1):
        video_list.append(text['output-name'] + str(i+1) + '.mp4')

    for i in range(len(text['scene-paths-deleted'])):
        movie.append(video_list[i])
        if text['scene-include-deleted']['scene' + str(i+1)] == True:
            movie.append(text['scene-paths-deleted']['scene' + str(i+1)])

    movie.append(video_list[len(video_list)-1])

    print(movie.give_inputs())
    movie.write()


if __name__ == '__main__':
    # everything()
    select('cutting-instructions.yaml')
