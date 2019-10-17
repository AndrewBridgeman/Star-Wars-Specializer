from simple_ffmpeg_cutting import Ffmpeg_cutting
import yaml

def cut(filename):
    stream = open(filename, 'r')
    text = yaml.safe_load(stream)
    input = text['file-path']
    output = text['output-name']

    cutter = Ffmpeg_cutting(input, output + '{}.mp4')

    if len(text['scene-times']) != 0:
        count = 0
        if text['scene-times']['scene1'] != 'start':
            cutter.add_span('00:00:00', text['scene-times']['scene1'])
        else:
            cutter.add_span('00:00:00', text['scene-times']['scene2'])
            count = 1

        for i in range(count, len(text['scene-times'])):
            if i == len(text['scene-times']) - 1:
                cutter.add_span(text['scene-times']['scene' + str(i+1)], '0')
            else:
                if text['scene-times']['scene' + str(i+2)] == 'end':
                    cutter.add_span(text['scene-times']['scene' + str(i+1)], '0')
                    break
                else:
                    cutter.add_span(text['scene-times']['scene' + str(i+1)], text['scene-times']['scene' + str(i+2)])

    cutter.write()

if __name__ == '__main__':
    # everything()
    cut('cutting-instructions.yaml')