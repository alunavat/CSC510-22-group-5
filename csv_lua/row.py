"""Row module deals with new rows being read from csv and store them in particular format"""


from copy import copy


class Row:  # pylint: disable=too-few-public-methods
    """
    Row holds one record of data
    """

    def __init__(self, row_data) -> None:
        self.cells = row_data
        self.cooked = copy(row_data)
        self.is_evaled = False
