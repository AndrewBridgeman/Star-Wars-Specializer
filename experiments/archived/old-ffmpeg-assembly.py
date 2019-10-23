#!/usr/bin/env pipenv run python

from assembly_class import assembly

import yaml
import os.path
from os import path

video_list = []

def select(filename):
    movie = assembly('final.mp4')

    stream = open(filename, 'r')
    text = yaml.safe_load(stream)

    num_alternate = 0
    start = False
    end = False
    j = 0

    #Get number of alternate scenes
    for i in range(len(text['scene-times'])):
        if vid_type(text['scene-times']['scene' + str(i+1)]) == 'a':
            num_alternate = num_alternate + 1

    if text['scene-times']['scene1'][0] == 'start':
        start = True
        num_alternate = num_alternate - 1

    if text['scene-times']['scene' + str(len(text['scene-times']))][1] == 'end':
        end = True
        num_alternate = num_alternate -1


    #Get video files
    for i in range(1, len(text['scene-paths']) + num_alternate + 2):
        if(path.exists(text['output-name-not-alternate'].format(i))):
            video_list.append((text['output-name-not-alternate'].format(i), 'not-a'))
        else:
            video_list.append((text['output-name-alternate'].format(i), 'a'))


    vid_count = 0

    if start:
        if text['scene-include']['scene1']:
            movie.append(text['scene-paths']['scene1'])
        else:
            movie.append(video_list[0][0])
        j = 1
        vid_count = 1

    #Concat files

    for i in range(j, len(text['scene-paths'])):

        if video_list[vid_count][1] == 'not-a':
            movie.append(video_list[vid_count][0])

        if vid_type(text['scene-times']['scene' + str(i+1)]) == 'd' and \
                text['scene-include']['scene' + str(i+1)] == True:
            movie.append(text['scene-paths']['scene' + str(i+1)])

        vid_count = vid_count+1

        if video_list[vid_count][1] == 'a':
            if vid_type(text['scene-times']['scene' + str(i+1)]) == 'a' and \
                    text['scene-include']['scene' + str(i+1)] == True:
                movie.append(text['scene-paths']['scene' + str(i+1)])
            else:
                movie.append(video_list[vid_count][0])
            vid_count = vid_count + 1

    if end == False:
        movie.append(video_list[len(video_list)-1][0])

    print(movie.give_inputs())
    movie.write()



def vid_type(input):
    if len(input) == 2:
        return 'a'
    else:
        return 'd'

if __name__ == '__main__':
    # everything()
    select('instructions.yaml')