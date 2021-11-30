import random
import sys


class macro():
    def __init__(self):
        self._ismacro = 1
        seedValue = random.randrange(sys.maxsize)
        random.seed(seedValue)
        self._time = random.randint(1, 100)

    @property
    def time(self):
        return self._time

    @property
    def ismacro(self):
        return self._ismacro

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return f"{self._time}m"
