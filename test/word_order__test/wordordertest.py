import unittest
from src.wordorder_8.utils import *

class testcase(unittest.TestCase):
    def test_word(self):
        actualinput = word_order()
        expectedoutput = 2 1
        self.assertEqual(actualinput, expectedinput)

if __name__ == '__main__':
    unittest.main()
