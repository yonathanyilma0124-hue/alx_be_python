import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest, TestCase):
    def setUp(self):
      self.calc = SimpleCalculator():
    def test_addition(self):
      self.assertEqual(self.calc.add(2, 3), 5)
      self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
      self.assertEqual(self.calc.subtract(4, 1), 3)
      self.assertEqual(seld.calc.subtract(-1, -2), -3)
    def test_multiplication(self):
      self.assertEqual(self.calc.multiply(4, 2), 8)
      self.assertEqual(self.calc.mutliply(6, 6), 36)
    def test_division(self):
      self.assertEqual(self.calc.divide(5, 1), 5)
      self.assertEqual(self.calc.divide(100, 2), 50)
    def test_division_by_zero(self):
      self.assertIsNone(self.calc.divide(6, 0))
if __name__=="__main__":
    unittest.main()
