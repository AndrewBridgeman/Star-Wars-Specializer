from cutting_class import Cutting
from assembly_class import Assembly

from file_reader import FileReader

import yaml


class Editing:
    def __init__(self, filename):
        self._text = yaml.safe_load(open(filename, 'r'))
        data = FileReader(self._text)
        data.read()
        self._original_instructions = data.get_original_instructions()
        self._special_instructions = data.get_special_instructions()
        self._video_list = data.get_video_list()

    def cut(self, original, special, clip_dir):
        cutter_original = Cutting(original, clip_dir)
        cutter_special = Cutting(special, clip_dir)

        # cutter_original.add_span('00:00:00', '00:00:10', 'temp{}.mp4', 1)
        # cutter_original.add_span('00:00:10', '00:00:24', 'temp{}.mp4', 2)
        # cutter_original.add_span('00:00:24', '0', 'temp{}.mp4', 3)
        # cutter_original.write()

        for i in self._original_instructions:
            cutter_original.add_span(i[0], i[1], i[2], i[3])

        for i in self._special_instructions:
            cutter_special.add_span(i[0], i[1], i[2], i[3])

        cutter_original.write()
        cutter_special.write()

    def assemble(self, clip_dir, output):
        temp_instructions = yaml.safe_load(open('temp-assembly-instructions.yaml', 'r'))

        movie = Assembly(output)

        instructions_count = 0

        for i in range(len(self._video_list)):

            if self._video_list[i].get_type() == 'single':
                movie.append(clip_dir + '/' + self._video_list[i].get_cut())

            elif self._video_list[i].get_type() == 'alternative':
                if temp_instructions['scene-include']['a' + str(instructions_count + 1)]:
                    movie.append(clip_dir + '/' + self._video_list[i].get_special_cut())

                else:
                    if self._video_list[i].get_cut() != '':
                        movie.append(clip_dir + '/' + self._video_list[i].get_cut())

                instructions_count = instructions_count + 1

        print(movie.give_inputs())

        movie.write()
