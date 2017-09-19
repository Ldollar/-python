# -*- coding:utf-8 -*-
import unittest
import sys
import HTMLTestRunner
from time import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

#import allcase_list
sys.path.append("\\test_case")
from test_case import *
from test_case import test_login
from test_case import test_select
reload(sys)

sys.setdefaultencoding('utf8')



testunit = unittest.TestSuite()

#将测试用例加入到测试容器（套件）中
#testunit.addTest(unittest.makeSuite(baidutest.BaiduTest))
#testunit.addTest(unittest.makeSuite(youdaotest.Youdao))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
#unittest.TestLoader.d

# 将用例组装数组
#alltestnames=allcase_list.caselist()   # 也可以通过TestLoader.discover获得
#创建测试套件
#testsuite=unittest.TestSuite()

#循环读取数组中 的用例

#for test in alltestnames:
    #testsuite.addTest(unittest.makeSuite(test)) #makesuite用于生产testsuite对象的实例

#runner= HTMLTestRunner()

#runner.run(testsuite)

#dicover 方法定义
def createsuite(listdir= r"F:\\autotest\\test_case"):

    #listdir = "E:\programing\project\interface_testing - python\test_case"
    discover = unittest.defaultTestLoader.discover(listdir,pattern='test_*.py')
    print discover
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print testunit
    return testunit
    #添加测试用例
    #testunit.addTest(unittest.makeSuite(test_login.TestLogin))  #一个一个添加？不便管理
    #testunit.addTest(unittest.makeSuite(test_select.TestSelct))
alltestnames =createsuite()
now = str(time())
#filename = "E:\programing\project\interface_testing_python\\report\\"+now+"result2.html"
filename = "F:\\autotest\\report\\"+now+"result2.html"
fp = file(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试测试" ,description=u"结果结果：")
runner.run(alltestnames)
