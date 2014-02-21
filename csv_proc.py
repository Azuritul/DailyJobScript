#!/usr/bin/env python

__author__ = 'Azuritul Wu'

import csv


inputReader = open('D:\BASEL.csv', 'rb')
output = open('D:\BASEL2.csv', 'wb')
del_count = 0
writer = csv.writer(output, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)

dict_reader = csv.DictReader(inputReader)

dics = [d for d in dict_reader]
header = dics[0].keys()

print dict_reader.fieldnames

dict_writer = csv.DictWriter(output, dict_reader.fieldnames)
row_count = 0

for r in dics:
    if row_count == 0:
        dict_writer.writeheader()
    pfolio = r['M_MX_PFOLIO    ']
    instrument = r['M_INSTRUMENT        ']

    if pfolio.find('CYFO001190011') != -1 and instrument.find('USD/CNH') != -1:
        del_count += 1
    elif pfolio.find('CYFO001190111') != -1 and instrument.find('USD/CNH') != -1:
        del_count += 1
    elif pfolio.find('CYFO004190211') != -1 and instrument.find('USD/CNH') != -1:
        del_count += 1
    else:
        dict_writer.writerow(r)
        row_count += 1

inputReader.close()
output.close()

print(del_count)