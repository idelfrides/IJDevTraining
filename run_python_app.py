#!/usr/bin/env python3
# -*- conding: utf-8 -*-


from StudyPython2.webScraping.web_scraping import (
    WebScraper
)
from StudyPython2.libs.lib_manager import (
    print_log
)


from StudyPython2.python_study import (
    _end_,
    numpy_study,
    run_abstract_class,
    test_lambda,
    test_map,
    test_output,
    test_reduce
)



def run_main_app():

    print_log(f'THIS IS THE MAIN MODULE OF THIS APP \n\n')

    scrap_obj = WebScraper()

    # url = ''

    # scrap_obj.scraping_weather()

    run_abstract_class()
    numpy_study()
    test_output()
    # spam()   # infinity loop

    test_list = [1, 2, 3, 4, 5]

    print(f'\n\t LAMBDA_FUNCTION RESULT: {test_lambda(4)}')

    print(f'\n\t ORIGINAL LIST:  {test_list}')

    print(f'\n\t MAP_FUNCTION RESULT:  {test_map(test_list)}')

    reduce_results = test_reduce(test_list)

    print(f'\n\t REDUCE RESULT SUM: {reduce_results[0]}')
    print(f'\n\t REDUCE RESULT SUBTRACTION: {reduce_results[1]}')
    print(f'\n\t REDUCE RESULT MULTIPLICATION: {reduce_results[2]}')
    print(f'\n\t REDUCE RESULT DIVISION: {reduce_results[3]}')

    return


# product_analysis
# weather_analysis
# climate_analysis#
# descout_produt



if __name__ == '__main__':
    run_main_app()

    _end_()