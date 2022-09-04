import sys
from test.csv_lua_test import csv_lua_tests
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
    argc = len(sys.argv)
    if argc == 1:
        print(HELP)
    i = 1
    while i < argc:
        arg = sys.argv[i]
        if arg.startswith('-'):
            if arg == '-h' or arg == '--help':
                print(HELP)
            elif arg == '-t':
                if i + 1 >= argc:
                    print("Incomplete -t argument", file=sys.stderr)
                    exit(1)
                extra_arg = sys.argv[i + 1]
                if extra_arg == 'ALL':
                    unittest.main(module=csv_lua_tests)
                elif extra_arg == 'sym':
                    csv_lua_tests().test_sym()
                elif extra_arg == 'num':
                    csv_lua_tests().test_num()
                elif extra_arg == 'the':
                    csv_lua_tests().test_settings()
                elif extra_arg == 'bignum':
                    csv_lua_tests().test_num_holds_nums()
                else:
                    print(f"Argument {extra_arg} not found", file=sys.stderr)
                i += 1
        else:
            print(f"Bad command argument {sys.argv[i]}", file=sys.stderr)
            exit(1)
        i += 1