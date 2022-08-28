#!src/bin/env python3
# encoding: utf-8

from ensurepip import version
import glob
from logging import root
import os, sys
import time
from turtle import Turtle
from urllib import request
import requests

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# ROOT_DIR = '/'.join([ROOT_DIR, 'main_module_app.py'])
# sys.path.append(ROOT_DIR)


from IJDevLibs.IJhandleFilesLib import (
    clean_folder,
    convert_xlsx_to_csv_file,
    create_diretory,
    create_file,
    write_content_infile,
    write_log_file
)

from IJDevLibs.IJGeneralLib import (
    build_line, complete_make_response,
    custom_show_info, define_random_number,
    delete_file, download_images_from_server,
    get_my_project_root_path,
    home_path, make_reponse,
    make_sound, print_log,
    ij_smart_menu, convert_hour_to_minute,
    convert_hour_to_second,
    convert_minutes_to_second,
    convert_minutes_to_hour,
    delete_dir, show_info,
)

from IJDevLibs.setup_app import (
    setupIJDevlibs
)

from IJDevLibs.utils.config_contants_paths  import (
    SLEEP_TIME_ONE, SLEEP_TIME_TWO,
    SLEEP_TIME_ZERO, FILE_OPERATION_TYPE
)

from IJDevLibs.api_libs.brasilian_generator import (
    BrazilianGeneratorAPI
)

# ---------------------------------------------------------------
#                    FUNCTIONS GOES HERE
# ---------------------------------------------------------------


def run_app(choice):

    minutes = 4587
    hours = 5

    brothers = ['obama', 'pool', 'meter jessic', 'vinda', 'cafe', 'irina']

    # brothers = [choice]

    print('RUN APP TEST...')


    # ------------------------ IJGeneralLib ------------------------------


    print_log(f'YOU CHOICE --> [ {str(choice).title()} ]')

    write_content_infile(
        content_list=brothers,
        filename='my_brothers',
        operation=FILE_OPERATION_TYPE['add new'],
        dirname='files_folder'
    )

    write_log_file(
        content=brothers, distiny_dir='stage/log_folder', filename='test_output'
    )

    build_line(shape='*', length_line=100)
    print(f'\n {minutes} minutes = {convert_minutes_to_second(minutes)} s')
    print(f'\n {minutes} minutes = {convert_minutes_to_hour(minutes)} h')
    print(f'\n {hours} h = {convert_hour_to_minute(hours)} minutes')
    print(f'\n {hours} h = {convert_hour_to_second(hours)} s')
    build_line(shape='*', length_line=100)

    # make_sound(frequency=350)

    BASE_URL = 'http://www.evolusom.com.br/lojas/1/img/produtos/'

    url_image_list = [
        'z-00257686-14393850950.jpg',
        'z-00358011-15626947800.jpg',
        'z-00358011-15626947910.jpg',
        'z-00358011-15626947911.jpg',
        'z-00267628-14600361802.jpg',
        'z-00246664-14552962920.jpg',
        'z-00246664-14552962921.jpg',
        'z-00246674-14552953210.jpg',
        'f-00246684-1427291215.jpg',
        'z-00273691-14676563750.jpg',
        'z-00273691-14676563830.jpg',
        'z-00273691-14676563831.jpg',
        'z-00298477-14903793100.jpg',
        'z-00298477-14903793160.jpg'
    ]

    for image_name in url_image_list:
        url_image = BASE_URL + image_name

        url_image_list.remove(image_name)
        url_image_list.append(url_image)

    create_diretory(dirname='evolusom_images', workspace_='stage')

    # import pdb; pdb.set_trace()

    root_p = get_my_project_root_path()
    print(f'\n\n ROOT PROJECT: \t {root_p}')

    for pngfile in glob.glob(f'{root_p}/*.jpg', recursive=True):
        print(pngfile)
        delete_file(
            dir_name='IJDevelopementLibsTest',
            file_name=pngfile
        )


    download_images_from_server(
        url_image_list=url_image_list,
        save_image_dir='stage/evolusom_images'
    )

    delete_file(dir_name='stage/log_folder', file_name='')

    print(make_reponse(endpoint='run_app'))

    complete_make_response(
        total_minutes=2,
        total_seconds=35,
        user_key='',
        user_key_value='THE BEST ONE'
    )

    custom_show_info(some_code='7777', person='IJ WM')

    define_random_number()

    print('\n\n home stage path --> ',  home_path(destiny_dir='stage'))
    print('\n home_path 2 --> ', home_path(destiny_dir='stage_test'))

    print('\n\t project root:', get_my_project_root_path())

    vpath = 'media/ijdev/DATA/PROFISSIONAL/VALERIA_FERREIRA_LIMA/MAGAZINE_LUIZA/PARTITIONS_FILES/'


    # -------------------- IJhandleFilesLib ----------------------------------

    # convert_xlsx_to_csv_file(
    #     origin_full_file_path=f'{vpath}evolusom_produtos_loja_magalu_1.xlsx',
    #     destiny_real_path=vpath,
    #     result_file_name='test_convert_xlsx_csv'
    # )

    create_file(distiny_dir='stage_test', file_name='create_file_test')

    bgapi = BrazilianGeneratorAPI()

    #   import pdb; pdb.set_trace()

    __BASE_URL__  = 'https://geradorbrasileiro.com/api/faker/pessoa'
    url_params = {
        'limit': 5
    }

    try:
        payload = requests.get(__BASE_URL__, params=url_params)
    except Exception as error:
        print_log(f'EXCEPTION: {error}')
    else:
        print(payload)
        # for x in payload:
        #     print(x)

    print(bgapi.brasilian_api_generator(type_data='pessoa', quantity=5))

    return


if __name__ == '__main__':

    show_info(
        type_='app_info', app_name='IJDEVLIBS TEST',
        desc_='testing my lib IJDevLibs', version_='1.1.0',
        user_key='@UTHOR',
        user_key_value='ME IJ WM BEST PYTHON DEV EVER'
    )
    time.sleep(10)

    setupIJDevlibs(clean_dir_if_exists=True)

    delete_dir(workspace_name=f'{os.getcwd()}/stage',
        dir_name_list=['files_folder', 'log_folder', 'evolusom_images']
    )

    while True:

        menu_options = ['pool', 'meter jessic', 'vinda', 'cafe', 'irina']

        response_ = ij_smart_menu(menu_options)

        if response_ == 0:
            print('\n\n THE APP WILL BE QUIT ...\n\n')
            time.sleep(SLEEP_TIME_ZERO)
            exit(0)

        run_app(menu_options[response_ - 1])

        build_line(shape='*', length_line=100)
        print(f'\n THE APP GOING TO SLEEP [ {SLEEP_TIME_ZERO} ] minute(s)\n')
        build_line(shape='*', length_line=100)

        make_sound()
        time.sleep(SLEEP_TIME_ZERO * 60)
