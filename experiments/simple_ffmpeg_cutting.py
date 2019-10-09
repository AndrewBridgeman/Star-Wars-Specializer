import subprocess
import sys

class Ffmpeg_cutting:
    """Calls ffmpeg to append video files."""

    def __init__(self, output):
        self._output = output
        self._inputs = []
        self._time1 = ''
        self._time2 = ''

    def append(self, input):
        self._inputs.append(input)

    def extend(self, inputs):
        self._inputs.extend(inputs)

    def add_times(self, time1, time2):
        self._time1 = time1
        self._time2 = time2

    def write(self):
        command = self._build_command()
        completed = subprocess.run(command,
                capture_output = True)
        if completed.returncode != 0:
            sys.stderr.write('Error from ffmpeg:\n')
            sys.stderr.write(completed.stderr.decode())
            sys.stderr.write('\n')
            sys.exit(2)

    def _build_command(self):
        command = ['ffmpeg', '-y']
        command.append('-t')
        command.append(self._time2)
        command.extend(['-i', self._inputs[0]])
        command.append('-ss')
        command.append(self._time1)
        command.append(self._output)
        print(command)
        return command