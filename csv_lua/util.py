"""Util module contains miscellaneous methods."""

import math


def percentile(items, value):
    """Find item at value percentile of items."""
    if not value:
        value = 0.5
    value = math.floor((value * len(items)) + 0.5)
    return items[max(0, min(value, len(items) - 1))]

def coerce(s):
    pass

def fun(s1):
    pass