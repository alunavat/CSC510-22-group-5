import unittest

from csv_lua import sym_code as sym
from csv_lua import num_code as num
from csv_lua import settings as settings

class csv_lua_test(unittest.TestCase):
  # Basic test cases

    #TODO: These are just basic checks, need to be updated to replicate csv.lua code
    
    def test1(self):
        list = ['a','a','a','a','b','b','c']
        symObj = sym.sym()
        for x in list:
            sym.sym.add(symObj, x)
        mode = sym.sym.mid(symObj)
        entropy = sym.sym.div(symObj)
        self.assertEqual(mode, "a")
        self.assertTrue(1.37 <= entropy <= 1.38)

    def test2(self):
        settingObj = settings.settings()
        setting_dict = settingObj.settings_dict_get()
        for x in setting_dict:
            print (x + ": " + str(setting_dict[x]))
        self.assertEqual(1, 1)

    def test3(self):
        num_obj = num.num()
        for i in range (1,100):
            num_obj.add(i)
        mid = num_obj.mid()
        div = num_obj.div()
        self.assertTrue(50 <= mid <= 52)
        self.assertTrue(30.5 <= mid <= 32)

    # def test4(self):

    if __name__ == '__main__':
        unittest.main()
