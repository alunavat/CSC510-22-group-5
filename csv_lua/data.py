"""data module deals with dataframe classes"""

from typing import Callable
from csv_lua.cols import Cols
from csv_lua.row import Row
from csv_lua.util import csv


class Data:
    """Data class represents a dataframe"""

    cols: Cols
    """Column summaries of the dataframe"""
    rows: list[Row]
    """All the rows of the dataframe"""

    def __init__(self, src: str | list[str]) -> None:
        """Create a dataframe from a csv or list of column names"""
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            csv(src, self.add)
        else:
            if src:
                for _, row in src:
                    self.add(row)

    def add(self, row: str) -> None:
        """add adds a row to dataframe"""
        if not self.cols:
            self.cols = Cols(row)
        else:
            row = Row(row)
            self.rows.append(row)
            for todo in (self.cols.independent_cols, self.cols.dependent_cols):
                for col in todo:
                    col.add(row.cells[col.col_pos])

    def stats(
        self, places: int, cols_to_show: list[str], method: Callable
    ) -> dict:
        """stats show statistics for the dataframe"""
        if not places:
            places = 2
        if not cols_to_show:
            cols_to_show = self.cols.dependent_cols
        data = {}
        for col in cols_to_show:
            value = method(col)
            data[col.name] = (
                round(value, places) if isinstance(value, float) else value
            )
        return data
