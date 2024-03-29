#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""# Python main app module

    This module hold a functions cal all package and test them features
"""

from dataclasses import asdict, astuple
from datetime import datetime
from random import randint

from PythonTraining import eleven_tips, python_study, decorators
from utilLibs import lib_manager
from utilLibs import lib_show_info as info
from PythonTraining.webScraping import web_scraping


def run_main_app():
    """# Main function

    This function is responsable to control whole app execution

    Returns:
        None: None
    """

    mixpanel_key_id = "BoutiqeueDevServiceAccount.e1ebf7.mp-service-account"
    mixpanel_secret_key = "rc3GLXQ4AIiGrxfdMUGiCdtwafiIFupw"

    print("=" * 80)
    lib_manager.print_log("THIS IS THE MAIN MODULE OF THIS APP \n\n")
    print("=" * 80)

    scrap_obj = web_scraping.WebScraper()
    scrap_obj.scraping_weather()

    python_study.run_abstract_class()

    python_study.test_output()

    default_value = 20
    python_study.calculate_area_retangle(
        width=randint(5, default_value),
        heigth=randint(default_value, 50)
    )
    # spam()   # infinity loop

    test_list = [1, 2, 3, 4, 5]
    test_set = {1, 2, 3, 4, 5}

    print("\n\t")
    value_ = randint(1, 100)
    print(
        f"\n\tLAMBDA_FUNCTION RESULT: {python_study.test_lambda_func(value_=value_)}")

    print(f"\n\tORIGINAL LIST:  {test_list}")

    print(
        f"\n\tMAP_FUNCTION RESULT: {python_study.test_map(some_iterable=test_set)}")

    reduce_results = python_study.test_reduce(some_iterable=test_list)

    print(f"\n\t REDUCE RESULT SUM: {reduce_results[0]}")
    print(f"\n\t REDUCE RESULT SUBTRACTION: {reduce_results[1]}")
    print(f"\n\t REDUCE RESULT MULTIPLICATION: {reduce_results[2]}")
    print(f"\n\t REDUCE RESULT DIVISION: {reduce_results[3]}")

    eleven_tips.tip1_enumerate_instead_range_len(
        some_list=[4, 59, 111, 7, 8, -9, -71, -5])

    eleven_tips.tip2_list_comprehension_instead_for_loop(some_list=[1, 2])

    eleven_tips.tip3_sort_complex_iterables_with_sorted_method(
        some_iterabe=[6, 8, 3, 1, -5, 9, 7])

    some_list = [9, 9, 9, 2, 2, 2, 2, 1, 1, 4, 4, 6, 6, 5, 5, 7, 7, 7]

    eleven_tips.tip4_store_unique_values_with_sets(some_list=some_list)

    eleven_tips.tip5_save_memory_with_generator()

    eleven_tips.tip7_count_hashable_objects_with_collections_counter(
        some_list=some_list)

    python_study.show_laptop_battery_info()

    # import pdb
    # pdb.set_trace()

    key_id = input("\n\n ENTER YOUR ACCESS KEY ID -->  ")
    secret_key = input("\n\n ENTER YOUR SECRET ACCESS KEY -->  ")

    key_id = (
        key_id if key_id else mixpanel_key_id
    )
    secret_key = (
        secret_key if secret_key else mixpanel_secret_key
    )

    credential_encoded = python_study.format_base64(
        key_id=key_id, secret_key=secret_key)

    print(f"credential_encoded --> {credential_encoded}\n\n")

    print(
        f"EPOCH RESULT --> {python_study.convert_human_epoch_by_days(days=7)}\n\n")

    print(
        f"HUMAN TIME RESULT --> {python_study.convert_epoch_timestamp_human(epoch_timestamp=1663771900)}\n\n")

    human_time = input("ENTER HUMAN TIME in format ['%Y-%m-%d %H:%M:%S']: ")

    if human_time:
        print(
            f"HUMAN TIME: {human_time} = EPOCH TIME RESULT --> {python_study.convert_human_epoch(human_time)}\n\n")
    else:
        human_time = str(datetime.today())[:19]
        print(
            f"HUMAN TIME: {human_time} = EPOCH TIME RESULT --> {python_study.convert_human_epoch()}\n\n")

    house = decorators.House(50_000.0)
    print(f"DECORATORS TESTING [ GETTER ]:  {house.price}")
    house.price = -200000
    print(f"DECORATORS TESTING [ NEG SETTER ]:  {house.price}")
    house.price = 100_000.0
    print(f"DECORATORS TESTING [ SETTER ]:  {house.price}")
    # del house.price

    meu_livro = decorators.Livro(
        "Titulo do Livro", paginas=["pagina1", "pagina2"]
    )

    meu_outro_livro = decorators.Livro.cria_a_partir_de_paginas(
        ["pagina1", "pagina2"])
    print(meu_livro)

    # myclass = decorators.MyClass("TESTING MY CLASS")
    # myclass.some_class_method()

    # This one produce an error
    # print(f"DECORATORS TESTING [ AFTER DELLETER ]:  {house.price}")
    info.make_newlines()

    p_1 = decorators.Person("OBAMA", 61)
    p_2 = decorators.Person("WM", 32)
    p_3 = decorators.Person("CAFE", 20)
    p_4 = decorators.Person("CAFE", 20)
    p_5 = decorators.Person("IRINA", 13)
    p_6 = decorators.Person("POOL", 29)

    print(f"\n\n PERSON 1: {p_1}")
    print(f"\n\n PERSON 2: {p_2}")
    print(f"\n\n PERSON 3: {p_3}")
    print(f"\n\n PERSON 4: {p_4}")
    print(f"\n\n PERSON 5: {p_5}")
    print(f"\n\n PERSON 6: {p_6}")

    print(f"\n\n COMPARE PERSONS \n {p_3} and {p_1} \n RESULT: {p_3 == p_1}")

    print(f"TUPLE -> {astuple(p_1)}")
    # p1.iq = 277
    print(f"DICT -> {asdict(p_1)}")
    print(f"DICT -> {asdict(p_5)}")

    info.make_newlines(5)

    python_study.convert_xml_json()

    # members = [p1, p2, p3, p5, p6]

    # sorted_members = sorted(members)
    # for member in sorted_members:
    #     print(f"{member.name}(age={member.age})")

    python_study.make_sha1(
        "6c17ed6fce89149195ed11a629343fae",
        "rest/subscriber/add",
        '{"subscriber":"idelfrides.papai@relyance.ai"}',
        "044921afecdb371b13ab8da30636e297444bd8f9"
    )

    list_one = ["Guine-BISSAU", "Angola", "Cabo Verde",
                "Mocambique", "Sao Tome e principe", "BRASIL", "PORTUGAL"]

    list_two = ["guine-biSSAU", "angoLA", "CABO Verde",
                "MOCAMBIQUE", "sao tome e PRINCIPE", "brasil", "portugal"]

    python_study.compare_two_lists(list_one, list_two)

    python_study.warlus_operator(values_list=test_list)

    # ----------------- End part ---------------------
    info.end_app()
    return


if __name__ == '__main__':
    run_main_app()
