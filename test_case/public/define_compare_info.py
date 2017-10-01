# coding=utf-8
# -*- coding:utf-8 -*-


HTTP_CODE_SUCCESS = 200

import json

import logging
from swaggerpy.http_client import SynchronousHttpClient

import define_regex
from define_log import LogDefine


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
        try:
            res = self.http_client.request(method=method, url=url, params=parameters, data=data)
            s = self.http_client.session
            s.keep_alive = False
            http_code = res.status_code
            if http_code == HTTP_CODE_SUCCESS:
                logging.info("if code == 200 ,request success!")
                print u"返回200，请求成功", res.url
                #print res.text
                print u"响应时间 : %s" % res.elapsed
                #print u"eeeeeeeeeeeeeeeeeeeeeeeeeeee",type(res.json())
                return res

            else:
                logging.error("not return code 200 ,request hava some problem")
                print res.url
                print u"响应出错 code %s" % http_code
                print res.text
        except Exception, e:
            logging.info(u"请求出问题了 %s ", e)
            print e

    #def parse_method_res(self, response, expected_data=None):

    def parse_method_res(self, code1, response):

        """对返回数据处理分析"""
        try:
            #print 1111111111111111111111
            data = code1
            #print u"expexct_data",data,type(data)
            #print u"ereponse 111111````",response
            #print u"expect---code",type(data["expect_code"]),data["expect_code"]
            #print "+++++++++++++++++++++++++++++++"
            s = define_regex.find_code(text=response.text,rex_str=code1["expect_str"])
            #print s
            #print type(s),type(code1["expect_code_int"])
            logging.info("type vs type %s vs %s", type(s), type(code1["expect_code_int"]))
            #print int(s)
            if int(s) == code1["expect_code_int"]:
                logging.info("correct response code: %s ", s)
                print u"返回正确 %s: %s" % (code1["expect_str"],s)
                if None :
                    pass
            else:
                logging.error("incorrect response code: %s", s)
                # self.verification.append("incorrect response")
                print u"接口请求失败 code: %s " % s
                print u"------------------------------------------------"

        except Exception, e:
            logging.info(u"Response 可能没有获取到并且检查assert条件是否设置妥当  %s ", e)
            print u"Response 可能没有获取到 %s" % e


    def iteration_request(self, method, url, parameters, data=None, expected_data=None):

        res_iter = self.define_request_method(method, url, parameters,data)
        self.parse_method_res(expect_data=expected_data, response=res_iter)




a = InterfaceModel()
#s=a.iteration_request(method="get", url="http://121.40.68.137:12008/api/v1/media/audio",
                    #parameters={"audioId": "random(1,2,3)"},expected_data={'expect_method': 'get', 'expect_message': 'wo wowowowowowowowowowow', 'expect_code': 0,"parameters": {"query": { "audioId": "random(1,2,3)"}}})
#print s
# s=a.define_request_method(method="get",url="http://api.aituyou.me:8000/xbot/v1/audio/categorylist?type=music",parameters={
#            "audiolistId": "ajsflkjal",
#            "start":"1",
#            "count":"10"
#        })
# print s.json()
# a.parse_method_res(response=s)
