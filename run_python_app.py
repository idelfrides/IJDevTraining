#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""# Python main app module

    This module hold a functions cal all package and test them features
"""

from random import randint
from PythonTraining.webScraping import web_scraping
from PythonTraining.libs import lib_manager
from PythonTraining import python_study
from PythonTraining import eleven_tips


def run_main_app():
    """# Main function

    This function is responsable to control app execution at all

    Returns:
        None: None
    """

    print("=" * 80)
    lib_manager.print_log("THIS IS THE MAIN MODULE OF THIS APP \n\n")
    print("=" * 80)

    scrap_obj = web_scraping.WebScraper()
    scrap_obj.scraping_weather()

    python_study.run_abstract_class()
    python_study.test_output()
    python_study.calculate_area_retangle(
        width=randint(1, 10), heigth=randint(1, 20)
    )
    # spam()   # infinity loop

    test_list = [1, 2, 3, 4, 5]

    print(
        f"\n\t LAMBDA_FUNCTION RESULT: {python_study.test_lambda_f(value_=randint(1, 100))}"
    )

    print(f"\n\t ORIGINAL LIST:  {test_list}")

    print(
        f"\n\tMAP_FUNCTION RESULT: {python_study.test_map(some_iterable=test_list)}")

    reduce_results = python_study.test_reduce(some_iterable=test_list)

    print(f"\n\t REDUCE RESULT SUBTRACTION: {reduce_results[1]}")
    print(f"\n\t REDUCE RESULT SUM: {reduce_results[0]}")
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

    # ----------------- End part ---------------------
    python_study.end_app()
    return

# product_analysis
# weather_analysis
# climate_analysis#
# descount_produt


if __name__ == '__main__':
    run_main_app()
