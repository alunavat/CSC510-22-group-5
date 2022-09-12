"""Util module contains miscellaneous methods."""

import math


def percentile(items, value):
    """Find item at value percentile of items."""
    if not value:
        value = 0.5
    value = math.floor((value * len(items)) + 0.5)
    return items[max(0, min(value, len(items) - 1))]

def rnd(X, Places):
    if not Places:
        Places = 2
    mult = pow(10, Places)
    return math.floor(X*mult +0.5)/mult

def coerce(s):
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            try:
                return s
            except:
                print("Type conversion Failed")

def csv(file_name,function):
    file = open(file_name, 'r')
    lines = file.readlines()
    for i in (lines):
        t={}
        for j in (i.strip().split(",")):
            t[1+len(t)] = coerce(j)
        function(t)
        
def fun(s1):
    if s1:
        return True
    if not s1:
        return False
    return s1

