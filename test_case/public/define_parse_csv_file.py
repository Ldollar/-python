# /usr/bin/env python
# -*- coding:utf-8 -*-
import json

#from test_case.public.define_find_expect_csv import test_interface_by_csv
import unittest
from time import time

import HTMLTestRunner
from nose_parameterized import param
from nose_parameterized import parameterized

from define_find_expect_csv import Fwe
from define_find_expect_json import get_json_obj_info

from test_get_model import InterfaceModel

#aaaaa=test_interface_by_csv(path=r"E:\programing\project\interface_testing_python\ssssss111.csv")
a=Fwe()
b=a.test_interface_by_csv(path=r"F:\autotest\ssssss111.csv")

#for i ,k in enumerate(b):
    #print i,k
class ParseCsvFile(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass


    @parameterized.expand(
        param.explicit([b[i]])
        for i,k in enumerate(b)
    )
    def test_interface(self, rows):
        #reader=test_interface_by_csv(path=r"E:\programing\project\interface_testing_python\ssssss111.csv")
        #for i, rows in enumerate(reader):
        #print rows
        read_json = json.loads(rows["expect_json"])
        read_url = rows["url"]
        read_method = rows["method"]
        # expect_in = read_json
        # print read_method ,read_url
        # print read_json
        params_parse = get_json_obj_info(expect=read_json)
        # print params_parse["expect_parameters"].keys()
        interface_obj = InterfaceModel()
        #test_obj = TestCases()

        if rows["method"] == "get":
            # print "dddddddddddddddddddddddddddddd"
            # print params_parse["expect_parameters"].keys()[0}
            if len(params_parse["expect_parameters"].keys()) == 1 and params_parse["expect_parameters"].keys()[0] == "query":
                # print params_parse["expect_parameters"]["query"]
                #add_testcase=addInterfaceTestCase()
                #add_testcase.test_case(method=read_method,url=read_url,parameters=params_parse["expect_parameters"]["query"],params_parse=params_parse)
                interface_res = interface_obj.define_request_method(method=read_method, url=read_url,
                                                                    parameters=params_parse["expect_parameters"]["query"])
                interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)
                #interface_res = test_obj.test_define_request_method(method=read_method, url=read_url,parameters=params_parse["expect_parameters"]["query"])
                #test_obj.test_parse_method_res(response=interface_res, expected_data=params_parse)
            else:
                print 555555555555555555
        elif rows["method"] == "post":
            # print 1121213213123123213213213213
            if len(params_parse["expect_parameters"].keys()) > 1:
                # print params_parse["expect_parameters"]["body"],params_parse["expect_parameters"]["query"]
                # add_testcase = addInterfaceTestCase()
                # add_testcase.test_case(method=read_method, url=read_url,
                # parameters=params_parse["expect_parameters"]["query"],
                # params_parse=params_parse)
                interface_res = interface_obj.define_request_method(method=rows["method"], url=read_url,
                                                                    parameters=params_parse["expect_parameters"]["query"], data=json.dumps(params_parse["expect_parameters"]["body"]))
                # print interface_res
                interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)
                #interface_res = test_obj.test_define_request_method(method=read_method, url=read_url,
                 #                                                   parameters=params_parse["expect_parameters"]["query"])
                #test_obj.test_parse_method_res(response=interface_res, expected_data=params_parse)

    @classmethod
    def tearDown(self):
        pass



#unittest.main(verbosity=1)
suite = unittest.TestSuite()
#a=ParseCsvFile()
#unittest.TextTestRunner().run(suite)
suite.addTest(unittest.makeSuite(ParseCsvFile))
now = str(time())
## filename = "E:\programing\project\interface_testing_python\\report\\"+now+"result2.html"
filename = "F:\\autotest\\report\\" + now + "result2.html"
fp = file(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试测试", description=u"结果结果：")
runner.run(suite)
