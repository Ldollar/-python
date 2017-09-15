# coding=utf-8
# -*- coding:utf-8 -*-
import unittest
from time import sleep

from selenium import webdriver

from test_case.public import login
from test_case.public import quit_login


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\TY\Downloads\chromedriver_win32(1)\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.get("")

        self.verification = []

    def test_login(self):
        """登录操作"""
        login.login(driver=self.driver)
        sleep(2)

    #def test_quit_login(self):
        #quit_login.quit(driver=self.driver)
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([],self.verification)

if __name__=="__main__":
    unittest.main()
