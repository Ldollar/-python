# coding:utf-8
#存放用例名字
#把test_case目录添加到path下，相对路径
import  sys

from test_case import *

sys.path.append("\\test_case")
from  test_case import *

#用例文件列表
def caselist():
    alltestnames = [
        #baidutest.BaiduTest,
        #youdaotest.Youdao
    ]
    print "sucess read case list!!"

    return alltestnames