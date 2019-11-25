import subprocess
import sys


class Cutting:
    def __init__(self, vid_input, clip_dir):
        self._input = vid_input
        self._outputs = []
        self._dir = clip_dir
        self.sample_rate = '44100'
        self.video_codec = 'libx264'
        self.audio_codec = 'aac'

    def add_span(self, time1, time2, name, num=None):
        if time1 != 'none' and time2 != 'none':
            self._outputs.append((time1, time2, name, num))

    def _fill_template(self, name, n):
        return name.format(n)

    def write(self, res):
        for i in range(len(self._outputs)):
            command = self._build_command(self._outputs[i], res)
            completed = subprocess.run(command, capture_output=True)
            if completed.returncode != 0:
                sys.stderr.write('Error from ffmpeg:\n')
                sys.stderr.write(completed.stderr.decode())
                sys.stderr.write('\n')
                sys.exit(2)

    def _build_command(self, output, res):
        command = ['ffmpeg', '-y']
        command.append('-t')
        command.append(output[1])
        command.extend(['-i', self._input])
        command.append('-ss')
        command.append(output[0])
        command.extend(['-vf', 'scale='+str(res[0])+':'+str(res[1])+':force_original_aspect_ratio=decrease,pad=' + str(res[0]) + ':' + str(res[1]) + ':(ow-iw)/2:(oh-ih)/2'])
        command.extend(['-ar', self.sample_rate, '-c:a', self.audio_codec, '-c:v', self.video_codec, '-bsf:v', 'h264_mp4toannexb', '-f', 'mpegts'])
        if len(output) == 3:
            command.append(self._dir + '/' + output[2])
        else:
            command.append(self._dir + '/' + self._fill_template(output[2], output[3]))
        return command
