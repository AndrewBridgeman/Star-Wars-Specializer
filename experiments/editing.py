from cutting_class import Cutting
from assembly_class import Assembly

from single_scene import SingleScene
from alternate_scene import AlternateScene

import yaml


class Editing:
    def __init__(self, filename):
        #convert data here
        self._text = yaml.safe_load(open(filename, 'r'))
        self._video_list = []

    def cut(self):
        num_count = 1

        original_video = (self._text['scene-times']['original'])
        special_video = (self._text['scene-times']['special'])

        cutter_original = Cutting(original_video)
        cutter_special = Cutting(special_video)

        # cutter_original.add_span('00:00:00', '00:00:10', 'temp{}.mp4', 1)
        # cutter_original.add_span('00:00:10', '00:00:24', 'temp{}.mp4', 2)
        # cutter_original.add_span('00:00:24', '0', 'temp{}.mp4', 3)
        # cutter_original.write()

        previous_time = '00:00:00'

        for i in range(len(self._text['scene-times']['scenes'])):

            current = self._text['scene-times']['scenes'][i]
            if 'alternatives' in (current.keys()):
                current = current['alternatives']
                new_scene = AlternateScene(current[0]['start'], current[0]['end'], 'alternative', \
                                            current[1]['start'], current[1]['end'])

                file_name_original = 'x{}original.mp4'
                file_name_special = 'x{}special.mp4'

                if new_scene.get_start_time() == 'continue':
                    new_scene.set_start_time(previous_time)

                if current[0]['start'] != 'none':
                    new_scene.set_cut(file_name_original.format(num_count))
                    cutter_original.add_span(new_scene.get_start_time(), new_scene.get_end_time(),
                                             file_name_original, num_count)
                    num_count = num_count + 1
                    previous_time = new_scene.get_end_time()


                new_scene.set_special_cut(file_name_special.format(num_count))
                cutter_special.add_span(new_scene.get_special_start_time(), new_scene.get_special_end_time(),\
                                        file_name_special, num_count)

                num_count = num_count + 1

                self._video_list.append(new_scene)

            # single scene case
            else:
                new_scene = SingleScene(current['start'], current['end'], 'single')
                file_name = 'x{}single.mp4'

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

        movie = Assembly(self._text['scene-times']['to'])

        instructions_count = 0

        for i in range(len(self._video_list)):

            if self._video_list[i].get_type() == 'single':
                movie.append(self._video_list[i].get_cut())

            elif self._video_list[i].get_type() == 'alternative':
                if temp_instructions['scene-include']['a' + str(instructions_count + 1)]:
                    movie.append(self._video_list[i].get_special_cut())

                else:
                    if self._video_list[i].get_cut() != '':
                        movie.append(self._video_list[i].get_cut())

                instructions_count = instructions_count + 1

        print(movie.give_inputs())

        movie.write()
