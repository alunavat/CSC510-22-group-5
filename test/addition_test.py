import unittest

from addition_code import addition as add

class Test(unittest.TestCase):
  # Basic test cases

  # Instantiate Addition class
  def test1(self):
    total = add.Addition(1, 2)
    self.assertEqual(3, total.main())

if __name__ == '__main__':
  unittest.main()
