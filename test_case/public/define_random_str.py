# -*- coding:utf-8 -*-
"""type 1:
    type 2:










"""
from random import Random, random
class defineRandom():
#指定长度，指定字符集
    #def __init__(self,minlength=None,maxlength=None,type=None):
    def __init__(self):
        # self.type = type
        # self.minlength= minlength
        # self.maxlength= maxlength
        pass
    def random_rd(self,minlength,maxlength,charset):


        str = ''

        #chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()<>?/{}[]|,.;:\+-~ '
        if charset==3:
            chars = charset

            length = len(chars) - 1

            random = Random()

            if maxlength <= 0:
                str = ''
                return (str)

            elif maxlength == "random":
                for i in xrange(minlength, random.randint(minlength, random()) + 1):
                    str += chars[random.randint(0, length)]
            else:
                for i in xrange(minlength, random.randint(minlength, maxlength) + 1):
                    # print i
                    str += chars[random.randint(0, length)]

                return (str)

    #随机任意长度的字符串，包含数字字母特殊字符，min代表最小长度，max代表最大长度
    def random_str(self,minlength=None,maxlength=None):
        str = ''

        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()<>?/{}[]|,.;:\+-~ '

        length = len(chars) - 1

        random = Random()

        if maxlength <= 0:
            str=''
            return (str)

        else:
            for i in xrange(minlength,random.randint(minlength,maxlength)+1):
                #print i
                str += chars[random.randint(0, length)]

            return (str)

    #生成0-9 任意一个数字
    def random_int(self,minlength,maxlength):
        random = Random()
        integer=random.randint(minlength,maxlength)
        return integer
    #生成 任意长度的数字

    #生成指定的list中任意一个
    def random_set(list):
        random = Random()
        value = random.choice(list)     #这个貌似比较简便
        return value

