from cutting_class import cutting
from single_scene import single_scene
from deleted_scene import deleted_scene
from alternate_scene import alternate_scene

import yaml


def cut(filename):
    stream = open(filename, 'r')
    text = yaml.safe_load(stream)

    video_list = []

    master_video = (text['scene-times']['from'])
    cutter = cutting(master_video)
    previous_time = '00:00:00'

    for i in range(len(text['scene-times']['scenes'])):

        current = text['scene-times']['scenes'][i]

        if 'deleted' in (current.keys()):
            new_scene = deleted_scene(current['from'])
            video_list.append(new_scene)

        else:
            if 'alternate' in (current.keys()):
                new_scene = alternate_scene(current['start'], current['end'], current['from'])
                file_name = text['scene-times']['alternate-name']

            else:
                new_scene = single_scene(current['start'], current['end'])
                video_list.append(new_scene)
                file_name = text['scene-times']['single-scene-name']

            if new_scene.get_start_time() == 'continue':
                new_scene.set_start_time(previous_time)

            previous_time = new_scene.get_end_time()

            video_list.append(new_scene)
            cutter.add_span(new_scene.get_start_time(), new_scene.get_end_time(), file_name)

    cutter.write()


if __name__ == '__main__':
    # everything()
    cut('cutting-instructions.yaml')
