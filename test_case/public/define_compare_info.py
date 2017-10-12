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
                print u"响应时间 : %s" % res.elapsed
                return res

            else:
                logging.error("not return code 200 ,request hava some problem")
                print res.url
                print u"响应出错 code %s" % http_code
                print res.text
        except Exception, e:
            logging.info(u"请求出问题了 %s ", e)
            print e



    def parse_method_res(self, response,messages=None, code1=None):

        """对返回数据处理分析"""
        try:
            error_message ={}
            s = define_regex.find_code(text=response.text,rex_str=code1["expect_str"])
            logging.info("type vs type %s vs %s", type(s), type(code1["expect_code_int"]))
            if int(s) == code1["expect_code_int"]:
                logging.info("correct response code: %s ", s)
                print u"返回正确 %s: %s" % (code1["expect_str"],s)
                if messages :
                    #print messages

                    for i in xrange(0,len(messages)):
                        #print i,messages[i][0]

                        compare_str = define_regex.find_message(res=response.text,res_str_zhongwen=messages[i][0])
                        #print response.text
                        #print i,123456,compare_str
                        #print ("type vs type %s vs %s", type(compare_str), type(messages["message_info"]))
                        #print compare_str,messages["message_info"]
                        #print "value123456",str(messages[i][1])
                        if str(compare_str) == str(messages[i][1]):
                            print u"第 %s 次验证信息正确 %s: %s" % (i+1,messages[i][0], compare_str)

                        else:
                            error_message[messages[i][0]]=compare_str
                            print u"第 %s 次验证信息不正确，验证信息为 %s : %s" %(i+1,messages[i][0],messages[i][1])
                            print u"第 %s 次验证信息不正确,从接口获得的信息为  %s: %s" % (i+1,messages[i][0], compare_str)
                            #print u"返回的Response信息 ：%s " %response.json()

                    if error_message:
                        print u"验证信息不正确 : %s" % error_message
                        print u"返回的Response信息为 : %s " % response.json()

                    else:
                        print u"验证信息正确 , 666"

            else:
                logging.error("incorrect response code: %s", s)
                # self.verification.append("incorrect response")
                print u"接口请求失败 code: %s " % s
                print u"------------------------------------------------"

        except Exception, e:
            logging.info(u"Response 可能没有获取到并且检查assert条件是否设置妥当  %s ", e)
            print u"Response 可能没有获取到 %s" % e

        print "-----------------------------------------------------------------------------------"
    def iteration_request(self, method, url, parameters, data=None, expected_data=None):

        res_iter = self.define_request_method(method, url, parameters,data)
        self.parse_method_res(expect_data=expected_data, response=res_iter)




a = InterfaceModel()



