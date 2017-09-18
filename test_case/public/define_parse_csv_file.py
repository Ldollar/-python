# /usr/bin/env python
# -*- coding:utf-8 -*-
import json

#from test_case.public.define_find_expect_csv import control_csv_file
from test_case.public.define_find_expect_json import get_json_obj_info
#from test_case.public.test_define_testcase import addInterfaceTestCase
from test_case.test_get_model import InterfaceModel

#aaaaa=control_csv_file(path=r"E:\programing\project\interface_testing_python\ssssss111.csv")
def model123(rows):
    #reader=control_csv_file(path=r"E:\programing\project\interface_testing_python\ssssss111.csv")
    #for i, rows in enumerate(reader):
    read_json = json.loads(rows["expect_json"])
    read_url = rows["url"]
    read_method = rows["method"]
    # expect_in = read_json
    # print read_method ,read_url
    # print read_json
    params_parse = get_json_obj_info(expect=read_json)
    # print params_parse["expect_parameters"].keys()
    interface_obj = InterfaceModel()

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
                                                                parameters=params_parse["expect_parameters"]["query"], data=json.dumps(
                    params_parse["expect_parameters"]["body"]))
            # print interface_res
            interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)

#model()