# /usr/bin/env python
# -*- coding:utf-8 -*-
import codecs
import csv
import json

import logging
import sys

from test_case.public.define_find_expect_json import get_json_obj_info
from test_case.public.define_log import LogDefine
from test_case.test_get_model import InterfaceModel

reload(sys)
sys.setdefaultencoding('gb18030')

path=r"F:\autotest\ssssss111.csv"
def control_csv_file(path):
    LogDefine()
    with codecs.open(path,"rb") as f:
        logging.info(u"成功打开csvw文件")
        reader = csv.DictReader(f)
        #print reader
        for i,rows in enumerate(reader):
            bb=json.loads(rows["expect_json"])
            uuuuuuuu=rows["url"]
            mmmm=rows["method"]
            aaaa=get_json_obj_info(expect=bb)
            print aaaa
            cccccccc=InterfaceModel()
            zzzz=cccccccc.define_request_method(method=mmmm,url=uuuuuuuu,parameters=aaaa["expect_parameters"])
            cccccccc.parse_method_res(response=zzzz,expected_data=aaaa)



a=control_csv_file(path=r"F:\autotest\ssssss111.csv")
#print json.loads(a)
#print a
