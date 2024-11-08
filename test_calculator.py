import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3, -2), 1)
    # Add the following test methods to the TestCalculator class:

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(1,2),-1)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(3,-3),-9)
        self.assertEqual(self.calc.multiply(-3,-3),9)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(6,2),3)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(4,2),0)
        self.assertEqual(self.calc.modulo(1,2),1)
if __name__ == '__main__':
    unittest.main()