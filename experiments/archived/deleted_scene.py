class deleted_scene:

    def __init__(self, cut, start, end):
        if start == 'start':
            self._start_time = '00:00:00'
        else:
            self._start_time = start

        if end == 'end':
            self._end_time = '0'
        else:
            self._end_time = end

        self._cut = cut

    def get_cut(self):
        return self._cut

    def set_cut(self, cut):
        self._cut = cut

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time
