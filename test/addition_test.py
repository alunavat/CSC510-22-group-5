import unittest

from addition_code import addition as add

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

if __name__ == '__main__':
  unittest.main()
