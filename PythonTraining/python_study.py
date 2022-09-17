#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""Python study module"""

import time
from functools import reduce
from typing import List

import numpy as np
import psutil

from PythonTraining import abstract_classes
from PythonTraining.libs import lib_manager

# product_analysis
# weather_analysis
# climate_analysis#
# descout_produt


def show_laptop_battery_info() -> None:
    """# Get laptop battery info

    Returns:
        None: Do not return any value
    """

    laptop_battery = psutil.sensors_battery()

    battery_percent = laptop_battery.percent

    if (battery_percent <= 20) and not is_laptop_battery_plugged():
        print(
            f"\n\n\n MacBook Pro Power Battery is {battery_percent}%. \n Plugg it on power.")
        # lib_manager.make_sound()

    return


def is_laptop_battery_plugged() -> bool:
    """# Get laptop battery Power Plugget 

    Returns:
        Bol: Return True if plugged, False otherwise
    """

    laptop_battery = psutil.sensors_battery()

    return laptop_battery.power_plugged


def numpy_study() -> None:
    """# numpy test

    Returns:
        None: Do not return data
    """

    _a_ = np.array([
        [1, 2],
        [2, 3],
        [4, 5]
    ])

    _b_ = np.array([
        [12, 21, 43],
        [42, 45, 14],
        [35, 46, 44],
        [11, 22, 90],
    ])

    print(f'A --> {_a_}')
    print(f'\n B --> {_b_}')

    _c_ = _b_ @ _a_

    print(f'\n\t C2 NORMAL --> {_c_}')
    print(f'\n\t C2 SHAPE --> {_c_.shape}')

    return


def test_lambda_f(value_: int = 3) -> int:
    """# Test Lambda function

    Args:
        value_ (int): value to valculate with lambda function

    Returns:
        int: operation result
    """

    # def lambda_function(value): return value * 2
    def lambda_function(value_): return value_ * 2

    return lambda_function(value_)


def test_map(some_iterable=[1, 2, 3]) -> List:
    """# Study and Test build_in function: map
    The map function receive two arguments:
        [1] --> a function\n
        [2] --> an iterable\n
        --> map applys the given function [1] over each value in the iterable [2]

    Args:
        some_itareble(list, tuple): a itareble of values

    Return:
        list : a list of mapped vslues such as 'test_lambda_f' function
    """

    # lambda_function = lambda x:x*2
    # return list(map(lambda_function, some_itareble))

    return list(map(test_lambda_f, some_iterable))


def test_reduce(some_iterable=(1, 2)) -> int:
    """## Study and Test build_in function: reduce
    reduce function receive as argument:
        --> function\n
        --> iterable\n
        reduce applys the given function over each value in the iterable

    Args:
        some_iterable(list, tuple): a list or tuple of values

    Return:
        int : four result of operations bellow
    """

    def lambda_reduce_sum(x, y): return x + y
    def lambda_reduce_mult(x, y): return x * y
    def lambda_reduce_sub(x, y): return x - y
    def lambda_reduce_div(x, y): return x / y

    sum_ = reduce(lambda_reduce_sum, some_iterable)
    sub_ = reduce(lambda_reduce_sub, some_iterable)
    mult_ = reduce(lambda_reduce_mult, some_iterable)
    div_ = reduce(lambda_reduce_div, some_iterable)

    return sum_, sub_, mult_, div_


def test_output() -> None:
    """# Test some stuffs

    Returns:
        None : do not return values
    """

    x_value, y_value, z_value = 5, 9, 7

    if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:

        print(1, end=' ')
        print(2, end=' ')
        if 'a' in 'qux':
            print(3, end=' ')
        print(4, end=' ')

    lib_manager.print_log(f'TEST -> {x_value} | {y_value} | {z_value}')

    return


def spam() -> None:
    """# spam - infinit while loop

    Returns:
        None: do not return values
    """

    while '0':
        lib_manager.print_log('0')
        time.sleep(3)

    return


def run_abstract_class() -> None:
    """# Test and studu abstruact class

    Returns:
        None: do not return values
    """

    bobo = abstract_classes.JackRussellTerrier()
    bobo.walk()

    human = abstract_classes.Person()
    human.name_type = 'MR OBAMA'
    human.move()
    human.talk()
    human.eat()

    dog = abstract_classes.Dog()
    dog.name_type = 'BOBY DOG'
    dog.move()
    dog.eat()
    dog.talk()

    cat = abstract_classes.Cat()
    cat.name_type = 'NICKY CAT'
    cat.move()
    cat.eat()
    cat.talk()

    lion = abstract_classes.Lion()
    lion.name_type = 'FINCH LION'
    lion.move()
    lion.eat()
    lion.eat()

    eagle = abstract_classes.Eagle()
    eagle.name_type = 'EAGLE FLY'
    eagle.move()
    eagle.eat()
    eagle.talk()

    return


def end_app():
    """# Finish app execution

    Returns:
        None: None
    """

    print('\n\n\n')
    print('#'*80)
    print('\n\t\t\t\t END RUNNING APP \n')
    print('#'*80)
    print('\n\n')

    return


class Rectangle():
    """# Rectangle class

    Args:
        width (int, optional): width of rectangle. Defaults to 1.
        heigth (int, optional): heigth of rectangle. Defaults to 1.

    Returns:
        None: The class actually do not return values, but a method onside it does
    """

    def __init__(self, width, heigth) -> None:
        self.width = width
        self.heigth = heigth

    def get_area(self):
        return self.width * self.heigth

    def set_width(self, width):
        self.width = width

    def set_heigth(self, heigth):
        self.heigth = heigth


def calculate_area_retangle(width: int = 1, heigth: int = 1):
    """# Calculate a rectangle area

    Args:
        width (int, optional): width of rectangle. Defaults to 1.
        heigth (int, optional): heigth of rectangle. Defaults to 1.

    Returns:
        int: result of (width * heigth)
    """

    return width * heigth
