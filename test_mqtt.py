#!/user/bin/env python
#coding=utf8
import requests
import time

from test_case.public.define_random_str import defineRandom

class requestContext():

    def __init__(self,data):
        self.data111 = data

    def __enter__(self):
        res = requests.post(url="http://www.aituyou.com:12112/api/v1/push/mqtt", json=self.data111, )
        return res


    def __exit__(self, exc_type, exc_val, exc_tb):

        print "__exit__ zhixingla"
        #return True
def push_mqtt(data1):
    res = requests.post(url="http://www.aituyou.com:12112/api/v1/push/mqtt",json=data1,)
    print res.content
    res.close()

#command_push(cmd = 'adb -s 192.168.0.154:6555 logcat -v threadtime -s ZhixingDZVoltageMonitor')

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
    #print bbbb
    #bbbb = "{\"action\":\"tsd.event.update_recording_parameter\",\"dataInts\":{\"recordingMode\":\"1\",\"duration\":\"3\",\"resolution\":\"1080\"\"frameRate\":\"25\"}}"
    #cccc = make_json_data(aaaa=bbbb)
    cccc = make_json_data(aaaa="{\"action\":\"tsd.event.update.request_update_info\"}")
    acv = requestContext(data=cccc)
    with acv as req:
         print "***********************************"
         #print bbbb
         print "------------------------------------"
         print req.content
         print "***********************************"
         time.sleep(10)
