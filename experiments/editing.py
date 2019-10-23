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

        original_video = (self._text['scene-times']['from-original'])
        special_video = (self._text['scene-times']['from-special'])

        cutter_original = cutting(original_video)
        cutter_special = cutting(special_video)

        previous_time = '00:00:00'

        for i in range(len(self._text['scene-times']['scenes'])):

            current = self._text['scene-times']['scenes'][i]

            if 'deleted' in (current.keys()):
                new_scene = deleted_scene(special_video, current['special-start'], current['special-end'])
                file_name = self._text['scene-times']['deleted-name']
                new_scene.set_cut(file_name.format(num_count))

                self._video_list.append(new_scene)
                cutter_special.add_span(new_scene.get_start_time(), new_scene.get_end_time(), file_name, num_count)
                num_count = num_count + 1

            else:
                if 'alternate' in (current.keys()):
                    new_scene = alternate_scene(current['start'], current['end'], \
                                                current['special-start'], current['special-end'])
                    file_name_original = self._text['scene-times']['original-alternate-name']
                    file_name_special = self._text['scene-times']['special-alternate-name']

                    if new_scene.get_original_start_time() == 'continue':
                        new_scene.set_original_start_time(previous_time)

                    new_scene.set_original_cut(file_name_original.format(num_count))
                    cutter_original.add_span(new_scene.get_original_start_time(), new_scene.get_original_end_time(),
                                             file_name_original, num_count)

                    num_count = num_count + 1

                    new_scene.set_special_cut(file_name_special.format(num_count))
                    cutter_special.add_span(new_scene.get_special_start_time(), new_scene.get_special_end_time(),\
                                            file_name_special, num_count)

                    num_count = num_count + 1

                    previous_time = new_scene.get_original_end_time()

                    self._video_list.append(new_scene)

                # single scene case
                else:
                    new_scene = single_scene(current['start'], current['end'])
                    file_name = self._text['scene-times']['single-scene-name']

                    if new_scene.get_start_time() == 'continue':
                        new_scene.set_start_time(previous_time)

                    new_scene.set_cut(file_name.format(num_count))

                    self._video_list.append(new_scene)
                    cutter_original.add_span(new_scene.get_start_time(), new_scene.get_end_time(), file_name, num_count)
                    previous_time = new_scene.get_end_time()

                    num_count = num_count + 1

        cutter_original.write()
        cutter_special.write()

    def assemble(self):
        temp_instructions = yaml.safe_load(open('temp-assembly-instructions.yaml', 'r'))

        movie = assembly(self._text['scene-times']['to'])

        instructions_count = 0

        for i in range(len(self._video_list)):

            if isinstance(self._video_list[i], single_scene):
                movie.append(self._video_list[i].get_cut())

            elif isinstance(self._video_list[i], alternate_scene):
                if temp_instructions['scene-include']['alternate' + str(instructions_count + 1)]:
                    movie.append(self._video_list[i].get_special_cut())

                else:
                    movie.append(self._video_list[i].get_original_cut())

                instructions_count = instructions_count + 1

            elif isinstance(self._video_list[i], deleted_scene):
                if temp_instructions['scene-include']['deleted' + str(instructions_count + 1)]:
                    movie.append(self._video_list[i].get_cut())

                instructions_count = instructions_count + 1

        print(movie.give_inputs())

        movie.write()
