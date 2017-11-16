#!/user/bin/env python
#coding=utf8
import requests
import time

from test_case.public.define_random_str import defineRandom

class requestContext():

    def __init__(self,data,url):
        self.data111 = data
        self.url = url

    def __enter__(self):
        res = requests.post(url=self.url, json=self.data111, )
        return res


    def __exit__(self, exc_type, exc_val, exc_tb):

        print "__exit__ zhixingla"
        #return True
def push_mqtt(url,data1):
    res = requests.post(url=url,json=data1,)
    print res.content
    res.close()

def make_json_data(aaaa,interval=None):
    json_data = {   "key": "xb.dz.device.unique.354008079843400",
        "messageId": "25b2fa5a-affe-4992-830c-838befd18c40",
        "timestamp": 1509606294000,
        "expire": 0,
        "type": "push",
        #"content": "{\"action\":\"com.tuyou.tsd.coeus.os.voltage.interval\",\"dataLongs\":{\"interval\":\""+interval+"\"}}",
        "content": aaaa+"echo ni ni ni ni ni 123456",
        "ack": "true",
        "ackTopic": "feedback",
        "ch": "终端推送消息"
    }
    return json_data


for x in xrange(1,10):
    print x
    rd = defineRandom()
    bbbb = rd.random_str(minlength=50, maxlength=1000)
    cccc = make_json_data(aaaa="{\"action\":\"tsd.event.update.request_update_info\"}")
    acv = requestContext(data=cccc)
    with acv as req:
         print "***********************************"
         #print bbbb
         print "------------------------------------"
         print req.content
         print "***********************************"
         time.sleep(10)
