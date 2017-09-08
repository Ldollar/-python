# -*- coding:utf-8 -*-
import os
"""
caselist=os.listdir("F:\\autotest\\test_case")
for a in caselist:
    s= a.split('.')[-1]
    if s == "py":
        os.system("F:\\autotest\\test_case\\%s 1>>log.txt 2>&1" %a)
        # 2. 2>&1是什么意思？2>&1应该分成两个部分来看,
        # 一个是2>以及另一个是&1，其中2>就是将标准出错重定向到某个特定的地方；
        # &1是指无论标准输出在哪里。所以2>&1的意思就是说无论标准出错在哪里(哪怕是没有?)，
        # 都将标准出错重定向到标准输出中。
"""

