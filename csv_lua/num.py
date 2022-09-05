import random
from csv_lua import settings as settings
from csv_lua import helpers_code as helper
import math

class num:
    '''
    Num summarizes a stream of numbers.
    '''

    def __init__(self):
        self.n = 0
        self.at = 0
        self.name = ""
        self._has = []
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True
        self.w = 1
        self.help = helper.Helpers()

    def nums(self):
        if not self.isSorted:
            self.isSorted = True
            self._has.sort()
        return self._has

    def add(self, v, nums = 512):
        settingObj = settings.settings()
        settingObj.settings_dict_set("nums",nums)
        setting_dict = settingObj.settings_dict_get()
        if v!="?":
            v = int(v)
            self.n=self.n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < setting_dict["nums"]:
                self._has.append(v)
            else:
                pos = random.randint(0, len(self._has) - 1)
                self._has[pos] = v
            self.isSorted = False

    def div(self):
        a = self.nums()
        return (self.help.per(t= a, p= 0.9) - self.help.per(t= a, p= 0.1))/2.58

    def mid(self):
        return self.help.per(t= self.nums(), p= 0.5)
