"""CLI module is to provide the command line interface for the application."""

from pathlib import Path
import sys
from test.csv_lua_test import CsvLuaTests
from csv_lua import settings

HELP = f"""
python cli.py

-h, --help               = Show this help message and exit
-e, --eg        all      = Run all tests
                sym      = Run test for sym
                num      = Run test for num
                bignum   = Run test for holding certain count in num
                the      = Run test for settings
-d, --dump               = On test failure, exit with stack dump
-n, --nums      NUM      = Set NUM as number of nums to keep
-s, --seed      SEED     = Set SEED as random number seed
-S, --seperator SEP      = Set SEP as field seperator
-f, --file      FILEPATH = Read data from FILEPATH

Defaults are:
     --help: {settings.settings["show_help"]}
       --eg: {settings.settings["eg"]}
     --dump: {settings.settings["dump"]}
     --nums: {settings.settings["nums"]}
     --seed: {settings.settings["seed"]}
--seperator: {settings.settings["seperator"]}
     --file: {settings.settings["file"]}
"""

TESTS = {
    "sym": "test_sym",
    "num": "test_num",
    "bignum": "test_num_holds_nums",
    "the": "test_settings",
    "all": "all",
    "nothing": None,
}


def parse_settings(argv, argc):
    """
    parse_settings parses arguments passed and sets settings
    """
    for idx in range(0, argc, 2):
        try:
            if not argv[idx].startswith("-"):
                raise Exception(f"Bad argument {argv[idx]}")
            if argv[idx] in ("-e", "--eg"):
                if idx + 1 < argc and argv[idx + 1] in TESTS:
                    settings.settings["eg"] = TESTS[argv[idx + 1]]
                    idx += 2
                else:
                    idx += 1
            elif argv[idx] in ("-d", "--dump"):
                if idx + 1 < argc and argv[idx + 1].lower() in (
                    "true",
                    "false",
                ):
                    settings.settings["dump"] = argv[idx + 1].lower() == "true"
                    idx += 2
                else:
                    settings.settings["dump"] = True
                    idx += 1
            elif argv[idx] in ("-f", "--file"):
                if (
                    idx + 1 < argc
                    and Path.exists(argv[idx + 1])
                    and Path.is_file(argv[idx + 1])
                ):
                    settings.settings["file"] = argv[idx + 1]
                    idx += 2
                else:
                    raise Exception(
                        "Filepath is either missing, does not exist or"
                        " is not a file for -f/--file"
                    )
            elif argv[idx] in ("-n", "--nums"):
                if idx + 1 < argc and int(argv[idx + 1]):
                    settings.settings["nums"] = int(argv[idx + 1])
                    idx += 2
                else:
                    raise Exception(
                        "Nums either missing or is not a number for -n/--nums"
                    )
            elif argv[idx] in ("-s", "--seed"):
                if idx + 1 < argc and int(argv[idx + 1]):
                    settings.update_seed(int(argv[idx + 1]))
                    idx += 2
                else:
                    raise Exception(
                        "Seed either missing or is not a number for -s/--seed"
                    )
            elif argv[idx] in ("-S", "--seperator"):
                if idx + 1 < argc:
                    settings.settings["seperator"] = argv[idx + 1]
                    idx += 2
                else:
                    raise Exception("Seperator missing for -S/--seperator")
            else:
                raise Exception(f"Unknown argument {argv[idx]}")
        except Exception as exc:  # pylint: disable=broad-except
            print(exc.args[0])
            print_help()


def print_help():
    """print_help prints help message and exits"""
    print(HELP)
    sys.exit()


if __name__ == "__main__":
    ARG_COUNT = len(sys.argv)
    if (ARG_COUNT == 1) or ("-h" in sys.argv) or ("--help" in sys.argv):
        print_help()
    parse_settings(sys.argv[1:], ARG_COUNT - 1)
    if settings.settings["eg"] == "all":
        CsvLuaTests(settings.settings["dump"]).run_all_tests()
    elif settings.settings["eg"] == "nothing":
        sys.exit()
    else:
        CsvLuaTests(settings.settings["dump"]).run_test(
            settings.settings["eg"]
        )
