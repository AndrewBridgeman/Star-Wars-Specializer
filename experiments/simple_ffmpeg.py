import subprocess
import sys

class Ffmpeg:
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
        for input in self._inputs:
            command.extend(['-i', input])
        command.extend(['-filter_complex', self._concat()])
        command.append(self._output)
        return command

