test1 = 'files/test1.mp4'
test2 = 'files/test2.mp4'

from simple_ffmpeg_cutting import Ffmpeg_cutting

def cut(filename):
    file = open(filename)
    lines = file.readlines()
    if 'start\n' in lines:
        lines.remove('start\n')

    if 'start' in lines:
        lines.remove('start')

    if 'end\n' in lines:
        lines.remove('end\n')

    if 'end' in lines:
        lines.remove('end')

    cutter = Ffmpeg_cutting(test1, 'out{}.mp4')

    cutter.add_span('00:00:00', lines[0].strip())

    for i in range(len(lines)):
        if i == len(lines) - 1:
            cutter.add_span(lines[i].strip(), '0')
        else:
            cutter.add_span(lines[i].strip(), lines[i+1].strip())
    cutter.write()

if __name__ == '__main__':
    # everything()
    cut('ffmpeg-cutting-input.txt')
