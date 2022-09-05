"""csv_lua_test module contains all tests for csv_lua."""

import unittest

from csv_lua.sym import Sym
from csv_lua.num import Num
from csv_lua import settings


class CsvLuaTests(unittest.TestCase):
    """
    CsvLuaTests contains tests for Sym, Num, The, and BigNum
    """

    def test_sym(self):
        """test_sym covers eg.sym test"""
        items = ["a", "a", "a", "a", "b", "b", "c"]
        sym = Sym()
        for item in items:
            sym.add(item)
        mode = sym.mid()
        entropy = sym.div()
        print("\nSym() Test")
        print("-------------------------")
        print({"mid": mode, "div": entropy})
        self.assertEqual(mode, "a")
        self.assertTrue(1.37 <= entropy <= 1.38)

    def test_settings(self):
        """test_settings covers eg.the test"""
        print("\nThe() Test")
        print("-------------------------")
        print(settings.settings)
        self.assertEqual(1, 1)

    def test_num(self):
        """test_num covers eg.num test"""
        num = Num()
        for i in range(1, 100):
            num.add(i)
        mid = num.mid()
        div = num.div()
        print("\nNum() Test")
        print("-------------------------")
        print({"mid": mid, "div": div})
        self.assertTrue(50 <= mid <= 52)
        self.assertTrue(30.5 <= div <= 32)

    def test_num_holds_nums(self):
        """test_num_holds_nums covers eg.bignum test"""
        num = Num()
        for i in range(1, 1000):
            num.add(i, nums=32)
        print("\nBigNum() Test")
        print("-------------------------")
        print(num.nums())
        self.assertEqual(32, len(num.nums()))


if __name__ == "__main__":
    unittest.main()
