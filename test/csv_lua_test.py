import unittest

from csv_lua import sym_code as sym
from csv_lua import num_code as num
from csv_lua import settings as settings
from csv_lua import helpers_code as helper

class csv_lua_tests(unittest.TestCase):
  # Basic test cases

    #TODO: These are just basic checks, need to be updated to replicate csv.lua code
    
    def test_sym(self):
        # Covers eg.sym
        list = ['a','a','a','a','b','b','c']
        symObj = sym.sym()
        for x in list:
            sym.sym.add(symObj, x)
        mode = sym.sym.mid(symObj)
        entropy = sym.sym.div(symObj)
        self.assertEqual(mode, "a")
        self.assertTrue(1.37 <= entropy <= 1.38)

    def test_settings(self):
        # Covers eg.the
        settingObj = settings.settings()
        setting_dict = settingObj.settings_dict_get()
        help = helper.Helpers()
        help.oo(setting_dict)
        self.assertEqual(1, 1)

    def test_num(self):
        # Covers eg.num
        num_obj = num.num()
        for i in range (1,100):
            num_obj.add(i)
        mid = num_obj.mid()
        div = num_obj.div()
        self.assertTrue(50 <= mid <= 52)
        self.assertTrue(30.5 <= div <= 32)

    def test_num_holds_nums(self):
        # Covers eg.bignum
        num_obj = num.num()
        for i in range (1,1000):
            num_obj.add(i, nums=32)
        help = helper.Helpers()
        help.oo(num_obj.nums())
        self.assertEqual(32, len(num_obj._has))

if __name__ == '__main__':
    unittest.main()
