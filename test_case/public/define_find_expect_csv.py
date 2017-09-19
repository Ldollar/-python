# /usr/bin/env python
# -*- coding:utf-8 -*-
import codecs
import csv

import logging
import sys

from define_log import LogDefine

reload(sys)
sys.setdefaultencoding('utf-8')

path=r"F:\autotest\ssssss111.csv"
class Fwe():
    def test_interface_by_csv(self,path=r"F:\autotest\ssssss111.csv"):
        LogDefine()
        rowsall =[]

        with codecs.open(path,"rb") as f:
            logging.info(u"成功打开csvw文件")
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                rowsall.append(row)
        return rowsall






