# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math


class TestMath(unittest.TestCase):

    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)

    def test_isnan_recognizes_numbers(self):
        self.assertFalse(math.isnan(4))

if __name__ == "__main__":
    unittest.main()
