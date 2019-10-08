test1 = 'files/test1.mp4'
test2 = 'files/test2.mp4'

from simple_ffmpeg_cutting import Ffmpeg_cutting

timestamp = '00:00:15'

movie = Ffmpeg_cutting('out.mp4')
movie.append(test1)
movie.add_times('00:00:00', timestamp)
movie.write()

movie = Ffmpeg_cutting('out2.mp4')
movie.append(test1)
movie.add_times(timestamp, '0')
movie.write()
