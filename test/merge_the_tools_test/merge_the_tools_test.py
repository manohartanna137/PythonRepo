import unittest
from src.merge_the_tools_5.utils import *


class MyTestCase(unittest.TestCase):
    def test_merge_tools(self):
        # Test case 1
        strings = 'AABCAAADA'
        k = 3
        expected_output = ['AB', 'CA', 'AD']
        transformed = merge_the_tools(strings, k)
        self.assertEqual(transformed, expected_output)


if __name__ == '__main__':
    unittest.main()