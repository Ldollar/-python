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


#test = pinyin.get_pinyin()

#dir_math = os.path.abspath(os.getcwd())
#for dirpath, dirnames, filenames in os.walk(dir_math+"\\songAndimage\\" + "chezaiyinyue" + "\\"):

    #for filename in filenames:
        #s = filename.split(".")[0]
        #if s.decode("gbk").encode("utf-8") == "公路之歌":
            #print s.decode("gbk").encode("utf-8")
            #test = pypinyin.lazy_pinyin(s.decode("gbk"))
            #print ''.join(test)

#print u"Tragédie - Hey Oh"
