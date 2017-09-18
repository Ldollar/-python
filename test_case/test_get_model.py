# coding=utf-8
# -*- coding:utf-8 -*-
from test_case.public import define_random_str

HTTP_CODE_SUCCESS = 200

import json

import logging
from swaggerpy.http_client import SynchronousHttpClient

from test_case.public import define_regex
from test_case.public.define_log import LogDefine


class InterfaceModel():
    def __init__(self):
        LogDefine()
        self.http_client = SynchronousHttpClient()
        # self.host
        # self.port
        # self.method
        # self.parameters
        # self.data
        self.verification = []

    def define_request_method(self, method, url, parameters=None, data=None):

        """请求模板"""
        res = self.http_client.request(method=method, url=url, params=parameters, data=data)
        http_code = res.status_code
        if http_code == HTTP_CODE_SUCCESS:
            logging.info("if code == 200 ,request success!")
            print u"返回200，请求成功", res.url
            print res.text
            return res

        else:
            logging.error("not return code 200 ,request hava some problem")
            print res.url
            print u"响应出错 code %s" % http_code
            print res.text

    def parse_method_res(self, response, expected_data=None):

        """对返回数据处理分析"""
        data = json.loads(json.dumps(expected_data))
        print data["expect_code"]
        s = define_regex.find_code(text=response.text)
        print type(s),type(data["expect_code"])
        if int(s) == data["expect_code"]:
            logging.info("correct response code: %s ", s)
            print u"返回正确 code: %s" % s
        else:
            logging.error("incorrect response code: %s", s)
            # self.verification.append("incorrect response")
            print u"接口请求失败 code: %s " % s


a=InterfaceModel()
#s=a.define_request_method(method="get",url="http://api.aituyou.me:8000/xbot/v1/audio/categorylist?type=music",parameters={
#            "audiolistId": "ajsflkjal",
#            "start":"1",
#            "count":"10"
#        })
# print s.json()
##a.parse_method_res(response=s,judge_code=0)
