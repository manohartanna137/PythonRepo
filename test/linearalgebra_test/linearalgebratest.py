import unittest

from src.linearalgebra_13.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        list1 =[[1,3],[2,4]]
        actualinput =lin_algebra(list1)
        expectedoutput=-2.0
        self.assertEqual(actualinput,expectedoutput)

if __name__ == '__main__':
    unittest.main()
