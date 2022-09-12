"""Columns' holds summaries of columns"""
"""Columns ar created once, then they may appear in multiple slots"""

from csv_lua.num import Num
from csv_lua.sym import Sym

class Cols:

    def __init__(self, names) -> None:
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}
        self.parse_names()

    def parse_names(self) -> None:
        """Summarise columns"""
        for c,s in self.names:
            if s[0].isupper():
                type = Num
            else:
                type = Sym
            self.all[len(self.all) + 1] = (type)(c,s)
            col = (type)(c,s)
            if not s.endsswith(":"):
                if s.endswith('+') or s.endswith('-') or s.endswith('!'):
                    self.y[len(self.y) + 1] = col
                else:
                    self.x[len(self.x) + 1] = col
                if s.endswith('!'):
                    self.klass = col
