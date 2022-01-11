import random
import sys


class small_cell():
    def __init__(self):
        self._is_macro_cell = 0
        seedValue = random.randrange(sys.maxsize)
        random.seed(seedValue)
        self._time_in_mili = random.randint(1, 300)
        self._time = self._time_in_mili * 1E-3

    @property
    def time(self):
        return self._time

    @property
    def is_macro_cell(self):
        return self._is_macro_cell

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return f"{self._time_in_mili}"
