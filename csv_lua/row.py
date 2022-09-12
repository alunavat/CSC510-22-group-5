"""Row module deals with new rows being read from csv and store them in particular format"""

class Row:
    """
    Row adds data read from csv in a particular format
    """

    def __init__(self, rowData) -> None:
        self.cells = rowData
        self.cooked = rowData.copy()
        self.isEvaled = False
