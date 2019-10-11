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

    movie = Ffmpeg_cutting('out1.mp4')
    movie.append(test1)

    movie.add_times('00:00:00', lines[0].strip())
    movie.write()

    count = 1

    for i in range(len(lines)):
        count = count + 1
        movie = Ffmpeg_cutting('out' + str(count) + '.mp4')
        movie.append(test1)
        if i==len(lines)-1:
            movie.add_times(lines[i].strip(), '0')
        else:
            movie.add_times(lines[i].strip(), lines[i+1].strip())
        movie.write()

if __name__ == '__main__':
    # everything()
    cut('ffmpeg-cutting-input.txt')
