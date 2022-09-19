"""Cols module is for dealing with columns"""

from csv_lua.num import Num
from csv_lua.sym import Sym


class Cols:  # pylint: disable=too-few-public-methods
    """
    Columns' holds summaries of columns. Columns
    are created once, then they may appear in multiple slots
    """

    names: list[str]
    """The names of the columns"""
    all: list[Num | Sym]
    """All the columns (including skipped ones)"""
    klass: Num | Sym
    """Class of the single dependent column if it exists"""
    independent_cols: list[Num | Sym]
    """Columns that are independent and not skipped"""
    dependent_cols: list[Num | Sym]
    """Columns that are dependent and not skipped"""

    def __init__(self, names: list[str]) -> None:
        """Create a new columns and parse the column names"""
        self.names = names
        self.all = []
        self.klass = None
        self.independent_cols = []  # Same as x
        self.dependent_cols = []  # Same as y
        self.parse_names()

    def parse_names(self) -> None:
        """Parse column names"""
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
