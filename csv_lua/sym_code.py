import math
class sym:
  def __init__(self) -> None:
    self.n = 0
    self.at = 0
    self.name = ""
    self._has = dict()

  def add(self,v) -> None:
    if v != '?':
      self.n = self.n+1
      self._has[v] = self._has.get(v,0) + 1

  def mid(self) -> str:
    most = -1
    mode = None
    for k,v in self._has.items():
      if v > most:
        mode = k
        most = v
    return mode
  
  def div(self) -> float:
    e = 0
    for k,v in self._has.items():
      if v > 0:
        p = v/self.n
        e -= p*math.log2(p) 
    return e 