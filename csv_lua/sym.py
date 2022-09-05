"""Sym module deals with symbolic columns of a CSV"""

import math


class Sym:
    """
    Sym summarizes a stream of symbols.
    """

    def __init__(self, size=0, col_pos=0, name="") -> None:
        self.size = size
        self.col_pos = col_pos
        self.name = name
        self._has = {}

    def add(self, symbol) -> None:
        """Add method adds a symbol to stream."""
        if symbol != "?":
            self.size += 1
            self._has[symbol] = self._has.get(symbol, 0) + 1

    def mid(self) -> str:
        """Mid method calculates the middle of the symbol stream."""
        most = -1
        mode = None
        for key, count in self._has.items():
            if count > most:
                mode = key
                most = count
        return mode

    def div(self) -> float:
        """Div method calculates the diversity of the symbol stream."""
        entropy = 0
        for _, count in self._has.items():
            if count > 0:
                probability = count / self.size
                entropy -= probability * math.log2(probability)
        return entropy
