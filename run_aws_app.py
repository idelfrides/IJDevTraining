#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""# AWS main app module

    This module hold a functions call all package and test them features
"""

from datetime import datetime
from random import randint

from AWSTraining import amazon_study as aws

from utilLibs import lib_manager as lm
from utilLibs import lib_show_info as info


def run_main_app():
    """# Main function

    This function is responsable to control app execution at all

    Returns:
        None: None
    """

    print("=" * 80)
    lm.print_log("THIS IS THE MAIN MODULE OF THIS APP \n\n")
    print("=" * 80)

    aws.aws_ses()

    # ----------------- End part ---------------------
    info.end_app()
    return

# product_analysis
# weather_analysis
# climate_analysis#
# descount_produt


if __name__ == '__main__':
    run_main_app()
