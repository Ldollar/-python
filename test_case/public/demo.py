# coding=utf-8
# -*- coding:utf-8 -*-
import json
import unittest

import logging
import swaggerpy
from swaggerpy.client import SwaggerClient
from swaggerpy.http_client import SynchronousHttpClient

from test_case.public import define_regex
from test_case.public import get_response
from test_case.public.define_log import LogDefine


class TestSerch(unittest.TestCase):
    def setUp(self,method, url):
        LogDefine()
        self.parameters = {"keywords": "prh<1+,expect_info/6\3%V0a]%9-n[6IrJPW3\CHx+,$3;)/H;\)EB;f0g5:sGmH|+d%wEWHXGg|!B/5#KwG:3hA$LpU?>7,O?(o5|eLGBYq"}
        self.verification = []
        self.res = get_response.make_request(method=method, url=url, parameters=self.parameters)

    def test_searchxmly(self):
        """喜马拉雅音乐搜索"""
        res = self.res
        response_code = res.status_code
        if response_code == 200:
            logging.info("get code == 200 ,request success!")
            print "返回200，响应成功"
            print res.text
            s=define_regex.find_code(text=res.text)
            if s>=0 :
                logging.info("correct response code: %s ",s)
                print u"返回正确 code: %s" %s
            else:
                logging.error("incorrect response code: %s",s)
                print u"接口请求失败 code: %s " %s
        else:
            logging.error("not return code 200 ,maybe hava some problem")
            print u"响应出错 code %s" %response_code

    def tearDown(self):
        self.assertEqual([],self.verification)

if __name__=="__main__":
    unittest.main()