__author__ = 'yungchou.wu'
import fnmatch
import os
import shutil
import logging
import sys

def scrap_middle_name(file):
    """
    Getting folder name from the splitted file_name
    If the file_name is data_FXVOL_20130612.xml, then the folder name returned will be 'FXVOL'
    """
    if file.startswith('data_') and file.endswith('.xml'):
        split_name = file.split('_')
        return split_name[1]

def scrap_last_name(file):
    """
    Getting folder name from the splitted file_name
    If the file_name is data_FXVOL_20130612.xml, then the folder name returned will be '201306'
    """
    if file.startswith('data_') and file.endswith('.xml'):
        split_name = file.split('_')
        return split_name[2][0:6]

def group_by_filename(dir, kind):
    file_list = os.listdir(dir)
    folder_name = ''
    for filename in file_list:
        if fnmatch.fnmatch(filename, 'data_*.xml'):
            if kind == 'month':
                folder_name = scrap_last_name(filename)
            elif kind == 'name':
                folder_name = scrap_middle_name(filename)

            if not os.path.exists(folder_name) and folder_name != '':
                os.mkdir(folder_name)

            src_file = os.path.join(os.getcwd(), filename)
            dest_file = os.path.join(os.getcwd(), folder_name)
            logging.info('Moving ' + filename + ' to ' + dest_file)
            shutil.move(src_file, dest_file)

curr_ver = sys.version_info
if curr_ver >= (3,2):
    prompt = input
else:
    prompt = raw_input

logging.basicConfig(format='%(asctime)s %(message)s',filename='groupby.log',level=logging.INFO)
kind = prompt("by month or by name? ")
group_by_filename('.', kind)


