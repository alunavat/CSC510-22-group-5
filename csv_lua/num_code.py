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
        self._has = dict()
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True
        self.w = 1
        self.help = helper.Helpers()

    def nums(self):
        if not self.isSorted:
            self.isSorted = True
        return sorted(self._has)

    def add(self, v, nums = 512):
        settingObj = settings.settings()
        settingObj.settings_dict_set("nums",nums)
        setting_dict = settingObj.settings_dict_get()
        if v!="?":
            self.n=self.n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < setting_dict["nums"]:
                pos = 1+ len(self._has)
            elif random.uniform(0, 1) < setting_dict["nums"]/self.n:
                pos = random.randint(1, len(self._has))
            else:
                pos = None
            if pos != None:
                self.isSorted = False
                try:
                    self._has[pos] = int(v)
                except:
                    self._has[pos] = None

    def div(self):
        a = self.nums()
        return (self.help.per(t= a, p= 0.9) - self.help.per(t= a, p= 0.1))/2.58

    def mid(self):
        return self.help.per(t= self.nums(), p= 0.5)
