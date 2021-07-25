# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `ZeroDivisionError` gets raised correctly.

import unittest
from mymath import subtract_divide
class TestMath(unittest.TestCase):

    def test_subtract_divides(self):
        self.assertEqual(subtract_divide(10, 5, 3), 5.0)

    def test_raise_zerodiv_error(self):
       with self.assertRaises(ZeroDivisionError):
           0/0


if __name__ == "__main__":
    unittest.main(verbosity=2)