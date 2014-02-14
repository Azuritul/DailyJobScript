#!/usr/bin/env python
import os

__author__ = 'Azuritul Wu'

import tarfile
import logging
import sys
from contextlib import closing
from datetime import date

"""
    Archiving audit file in the last month
    File name pattern
    AUDIT_20140206_050820.csv
    tar -czvf AUDIT_yyyyMMDD_*.csv AUDIT_yyyy_JAN.tar.gz
"""


def do_tar(target_dir):
    month_str_arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    month_digit_arr = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    curr_month = date.today().strftime('%b')
    curr_year = date.today().strftime('%Y')
    filename_year = curr_year
    pre_month_idx = month_str_arr.index(curr_month.upper()) - 1

    if curr_month == 0:
        pre_month_idx = 11
        filename_year = int(curr_year) - 1

    tar_name = 'AUDIT_' + str(filename_year) + '_' + month_str_arr[pre_month_idx] + '.tar.gz'

    matched_file_name = str(filename_year) + str(month_digit_arr[pre_month_idx])

    with closing(tarfile.open(tar_name, "w:gz")) as tar:
        file_list = [f for f in os.listdir(target_dir) if
                     f.count('_') > 1 and f.split('_')[1].find(matched_file_name) != -1]

        logging.info('Start tar operation ...')

        for pending in file_list:
            logging.info('Tarring ' + pending)
            tar.add(pending)

        logging.info('Finished tar operation, totally tar ' + str(len(file_list)) + ' files')


def main(arguments):
    target_folder = arguments[1]
    do_tar(target_folder)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', filename='archive_audit.log', level=logging.INFO)
    if len(sys.argv) < 2:
        print('Please provide tar folder.')
        sys.exit()
    main(sys.argv[0:])
