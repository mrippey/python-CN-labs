# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.


# 1) Function to read and write to file 
import pathlib
import unittest
import example_function as ef 

class TestFileReadWrite(unittest.TestCase):

    def test_file_exists(self, path):
        if not pathlib.Path(path).is_file():
            raise AssertionError(f'File {str(path)} could not be found')

    def test_ensure_lines_written(self, path):
       content = 'This is a test, and only a test'
       file_pth = pathlib.Path(path)

       with patch('example_function.open'.format(__name__),
            new=mock_open(read_data=content)) as  afile:
            afile.assert_called_once_with(file_pth, 'r')
       expected = len(content.split('\n'))
       self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(verbosity=2)


# 2) Function accepts any two numbers from user, must be within 0 - 100
class TestUserInputNum(unittest.TestCase):

    def test_both_args_nums(self, num1, num2):
        self.assertIsInstance(num1, int)
        self.assertIsInstance(num2, int)

    def test_ints_are_in_range(self, num1, num2):
        self.assertGreaterEqual(num1, 0)
        self.assertLessEqual(num2, 100)
        