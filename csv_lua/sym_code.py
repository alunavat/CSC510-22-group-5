class sym:
  def __init__(self) -> None:
    self.n = 0
    self.at = 0
    self.name = ""
    self._has = dict()

  def add(self,v) -> None:
    if v is not '?':
      self.n = self.n+1
      self._has[v] = self._has.get(v,0) + 1

  def mid(self) -> str:
    sortedDict = sorted(self._has, key=self._has.get, reverse=True)
    return sortedDict[0]