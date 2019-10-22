class alternate_scene:

    def __init__ (self, start_time, end_time, path):
        if start_time == 'start':
            self._start_time = '00:00:00'
        else:
            self._start_time = start_time

        if end_time == 'end':
            self._end_time = '0'
        else:
            self._end_time = end_time

        self._path = path

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def set_start_time(self, new_time):
        self._start_time = new_time

    def set_end_time(self, new_time):
        self._start_time = new_time

    def get_path(self):
        return self._path