# https://github.com/lesniew1/lab11-SL-NP
# Partner 1: Stephen Lesniewski
# Partner 2: Nicholas Phipps

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(121,245),366)
        self.assertEqual(add(999,-989),10)
        self.assertAlmostEqual(add(100.1,99.9),200)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(121, 245), -124)
        self.assertEqual(subtract(20, -2006), 2026)
        self.assertAlmostEqual(subtract(100.1, 99.9), 0.2)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(-4,5),-20)
        self.assertEqual(mul(0,10),0)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10),5)
        self.assertEqual(div(-20, 5),-4)
        self.assertEqual(div(4,10),2.5)
    # ##########################

    #Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostequal(logarithm(10, 100), 2)
        self.assertAlmostequal(logarithm(5, 125), 3)
        self.asertAlmostequal(logarithm(3, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
    ##########################
    
    #Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(16),4)
        self.assertAlmostEqual(square_root(25),5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()