
class Num:
    def __init__(self):
        pass

    def new(self):
        pass

    def nums(self):
        pass

    def add(self, v, pos):
        # if v~="?" then
        #     self.n = self.n + 1
        #     self.lo = math.min(v, self.lo)
        #     self.hi = math.max(v, self.hi)
        if v!="?":
            self.n=n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < the[nums]:
                pos = 1+ len(self._has)
            elif random.uniform(0, 1) < the[nums]/self.n:
                pos = random.randint(1, len(self._has))
            if pos:
                self.isSorted = False
                try:
                    self._has[pos] = int(v)
                except:
                    self._has[pos] = None
        pass

    def div(self, a):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1))/2.58
        pass

    def mid(self):
        return per(self.nums(), 0.5)
        pass