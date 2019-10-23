class alternate_scene:

    # _new_path is the alternate scene
    # _original_path is the section of the original video that would be replaced by the alternate scene
    def __init__(self, start_time, end_time, new_path):
        if start_time == 'start':
            self._start_time = '00:00:00'
        else:
            self._start_time = start_time

        if end_time == 'end':
            self._end_time = '0'
        else:
            self._end_time = end_time

        self._original_path = ''
        self._new_path = new_path

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def set_start_time(self, new_time):
        self._start_time = new_time

    def set_end_time(self, new_time):
        self._start_time = new_time

    def get_original_path(self):
        return self._original_path

    def get_new_path(self):
        return self._new_path

    def set_path(self, path):
        self._original_path = path
