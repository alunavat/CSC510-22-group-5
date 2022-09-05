"""CLI module is to provide the command line interface for the application."""

import sys
from test.csv_lua_test import CsvLuaTests
import unittest

HELP = """
python cli.py

-h, --help = Show this help message and exit
-t ALL = Run all tests
   sym = Run test for sym
   num = Run test for num
   bignum = Run test for holding certain count in num
   the = Run test for settings
"""

if __name__ == "__main__":
    tests = ["sym", "num", "bignum", "the", "ALL"]
    ARG_COUNT = len(sys.argv)
    if ARG_COUNT == 1:
        print(HELP)
    i = 1
    while i < ARG_COUNT:
        ARGUMENT = sys.argv[i]
        if ARGUMENT.startswith("-"):
            if ARGUMENT in ("-h", "--help"):
                print(HELP)
            elif ARGUMENT == "-t":
                if i + 1 >= ARG_COUNT:
                    print("Incomplete -t argument", file=sys.stderr)
                    sys.exit(1)
                EXTRA_ARGUMENT = sys.argv[i + 1]
                if EXTRA_ARGUMENT == "ALL":
                    CsvLuaTests().test_sym()
                    CsvLuaTests().test_num()
                    CsvLuaTests().test_settings()
                    CsvLuaTests().test_num_holds_nums()
                elif EXTRA_ARGUMENT == "sym":
                    CsvLuaTests().test_sym()
                elif EXTRA_ARGUMENT == "num":
                    CsvLuaTests().test_num()
                elif EXTRA_ARGUMENT == "the":
                    CsvLuaTests().test_settings()
                elif EXTRA_ARGUMENT == "bignum":
                    CsvLuaTests().test_num_holds_nums()
                else:
                    print(
                        f"Argument {EXTRA_ARGUMENT} not found", file=sys.stderr
                    )
                i += 1
        else:
            print(f"Bad command argument {sys.argv[i]}", file=sys.stderr)
            sys.exit(1)
        i += 1
