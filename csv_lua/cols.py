"""Cols module is for dealing with columns"""

from csv_lua.num import Num
from csv_lua.sym import Sym


class Cols:  # pylint: disable=too-few-public-methods
    """
    Columns' holds summaries of columns. Columns
    are created once, then they may appear in multiple slots
    """

    def __init__(self, names) -> None:
        self.names = names
        self.all = []
        self.klass = None
        self.independent_cols = []  # Same as x
        self.dependent_cols = []  # Same as y
        self.parse_names()

    def parse_names(self) -> None:
        """Summarise columns"""
        for pos, name in enumerate(self.names):
            if name[0].isupper():
                col_type = Num
            else:
                col_type = Sym
            self.all.append((col_type)(pos, name))
            col = self.all[-1]
            if name[-1] != ":":
                if name[-1] in "+-":
                    self.dependent_cols.append(col)
                else:
                    self.independent_cols.append(col)
                if name[-1] == "!":
                    self.klass = col
