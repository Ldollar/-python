# /usr/bin/env python
# -*- coding:utf-8 -*-

import functools
import json
import logging

import time

import sys


def requires_ints(func):
    @functools.wraps(func)
    def check_int(*args,**kwargs):

        kwargs_values=[i for i in kwargs.values()]
        for arg in args+kwargs_values:
            if not isinstance(arg,int):
                raise TypeError('%s only accept integers as arguments.'%func.__name__)
        return func(*arg,**kwargs)
    return check_int

def json_output(func):
    @functools.wraps(func)
    def define_json_output(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return define_json_output

def error_json_output(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        try:
            result = func(*args,**kwargs)
        except Exception,e:
            result={
                "status":"error",
                "error_message":str(e)
            }
        return json.dumps(result)
    return inner

def logged(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        start = time.time()

        return_value = func(*args,**kwargs)

        end = time.time()

        delta = end - start
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d : %(message)s",
                            stream=sys.stdout,filename="log.txt")
        logger = logging.getLogger("decorated.logger")

        logging.getLogger('func')
        logging.info("1111111132321321312312")
        return return_value
    return inner

@logged
def get():
    logging.info("1111111")
    print 111111

get()