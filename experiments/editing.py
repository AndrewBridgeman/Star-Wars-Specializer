from cutting_class import cutting
from assembly_class import assembly

from single_scene import single_scene
from deleted_scene import deleted_scene
from alternate_scene import alternate_scene

import yaml


class editing:
    def __init__(self, filename):
        self._text = yaml.safe_load(open(filename, 'r'))
        self._video_list = []

    def cut(self):
        num_count = 1

        master_video = (self._text['scene-times']['from'])
        cutter = cutting(master_video)
        previous_time = '00:00:00'

        for i in range(len(self._text['scene-times']['scenes'])):

            current = self._text['scene-times']['scenes'][i]

            if 'deleted' in (current.keys()):
                new_scene = deleted_scene(current['from'])
                self._video_list.append(new_scene)

            else:
                if 'alternate' in (current.keys()):
                    new_scene = alternate_scene(current['start'], current['end'], current['from'])
                    file_name = self._text['scene-times']['alternate-name']

                else:
                    new_scene = single_scene(current['start'], current['end'])
                    file_name = self._text['scene-times']['single-scene-name']

                if new_scene.get_start_time() == 'continue':
                    new_scene.set_start_time(previous_time)

                previous_time = new_scene.get_end_time()

                new_scene.set_path(file_name.format(num_count))
                num_count = num_count + 1

                self._video_list.append(new_scene)
                cutter.add_span(new_scene.get_start_time(), new_scene.get_end_time(), file_name)

        cutter.write()

    def assemble(self):
        temp_instructions = yaml.safe_load(open('temp-assembly-instructions.yaml', 'r'))

        movie = assembly('final.mp4')

        instructions_count = 0

        for i in range(len(self._video_list)):

            if isinstance(self._video_list[i], single_scene):
                movie.append(self._video_list[i].get_path())

            elif isinstance(self._video_list[i], alternate_scene):
                if temp_instructions['scene-include']['alternate' + str(instructions_count + 1)]:
                    movie.append(self._video_list[i].get_new_path())

                else:
                    movie.append(self._video_list[i].get_original_path())

                instructions_count = instructions_count + 1

            elif isinstance(self._video_list[i], deleted_scene):
                if temp_instructions['scene-include']['deleted' + str(instructions_count + 1)]:
                    movie.append(self._video_list[i].get_path())

                instructions_count = instructions_count + 1

        print(movie.give_inputs())

        movie.write()
