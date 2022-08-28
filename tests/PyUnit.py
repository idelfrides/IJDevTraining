#!usr/bin/env python3
# -*- coding: utf-8 -*-

""" # Using Python Built-in PyUnit Framework """

import unittest


# from StudyPython.python_study import Rectangle

# from StudyPython.python_study import (
#     Rectangle
# )


class Rectangle2:

    def __init__(self, width, heigth) -> None:
        self.width = width
        self.heigth = heigth

    def get_area(self):
        return self.width * self.heigth

    def set_width(self, width):
        self.width = width

    def set_heigth(self, heigth):
        self.heigth = heigth


class TestGetAreaRectangle(unittest.TestCase):

    def test_normal_case(self):
        # self.rectangle.set_width(2)
        # self.rectangle.set_heigth(3)
        rectangle = Rectangle2(-1, 8)
        self.assertEqual(self.rectangle.get_area(), 6, msg='INCORECT AREA')

    def test_negative_case(self):
        """### Expect -1 as output to denote error when looning at a negative area """
        # self.rectangle.set_heigth(2)
        # self.rectangle.set_width(-1)
        rectangle = Rectangle2(-1, 8)
        self.assertEqual(rectangle.get_area(), -1,
            msg='INCORRECT NEGATIVE OUTPUT')

    def test_greater_equal(self):
        """### Test i value is greater than or egual to a particular target"""
        rectangle = Rectangle2(-1, 8)
        self.assertGreaterEqual(rectangle.get_area(), -1, msg='NOT GREATER or EGUAL')

    def test_assert_raises(self):
        """### using asserRaises to detect if an expected error is raised when  running a partivular block of code """
        with self.assertRaises(ZeroDivisionError):
            a = 1/0


class TestGetAreaRectangleWithSetUp(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        # this method is only run once for the entire class rather than being run for each test which is done for setUp()
        self.rectangle = Rectangle2(0, 0)

    def test_normal_case(self):
        self.rectangle.set_width(2)
        self.rectangle.set_heigth(3)
        self.assertEqual(self.rectangle.get_area(), 6, msg='INCORECT AREA')

    def test_negative_case(self):
        """### Expect -1 as output to denote error when looning at a negative area """
        self.rectangle.set_heigth(2)
        self.rectangle.set_width(-1)
        self.assertEqual(self.rectangle.get_area(), -3,
            msg='INCORRECT NEGATIVE OUTPUT')

    def test_greater_equal(self):
        """### Test if value is greater than or egual to a particular target"""
        self.rectangle.set_heigth(1)
        self.rectangle.set_width(8)
        self.assertGreaterEqual(self.rectangle.get_area(), 7, msg='NOT GREATER or EGUAL')

    def test_assert_raises(self):
        """### using asserRaises to detect if an expected error is raised when  running a particular block of code """
        with self.assertRaises(ZeroDivisionError):
            a = 7/0



if __name__ == '__main__':
    # load all unit test from TestGetAreaRectangle into a test suite

    loader = unittest.TestLoader()
    loader2 = unittest.TestLoader()

    calculate_area_suite = (
        loader.loadTestsFromTestCase(TestGetAreaRectangle)
    )

    calculate_area_suite_setup = (
        loader2.loadTestsFromTestCase(TestGetAreaRectangleWithSetUp)
    )

    runner = unittest.TextTestRunner()
    runner.run(calculate_area_suite)
    runner.run(calculate_area_suite_setup)

    # unittest.main()
