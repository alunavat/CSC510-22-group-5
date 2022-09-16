"""Engine module is for the test engine"""

from copy import deepcopy
import sys
import traceback

from csv_lua import settings


class TestSuite:
    """TestSuite can be subclassed to create test suites"""

    TEST_SEPERATOR = "=" * 40

    def __init__(self, dump):
        self.dump = dump
        self.crashed = False
        self.failed = False

    def run_all_tests(self):
        """
        run_all_tests runs all the tests (methods that start with `test_`)
        """
        test_names = [name for name in dir(self) if name.startswith("test_")]
        for test_name in test_names:
            self.run_test(test_name)

    def run_test(self, test_name):
        """
        run_test runs a single test and crashes if dump is False, else
        prints exception
        """
        print(TestSuite.TEST_SEPERATOR)
        if test_name not in dir(self):
            print(f"Test {test_name} does not exist!")
            print(TestSuite.TEST_SEPERATOR)
            return
        print(f"Running {test_name} test")
        self.crashed = False
        self.failed = False

        defaults = deepcopy(settings.settings)

        try:
            method = getattr(self, test_name)
            print(method.__doc__)
            method()
        except:  # pylint: disable=bare-except
            if self.dump:
                traceback.print_exc(file=sys.stdout)
                self.failed = True
                sys.exit(1)
            self.crashed = True
        finally:
            if self.crashed:
                print("CRASHED")
            elif self.failed:
                print("FAILED")
            else:
                print("PASSED")
            print(TestSuite.TEST_SEPERATOR)
            settings.settings = deepcopy(defaults)

    def assert_equal(self, arg1, arg2, message=""):
        """assert_equal checks whether arg1 and arg2 are equal"""
        if arg1 != arg2:
            if message:
                print(message)
            self.failed = True

    def assert_true(self, condition, message=""):
        """assert_true checks whether condition is truthy"""
        if not condition:
            if message:
                print(message)
            self.failed = True
