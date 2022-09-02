import random
class Num:
    '''
    Num summarizes a stream of numbers.
    '''

    def __init__(self):
        self.n = 0
        self.at = 0
        self.name = ""
        self._has = dict()
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True
        self.w = 1

    def nums(self):
        if not self.isSorted:
            self.isSorted = True
            return sorted(self._has)

    def add(self, v, pos):
        # if v~="?" then
        #     self.n = self.n + 1
        #     self.lo = math.min(v, self.lo)
        #     self.hi = math.max(v, self.hi)
        if v!="?":
            self.n=self.n+1
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

    def div(self, a):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1))/2.58

    def mid(self):
        return per(self.nums(), 0.5)
