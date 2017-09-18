# /usr/bin/env python
# -*- coding:utf-8 -*-
import codecs
import csv
import json

import logging
import sys

import test_case
from test_case.public.define_find_expect_json import get_json_obj_info
from test_case.public.define_log import LogDefine
#from test_case.public.test_define_testcase import addInterfaceTestCase
from test_case.public.define_parse_csv_file import model123
from test_case.test_get_model import InterfaceModel

reload(sys)
sys.setdefaultencoding('gb18030')

path=r"F:\autotest\ssssss111.csv"
def control_csv_file(path):
    LogDefine()
    with codecs.open(path,"rb") as f:
        logging.info(u"成功打开csvw文件")
        reader = csv.DictReader(f)
        for i, rows in enumerate(reader):
            model123(rows=rows)
        #return reader

control_csv_file(path=r"E:\programing\project\interface_testing_python\ssssss111.csv")