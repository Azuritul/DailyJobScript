#!/usr/bin/env python
import sys

__author__ = 'Azuritul Wu'

import tarfile
import logging
from contextlib import closing
from datetime import date

"""
    Archiving audit file in the last month
    File name pattern
    AUDIT_20140206_050820.csv
    tar -czvf AUDIT_yyyyMMDD_*.csv AUDIT_yyyy_JAN.tar.gz
"""
def make_tarfile(output_filename, source_dir):
    with closing(tarfile.open(output_filename, "w:gz")) as tar:
        tar.add(source_dir)

def gen_tar_name():
    month_arr = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    curr_month = date.today().strftime('%b')
    curr_year = date.today().strftime('%Y')
    filename_year = curr_year
    pre_month = month_arr.index(curr_month.upper()) - 1

    if curr_month == 0:
        pre_month = 11
        filename_year = int(curr_year) - 1

    print('previous month is : ' , month_arr[pre_month] )
    return 'AUDIT_' + str(filename_year) + '_' + month_arr[pre_month] + '.tar'

def main(arguments):
    target_folder = arguments[1]
    make_tarfile(gen_tar_name(), target_folder)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', filename='archive_audit.log', level=logging.INFO)
    main(sys.argv[0:])
