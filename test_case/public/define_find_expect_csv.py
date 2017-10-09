# /usr/bin/env python
# -*- coding:utf-8 -*-
"""读取CSV文件，并返回CSV 行 数组 需要一个配置文件"""
import codecs
import csv
import json

import logging
import sys

from define_log import LogDefine


reload(sys)
sys.setdefaultencoding('utf-8')

path=r"F:\autotest\ssssss111.csv"
class FindCsvFile():
    #def __init__(self):
        #self.path = "从配置文件获取"
    @classmethod
    def find_interface_info_by_csv(self, path=r"F:\autotest\ssssss111.csv"):
        LogDefine()
        rowsall =[]
        try:
            logging.info(u"打开CSV文件")
            with codecs.open(path,"rb") as f:
                logging.info(u"成功打开csvw文件")
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    rowsall.append(row)
            return rowsall
        except Exception,e:
            logging.error("read the csv file %s wrong!!! %s ",path,e)
            print "read the csv file %s wrong!!! %s"%(path,e)
            print u"看是否需要将文档再次另存为CSV文件"


#a = FindCsvFile.find_interface_info_by_csv()
#for zz in a:
   # print zz
    #read_json = json.loads(zz["expect_json"])
    #print read_json["time"]


