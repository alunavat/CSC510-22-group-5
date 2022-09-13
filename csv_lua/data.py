from csv_lua.cols import Cols
from csv_lua.util import rnd

class Data:
    def __init__(self,src) -> None:
        self.cols = None
        self.rows = dict()
        if isinstance(src, str):
            util.csv(src, temp)
        else:
            temp_list = []
            if src != None:
                temp_list=src
            for c,s in temp_list:
                self.add(s)
            pass

    def temp(self, row):
        self.add(row)

    def push(t,x):
        t[1+len(t)] = x
        return t

    def add(self, xs, row):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = self.push(self.rows, xs if xs.cells else Row(xs))
            for i, todo in [self.cols.x, self.cols.y]:
                for j, col in todo:
                    col.add(row.cells[col.at])
        pass


    def stats(self, places, showCols, fun, t, v):
        showCols, fun = showCols if showCols else self.cols.y, fun if fun else "mid"
        t = {}
        for i, col in showCols:
            v = fun(col)
            v = rnd(v, places) if isinstance(v, float) else v
            t[col.name] = v
        return t
