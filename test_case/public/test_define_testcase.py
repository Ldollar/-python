# /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from unittest import TestCase

from test_case.public.define_find_expect_csv import control_csv_file
#from test_case.test_get_model import InterfaceModel

path=r"E:\programing\project\interface_testing_python\ssssss111.csv"
class addInterfaceTestCase(TestCase):
    def setup(self):
        pass

    def __generateTestCases(self):
        arglists = [('arg11', 'arg12'), ('arg21', 'arg22'), ('arg31', 'arg32')]
        for args in arglists:
            setattr(addInterfaceTestCase, 'test_func_%s_%s' % (args[0], args[1]),
                    addInterfaceTestCase.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员

    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.getTest(arg1, arg2)

        return func
    def test_case(self):#method,url,parameters,params_parse):
        #interface_obj = InterfaceModel()
        #interface_res = interface_obj.define_request_method(method=method, url=url,
                                                            #parameters=parameters)
        #interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)
        control_csv_file(path=path)
        #aaa=addInterfaceTestCase()
        #aaa.__generateTestCases()

    def tearDown(self):
        pass

#class addInterfaceTestCase(BaseJsonTestCase):
    #def test_case(self,method,url,parameters,params_parse):
     #   interface_obj = InterfaceModel()
      #  interface_res = interface_obj.define_request_method(method=method, url=url,
       #                                                     parameters=parameters)
#        interface_obj.parse_method_res(response=interface_res, expected_data=params_parse)
#
if __name__=="__main__":
    aaa = addInterfaceTestCase()
    aaa.__generateTestCases()
    unittest.main()