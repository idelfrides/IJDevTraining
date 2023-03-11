#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""Python study module"""

import base64
import calendar
from hashlib import sha1
import json
import time
from datetime import datetime, timedelta
from functools import reduce
from typing import ByteString, List

import numpy as np
import psutil
import xmltodict

from PythonTraining import abstract_classes
from utilLibs import lib_manager
#


def warlus_operator(values_list: List = [1, 2, 3, 4]) -> None:
    """## Warlus operator ':=' 
       Permite realizar atribuição e verificar condicional na mesma instrução

    Args:
        values_list (List, optional): _description_. Defaults to [1,2,3].

    Returns:
        None: Do not return values
    """

    if (n := len(values_list)) > 3:
        lib_manager.print_log(
            f"LIST LEN IS TOO LONG ({n} elements, expected < 4)")
        return

    print(values_list)


def show_ellipsis() -> None:
    """Ellipsis '...' is similar to the "pass"keyword 

    Returns:
        None:  Do not return values
    """
    ...

    if 3 > 7:
        ...

    for i in range(7):
        ...


def compare_two_lists(list_one: List[str], list_two: List[str]):
    """ Compare two lists

    Args:
        list_one (List[str]): List one
        list_two (List[str]): List two

    Returns:
        _type_: None
    """

    list_two_lowercase = list(map(str.lower, list_two))

    for value_one in list_one:
        if value_one.lower() in list_two_lowercase:
            lib_manager.print_log(f"VALUE {value_one} EXISTS IN LIST 2")
        else:
            lib_manager.print_log(f"VALUE {value_one} NOT EXISTS IN LIST 2")

    return


def make_sha1(*args):
    """ *args must bring values for 
        - ApiKey | GET_data | POST_data | ApiSecret 
    """

    # import pdb
    # pdb.set_trace()

    form_params = "".join(args).encode()
    x_rest_apisign_obj = sha1(form_params)
    x_rest_apisign = x_rest_apisign_obj.hexdigest()
    print()
    print()
    print()
    print(f"\t X-Rest-ApiSign:   {x_rest_apisign}")


def convert_epoch_timestamp_human(epoch_timestamp: float) -> str:
    human_time = time.strftime(
        "%a, %d %b %Y %H:%M:%S +0000", time.gmtime(epoch_timestamp))

    return human_time


def convert_human_epoch(human_time: str = "") -> str:

    if not human_time:
        human_time = str(datetime.today())[:19]

    epoch_time = calendar.timegm(
        time.strptime(human_time, '%Y-%m-%d %H:%M:%S'))

    # epoch_time2 = calendar.timegm(human_time.utctimetuple())

    return epoch_time  # , epoch_time2


def convert_human_epoch_by_days(days: int = 7) -> str:
    _datetime = datetime.utcnow() - timedelta(days=days)
    unixtime = calendar.timegm(_datetime.utctimetuple())

    return f"{unixtime}"


def format_base64(**kwargs) -> ByteString:
    """# Format user credentials to base 64

    Returns:
        ByteString: username:secret formatted to base string
    """
    # Access keys (access key ID and secret access key)
    credential = ":".join([kwargs.get("key_id"), kwargs.get("secret_key")])

    simple_credential_encode = credential.encode("ascii")

    credential_encoded = base64.b64encode(simple_credential_encode)

    return credential_encoded


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


def test_lambda_func(value_: int = 3) -> int:
    """# Test Lambda function
    Sinxte:
        variavle_holds_lambda = lambda {PARAMETER}:{OPERATION WITH PARAMETER}

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
        --> map applys the given function [1] FOR/over each value in the iterable [2]

    Args:
        some_itareble(list, tuple, set): an itareble of values

    Return:
        list : a list of mapped values such as 'test_lambda_func' function
    """

    # lambda_function = lambda x:x*2
    # return list(map(lambda_function, some_itareble))

    return list(map(test_lambda_func, some_iterable))


def test_reduce(some_iterable=(1, 2)) -> int:
    """## Study and Test build_in function: reduce
    reduce function receive as argument:
        --> function\n
        --> iterable\n
        reduce applys the given function over each value in the iterable

    Args:
        some_iterable(list, tuple, set): a list or tuple of values

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

    lib_manager.print_log(f'TEST -> X={x_value} | Y={y_value} | Z={z_value}')

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
    """# Test and studing abstract classes

    Returns:
        Type: None, do not return values
    """

    bobo = abstract_classes.JackRussellTerrier()
    bobo.walk()
    bobo.speak()

    human = abstract_classes.Person()
    human.name_type = 'MR. OBAMA'
    human.move()
    human.eat()
    human.talk()

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
    lion.talk()

    eagle = abstract_classes.Eagle()
    eagle.name_type = 'EAGLE FLY'
    eagle.move()
    eagle.eat()
    eagle.talk()

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


def convert_xml_json(filename="help_file.xml"):
    """# Convert XML into JSON format
    """
    # from lib_manager
    # import pdb
    # pdb.set_trace()

    full_path = "/".join([lib_manager.get_cwdir(), "utils", filename])

    file_content = lib_manager.read_files(full_path)
    obj = xmltodict.parse(file_content)
    print(json.dumps(obj))

    # obj = xmltodict.parse("""
    #     <IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2022-11-21T14:31:20.397-08:00">
    #         <QueryResponse startPosition="1" maxResults="1">
    #             <Employee domain="QBO" sparse="false">
    #                 <Id>
    #                     55
    #                 </Id>
    #                 <SyncToken>
    #                     0
    #                 </SyncToken>
    #                 <MetaData>
    #                     <CreateTime>
    #                         2022-08-18T11:21:48-07:00
    #                     </CreateTime>
    #                     <LastUpdatedTime>
    #                         2022-08-18T11:21:48-07:00
    #                     </LastUpdatedTime>
    #                 </MetaData>
    #                 <GivenName>
    #                     Emily
    #                 </GivenName>
    #                 <FamilyName>
    #                     Platt
    #                 </FamilyName>
    #                 <DisplayName>
    #                     Emily Platt
    #                 </DisplayName>
    #                 <PrintOnCheckName>
    #                     Emily Platt
    #                 </PrintOnCheckName>
    #                 <Active>
    #                     true
    #                 </Active>
    #                 <V4IDPseudonym>
    #                     002098e634f18ab7f8437fb00aed4417c16735
    #                 </V4IDPseudonym>
    #                 <BillableTime>
    #                     false
    #                 </BillableTime>
    #             </Employee>
    #         </QueryResponse>
    #     </IntuitResponse>""")

    # print(json.dumps(obj))
