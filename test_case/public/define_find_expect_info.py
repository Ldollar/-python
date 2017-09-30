# /usr/bin/env python
# -*- coding:utf-8 -*-
"""解析json文件，获取method code parameters
obj = {
    "post": {
        "parameters": [
            {
                "name": "null",
                "value": {
                    "$ref": "#/definitions/xxxbody"
                }
            }
        ],
        "code": {
            "expect": 0,
            "type": "int"
        },
        "message": {
            "expect": "?",
            "expert_type": "string"
        }
    },
    "get": {
        "name":"",
        "parameters": [
            {
                "name": "asdasd",
                "in":"query",
                "description": "",
                "value": {
                    "mode": "random",
                    "min": 1,
                    "max": 2,
                    "sets": "???????????",
                    "set_value": "random"
                },  # {userId:new023,audiolistId:random} or  {userId:random}
                "type": "??"
            },
            {
                "name": "asd",
                "description": "",
                "value": {
                    "mode": "normal",
                    "min": "null",
                    "max": "null",
                    "sets": "null",
                    "set_value": "new023"
                },
                "type": "??"
            },
            {
                "name": "566565656",
                "description": "",
                "value": {
                    "mode": "random",
                    "min": 1,
                    "max": 2,
                    "sets": "???????????",
                    "set_value": "random"
                },  # {userId:new023,audiolistId:random} or  {userId:random}
                "type": "??"
            },
            {
                "name": ".,/.,f/ds,f",
                "description": "",
                "value": {
                    "mode": "random",
                    "min": 1,
                    "max": 2,
                    "sets": "???????????",
                    "set_value": "random"
                },  # {userId:new023,audiolistId:random} or  {userId:random}
                "type": "??"
            }
        ],
        "code": {
            "expect": 0,
            "type": "int"
        },
        "message": {
            "expect": "??",
            "type": "string"
        }
    },
    "definitions": {
        "xxxSchemaValue": {
            "properties": [
                {
                    "name": "xxx",
                    "value": {
                        "type": "normal",
                        "min": "null",
                        "max": "null",
                        "sets": "null",
                        "set_value": "new023"
                    },
                    "type": "??"
                },
                {
                    "name": "expect_info am random str",
                    "description": "",
                    "value": {
                        "type": "random",
                        "min": 1,
                        "max": 2,
                        "sets": "???????????",
                        "set_value": " random(sets)"
                    },
                    "type": "??"
                }
            ]
        }
    }
}



obj2 = {

    "post": {
        "parameters": {
            "query":{
                "name": "123",
                "name1": "123",
                "name2": "random"
            },
            "body":{
                "device_id": "new023",
                "mode": "time",
                "frequency": "15",
                "type": [
                    "all"
                ],
                "expiry": "86400000",
                "event": "",
                "compress": "base64"
            }
        },

        "code": 0,
        "message": "wo wowowowowowowowowowow111111"
    }
}
"""
obj3={


            "query": {
                "device_id": "new023"
            },
            "body": {
                "device_id": "new023",
                "mode": "time",
                "frequency": "15",
                "type": [
                    "all"
                ],
                "expiry": "86400000",
                "event": "",
                "compress": "base64"
            }

}


import logging

import json
import define_random_str
from define_log import LogDefine
from test_case.public.define_find_expect_csv import FindCsvFile
from test_case.public.define_regex import match_string

LogDefine()


def by_protocol(obj):
    expect_json = json.loads(json.dumps(obj, indent=4))
    parameters_dict = {}
    expect_code = None
    # print s

    for expect_method in expect_json:
        # print expect_method
        # print s[expect_method]
        if expect_method == 'get':
            logging.info("this is get method,now let go")
            for expect_info in expect_json[expect_method]:
                logging.info("the value is %s", expect_info)
                if expect_info == "code":
                    logging.info("now let us find the expect code number")
                    # print expect_json[expect_method]["code"]["expect"]
                    expect_code = expect_json[expect_method]["code"]["expect"]

                    # print s[expect_method]["code"]["type"]
                elif expect_info == "parameters":
                    logging.info("now let us find the parameters")
                    for expect_param_info in expect_json[expect_method]["parameters"]:
                        if expect_param_info["name"]:
                            logging.info("check the value whether random or normal")
                            # print expect_param_info["name"]
                            if expect_param_info["value"]["mode"] == "random":
                                logging.info("the value is random")
                                random_string = define_random_str.random_str()
                                # print random_string
                                parameters_dict[expect_param_info["name"]] = random_string
                            else:
                                logging.info("the value is normal")
                                parameters_dict[expect_param_info["name"]] = expect_param_info["value"]["set_value"]
                        else:
                            logging.warning("this field is not parameters???")
                elif expect_info == "message":
                    logging.info("maybe need judge the message info")
                    pass
                else:
                    logging.warning("json object maybe wrong?")
                    pass

    print parameters_dict, expect_code


# 解析expect_json ，json信息，返回一个字典
def get_json_obj_info(expect):  # expect  type ：json   格式为obj2

    expect_json = json.loads(json.dumps(expect, indent=4))
    logging.info("expect_json type is %s ", type(expect_json))
    # print type(expect_json)
    expect_set_info = {}
    expect_parameters_query_dict = {}
    expect_parameters_body_dict = {}
    expect_parameters_in_dict = {}  # 保存 expect_parameters_query_dict or expect_parameters_body_dict
    if expect:
        for method in expect_json:
            logging.info(u"开始遍历expect_json")
            #print expect_json[method]
            if type(expect_json[method])==dict:
                #print 11111111111111111111111111111
                logging.info("i am a dict !!!!!!!")
                expect_set_info["expect_method"] = method
                #print type(expect_json[method])
                for expect_info in expect_json[method]:
                    # print expect_json[method]
                    if expect_info == "code":
                        logging.info("i am a code %s: ", expect_info)
                        # print expect_json[method][expect_info]
                        expect_set_info["expect_code"] = expect_json[method][expect_info]
                    elif expect_info == "parameters":
                        logging.info("i am a parameters %s: ", expect_info)
                        # print expect_json[method][expect_info]
                        for expect_in in expect_json[method][expect_info]:
                            logging.info("right here now expect_in")
                            # print expect_in
                            if expect_in == "query":
                                logging.info("this is query parameters")
                                # print expect_json[method][expect_info][expect_in]
                                for judge_name_value in expect_json[method][expect_info][expect_in]:
                                    logging.info("right here now judge_set_value")
                                    # print judge_name_value
                                    # print expect_json[method][expect_info][expect_in][judge_name_value]
                                    # if expect_json[method][expect_info][expect_in][judge_name_value] == "random":
                                    whether_random = match_string(rules="random\\((\S+)\\)",
                                                                  text=expect_json[method][expect_info][expect_in][
                                                                      judge_name_value])
                                    if whether_random:
                                        #print u"----i am a random value ----", whether_random
                                        # print judge_name_value
                                        logging.info("the value is random")
                                        Rd = define_random_str.defineRandom(minlength=int(whether_random[0]),maxlength=int(whether_random[1]),type=whether_random[2])
                                        expect_parameters_query_dict[judge_name_value] = Rd.random_str()
                                        #print u"expect_parameters_query_dict[judge_name_value]---random",expect_parameters_query_dict[judge_name_value]
                                    else:
                                        # print judge_name_value
                                        logging.info("the value is normal")
                                        # print expect_json[method][expect_info][expect_in][judge_name_value]
                                        expect_parameters_query_dict[judge_name_value] = expect_json[method][expect_info][expect_in][judge_name_value]
                                # print expect_parameters_query_dict
                                expect_parameters_in_dict[expect_in] = expect_parameters_query_dict
                                # print expect_parameters_in_dict
                            elif expect_in == "body":
                                logging.info("this is query parameters")
                                # print expect_json[method][expect_info][expect_in]
                                for judge_name_value in expect_json[method][expect_info][expect_in]:
                                    logging.info("right here now judge_set_value")
                                    #print judge_name_value
                                    #print u"expect_json[method][expect_info][expect_in]等于",expect_json[method][expect_info][expect_in][judge_name_value]
                                    whether_random = match_string(rules="random\\((\S+)\\)",
                                                                  text=expect_json[method][expect_info][expect_in][
                                                                      judge_name_value])
                                    #print u"whether_random,是否随机",whether_random
                                    if whether_random:
                                        #print u"----i am a random value ----",judge_name_value
                                        logging.info("the value is random")
                                        Rd = define_random_str.defineRandom(minlength=int(whether_random[0]),
                                                                            maxlength=int(whether_random[1]),
                                                                            type=whether_random[2])
                                        expect_parameters_query_dict[judge_name_value] = Rd.random_str()
                                        #print u"expect_parameters_query_dict[judge_name_value]---random",expect_parameters_query_dict[judge_name_value]
                                    else:
                                        #print u"i am a normal value"
                                        logging.info("the value is normal")
                                        # print expect_json[method][expect_info][expect_in][judge_name_value]
                                        expect_parameters_body_dict[judge_name_value] = expect_json[method][expect_info][expect_in][judge_name_value]
                                # print expect_parameters_body_dict
                                if expect_parameters_body_dict:
                                    logging.info("judge the expect_parameters_body_dict whether have length")
                                    expect_parameters_in_dict[expect_in] = expect_parameters_body_dict
                                else:
                                    pass

                        expect_set_info["expect_parameters"] = expect_parameters_in_dict
                        # expect_set_info["expect_parameters_query_dict"] = expect_json[method][expect_info]
                    elif expect_info == "message":
                        logging.info("i am a message %s: ", expect_info)
                        # print expect_json[method][expect_info]
                        expect_set_info["expect_message"] = expect_json[method][expect_info]
                    else:
                        logging.info("please check the info of json file")
                        print u"是否加入不需要的参数"
            else:
                logging.warning("i am int ,i can do many things")
        # print expect_parameters_query_dict
        return expect_set_info
    else:
        return expect_set_info


# 装饰器对数据json化？？？
def get_parameters_json_info(expect_parameters):
    try:
        expect_json = json.loads(expect_parameters)
        #print type(expect_json)
        return expect_json
    except:
        print u"请在文档中输入《json格式》的parameters参数"
#a = FindCsvFile.find_interface_info_by_csv()

#装饰器判断是否是需要的字符串？？？
def get_url_info(url_info):
    """拼接URL字符串"""
    try:
        protocal=url_info["request_protocal"]
        host=url_info["host"]
        base_path=url_info["base_path"]
        path=url_info["paths"]
        url = protocal+"://"+host+base_path+path
        #print url
        return url
    except Exception,e:
        print u"检查CSV文件的每个字段是否出错 request_protocal ，host，base_path，paths %s"%e
        return None

#判断返回值是否为int
def get_assert_code_info(code_info):

    expect_int_compare={}
    expect_code = code_info
    expect_int_compare["expect_code_int"]=int(expect_code.split(":")[1])
    expect_int_compare["expect_str"] = expect_code.split(":")[0].strip('"')
    return expect_int_compare

def get_method_info(method_info):

    try:
        method = method_info
        return method
    except Exception,e:
        print u"检查CSV文件的 'method' 字段是否出错  %s  " % e
        return None





a = FindCsvFile()
b = a.find_interface_info_by_csv(path=r"F:\autotest\ssssss111.csv")
#a=get_parameters_json_info()
#print b[2]
#bc=get_url_info(url_info=b)
##print c

#for zz in b:
    #print zz
    #ss=get_parameters_json_info(expect_parameters=zz["parameters_json"])
    #print ss
    #print zz
    #n=get_url_info(url_info=zz)
    #n=get_assert_code_info(code_info=zz["assert_code"])
    #n = get_method_info(method_info=zz)
    #print n[1]
    #print n
    #read_json = json.loads(zz["expect_json"])
    #print read_json["time"]
    #ss=get_json_obj_info(expect=read_json)
    #print ss
