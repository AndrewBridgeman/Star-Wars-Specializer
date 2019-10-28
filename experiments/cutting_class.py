import subprocess
import sys


class cutting:

    def __init__(self, vid_input):
        self._input = vid_input
        self._outputs = []

    def add_span(self, time1, time2, name, num):
        if time1 != 'none' and time2!= 'none':
            self._outputs.append((time1, time2, name, num))

    def _fill_template(self, name, n):
        return name.format(n)

    def write(self):
        for i in range(len(self._outputs)):
            command = self._build_command(self._outputs[i])
            completed = subprocess.run(command, capture_output=True)
            if completed.returncode != 0:
                sys.stderr.write('Error from ffmpeg:\n')
                sys.stderr.write(completed.stderr.decode())
                sys.stderr.write('\n')
                sys.exit(2)

    def _build_command(self, output):
        command = ['ffmpeg', '-y']
        command.append('-t')
        command.append(output[1])
        command.extend(['-i', self._input])
        command.append('-ss')
        command.append(output[0])
        command.append(self._fill_template(output[2], output[3]))
        return command
