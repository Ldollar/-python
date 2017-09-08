# usr/env/bin python
# -*- coding:utf-8 -*-
import logging
import os
from time import sleep

from selenium import webdriver



def quit(driver):
    """离开了"""
    #driver = webdriver.Chrome(r"C:\Users\TY\Downloads\chromedriver_win32(1)\chromedriver.exe")
    #driver.get("http://web.aituyou.me/ins/#/login")
    try:
        logging.info("------beginning quit-----")
        driver.implicitly_wait(20)
        driver.quit()
    except:
        logging.info("---------quite was wrong--------")
        driver.get_screenshot_as_file(os.getcwd())