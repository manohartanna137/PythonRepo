import unittest
from src.calendar_problem_1.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualinput = weekday(12,23,2022)
        expectedoutput = "FRIDAY"
        self.assertEqual(actualinput, expectedoutput)



if __name__ == '__main__':
    unittest.main()

