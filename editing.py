from cutting_class import Cutting
from assembly_class import Assembly

from file_reader import FileReader

import yaml
import sys
import subprocess
import re

class Editing:
    def __init__(self, filename):
        self._text = yaml.safe_load(open(filename, 'r'))
        data = FileReader(self._text)
        data.read()
        self._original_instructions = data.get_original_instructions()
        self._special_instructions = data.get_special_instructions()
        self._video_list = data.get_video_list()
        self._names = data.get_names()

    def init_cut(self, file, time, directory, original_name, special_name):
        cutter = Cutting(file, directory)
        cutter.add_span('00:00:00.000', time, original_name)
        cutter.add_span(time, '0', special_name)
        cutter.write()

    def cut(self, original, special, clip_dir, res):
        cutter_original = Cutting(original, clip_dir)
        cutter_special = Cutting(special, clip_dir)

        for i in self._original_instructions:
            cutter_original.add_span(i[0], i[1], i[2], i[3])

        for i in self._special_instructions:
            cutter_special.add_span(i[0], i[1], i[2], i[3])

        cutter_original.write(res)
        cutter_special.write(res)

    def get_res(self, original):
        command = self.build_command(original)
        completed = subprocess.run(command, capture_output=True)
        if completed.returncode != 0:
            sys.stderr.write('Error from ffmpeg:\n')
            sys.stderr.write(completed.stderr.decode())
            sys.stderr.write('\n')
            sys.exit(2)
        res = subprocess.check_output(command)
        res = str(res)
        temp = re.findall(r'\d+', res)
        res = list(map(int, temp))
        return res

    def build_command(self, original):
        command = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height']
        command.extend(['-of', 'csv=s=x:p=0'])
        command.append(original)
        return command

    def assemble(self, clip_dir, choices, output):
        movie = Assembly(output)

        instructions_count = 0

        for i in range(len(self._video_list)):

            if self._video_list[i].get_type() == 'single':
                movie.append(clip_dir + '/' + self._video_list[i].get_cut())

            elif self._video_list[i].get_type() == 'alternative':
                if choices[instructions_count]:
                    movie.append(clip_dir + '/' + self._video_list[i].get_special_cut())

                else:
                    if self._video_list[i].get_cut() != '':
                        movie.append(clip_dir + '/' + self._video_list[i].get_cut())

                instructions_count = instructions_count + 1

        print(movie.give_inputs())

        movie.write()

    def get_names(self):
        return self._names
