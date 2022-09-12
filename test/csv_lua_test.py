"""csv_lua_test module contains all tests for csv_lua."""

from csv_lua.sym import Sym
from csv_lua.num import Num
from csv_lua import settings

from csv_lua.test_engine import TestSuite


class CsvLuaTests(TestSuite):
    """
    CsvLuaTests contains tests for Sym, Num, The, and BigNum
    """

    def __init__(self, dump=True):
        super().__init__(dump)

    def test_sym(self):
        """test_sym covers eg.sym test"""
        items = ["a", "a", "a", "a", "b", "b", "c"]
        sym = Sym()
        for item in items:
            sym.add(item)
        mode = sym.mid()
        entropy = sym.div()
        print({"mid": mode, "div": entropy})
        self.assert_equal(mode, "a")
        self.assert_true(1.37 <= entropy <= 1.38)

    def test_settings(self):
        """test_settings covers eg.the test"""
        print(settings.settings)
        self.assert_equal(1, 1)

    def test_num(self):
        """test_num covers eg.num test"""
        num = Num()
        for i in range(1, 100):
            num.add(i)
        mid = num.mid()
        div = num.div()
        print({"mid": mid, "div": div})
        self.assert_true(50 <= mid <= 52)
        self.assert_true(30.5 <= div <= 32)

    def test_num_holds_nums(self):
        """test_num_holds_nums covers eg.bignum test"""
        num = Num()
        for i in range(1, 1000):
            num.add(i, nums=32)
        print(num.nums())
        self.assert_equal(32, len(num.nums()))


if __name__ == "__main__":
    CsvLuaTests().run_all_tests()
