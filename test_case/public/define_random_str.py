# -*- coding:utf-8 -*-

from random import Random


def random_str(randomlength=10):
    str = ''

    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()<>?/{}[]|,.;:\+-~ '

    length = len(chars) - 1

    random = Random()

    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return (str)
    #print str
#random_str()