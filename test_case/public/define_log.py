#!usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os

import sys




class LogDefine():
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d : %(message)s",
                            stream=sys.stdout,filename="log.txt")

