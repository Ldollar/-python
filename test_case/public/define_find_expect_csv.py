# /usr/bin/env python
# -*- coding:utf-8 -*-
import codecs
import csv
import json

import logging
import sys
import unittest
from time import time

#import HTMLTestRunner
#from nose_parameterized import parameterized

#import test_case
from test_case.public.define_find_expect_json import get_json_obj_info
from test_case.public.define_log import LogDefine
#from test_case.public.test_define_testcase import addInterfaceTestCase
#from test_case.public.define_parse_csv_file import ParseCsvFile
#from test_case.public.model_demo import ParametrizedTestCase
from test_case.test_get_model import InterfaceModel

reload(sys)
sys.setdefaultencoding('utf-8')

path=r"F:\autotest\ssssss111.csv"
class Fwe():


    def test_interface_by_csv(self,path=r"F:\autotest\ssssss111.csv"):
        LogDefine()
        #aaaaaa=ParseCsvFile()
        now = str(time())
        rowsall =[]
        #filename = "F:\\autotest\\report\\" + now + "result2.html"
        #fp = file(filename, 'wb')
        with codecs.open(path,"rb") as f:
            logging.info(u"成功打开csvw文件")
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                #aaaaaa =ParseCsvFile()
                #suite = unittest.TestSuite()
                #parameterized.expand(row)
                #ParseCsvFile.test_interface()
                #suite.addTest(ParametrizedTestCase.parametrize(ParseCsvFile,param=row))
                rowsall.append(row)


                #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试测试", description=u"结果结果：")
        return rowsall





#test_interface_by_csv(path=r"E:\programing\project\interface_testing_python\ssssss111.csv")

#a=Fwe()
#b=a.test_interface_by_csv(path=r"F:\autotest\ssssss111.csv")
#print len(b[1])
#for i ,k in enumerate(b):
#    print i,k

