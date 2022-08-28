#!usr/bin/env python3
# -*- coding: utf-8 -*-

""" # Using Python Built-in Using PyTest """

import pytest


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



class TestGetAreaRectangle:

    def test_normal_case(self):
        rectangle = Rectangle2(2, 3)
        assert rectangle.get_area() == 6  # msg='CORECT AREA')


    def test_bad_case(self):
        """### Expect -1 as output to denote error when looning at a negative area """
        rectangle = Rectangle2(1, 7)
        assert rectangle.get_area() == 7 # msg='INCORRECT AREA')


    def test_negative_case(self):
        """### Expect -1 as output to denote error when looning at a negative area """
        rectangle = Rectangle2(-1, 9)
        assert rectangle.get_area() > -10 # msg='INCORRECT NEGATIVE OUTPUT')


    def test_greater_equal(self):
        """### Test i value is greater than or egual to a particular target"""
        rectangle = Rectangle2(3, 8)
        assert rectangle.get_area() >= 20 # msg='NOT GREATER or EGUAL')

    def test_negative_case_2(self):
        """### Expect -1 as output to denote error when looning at a negative area """
        rectangle = Rectangle2(1, -3)
        assert rectangle.get_area() > -10 # msg='INCORRECT NEGATIVE OUTPUT')


@pytest.fixture
def rectangle():
    return Rectangle2(0, 0)


def test_negative_case3(rectangle):
    """### Expect -1 as output to denote error when looning at a negative area """

    print('\n\n\t I AM NEGATIVE CASE 3')

    print(f'\n\n\t WIDTH:  {rectangle.width}')
    rectangle.set_width(-1)
    rectangle.set_heigth(2)
    assert rectangle.get_area() == -4 # msg='INCORRECT NEGATIVE OUTPUT')



'''
if __name__ == '__main__':
    # load all unit test from TestGetAreaRectangle into a test suite

    loader = unittest.TestLoader()
    loader_setup = unittest.TestLoader()

    calculate_area_suite = (
        loader.loadTestsFromTestCase(TestGetAreaRectangle)
    )

    calculate_area_suite_setup = (
        loader_setup.loadTestsFromTestCase(TestGetAreaRectangleWithSetUp)
    )

    runner = unittest.TextTestRunner()
    runner.run(calculate_area_suite)
    # runner.run(calculate_area_suite_setup)

    # unittest.main()

'''