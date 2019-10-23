class single_scene:

    def __init__(self, start_time, end_time):
        if start_time == 'start':
            self._start_time = '00:00:00'
        else:
            self._start_time = start_time

        if end_time == 'end':
            self._end_time = '0'
        else:
            self._end_time = end_time

        self._cut = ''

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def set_start_time(self, new_time):
        self._start_time = new_time

    def set_end_time(self, new_time):
        self._start_time = new_time

    def get_cut(self):
        return self._cut

    def set_cut(self, cut):
        self._cut = cut
