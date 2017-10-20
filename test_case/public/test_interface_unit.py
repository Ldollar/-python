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
from define_find_expect_info import get_json_obj_info, get_url_info, get_method_info, get_parameters_json_info, \
    get_assert_code_info, get_assert_message_info
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
        params_parse = get_parameters_json_info(expect_parameters=rows["parameters_json"])
        read_url = get_url_info(url_info=rows)  # 封装expect——info类，初始化就获得CSV信息
        read_method = get_method_info(method_info=rows["method"])
        read_code = get_assert_code_info(code_info=rows["assert_code"])
        read_message = get_assert_message_info(message_info=rows["assert_message"])
        interface_obj = InterfaceModel()

        if rows["method"] == "get":
            logging.info("the request method is %s", rows["method"])
            if len(params_parse.keys()) == 1 and params_parse.keys()[0] == "query":
                logging.info("parameters contain query ....")
                interface_res = interface_obj.define_request_method(method=read_method, url=read_url,
                                                                    parameters=params_parse["query"])
                interface_obj.parse_method_res(response=interface_res, code1=read_code, messages=read_message)

            else:
                print u"this is a 'get' method ,it just included query parameters"
                logging.info("the parameters maybe contained other method")
        elif rows["method"] == "post":
            logging.info("the request method is %s", rows["method"])
            if len(params_parse.keys()) > 1:
                logging.info("parameters contained query or body and so on")
                interface_res = interface_obj.define_request_method(method=rows["method"], url=read_url,
                                                                    parameters=params_parse["query"], data=json.dumps(
                        params_parse["body"]))  # json.dumps变成一个json字串

                interface_obj.parse_method_res(response=interface_res, code1=read_code, messages=read_message)

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
