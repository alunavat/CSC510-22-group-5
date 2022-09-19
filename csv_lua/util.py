"""Util module contains miscellaneous methods."""

import math
from typing import Callable
from csv_lua.settings import settings


def percentile(items: list, value: float | None):
    """percentile finds item at value percentile of items"""
    if not value:
        value = 0.5
    value = math.floor((value * len(items)) + 0.5)
    return items[max(0, min(value, len(items) - 1))]


def coerce(value: str):
    """coerce converts value to float if possible"""
    try:
        return float(value)
    except ValueError:
        try:
            return int(value)
        except ValueError:
            return value


def csv(file_name: str, function: Callable):
    """csv method opens a csv file and runs function on every row"""
    with open(file_name, encoding="utf8") as file:
        for line in file.readlines():
            function(
                list(map(coerce, line.strip().split(settings["seperator"])))
            )
