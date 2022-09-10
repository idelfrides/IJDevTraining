#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""### Module of 11 tips to emprove your python code quikly
---

TIP #1 - Iterate with enumerate instead of raw range(len(x))

TIP #2 - Use list comprehention instead of raw for loops

TIP #3 - Sort complex iterable with "sorted()" build_in method

TIP #4 - Store unique values with Set

TIP #5 - Save memory with generator

TIP #6 - Define default values in  dictionaries with ".get()" and ".setdefault()"

TIP #7 - Count hashable objects with "collections.Counter"

TIP #8 - Format strings with "f-Strings"  (3.6+)

TIP #9 - COoncatenate strings with ".join()"

TIP #10 - Merge two dictionaries with "{**d1, **d2}" (3.5+)

TIP #11 - Simplify if-statement with "if x in [a, b, c, d]

"""

import collections
import sys
from typing import Iterable, List


def tip1_enumerate_instead_range_len(some_list: List[int]) -> None:
    """### Tip 1: Iterate with enumerate instead of iterating with range(len(x))

    Args:
        some_list (list): a list of integer values
    """

    print("\n\nTHIS IS TIP NUMBER ONE\n\n")

    # BAD WAY
    print("BAD WAY: iterating with range and len")
    # for i in range(len(some_list)):
    #     if some_list[i] < 0:
    #         some_list[i] = 0
    # print(some_list)

    # BEST WAY
    print("BEST WAY")
    for index_, value_ in enumerate(some_list):
        if value_ < 0:
            some_list[index_] = 0
    print(some_list)


def tip2_list_comprehension_instead_for_loop(some_list: List[int]) -> None:
    """### Tip 2: Use list comprehension instead of raw for loop

    Args:
        some_list (list): a list of integer values
    """

    print("\n\nTHIS IS TIP NUMBER TWO \n\n")

    some_list.clear()

    # BAD WAY
    print("BAD WAY")
    for i in range(10):
        some_list.append(i * i)
    print(some_list)

    some_list.clear()
    # BEST WAY
    print("BEST WAY")
    some_list = [i*i for i in range(10)]
    print(some_list)


def tip3_sort_complex_iterables_with_sorted_method(some_iterabe: Iterable) -> None:
    """### Tip 3: sort complex iterables with build_in sorted() method instead of implements it yourself

    Args:
        some_iterabe (iterabe): a iterabe (list, tuple, dict) of integer values
    """

    print("\n\nTHIS IS TIP NUMBER THERE \n\n")

    # BAD WAY
    print("BAD WAY IS CREATING A SORT FUNCTION BY YOUR SELF")

    # BEST WAY
    print("BEST WAY: ASCENDING ORDER")
    sorted_data = sorted(some_iterabe)
    print(sorted_data)

    print("\n\nBEST WAY: DESCENDING ORDER")
    sorted_data = sorted(some_iterabe, reverse=True)
    print(sorted_data)

    # complex list

    some_iterabe = [{"name": "Jessic", "age": 26},
                    {"name": "Cafe", "age": 20},
                    {"name": "Pool", "age": 29},
                    {"name": "Irina", "age": 13},
                    {"name": "Mr. Obama", "age": 32},
                    {"name": "Vinda", "age": 24},
                    {"name": "Formosa", "age": 31}
                    ]

    print(f"\n\nORIGINAL COMLEX : {some_iterabe}\n\n")
    sorted_data = sorted(some_iterabe, key=lambda x: x["age"], reverse=True)
    print(f"SORTED COMLEX: {sorted_data}\n\n")


def tip4_store_unique_values_with_sets(some_list: List[int]) -> None:
    """### Tip 4: store unique values with Sets

    Args:
        some_list (list): a list of integer values
    """

    print("\n\n THIS IS TIP NUMBER FOUR \n\n")

    # BAD WAY
    print("BAD WAY IS USING FOR THEN VERIFY ELEMENT BY ELEMENT")

    # BEST WAY
    print("BEST WAY: use a set ")

    print(f"\n\nORIGINAL LIST : {some_list}\n\n")
    set_data = set(some_list)
    print(f"CLEANED CONTENT SET: {set_data}\n\n")


def tip5_save_memory_with_generator() -> None:
    """### Tip 5: Save memory with generator

    """
    print("\n\n THIS IS TIP NUMBER FIVE \n\n")

    # BAD WAY
    print("BAD WAY: using list comprehension\n")
    # some_list = [i for i in range(1, 10000, 3)]
    my_list = list(range(10000))
    print(f"LIST COMPREHENSION -> {sum(my_list)}")
    print(sys.getsizeof(my_list), "bytes")

    # BEST WAY
    print("\nBEST WAY: using generator comprehension\n")
    my_gen = (y for y in range(10000))
    print(F"GENERATOR COMPREHENSION -> {sum(my_gen)}")
    print(sys.getsizeof(my_gen), "bytes")


def tip6_save_memory_with_generator() -> None:
    """### Tip 6: Define default values in  dictionaries with ".get()" and ".setdefault()"

    """

    print("\n\n THIS IS TIP NUMBER SIX \n\n")

    return


def tip7_count_hashable_objects_with_collections_counter(some_list: List[int]) -> None:
    """### Tip 7: Count hashable objects with "collections.Counter"

    Args:
        some_list (List): a list of values we need to count
    """

    print("\n\n THIS IS TIP NUMBER SEVEN \n\n")

    print(f"\n\nORIGINAL LIST : {some_list}\n\n")

    counter = collections.Counter(some_list)

    print(f"COUNTER RESULT {counter}")

    most_common = counter.most_common(1)
    print(f"MOST COMMON -> {most_common}")


def tip8_format_strings_with_f_strings() -> None:
    """### Tip 6: Format strings with "f-Strings"  (3.6+)

    """

    print("\n\n THIS IS TIP NUMBER EITH \n\n")

    return
