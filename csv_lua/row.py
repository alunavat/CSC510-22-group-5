"""Row module deals with new rows being read from csv and store them in particular format"""


from copy import copy


class Row:  # pylint: disable=too-few-public-methods
    """
    Row holds one record of data
    """

    cells: list[int | float | str]
    """One record"""
    cooked: list[int | float | str]
    """Used if we discretize data"""
    is_evaled: bool
    """Whether y-values are evaluated"""

    def __init__(self, row_data: list[int | float | str]) -> None:
        """Create a row"""
        self.cells = row_data
        self.cooked = copy(row_data)
        self.is_evaled = False
