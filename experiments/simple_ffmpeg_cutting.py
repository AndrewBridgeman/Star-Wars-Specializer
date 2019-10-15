import subprocess
import sys

class Ffmpeg_cutting:
    """Calls ffmpeg to append video files."""

    def __init__(self, input, template):
        self._input = input
        self._template = template
        self._outputs = []

    def add_span(self, time1, time2):
        self._outputs.append((time1, time2))

    def _fill_template(self, n):
        return self._template.format(n)

    def write(self):
        ## TODO: loop over self._outputs
        for i in range(len(self._outputs)):
            command = self._build_command(self._outputs[i], i)
            completed = subprocess.run(command,
                    capture_output = True)
            if completed.returncode != 0:
                sys.stderr.write('Error from ffmpeg:\n')
                sys.stderr.write(completed.stderr.decode())
                sys.stderr.write('\n')
                sys.exit(2)

    def _build_command(self, output, num):
        command = ['ffmpeg', '-y']
        command.append('-t')
        command.append(output[1])
        command.extend(['-i', self._input])
        command.append('-ss')
        command.append(output[0])
        command.append(self._fill_template(num+1))
        return command
