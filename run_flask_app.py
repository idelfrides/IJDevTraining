#!/usr/bin/env python3
# -*- conding: utf-8 -*-


from functools import reduce
import time
import numpy as np


from webScraping.web_scraping import WebScraper
from abstract_classes import (
    Eagle, Person, Dog,
    Cat, Lion, JackRussellTerrier
)
from libs.lib_manager import (
    print_log
)


def run_main_app():

    print_log(f'THIS IS THE MAIN MODULE OF THIS APP \n\n')

    scrap_obj = WebScraper()

    # url = ''

    scrap_obj.scraping_weather()

    return


# product_analysis
# weather_analysis
# climate_analysis#
# descout_produt


def numpy_study():

    A = np.array([
        [1, 2],
        [2, 3],
        [4, 5]
    ])

    B = np.array([
        [12, 21, 43],
        [42, 45, 14],
        [35, 46, 44],
        [11, 22, 90],
    ])

    print(A)
    print(B)

    C = A @ B
    C2 = A * B

    print(f'C NORMAL {C}')
    print(f'C NORMAL {C2}')

    print(f'C SHAPE --> {C2.shape}')

    return


def test_lambda(n):

    lambda_function = lambda x : x * 2

    return lambda_function(n)


def test_map(some_list):

    """
    # map function receive as argument:
    ### --> function
    ### --> iterable

    """

    # lambda_function = lambda x:x*2
    # return list(map(lambda_function, some_list))

    return list(map(test_lambda, some_list))


def test_reduce(some_iterable):
    """
    # reduce function receive as argument:
    ### --> function
    ### --> iterable
    ### return one value by operation aplied by the given function

    """

    lambda_reduce_sum = lambda x, y : x + y
    lambda_reduce_mult = lambda x, y : x * y
    lambda_reduce_sub = lambda x, y : x - y
    lambda_reduce_div = lambda x, y : x / y

    sum_ = reduce(lambda_reduce_sum, some_iterable)
    sub_ = reduce(lambda_reduce_sub, some_iterable)
    mult_= reduce(lambda_reduce_mult, some_iterable)
    div_ = reduce(lambda_reduce_div, some_iterable)

    # return reduce(lambda_reduce_sum, some_iterable)
    return sum_, sub_, mult_, div_



def test_output():

    x, y, z = 5, 9, 7

    if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:

        print(1, end=' ')
        print(2, end=' ')
        if 'a' in 'qux':
            print(3, end=' ')
        print(4, end=' ')


    print_log(f'TEST -> {x} | {y} | {z}')

    return


def spam():
    while '0':
        print_log('0')
        time.sleep(3)


def run_abstract_class():

    # dog = Dog()
    # dog.speak()

    bobo = JackRussellTerrier()
    bobo.walk()

    human = Person()
    human.name_type = 'MR OBAMA'
    human.move()

    dog = Dog()
    dog.name_type = 'BOBY DOG'
    dog.move()

    cat = Cat()
    cat.name_type = 'NICKY CAT'
    cat.move()

    lion = Lion()
    lion.name_type = 'FINCH LION'
    lion.move()

    eagle = Eagle()
    eagle.name_type = 'FLY'
    eagle.move()


if __name__ == '__main__':
    # run_main_app()
    run_abstract_class()
    # numpy_study()
    # test_output()
    # spam()

    test_list = [1, 2, 3, 4, 5]

    print(f'\n\t LAMBDA_FUNCTION RESULT: {test_lambda(4)}')

    print(f'\n\t ORIGINAL LIST:  {test_list}')

    print(f'\n\t MAP_FUNCTION RESULT:  {test_map(test_list)}')

    reduce_results = test_reduce(test_list)

    print(f'\n\t REDUCE RESULT SUM: {reduce_results[0]}')
    print(f'\n\t REDUCE RESULT SUBTRACTION: {reduce_results[1]}')
    print(f'\n\t REDUCE RESULT MULTIPLICATION: {reduce_results[2]}')
    print(f'\n\t REDUCE RESULT DIVISION: {reduce_results[3]}')

    '''

    551
    980


    image.png

    Mome: IDELFRIDES JORGE FERNANDES PAPAI

    CPF: 607.532.193-44

    RG (RNM) : 08018.003190/2021-72
    '''