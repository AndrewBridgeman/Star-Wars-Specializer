import subprocess
import sys


class Assembly:

    def __init__(self, output):
        self._output = output
        self._inputs = []

    def append(self, vid_input):
        self._inputs.append(vid_input)

    def give_inputs(self):
        return self._inputs

    def extend(self, inputs):
        self._inputs.extend(inputs)

    def write(self):
        # Change this line to try different methods
        command = self._concat_protocol()
        completed = subprocess.run(command, capture_output=True)
        if completed.returncode != 0:
            sys.stderr.write('Error from ffmpeg:\n')
            sys.stderr.write(completed.stderr.decode())
            sys.stderr.write('\n')
            sys.exit(2)

    def _concat(self):
        return 'concat = n ={}'.format(len(self._inputs))

    def _build_command(self):
        command = ['ffmpeg', '-y']
        for inputs in self._inputs:
            command.extend(['-i', inputs])
        command.extend(['-filter_complex', self._concat()])
        command.append(self._output)
        return command

    def _concat_demuxer(self):
        file = open("temp.txt", "w")
        for i in range(len(self._inputs)):
            file.write('file ' + "'" + self._inputs[i] + "'" + '\n')
        command = ['ffmpeg']
        command.extend(['-y', '-f', 'concat', '-safe', '0'])
        command.extend(['-i', 'temp.txt','-c', 'copy'])
        command.append(self._output)
        return command

    def _concat_protocol(self):
        command = ['ffmpeg', '-y', '-i']
        concat_list = 'concat:'
        for i in range(len(self._inputs)):
            if i == len(self._inputs)-1:
                concat_list = concat_list + self._inputs[i]
            else:
                concat_list = concat_list + self._inputs[i] + '|'
        command.append(concat_list)
        command.extend(['-c', 'copy', '-bsf:a', 'aac_adtstoasc'])
        command.append(self._output)
        return command
