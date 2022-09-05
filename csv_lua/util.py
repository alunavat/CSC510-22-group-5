import math

class Helpers:

    def per(self, t, p):
        if not p:
            p=0.5
        p = math.floor((p * len(t)) + 0.5)
        return t[max(1, min(p, len(t)))]

    def oo (self, t):
        print(t)
        return t