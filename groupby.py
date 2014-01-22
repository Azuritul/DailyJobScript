__author__ = 'Azuritul Wu'
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
    if file.startswith('data_') and file.endswith('.xml') and file.count('_') == 2:
        split_name = file.split('_')
        return split_name[1]

def scrap_last_name(file):
    """
    Getting folder name from the splitted file_name
    If the file_name is data_FXVOL_20130612.xml, then the folder name returned will be '201306'
    """
    if file.startswith('data_') and file.endswith('.xml') and file.count('_') == 2:
        split_name = file.split('_')
        return split_name[2][0:6]

def create_if_no_folder(folder_name, context_path):
    full_path = os.path.join(context_path, folder_name)
    if not os.path.exists(full_path) and folder_name != '':
        logging.info('folder not exist, creating ... ' + full_path)
        os.mkdir(full_path)
    return full_path

def decide_folder_name(filename, groupby):
    if groupby == 'month':
        return scrap_last_name(filename)
    elif groupby == 'name':
        return scrap_middle_name(filename)


def process_file(filename, kind, context_path):
    folder_name = decide_folder_name(filename, kind)
    destination_folder = create_if_no_folder(folder_name, context_path)
    src_file = os.path.join(context_path, filename)
    logging.info('Moving ' + filename + ' to ' + os.path.abspath(destination_folder))
    shutil.move(src_file, os.path.abspath(destination_folder))

def is_valid_file(filename):
    full_path = os.path.abspath(filename)
    if os.path.isfile(full_path) and fnmatch.fnmatch(filename, VALID_FILE_NAME):
        return True
    return False


def group_by_filename(dir, kind):
    file_list = os.listdir(dir)
    for filename in file_list:
        if os.path.isdir(filename):
            context_path = dir  + filename
        else:
            context_path = dir
        if fnmatch.fnmatch(filename, VALID_FILE_NAME):
            process_file(filename, kind, context_path)

def main(arguments):
    target = arguments[1]
    if arguments[0] == 'month' or arguments[0] == 'name':
        group_by_filename(target, arguments[0])
    else:
        logging.info('Do nothing')
        print('Please provide correct options: [month | name]')

curr_ver = sys.version_info
if curr_ver >= (3,2):
    prompt = input
else:
    prompt = raw_input

VALID_FILE_NAME = 'data_*_*.xml'
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s',filename='groupby.log',level=logging.INFO)
    main(sys.argv[1:])


