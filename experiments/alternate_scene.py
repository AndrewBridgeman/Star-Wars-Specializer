class alternate_scene:

    def __init__(self, original_start_time, original_end_time, special_start_time, special_end_time):
        if original_start_time == 'start':
            self._original_start_time = '00:00:00'
        else:
            self._original_start_time = original_start_time

        if original_end_time == 'end':
            self._original_end_time = '0'
        else:
            self._original_end_time = original_end_time

        if special_start_time == 'start':
            self._special_start_time = '00:00:00'
        else:
            self._special_start_time = special_start_time

        if special_end_time == 'end':
            self._special_end_time = '0'
        else:
            self._special_end_time = special_end_time

        self._original_cut = ''
        self._special_cut = ''

    def get_original_start_time(self):
        return self._original_start_time

    def get_original_end_time(self):
        return self._original_end_time

    def set_original_start_time(self, new_time):
        self._original_start_time = new_time

    def set_original_end_time(self, new_time):
        self._original_end_time = new_time

    def get_special_start_time(self):
        return self._special_start_time

    def get_special_end_time(self):
        return self._special_end_time

    def set_special_start_time(self, new_time):
        self._special_start_time = new_time

    def set_special_end_time(self, new_time):
        self._special_end_time = new_time

    def get_original_cut(self):
        return self._original_cut

    def get_special_cut(self):
        return self._special_cut

    def set_original_cut(self, cut):
        self._original_cut = cut

    def set_special_cut(self, cut):
        self._special_cut = cut
