from alternate_scene import AlternateScene
from single_scene import SingleScene


class FileReader:
    def __init__(self, text):
        self._text = text
        self._original_instructions = []
        self._special_instructions = []
        self._video_list = []
        self._names = []

    def read(self):
        num_count = 1

        previous_time = '00:00:00.000'

        for i in range(len(self._text['scenes'])):

            current = self._text['scenes'][i]

            if 'alternatives' in (current.keys()):
                current = current['alternatives']
                self._names.append(current[0]['name'])
                new_scene = AlternateScene(current[1]['start'], current[1]['end'], 'alternative', \
                                           current[2]['start'], current[2]['end'])

                file_name_original = 'x{}original.ts'
                file_name_special = 'x{}special.ts'

                if new_scene.get_start_time() == 'continue':
                    new_scene.set_start_time(previous_time)

                if current[1]['start'] != 'none':
                    new_scene.set_cut(file_name_original.format(num_count))
                    self._original_instructions.append((new_scene.get_start_time(), new_scene.get_end_time(), \
                                                        file_name_original, num_count))
                    num_count = num_count + 1
                    previous_time = new_scene.get_end_time()

                new_scene.set_special_cut(file_name_special.format(num_count))
                self._special_instructions.append((new_scene.get_special_start_time(), new_scene.get_special_end_time(), \
                                                   file_name_special, num_count))

                num_count = num_count + 1

                self._video_list.append(new_scene)

            # single scene case
            else:
                new_scene = SingleScene(current['start'], current['end'], 'single')
                file_name = 'x{}single.ts'

                if new_scene.get_start_time() == 'continue':
                    new_scene.set_start_time(previous_time)

                new_scene.set_cut(file_name.format(num_count))

                self._video_list.append(new_scene)
                self._original_instructions.append((new_scene.get_start_time(), new_scene.get_end_time(), file_name, num_count))
                previous_time = new_scene.get_end_time()

                num_count = num_count + 1

    def get_original_instructions(self):
        return self._original_instructions

    def get_special_instructions(self):
        return self._special_instructions

    def get_video_list(self):
        return self._video_list

    def get_names(self):
        return self._names
