# usr/env/bin python
# -*- coding:utf-8 -*-
import logging
import os
from time import sleep
import unittest
from selenium import webdriver


def login(driver):
    #driver = webdriver.Chrome(r"C:\Users\TY\Downloads\chromedriver_win32(1)\chromedriver.exe")

    try:
        logging.info("------beginning login-----")
        driver.implicitly_wait(20)
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("")
        driver.find_element_by_class_name("login_container").click()
        #sleep(2)
    except:
        logging.info("---------login was wrong--------")
        driver.get_screenshot_as_file(os.getcwd())

