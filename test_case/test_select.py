# usr/env/bin python
# -*- coding:utf-8 -*-
'''
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from test_case.public import login
from test_case.public import quit_login
import HTMLTestRunner


class TestSelct(unittest.TestCase): #继承TestCase类

    def setUp(self):    #初始化
        self.driver = webdriver.Chrome(r"C:\Users\TY\Downloads\chromedriver_win32(1)\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.get()

        self.verification = []

    def test_select(self):
        """查询操作"""
        login.login(driver=self.driver)
        self.driver.maximize_window()
        sleep(2)
        menu = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/input")#.find_element_by_xpath("/html/body/div[1]/div/div/section/ul/li[2]/ul/li[1]")#("/html/body/div[1]/div/div/section/ul/li[2]/ul/li[1]")
        ActionChains(self.driver).click(menu).perform()
        sleep(1)
        menu1 = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/li[4]")
        ActionChains(self.driver).click(menu1).perform()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/input").send_keys("AMK369")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[2]/button").click()
        sleep(6)


    def tearDown(self): #清除工作
        #self.driver.quit()
        self.assertEqual([],self.verification)

#构造测试集
#def suite():   #quanju suite

    #suite = unittest.TestSuite()
    #suite.addTest(TestSelct("test_select"))  #一个一个添加？ TestLoader？
    #return suite

if __name__=="__main__":
    unittest.main()   #按照单元测试规则，此句即可
    #unittest.main(defaultTest='suite')
    #suite = unittest.TestSuite()
    #suite.addTest(TestSelct("test_select"))

    #执行测试 TextTestRunner?  TestRUnner类-基本执行环境，驱动整个单元测试
    #runner = unittest.TextTestRunner()
    #runner.run(suite)
    #filename = "F:\\autotest\\report\\result.html"
    #fp = file(filename,'wb')
    #print 11111111111111111111111111
    #runner = HTMLTestRunner.HTMLTestRunner(
     #   stream=fp,
     #   title=u"测试报告",            #pycharm单元测试不运行main函数内的内容，所有执行全部代码需要选择，才能生成文档
     #   description=u"用例执行："
    #)
    #runner.run(suite)


'''
