"""This is the unit test case module

unit test case for school_func_lib module
"""

import unittest
import sys

sys.path.append(r"C:\Users\asisrann\Desktop\DDE\workspace\python\schoolapp\school_lib")
import school_lib

class TestSchoolFuncLib(unittest.TestCase):
    def setUp(self):
        self.marks = [10,10,10,10,10,10]
        print "setup called"

    def test_get_totoal_marks_01(self):
        total_marks = school_lib.get_totoal_marks_01(*tuple(self.marks))
        expected_total_marks = 60
        self.assertEqual(expected_total_marks, total_marks, "test case failed due to mismatch in total")

    def test_get_totoal_marks_02(self):
        total_marks = school_lib.get_totoal_marks_02(*tuple(self.marks))
        expected_total_marks = 60
        self.assertEqual(expected_total_marks, total_marks, "test case failed due to mismatch in total")

    def tearDown(self):
        print "teardown called"

if __name__ == "__main__":
    unittest.main