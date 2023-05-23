import unittest
from src.min_max_problem_11.utils import *


class MyTestCase(unittest.TestCase):
    def
        row, column = map(int, input("Enter the number of rows and columns: ").split())
        actual_input=find_max_min(row, column)
        expected_output=4

        self.assertEqual(actual_input, expected_output)
# inputs 4 5 6 1 2
#        7 8 9 4 5
#        1 2 3 4 5
#        0 1 4 7 8

if __name__ == '__main__':
    unittest.main()
