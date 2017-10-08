# coding=utf-8
# -*- coding:utf-8 -*-
import json
import unittest
import swaggerpy
from swaggerpy.client import SwaggerClient
from swaggerpy.http_client import SynchronousHttpClient

def make_request(method,url,parameters=None,data=None):
    http_client = SynchronousHttpClient()

    """
    method = 'get'
    parameters = {
        'keywords': '刘德华',
    }
    参数根据swagger定义的参数进行传递
    """
    z=http_client.request(method=method,url=url,params=parameters,data=data)  #Request请求传入method= 'get'|'post'|'put' 等,传入url 传入请求参数
    #http_client.websockets.difference()
    return z

