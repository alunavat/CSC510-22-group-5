import unittest

from addition_code import addition as add
from csv_lua import sym_code as sym
from csv_lua import settings as settings

class Test(unittest.TestCase):
  # Basic test cases

  # Instantiate Addition class
  def test1(self):
    total = add.Addition(1, 2)
    self.assertEqual(3, total.main())

  def test2(self):
    total = add.Addition(10, 20)
    self.assertEqual(30, total.main())

  def test3(self):
    total = add.Addition(5, 3)
    self.assertEqual(8, total.main())

  def test4(self):
    total = add.Addition(6, 18)
    self.assertNotEqual(23, total.main())

  def test5(self):
    total = add.Addition(-6, 18)
    self.assertEqual(12, total.main())

  def test6(self):
    total = add.Addition(-1, -2)
    self.assertEqual(-3, total.main())

  def test7(self):
    list = ['a','a','a','a','b','b','c']
    symObj = sym.sym()
    for x in list:
      sym.sym.add(symObj, x)
    mode = sym.sym.mid(symObj)
    self.assertEqual(mode, "a")

  def test8(self):
    settingObj = settings.settings();
    setting_dict = settingObj.settings_dict_get();
    for x in setting_dict:
      print (x + ": " + str(setting_dict[x]))
    self.assertEqual(1, 1)

if __name__ == '__main__':
  unittest.main()
