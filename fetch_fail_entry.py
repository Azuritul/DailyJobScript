#!/usr/bin/env python
NORMAL_LOG_SIZE = 455
__author__ = 'Azuritul Wu'

import os
import sys
import logging

"""
    Compare the size of files in directory from user input against NORMAL_LOG_SIZE.
    There might be problems if the two doesn't match.
    Output the mismatched file in possible_fail_entry.log
"""

logging.basicConfig(format='%(asctime)s %(message)s', filename='possible_fail_entry.log', level=logging.INFO)

curr_ver = sys.version_info


if curr_ver >= (3, 2):
    prompt = input
else:
    prompt = raw_input

log_dir = prompt("Please input log dir: ")

logging.info("Starting")
print("Starting...")

def process_input_dir(input_dir):
    input_dir = input_dir.strip()
    print("Process input folder: " + input_dir)
    if input_dir == '':
        input_dir = os.curdir
    return input_dir

log_dir = process_input_dir(log_dir)
file_list = os.listdir(log_dir)

for file in file_list:
    full_path = os.path.join(log_dir, file)
    size = os.path.getsize(full_path)
    if size != NORMAL_LOG_SIZE and file != 'possible_fail_entry.log' and file.endswith('.log'):
        logging.error(file + " with skeptical file size: " + str(size))

print("Finished...")
logging.info("Finished.")

