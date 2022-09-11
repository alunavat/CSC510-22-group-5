"""Columns' holds summaries of columns"""
"""Columns ar created once, then they may appear in multiple slots"""

from csv_lua.num import Num
from csv_lua.sym import Sym

class Cols:

    def __init__(self, names) -> None:
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        self.parse_names()

    def parse_names(self) -> None:
        """Summarise columns"""
        for c,s in self.names:
            if s[0].isupper():
                self.all.append((Num)(c,s))
            else:
                self.all.append((Sym)(c,s))
            col = self.all[-1]
            if not s.endsswith(":"):
                if s.endswith('+') or s.endswith('-') or s.endswith('!'):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if s.endswith('!'):
                    self.klass = col
