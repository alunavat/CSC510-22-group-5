from sys import flags
import numpy

class sym:
  def __init__(self) -> None:
    self.n = 0
    self.at = 0
    self.name = ""
    self._has = dict()

  def add(self,v) -> None:
    if v!='?':
      self.n = self.n+1
      if v not in self._has:
        self._has[v] = 1
      else:
        self._has[v] += 1

  def mid(self) -> str:
    sortedDict = sorted(self._has, key=self._has.get, reverse=True)
    return sortedDict[0]

  def main(self) -> float:
    return self._has['a']