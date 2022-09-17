"""Num module deals with numeric columns in a CSV"""

import random
from csv_lua.settings import settings
from csv_lua.util import percentile


class Num:
    """
    Num summarizes a stream of numbers.
    """

    def __init__(self, col_pos=0, name=""):
        self.size = 0
        self.col_pos = int(col_pos)
        self.name = name
        self._has = []
        self.low = float("inf")
        self.high = float("-inf")
        self.is_sorted = True
        self.w = 1

    def __str__(self):
        return str(
            {
                "at": self.col_pos,
                "hi": self.high,
                "lo": self.low,
                "isSorted": self.is_sorted,
                "n": self.size,
                "name": self.name,
                "w": self.w,
            }
        )

    def nums(self):
        """Nums method returns the numbers within the stream."""
        if not self.is_sorted:
            self.is_sorted = True
            self._has.sort()
        return self._has

    def add(self, value, nums=512):
        """Add method adds a number to the stream."""

        if value != "?":
            value = int(value)
            settings["nums"] = nums
            self.size += 1
            self.low = min(value, self.low)
            self.high = max(value, self.high)
            if len(self._has) < settings["nums"]:
                self._has.append(value)
            elif random.random() < settings["nums"] / self.size:
                pos = random.randint(0, len(self._has) - 1)
                self._has[pos] = value
            self.is_sorted = False

    def div(self):
        """Div method returns the diversity of the stream."""
        items = self.nums()
        return (percentile(items, 0.9) - percentile(items, 0.1)) / 2.56

    def mid(self):
        """Mid method returns the middle of the stream."""
        return percentile(self.nums(), 0.5)
