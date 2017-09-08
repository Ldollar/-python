# -*- coding:utf-8 -*-
"""
python 在执行import语句时，进行什么操作
1. 创建一个新的，空的module（可能包含多个module）
2. 把这个module对象插入sys.module中
3. 装载module的代码（如果需要，首先先编译）
4. 执行新的module中对应的代码

    执行第3步，找到module所在路径：
    当前路径（以及从当前目录指定的sys.path），然后是Pythonpath，
    当前路径或者pythonpath中存在于标准module同样的module，则会覆盖
    eg。1
    当前目录有xml.py  执行import xmlshi，导入的是当前目录下的module，而不是系统标准的xml


__init__ : 标识这是一个可引用的包
所有的测试用例放在此文件夹下

"""
