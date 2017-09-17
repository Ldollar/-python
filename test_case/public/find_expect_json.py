# /usr/bin/env python
# -*- coding:utf-8 -*-
import logging

import json
from test_case.public import define_random_str
from test_case.public.define_log import LogDefine

LogDefine()
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
        "parameters": [
            {
                "name": "asdasd",
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
        "parameters": [

                {
                    "name": "123",
                    "name1": "123",
                    "name2": "random"

                }
        ],
        "code": 0,
        "message": "qweqweqweqweq"
    },
    "get": {
        "parameters": [
            {
                "name": "123",
                "name1": "123",
                "name2": "random"

            }
        ],
        "code": 0,
        "message": "wo wowowowowowowowowowow"
    }

}


def by_protocol():
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
                    #print expect_json[expect_method]["code"]["expect"]
                    expect_code = expect_json[expect_method]["code"]["expect"]

                    # print s[expect_method]["code"]["type"]
                elif expect_info == "parameters":
                    logging.info("now let us find the parameters")
                    for expect_param_info in expect_json[expect_method]["parameters"]:
                        if expect_param_info["name"]:
                            logging.info("check the value whether random or normal")
                            #print expect_param_info["name"]
                            if expect_param_info["value"]["mode"] == "random":
                                logging.info("the value is random")
                                random_string = define_random_str.random_str()
                                #print random_string
                                parameters_dict[expect_param_info["name"]] = random_string
                            else:
                                logging.info("the value is normal")
                                parameters_dict[expect_param_info["name"]] = expect_param_info["value"]["set_value"]
                elif expect_info == "message":
                    logging.info("maybe need judge the message info")
                    pass
                else:
                    logging.warning("json object maybe wrong?")
                    pass

    print parameters_dict,expect_code

def get_json_obj():

    expect_json = json.loads(json.dumps(obj2, indent=4))
    #print expect_json
    expect_set_info={}
    expect_parameters_dict={}
    for method in expect_json:
        expect_set_info["expect_method"]=method
        #print expect_json[method]
        for expect_info in expect_json[method]:
            if expect_info=="code":
                logging.info("i am a code %s: ",expect_info)
                print expect_json[method][expect_info]
                expect_set_info["expect_code"] = expect_json[method][expect_info]
            elif expect_info=="parameters":
                logging.info("i am a parameters %s: ", expect_info)
                #print expect_json[method][expect_info]
                for expect_value in expect_json[method][expect_info]:
                    logging.info("right here now expect_value")
                    for judge_set_value in expect_value:
                        logging.info("right here now judge_set_value")
                        if expect_value[judge_set_value] == "random":
                            logging.info("the value is random")
                            expect_parameters_dict[expect_value[judge_set_value]] = define_random_str.random_str()
                        else:
                            logging.info("the value is normal")
                            expect_parameters_dict[expect_value[judge_set_value]] = expect_value[judge_set_value]

                expect_set_info["expect_parameters"]=expect_parameters_dict
                #expect_set_info["expect_parameters_dict"] = expect_json[method][expect_info]
            elif expect_info == "message":
                logging.info("i am a message %s: ", expect_info)
                print expect_json[method][expect_info]
                expect_set_info["expect_message"] = expect_json[method][expect_info]
            else:
                logging.info("please check the info of json file")
                print u"是否加入不需要的参数"
    #print expect_parameters_dict
    return expect_set_info

a = get_json_obj()
print a