# -*- coding:utf-8 -*-
import mock as mock
import unittest

class Count():
    def add(self):
        pass



class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13)
        result= count.add(8,5)
        print result
        self.assertEqual(result,13)


if __name__ == '__main__':
    unittest.main()