from scene_class import Scene


class AlternateScene(Scene):

    def __init__(self, start_time, end_time, type, special_start_time, special_end_time):

        super().__init__(start_time, end_time, type)

        if special_start_time == 'start':
            self._special_start_time = '00:00:00'
        else:
            self._special_start_time = special_start_time

        if special_end_time == 'end':
            self._special_end_time = '0'
        else:
            self._special_end_time = special_end_time

        self._special_cut = ''

    def get_special_start_time(self):
        return self._special_start_time

    def get_special_end_time(self):
        return self._special_end_time

    def set_special_start_time(self, new_time):
        self._special_start_time = new_time

    def set_special_end_time(self, new_time):
        self._special_end_time = new_time

    def get_special_cut(self):
        return self._special_cut

    def set_special_cut(self, cut):
        self._special_cut = cut
