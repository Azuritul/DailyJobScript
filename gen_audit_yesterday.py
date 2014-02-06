#!/usr/bin/env python

import subprocess
import logging
from datetime import date, timedelta

today = date.today()
yesterday = date.today() - timedelta(1)

logging.basicConfig(format='%(asctime)s %(message)s',filename='genAuditYesterday.log',level=logging.INFO)
cmd = '/usr/jdk/jdk1.6.0_14/bin/java -Xmx1g -classpath MarketDataCheck.jar com.fubon.mdc.audit.ExportMPAUD ' + yesterday.strftime('%Y%m%d') + ' 17:30'

logging.info('Start gen logging')
result = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
logging.info('Process started...')
