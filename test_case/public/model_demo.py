# /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest


class Test(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        def isParameterizedMethod(attrname):
            return attrname.startswith("param") and hasattr(getattr(self, attrname), '____')      #hasattr判断对象object的属性 ,getattr获得object属性值

        testFnNames = filter(isParameterizedMethod, dir(self))
        for func in testFnNames:
            name = func.split("_", 1)[1]
            collect = "collection_" + name
            if hasattr(getattr(self, collect), '__call__'):
                collectFunc = getattr(self, collect)
                array = collectFunc()
                for index in xrange(len(array)):
                    test = "%s_%d" % (name, index)
                    setattr(self.__class__, test, getattr(self, func)(array[index]))

        # must ed at last
        unittest.TestCase.__init__(self, methodName)