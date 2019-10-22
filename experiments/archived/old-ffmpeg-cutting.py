from simple_ffmpeg_cutting import Ffmpeg_cutting
import yaml

def cut(filename):
    stream = open(filename, 'r')
    text = yaml.safe_load(stream)
    input = text['file-path']
    print(text)
    a_name = text['output-name-alternate']
    name = text['output-name-not-alternate']
    cutter = Ffmpeg_cutting(input)

    if len(text['scene-times']) != 0:
        if vid_type(text['scene-times']['scene1']) == 'a':
            if text['scene-times']['scene1'][0] == 'start':
                cutter.add_span('00:00:00', text['scene-times']['scene1'][1], a_name)
            if text['scene-times']['scene1'][1] == 'end':
                cutter.add_span('00:00:00', text['scene-times']['scene1'][0], name)
            else:
                cutter.add_span('00:00:00', text['scene-times']['scene1'][0], name)
                cutter.add_span(text['scene-times']['scene1'][0], text['scene-times']['scene1'][1], a_name)
        else:
            cutter.add_span('00:00:00', text['scene-times']['scene1'], name)

        for i in range(2, len(text['scene-times'])+1):
            if vid_type(text['scene-times']['scene' + str(i)]) == 'd':
                if vid_type(text['scene-times']['scene' + str(i-1)]) == 'd':
                    cutter.add_span(text['scene-times']['scene' + str(i-1)], text['scene-times']['scene' + str(i)], name)
                else:
                    cutter.add_span(text['scene-times']['scene' + str(i-1)][1], text['scene-times']['scene' + str(i)], name)

            if vid_type(text['scene-times']['scene' + str(i)]) == 'a':
                if vid_type(text['scene-times']['scene' + str(i-1)]) == 'd':
                    cutter.add_span(text['scene-times']['scene' + str(i-1)], text['scene-times']['scene' + str(i)][0], name)
                else:
                    cutter.add_span(text['scene-times']['scene' + str(i-1)][1], text['scene-times']['scene' + str(i)][0], name)

                if text['scene-times']['scene' + str(i)][1] == 'end':
                    break

                cutter.add_span(text['scene-times']['scene' + str(i)][0], text['scene-times']['scene' + str(i)][1], a_name)

        last_num = len(text['scene-times'])

        if vid_type(text['scene-times']['scene' + str(last_num)]) == 'd':
            cutter.add_span(text['scene-times']['scene' + str(last_num)], '0', name)

        else:
            if text['scene-times']['scene' + str(last_num)][1] == 'end':
                cutter.add_span(text['scene-times']['scene' + str(last_num)][0], '0', a_name)
            else:
                cutter.add_span(text['scene-times']['scene' + str(last_num)][1], '0', name)


    cutter.write()


def vid_type(input):
    if len(input) == 2:
        return 'a'
    else:
        return 'd'

if __name__ == '__main__':
    # everything()
    cut('cutting-instructions.yaml')
