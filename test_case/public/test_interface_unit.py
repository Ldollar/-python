# /usr/bin/env python
# -*- coding:utf-8 -*-
import json
import unittest
from time import time
import HTMLTestRunner
import logging
from nose_parameterized import param
from nose_parameterized import parameterized

from define_find_expect_csv import FindCsvFile
from define_find_expect_json import get_json_obj_info
from define_log import LogDefine

from define_compare_info import InterfaceModel

a = FindCsvFile()
b = a.find_interface_info_by_csv(path=r"F:\autotest\ssssss111.csv")
LogDefine()


class InterfaceCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        pass

    @parameterized.expand(
        param.explicit([b[i]])
        for i, k in enumerate(b)
    )
    def test_interface(self, rows):
        logging.info("beginnig test_interface")
        read_json = json.loads(rows["expect_json"])
        read_url = rows["url"]
        read_method = rows["method"]
        # print read_method ,read_url
        # print read_json
        params_parse = get_json_obj_info(expect=read_json)
        # print u"55555555555555555555555555",params_parse,type(params_parse)
        # print params_parse["expect_parameters"].keys()
        interface_obj = InterfaceModel()

        if rows["method"] == "get":
            logging.info("the request method is %s", rows["method"])
            # print params_parse["expect_parameters"].keys()[0}
            if len(params_parse["expect_parameters"].keys()) == 1 and params_parse["expect_parameters"].keys()[
                0] == "query":
                logging.info("parameters contain query ....")
                # interface_res = interface_obj.define_request_method(method=read_method, url=read_url,
                #                                                    parameters=params_parse["expect_parameters"][
                #                                                        "query"])
                # interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)
                count1 = 0
                for i in xrange(1, read_json["time"] + 1):
                    #count1 = 0
                    count1 = count1+1
                    print u'-------------------------%s--------------------------' % (count1)
                    params_parse = get_json_obj_info(expect=read_json)
                    #print params_parse
                    interface_obj.iteration_request(method=read_method, url=read_url,
                                                    parameters=params_parse["expect_parameters"]["query"],
                                                    expected_data=params_parse)
            else:
                logging.info("the parameters maybe contained other method")
        elif rows["method"] == "post":
            logging.info("the request method is %s", rows["method"])
            if len(params_parse["expect_parameters"].keys()) > 1:
                logging.info("parameters contained query or body and so on")
                # interface_res = interface_obj.define_request_method(method=rows["method"], url=read_url,
                #                                                    parameters=params_parse["expect_parameters"][
                #                                                        "query"], data=json.dumps(
                #        params_parse["expect_parameters"]["body"]))

                # interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)
                count2=0
                for i in xrange(1, read_json["time"] + 1):
                #for i in read_json["time"]:
                    count2 = count2+1
                    print u'-------------------------%s--------------------------'%(count2)
                    params_parse = get_json_obj_info(expect=read_json)
                    #print params_parse
                    interface_obj.iteration_request(method=read_method, url=read_url,
                                                    parameters=params_parse["expect_parameters"]["query"],data=json.dumps(params_parse["expect_parameters"]["body"]),
                                                    expected_data=params_parse)
    @classmethod
    def tearDown(self):
        pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(InterfaceCase))
now = str(time())
filepath = "F:\\autotest\\report\\" + now + "result2.html"  # 配置报告存放位置
fp = file(filepath, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"接口测试", description=u"音乐：")
runner.run(suite)
