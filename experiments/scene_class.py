class Scene:
    def __init__(self, start_time, end_time, type):
        if start_time == 'start':
            self._start_time = '00:00:00'
        else:
            self._start_time = start_time

        if end_time == 'end':
            self._end_time = '0'
        else:
            self._end_time = end_time

        self._cut = ''
        self._type = type

    def set_start_time(self, time):
        self._start_time = time

    def set_end_time(self, time):
        self._end_time = time

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def set_cut(self, name):
        self._cut = name

    def get_cut(self):
        return self._cut

    def get_type(self):
        return self._type
