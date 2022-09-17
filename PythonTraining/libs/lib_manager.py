
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""### This module hold attributes and methods necessary to help
    build this app better."""


import os
from datetime import datetime


def convert_minutes_to_second(minutes):
    return 60 * minutes


def make_sound(duration=1, frequency=300):
    # duration = 1     # second
    # frequency = 250  # Hz
    os.system(
        f'play -nq -t alsa synth {duration} sine {frequency}')


def write_cpf_infile(cpf_list):
    print_log(f'WRITTING [ {len(cpf_list)} ] CPFs TO FILE ...')

    chdir_witout_log_v2(distiny_dir='utils')
    file_name = 'CPF_file.text'

    with open(file_name, 'w', encoding='utf-8') as file_obj:
        for cpf in cpf_list:
            cpf_with_end_line = cpf + '\n'
            file_obj.write(cpf_with_end_line)

    print_log('DONE')

    return


def change_directory(distiny_dir=None, return_cwdir=''):

    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    if not distiny_dir:
        print_log(f'CHANGING WORKSPACE TO DIR --> [ {root_dir} ]')
    else:
        print_log(f'CHANGING WORKSPACE TO DIR --> [ {distiny_dir} ]')
        return

    if return_cwdir.upper() == 'YES':
        return os.getcwd()


def chdir_witout_log(distiny_dir=None, return_cwdir=''):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    if not distiny_dir:
        pass
    else:
        os.chdir(distiny_dir)

    if return_cwdir.upper() == 'YES':
        return os.getcwd()


def chdir_witout_log_v2(distiny_dir=None, return_cwdir=''):

    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    project_root_dir = root_dir.split('/utils')[0]

    if not distiny_dir:
        pass
    else:
        os.chdir(project_root_dir)
        os.chdir(distiny_dir)

    if return_cwdir.upper() == 'YES':
        return os.getcwd()


def write_output_file(**kwarg):

    chdir_witout_log_v2(distiny_dir='output_files')

    filename = kwarg['filename']
    content = str(kwarg['content'])

    with open(filename, 'a', encoding='utf-8') as file_obj:
        content += '\n'
        log_time = datetime.now()
        log_time = f'[ {str(log_time)[:19]} ] '
        real_content = '| '.join([log_time, content])
        file_obj.write(real_content)

    return


def print_log(content):

    log_time = datetime.now()
    log_time = f'[ {str(log_time)[:19]} ] '
    real_content = '| '.join([log_time, content])

    print(f'\n{real_content}')

    return


def get_cwdir() -> str:
    """# The current work directory

    Returns:
        str: the current work directory
    """
    return os.getcwd()


class HoldSome:

    def __init__(self, some_obj):
        self.__some_sent = some_obj

    # Getter
    def get_invices_sent(self):
        return self.__some_sent

    # Setter
    def set_invices_sent(self, some_thing):
        self.__some_sent = some_thing
