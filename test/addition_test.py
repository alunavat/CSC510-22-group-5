import unittest
import Addition as add

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

  def test1(self):
    total = add.Addition(6, 18)
    self.assertEqual(24, total.main())

if __name__ == '__main__':
  unittest.main()
