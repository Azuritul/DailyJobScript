#!/usr/bin/env python
import os

__author__ = 'Azuritul Wu'

import tarfile
import logging
import sys
import csv
from contextlib import closing
from datetime import date

    # for row in reader:
    #     if row == [] or not row[0].isdigit():
    #       writer.writerow(row) <2>
    #       continue
    #
    #     num1 = int(row[0]); operator = row[1]; num2 = int(row[2])
    #     exp = '%i %s %i' % (num1, operator, num2)
    #     result = eval(exp)
    #
    #     row[3] = result
    #     total = total + result
    #     writer.writerow(row)
    #
    # writer.writerow(['', '', 'total', total])
#
# print open('/tmp/output.csv', 'r').read()

# with open("D:\BASEL.csv'", 'rb') as f:
#    reader = csv.DictReader(f)
#    dics = [ d for d in reader ]
#    print(dics)

# with open('D:\BASEL2.csv', 'wb') as out:
#     writer = csv.writer(out, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)
#     dictWriter = csv.DictWriter(out,  )

inputReader = open('D:\BASEL.csv', 'rb')
output = open('D:\BASEL2.csv', 'wb')
del_count = 0
writer = csv.writer(output, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)

dict_reader = csv.DictReader(inputReader)
# mheader = 'TIMESTAMP,M_IDENTITY,  M_BROKEN,M_CAP_FRAC0,M_CAP_FRAC1,M_CAP_FRAC20,M_CASH_CUR,   M_COUP0,   M_COUP1,M_CURRENCY0,M_CURRENCY1,M_C_CUR_PL,M_DTEFXN,M_ECP0         ,M_ECP1         ,M_ED_DATE,M_EI0          ,M_EI1          ,M_EI_FREQ0,M_EI_FREQ1,M_EP0          ,M_EP1          ,M_EP_FREQ0,M_EP_FREQ1,M_EP_TYPE0,M_EP_TYPE1, M_EQ_INUM,M_EQ_RATIO,M_FINAL_CAP1,M_FIN_CAP1, M_FIXING0, M_FIXING1,  M_FIXVAL,M_FIX_CLN0,M_FIX_CLN1,M_FST_PERIOD, M_GEN_NUM,M_INIT_CAP1,M_INSTRUMENT        ,  M_INS_CP, M_IN<p></p>S_PAY, M_INS_VOL,M_LN_PAYFRM0,M_LN_PAYFRM1,M_LN_PAYOUT0,M_LN_PAYOUT1,M_LN_PAYREC,M_LN_PAY_F20, M_LN_RNG0, M_LN_RNG1,M_LN_STRIKE1,M_MA,M_MRG_COMP0,M_MRG_COMP1,M_MX_REF_JOB,  M_NATURE,      M_NB,M_NOMCCY,  M_OPT_SK,M_PAYMENT0,M_PAYMENT1,M_PAY_CLN0,M_PAY_CLN1,M_PL_KEY1                     ,M_QTY_INDEX,M_REF_DATA,M_RT_LNVOL0,M_RT_LNVOL1,M_SE_CODE      ,M_SE_F_NAME                        ,M_START0       ,M_START1       ,M_START_DAT0,M_START_DAT1,M_ST_DATE,M_SYS_DATE,M_TB,    M_TPID,M_TP_ACCSCT    ,M_TP_AE,M_TP_BS,M_TP_BUY,M_TP_CNTRP     ,M_TP_CP,M_TP_DIGPAY,M_TP_DIGPAYC,M_TP_DSCEXO2                  ,M_TP_DSCTYPE                  ,M_TP_DTEEXP,M_TP_DTEFST,M_TP_DTELBL,M_TP_DTELST,M_TP_DTESYS,M_TP_DTETRN,M_TP_DVCS,M_TP_ENTITY,M_TP_FXBASE,M_TP_FXBRSTL,M_TP_INT,M_TP_LQTY0,M_TP_LQTY1,M_TP_LQTY2,M_TP_NBLTI,M_TP_NOMCUR,       M_TP_NOMINAL,M_TP_OBAR1,M_TP_OBAR2,M_TP_OBARRB1,M_TP_OBARRB2,M_TP_OBARTYP,M_MX_PFOLIO    ,                 M_TP_PRICE,                M_TP_QTYEQ,M_TP_RTAMO          ,M_TP_RTBUY,M_TP_RTCAP0,M_TP_RTCAP1,M_TP_RTCUR0,M_TP_RTCUR1,M_TP_RTDPC02,M_TP_RTDPC12,M_TP_RTFLWAD,M_TP_RTFV0,M_TP_RTFV1,M_TP_RTMAT0,M_TP_RTMAT1,M_TP_RTMBDC0,M_TP_RTMBDC1,M_TP_RTMBDG0,M_TP_RTMBDG1,M_TP_RTMCNV0   ,M_TP_RTMCNV1   ,M_TP_RTMEEG0,M_TP_RTMEEG1,M_TP_RTMFRF0,M_TP_RTMFRF1,M_TP_RTMFRP0   ,M_TP_RTMFRP1   ,M_TP_RTMGC02,M_TP_RTMGC12,M_TP_RTMMRG0,M_TP_RTMMRG1,M_TP_RTMNDX0        ,M_TP_RTMNDX1        ,M_TP_RTMRTE0,M_TP_RTMRTE1,M_TP_RTNBPHS,M_TP_RTPR0,M_TP_RTPR1,M_TP_RTRFCT0,M_TP_RTRFCT1,M_TP_RTVLC00,M_TP_RTVLC01,M_TP_RTVLC02,M_TP_RTVLC10,M_TP_RTVLC11,M_TP_RTVLC12,M_TP_RTVLN00,M_TP_RTVLN01,M_TP_RTVLN02,M_TP_RTVLN10,M_TP_RTVLN11,M_TP_RTVLN12,M_TP_RTXCHF,M_TP_RTXCHI,M_TP_SECAMT,M_TP_SECCNT    ,M_TP_SECDIGI,M_TP_SECLOT,M_TP_SMCUR,M_TP_STATUS0,M_TP_STATUS1,M_TP_STATUS2,M_TP_STRIKE,M_TP_STRIKE2,M_TP_STRTGY    ,M_TP_TRADER,M_TP_TYPO           ,M_TP_UQTYEQ,M_TP_VALSTAT,M_TRN_FMLY,M_TRN_GRP,M_TRN_TYPE'
# sttt = mheader.split(',')
# print sttt
dics = [d for d in dict_reader]
header = dics[0].keys()
print header
# header = sttt

dict_writer = csv.DictWriter(output, header)
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


# for row in csv.DictReader(inputReader):
#     pfolio = row['M_MX_PFOLIO    ']
#     instrument = row['M_INSTRUMENT        ']
#     if pfolio.find('CYFO001190011') != -1 and instrument.find('USD/CNH') != -1:
#         count += 1
#     elif pfolio.find('CYFO001190111') != -1 and instrument.find('USD/CNH') != -1:
#         count += 1
#     elif pfolio.find('CYFO004190211') != -1 and instrument.find('USD/CNH') != -1:
#         count += 1
#     else:
#         writer.writerow(row)
inputReader.close()
output.close()

print(del_count)