import subprocess
import sys

class Ffmpeg_cutting:
    """Calls ffmpeg to append video files."""

    def __init__(self, output):
        self._output = output
        self._inputs = []

    def append(self, input):
        self._inputs.append(input)

    def extend(self, inputs):
        self._inputs.extend(inputs)

    def write(self):
        command = self._build_command()
        completed = subprocess.run(command,
                capture_output = True)
        if completed.returncode != 0:
            sys.stderr.write('Error from ffmpeg:\n')
            sys.stderr.write(completed.stderr.decode())
            sys.stderr.write('\n')
            sys.exit(2)

    def _concat(self):
        count = len(self._inputs) - 1
        return ','.join(count * ['concat'])

    def _build_command(self):
        command = ['ffmpeg', '-y']
        command.append('-ss')
        command.append('00:00:01')
        command.extend(['-i', self._inputs[0]])
        command.append('-to')
        command.append('00:00:10')
        command.append('-c')
        command.append('copy')
        command.append(self._output)
        print(command)
        return command