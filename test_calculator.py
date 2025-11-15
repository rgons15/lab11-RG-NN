import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(7, 3), 7/3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()